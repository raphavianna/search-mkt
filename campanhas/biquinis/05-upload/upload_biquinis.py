#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sobe as 3 campanhas de Search da linha Biquíni + Hot Pant na conta Google
Ads (REST, conta direta) — campanha + orçamento + geo + idioma + negativas +
ad groups + keywords + RSAs + extensões, tudo numa operação atômica por
campanha. Reusa o padrão já aplicado em [007-SEARCH]-NEOPRENE.

Lê os artefatos já validados em `../03-csv/`:
  keywords.csv · negativas.csv · rsas.csv · sitelinks.csv · callouts.csv · snippets.csv

Credenciais via variáveis de ambiente (mesmas do integracao/google-ads):
  GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
  GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_CUSTOMER_ID (+ opc. LOGIN_CUSTOMER_ID).

Uso:
  python3 upload_biquinis.py validate   # ensaio (validateOnly; nada é gravado)
  python3 upload_biquinis.py execute     # cria de verdade — campanhas PAUSED

Todas as campanhas nascem PAUSED: sem gasto até revisão e ativação manual na
conta. URLs finais são provisórias (categoria) — trocar pela página exata
antes de ativar.
"""
import csv
import json
import os
import sys
import urllib.parse
import urllib.request
import urllib.error

BASE = os.path.dirname(os.path.abspath(__file__))
CSVDIR = os.path.join(BASE, '..', '03-csv')

GEO_BRASIL = 'geoTargetConstants/2076'
IDIOMA_PT = 'languageConstants/1014'
API_VERSOES = ['v25', 'v24', 'v23', 'v22', 'v21']

# nome interno (nos CSVs) -> (nome na conta [taxonomia real], orçamento diário em micros)
# Orçamento calibrado pelo forecast do Google Keyword Planner (2026-08-12):
# conjunto Search ~R$22/dia; split por ticket/demanda (Etapa 0/2).
CAMPANHAS = {
    'Search - Biquínis':              ('[011-SEARCH]-BIQUINI',   7_000_000),
    'Search - Hot Pant':              ('[012-SEARCH]-HOT-PANT',  11_000_000),
    'Search - Marca e Consideração':  ('[013-SEARCH]-MARCA',      4_000_000),
}

MATCH = {'Phrase': 'PHRASE', 'Exact': 'EXACT', 'Broad': 'BROAD'}


# ----------------------------------------------------------------- infra REST
def env(nome, obrigatoria=True):
    v = os.environ.get(nome, '').strip()
    if obrigatoria and not v:
        sys.exit(f'ERRO: variável {nome} ausente no ambiente')
    return v


def _ssl_context():
    import ssl
    ctx = ssl.create_default_context()
    bundle = os.environ.get('SSL_CERT_FILE') or '/root/.ccr/ca-bundle.crt'
    if os.path.exists(bundle):
        ctx.load_verify_locations(cafile=bundle)
    return ctx


def http_json(url, headers, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers,
                                 method='POST' if data else 'GET')
    try:
        with urllib.request.urlopen(req, timeout=120, context=_ssl_context()) as r:
            return json.loads(r.read().decode()), None
    except urllib.error.HTTPError as e:
        corpo = e.read().decode()
        try:
            corpo = json.loads(corpo)
        except ValueError:
            pass
        return None, (e.code, corpo)


def access_token():
    payload = {
        'client_id': env('GOOGLE_ADS_CLIENT_ID'),
        'client_secret': env('GOOGLE_ADS_CLIENT_SECRET'),
        'refresh_token': env('GOOGLE_ADS_REFRESH_TOKEN'),
        'grant_type': 'refresh_token',
    }
    data = '&'.join(f'{k}={urllib.parse.quote(v)}' for k, v in payload.items()).encode()
    req = urllib.request.Request('https://oauth2.googleapis.com/token', data=data,
                                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
    with urllib.request.urlopen(req, timeout=60, context=_ssl_context()) as r:
        return json.loads(r.read().decode())['access_token']


def headers_base(token):
    h = {
        'Authorization': f'Bearer {token}',
        'developer-token': env('GOOGLE_ADS_DEVELOPER_TOKEN'),
        'Content-Type': 'application/json',
    }
    login = env('GOOGLE_ADS_LOGIN_CUSTOMER_ID', obrigatoria=False)
    if login:
        h['login-customer-id'] = login.replace('-', '')
    return h


def descobre_versao(h):
    for v in API_VERSOES:
        _, err = http_json(f'https://googleads.googleapis.com/{v}/customers:listAccessibleCustomers', h)
        if err is None or err[0] != 404:
            return v
    sys.exit('ERRO: nenhuma versão da API respondeu')


# ------------------------------------------------------------- leitura de CSVs
def carrega():
    kws = {}          # campanha -> ad group -> [(texto, match)]
    for r in csv.DictReader(open(os.path.join(CSVDIR, 'keywords.csv'), encoding='utf-8')):
        kws.setdefault(r['Campaign'], {}).setdefault(r['Ad Group'], []).append(
            (r['Keyword'], MATCH.get(r['Match Type'], 'PHRASE')))

    negativas = [r['Keyword'] for r in
                 csv.DictReader(open(os.path.join(CSVDIR, 'negativas.csv'), encoding='utf-8'))]

    rsas = {}         # (campanha, ad group) -> dict do anúncio
    for r in csv.DictReader(open(os.path.join(CSVDIR, 'rsas.csv'), encoding='utf-8')):
        heads = []
        for i in range(1, 16):
            t = (r.get(f'Headline {i}') or '').strip()
            if not t:
                continue
            pos = (r.get(f'Headline {i} position') or '').strip()
            h = {'text': t}
            if pos:
                h['pinnedField'] = f'HEADLINE_{pos}'
            heads.append(h)
        descs = [{'text': (r.get(f'Description {i}') or '').strip()}
                 for i in range(1, 5) if (r.get(f'Description {i}') or '').strip()]
        rsas[(r['Campaign'], r['Ad Group'])] = {
            'headlines': heads, 'descriptions': descs,
            'path1': r.get('Path 1', ''), 'path2': r.get('Path 2', ''),
            'finalUrl': r['Final URL'],
        }

    sitelinks = [(r['Sitelink Text'], r['Description 1'], r['Description 2'], r['Final URL'])
                 for r in csv.DictReader(open(os.path.join(CSVDIR, 'sitelinks.csv'), encoding='utf-8'))]
    callouts = [r['Callout text'] for r in
                csv.DictReader(open(os.path.join(CSVDIR, 'callouts.csv'), encoding='utf-8'))]
    snippets = [(r['Header'], [v.strip() for v in r['Values (; )'].split(';')])
                for r in csv.DictReader(open(os.path.join(CSVDIR, 'snippets.csv'), encoding='utf-8'))]
    return kws, negativas, rsas, sitelinks, callouts, snippets


# -------------------------------------------------- montagem das operações
def ops_campanha(cid, camp_interna, kws, negativas, rsas, sitelinks, callouts, snippets):
    """Operações atômicas de UMA campanha (temp resource names negativos)."""
    nome_conta, budget = CAMPANHAS[camp_interna]
    contador = {'n': 0}

    def temp(colecao):
        contador['n'] += 1
        return f'customers/{cid}/{colecao}/-{contador["n"]}'

    budget_rn = temp('campaignBudgets')
    camp_rn = temp('campaigns')
    ops = [
        {'campaignBudgetOperation': {'create': {
            'resourceName': budget_rn, 'name': f'{nome_conta} - budget',
            'amountMicros': str(budget), 'deliveryMethod': 'STANDARD',
            'explicitlyShared': False}}},
        {'campaignOperation': {'create': {
            'resourceName': camp_rn, 'name': nome_conta, 'status': 'PAUSED',
            'advertisingChannelType': 'SEARCH', 'campaignBudget': budget_rn,
            'maximizeConversions': {},
            'networkSettings': {
                'targetGoogleSearch': True, 'targetSearchNetwork': False,
                'targetContentNetwork': False, 'targetPartnerSearchNetwork': False},
            'geoTargetTypeSetting': {
                'positiveGeoTargetType': 'PRESENCE', 'negativeGeoTargetType': 'PRESENCE'},
            'containsEuPoliticalAdvertising': 'DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING',
        }}},
        {'campaignCriterionOperation': {'create': {
            'campaign': camp_rn, 'location': {'geoTargetConstant': GEO_BRASIL}}}},
        {'campaignCriterionOperation': {'create': {
            'campaign': camp_rn, 'language': {'languageConstant': IDIOMA_PT}}}},
    ]
    for neg in negativas:
        ops.append({'campaignCriterionOperation': {'create': {
            'campaign': camp_rn, 'negative': True,
            'keyword': {'text': neg, 'matchType': 'PHRASE'}}}})

    # ad groups + keywords + RSA por grupo
    for grupo, lista in kws[camp_interna].items():
        ag_rn = temp('adGroups')
        ops.append({'adGroupOperation': {'create': {
            'resourceName': ag_rn, 'name': grupo, 'campaign': camp_rn,
            'status': 'ENABLED', 'type': 'SEARCH_STANDARD'}}})
        for texto, match in lista:
            ops.append({'adGroupCriterionOperation': {'create': {
                'adGroup': ag_rn, 'status': 'ENABLED',
                'keyword': {'text': texto, 'matchType': match}}}})
        rsa = rsas.get((camp_interna, grupo))
        if rsa:
            ad = {'finalUrls': [rsa['finalUrl']],
                  'responsiveSearchAd': {
                      'headlines': rsa['headlines'],
                      'descriptions': rsa['descriptions']}}
            if rsa['path1']:
                ad['responsiveSearchAd']['path1'] = rsa['path1']
            if rsa['path2']:
                ad['responsiveSearchAd']['path2'] = rsa['path2']
            ops.append({'adGroupAdOperation': {'create': {
                'adGroup': ag_rn, 'status': 'ENABLED', 'ad': ad}}})

    # extensões compartilhadas (assets + vínculo à campanha)
    links = []
    for t, d1, d2, u in sitelinks:
        rn = temp('assets')
        ops.append({'assetOperation': {'create': {
            'resourceName': rn, 'finalUrls': [u],
            'sitelinkAsset': {'linkText': t, 'description1': d1, 'description2': d2}}}})
        links.append((rn, 'SITELINK'))
    for c in callouts:
        rn = temp('assets')
        ops.append({'assetOperation': {'create': {
            'resourceName': rn, 'calloutAsset': {'calloutText': c}}}})
        links.append((rn, 'CALLOUT'))
    for header, valores in snippets:
        rn = temp('assets')
        ops.append({'assetOperation': {'create': {
            'resourceName': rn,
            'structuredSnippetAsset': {'header': header, 'values': valores}}}})
        links.append((rn, 'STRUCTURED_SNIPPET'))
    for rn, ft in links:
        ops.append({'campaignAssetOperation': {'create': {
            'campaign': camp_rn, 'asset': rn, 'fieldType': ft}}})

    return ops


def resumo(camp_interna, kws, negativas, rsas):
    nome_conta, budget = CAMPANHAS[camp_interna]
    grupos = kws[camp_interna]
    n_kw = sum(len(v) for v in grupos.values())
    n_rsa = sum(1 for g in grupos if (camp_interna, g) in rsas)
    return (f'{nome_conta}: R${budget//1_000_000}/dia · {len(grupos)} ad groups · '
            f'{n_kw} keywords · {n_rsa} RSAs · {len(negativas)} negativas')


# ------------------------------------------------------------------ execução
def run(modo):
    cid = env('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')
    h = headers_base(access_token())
    v = descobre_versao(h)
    url = f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:mutate'
    print(f'API {v} | customer {cid} | modo: {modo}\n')

    kws, negativas, rsas, sitelinks, callouts, snippets = carrega()

    for camp_interna in CAMPANHAS:
        print('· ' + resumo(camp_interna, kws, negativas, rsas))
    print()

    criadas = []
    for camp_interna in CAMPANHAS:
        nome_conta, _ = CAMPANHAS[camp_interna]
        ops = ops_campanha(cid, camp_interna, kws, negativas, rsas,
                           sitelinks, callouts, snippets)
        payload = {'mutateOperations': ops, 'validateOnly': (modo == 'validate')}
        resp, err = http_json(url, h, payload)
        if err:
            print(f'FALHA em {nome_conta} (HTTP {err[0]}):')
            print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000])
            sys.exit(1)
        if modo == 'validate':
            print(f'  VALIDAÇÃO OK — {nome_conta}: {len(ops)} operações. Nada gravado.')
        else:
            camp_real = next((r['campaignResult']['resourceName']
                              for r in resp['mutateOperationResponses']
                              if r.get('campaignResult')), '?')
            print(f'  CRIADA (PAUSED) — {nome_conta}: {camp_real} ({len(ops)} operações)')
            criadas.append((nome_conta, camp_real))

    print()
    if modo == 'validate':
        print('Ensaio concluído: as 3 campanhas passaram na validação do servidor. '
              'Rode "execute" para criar de verdade (PAUSED).')
    else:
        print('Upload concluído — 3 campanhas de Search criadas PAUSED:')
        for nome, rn in criadas:
            print(f'  {nome} -> {rn}')
        print('\nRevisar na conta, trocar URLs finais pela página exata e então ativar.')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: upload_biquinis.py validate|execute')
    run(sys.argv[1])
