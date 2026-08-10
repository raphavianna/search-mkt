#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sobe a campanha Neoprene (campanha + ad groups + KWs + negativas) via
Google Ads API (REST). Credenciais via variáveis de ambiente:
GOOGLE_ADS_DEVELOPER_TOKEN, GOOGLE_ADS_CLIENT_ID, GOOGLE_ADS_CLIENT_SECRET,
GOOGLE_ADS_REFRESH_TOKEN, GOOGLE_ADS_CUSTOMER_ID (+ opcional
GOOGLE_ADS_LOGIN_CUSTOMER_ID).

Uso:
  python3 upload_google_ads.py validate   # ensaio (validateOnly, nada é gravado)
  python3 upload_google_ads.py execute    # criação real (campanha PAUSADA)

A campanha nasce PAUSED: sem anúncios (Etapa 2 pendente) e sem gasto até
revisão manual e ativação na conta.
"""
import csv
import json
import os
import sys
import urllib.request
import urllib.error

CSV_KWS = os.path.join(os.path.dirname(__file__), '..', 'kw-planner', 'kw-consolidada-neoprene.csv')
CAMPANHA = '[UZH] [Search] [Neoprene] [BR]'
BUDGET_MICROS = 30_000_000          # R$30/dia — ajustar na conta antes de ativar
GEO_BRASIL = 'geoTargetConstants/2076'
IDIOMA_PT = 'languageConstants/1014'
GRUPOS_FORA = {'neoprene-concorrencia (nao ativar)', 'fora-da-campanha (observacao)'}
API_VERSOES = ['v22', 'v21', 'v20', 'v19', 'v18']

# Negativas de campanha (frase) — master/biblioteca-negativas.md + 01-kws.md §6.
# "borracha" e "mergulho" NÃO entram: há KWs positivas com esses termos.
NEGATIVAS = [
    # colisão com o jornal Zero Hora
    'jornal zero hora', 'zero hora noticias', 'zero hora rs',
    'zero hora porto alegre', 'gzh', 'gauchazh', 'zero hora classificados',
    'zero hora obituario', 'zero hora hoje', 'capa zero hora',
    # intenção sem compra / DIY
    'gratis', 'gratuito', 'como fazer', 'diy', 'molde', 'costurar', 'usado',
    'usada', 'segunda mao', 'aluguel', 'alugar', 'conserto', 'consertar',
    'reparo', 'como lavar', 'como colar', 'alargar',
    # B2B / atacado
    'atacado', 'atacadista', 'revenda', 'revendedor', 'fabrica',
    'fornecedor', 'cnpj',
    # emprego
    'vaga', 'vagas', 'emprego', 'trabalhe', 'curriculo', 'estagio',
    # marketplaces
    'shopee', 'shein', 'mercado livre', 'amazon', 'aliexpress',
    # matéria-prima (compra de tecido, não de produto)
    'tecido', 'metro', 'manta', 'placa',
    # outros nichos de neoprene
    'blazer', 'joelheira', 'tornozeleira', 'munhequeira', 'cachorro', 'pet',
    'cinta', 'sauna', 'emagrecer', 'emagrecimento', 'queima gordura',
    'academia',
    # produto não vendido / público
    'long john', 'longjohn', 'wetsuit', 'macacao', 'infantil', 'trilha',
    'pesca', '5mm',
]

MATCH = {'Phrase': 'PHRASE', 'Exact': 'EXACT'}


def env(nome, obrigatoria=True):
    v = os.environ.get(nome, '').strip()
    if obrigatoria and not v:
        sys.exit(f'ERRO: variável {nome} ausente no ambiente')
    return v


def http_json(url, headers, payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers,
                                 method='POST' if data else 'GET')
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
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
    with urllib.request.urlopen(req, timeout=60) as r:
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
        if err is None:
            return v
        code, corpo = err
        if code != 404:
            # 401/403 = versão existe mas credencial/permite não — versão serve
            return v
    sys.exit('ERRO: nenhuma versão da API respondeu')


def carrega_kws():
    grupos = {}
    for r in csv.DictReader(open(CSV_KWS, encoding='utf-8')):
        g = r['Ad group']
        if g in GRUPOS_FORA:
            continue
        grupos.setdefault(g, []).append((r['Keyword'], MATCH.get(r['Match sugerido'], 'PHRASE')))
    return grupos


def monta_operacoes(cid, grupos):
    """Três lotes: (A) budget+campanha+geo+idioma+negativas (atômico),
    (B) ad groups (atômico), (C) keywords (partial failure)."""
    budget_rn = f'customers/{cid}/campaignBudgets/-1'
    camp_rn = f'customers/{cid}/campaigns/-2'

    lote_a = [
        {'campaignBudgetOperation': {'create': {
            'resourceName': budget_rn,
            'name': f'{CAMPANHA} - budget',
            'amountMicros': str(BUDGET_MICROS),
            'deliveryMethod': 'STANDARD',
            'explicitlyShared': False,
        }}},
        {'campaignOperation': {'create': {
            'resourceName': camp_rn,
            'name': CAMPANHA,
            'status': 'PAUSED',
            'advertisingChannelType': 'SEARCH',
            'campaignBudget': budget_rn,
            'maximizeConversions': {},
            'networkSettings': {
                'targetGoogleSearch': True,
                'targetSearchNetwork': False,
                'targetContentNetwork': False,
                'targetPartnerSearchNetwork': False,
            },
            'geoTargetTypeSetting': {
                'positiveGeoTargetType': 'PRESENCE',
                'negativeGeoTargetType': 'PRESENCE',
            },
            'containsEuPoliticalAdvertising': 'DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING',
        }}},
        {'campaignCriterionOperation': {'create': {
            'campaign': camp_rn, 'location': {'geoTargetConstant': GEO_BRASIL}}}},
        {'campaignCriterionOperation': {'create': {
            'campaign': camp_rn, 'language': {'languageConstant': IDIOMA_PT}}}},
    ]
    for neg in NEGATIVAS:
        lote_a.append({'campaignCriterionOperation': {'create': {
            'campaign': camp_rn, 'negative': True,
            'keyword': {'text': neg, 'matchType': 'PHRASE'}}}})

    lote_b = []
    ag_rns = {}
    for i, g in enumerate(sorted(grupos), start=10):
        rn = f'customers/{cid}/adGroups/-{i}'
        ag_rns[g] = rn
        lote_b.append({'adGroupOperation': {'create': {
            'resourceName': rn,
            'name': g,
            'campaign': camp_rn,
            'status': 'ENABLED',
            'type': 'SEARCH_STANDARD',
        }}})

    lote_c = []
    for g, kws in grupos.items():
        for texto, match in kws:
            lote_c.append({'adGroupCriterionOperation': {'create': {
                'adGroup': ag_rns[g],
                'status': 'ENABLED',
                'keyword': {'text': texto, 'matchType': match},
            }}})
    return lote_a, lote_b, lote_c, camp_rn, ag_rns


def executa(modo):
    validate = (modo == 'validate')
    cid = env('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')
    token = access_token()
    h = headers_base(token)
    versao = descobre_versao(h)
    print(f'API {versao} | customer {cid} | modo: {modo}')
    url = f'https://googleads.googleapis.com/{versao}/customers/{cid}/googleAds:mutate'

    grupos = carrega_kws()
    lote_a, lote_b, lote_c, camp_rn, ag_rns = monta_operacoes(cid, grupos)

    if validate:
        # validateOnly aceita temp ids no mesmo request — valida tudo junto
        payload = {'mutateOperations': lote_a + lote_b + lote_c, 'validateOnly': True}
        resp, err = http_json(url, h, payload)
        if err:
            code, corpo = err
            # campo EU pode não existir em versões antigas — tenta sem ele
            if 'containsEuPoliticalAdvertising' in json.dumps(corpo):
                print('aviso: campo EU political não aceito nesta versão — removendo e revalidando')
                del lote_a[1]['campaignOperation']['create']['containsEuPoliticalAdvertising']
                payload = {'mutateOperations': lote_a + lote_b + lote_c, 'validateOnly': True}
                resp, err = http_json(url, h, payload)
            if err:
                print('FALHA NA VALIDAÇÃO:')
                print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000])
                sys.exit(1)
        print(f'VALIDAÇÃO OK — {len(lote_a)} ops campanha/negativas, '
              f'{len(lote_b)} ad groups, {len(lote_c)} keywords. Nada foi gravado.')
        return

    # execução real, em 3 fases
    resp, err = http_json(url, h, {'mutateOperations': lote_a})
    if err:
        if 'containsEuPoliticalAdvertising' in json.dumps(err[1]):
            del lote_a[1]['campaignOperation']['create']['containsEuPoliticalAdvertising']
            resp, err = http_json(url, h, {'mutateOperations': lote_a})
        if err:
            print('FALHA fase A (campanha):')
            print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000])
            sys.exit(1)
    resultados = resp['mutateOperationResponses']
    camp_real = resultados[1]['campaignResult']['resourceName']
    print(f'fase A ok — campanha criada PAUSADA: {camp_real} '
          f'({len(NEGATIVAS)} negativas, geo BR, idioma pt)')

    # fase B: ad groups apontando para a campanha real
    for op in lote_b:
        op['adGroupOperation']['create']['campaign'] = camp_real
    resp, err = http_json(url, h, {'mutateOperations': lote_b})
    if err:
        print('FALHA fase B (ad groups):')
        print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000])
        sys.exit(1)
    ag_reais = {}
    for g, r in zip(sorted(grupos), resp['mutateOperationResponses']):
        ag_reais[g] = r['adGroupResult']['resourceName']
        print(f'  ad group: {g} -> {ag_reais[g]}')

    # fase C: keywords com partialFailure (relata individuais que falharem)
    temp_para_grupo = {v: g for g, v in ag_rns.items()}
    for op in lote_c:
        cr = op['adGroupCriterionOperation']['create']
        cr['adGroup'] = ag_reais[temp_para_grupo[cr['adGroup']]]
    resp, err = http_json(url, h, {'mutateOperations': lote_c, 'partialFailure': True})
    if err:
        print('FALHA fase C (keywords):')
        print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000])
        sys.exit(1)
    falhas = resp.get('partialFailureError')
    criadas = sum(1 for r in resp['mutateOperationResponses'] if r)
    print(f'fase C ok — {criadas}/{len(lote_c)} keywords criadas')
    if falhas:
        print('keywords com falha (partialFailure):')
        print(json.dumps(falhas, indent=2, ensure_ascii=False)[:6000])


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: upload_google_ads.py validate|execute')
    executa(sys.argv[1])
