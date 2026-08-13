#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Substitui os sitelinks genéricos (todos apontando p/ home) por sitelinks
EFETIVOS por produto e categoria reais, em [011]-BIQUINI e [012]-HOT-PANT.
Remove os vínculos de sitelink antigos e cria os novos, por campanha.

URLs reais capturadas (reports/2026-08-13-urls-reais-via-busca.md).
Limites: texto ≤25, cada descrição ≤35 (validado no script).

Uso: python3 sitelinks_produtos.py validate|execute
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from upload_biquinis import access_token, headers_base, http_json, descobre_versao, env  # noqa: E402

CAMP = {'24136476223': 'BIQUINI', '24136476898': 'HOT-PANT'}

FIO   = 'https://usezerohora.com.br/produtos/biquini-fio-dental-marquinha-cortininha-com-regulagens/'
SUNK  = 'https://usezerohora.com.br/produtos/biquini-sunkini-hot-pant-top-faixa-surf-piscina-futevolei/'
NAD   = 'https://usezerohora.com.br/produtos/maio-biquini-hot-pant-top-nadador-esporte-protecao-uv50/'
ALCAS = 'https://usezerohora.com.br/produtos/maio-biquini-hot-pant-top-alcas-esporte-protecao-uv50/'
MAIO  = 'https://usezerohora.com.br/feminino/maio/'
SAIDA = 'https://usezerohora.com.br/feminino/saida-de-praia/conjunto-atoalhado/'
S_CORT   = 'https://usezerohora.com.br/search/?q=cortininha'
S_EMPINA = 'https://usezerohora.com.br/search/?q=empina+bumbum'
S_MANGA  = 'https://usezerohora.com.br/search/?q=hot+pant+manga'

# por campanha: (texto ≤25, desc1 ≤35, desc2 ≤35, url)
SITELINKS = {
    '24136476223': [  # [011]-BIQUINI
        ('Biquíni Fio Dental', 'Cortininha com regulagens', 'Marca de sol menor', FIO),
        ('Biquíni Esportivo', 'Fica no lugar no surf', 'Futevôlei, piscina e mar', SUNK),
        ('Biquíni Cortininha', 'Sem bojo e alcinha regulável', 'Modelos que valorizam', S_CORT),
        ('Empina Bumbum', 'Modelagem que levanta', 'Cortininha sem bojo', S_EMPINA),
        ('Maiôs', 'Body e proteção UV50', 'Para nadar e surfar', MAIO),
        ('Saída de Praia', 'Conjunto atoalhado', 'Completa o look de praia', SAIDA),
    ],
    '24136476898': [  # [012]-HOT-PANT
        ('Hot Pant Top Nadador', 'Recorte esportivo', 'Liberdade de braço na água', NAD),
        ('Hot Pant Fitness', 'Do treino à praia', 'Proteção UV50', ALCAS),
        ('Hot Pant Surf', 'Fica no lugar na onda', 'Futevôlei, piscina e mar', SUNK),
        ('Manga 3/4 e Longa', 'Cobre e protege do sol', 'Feito para surfar', S_MANGA),
        ('Maiôs', 'Body e proteção UV50', 'Para nadar e surfar', MAIO),
        ('Saída de Praia', 'Conjunto atoalhado', 'Completa o look de praia', SAIDA),
    ],
}


def valida_limites():
    erros = []
    for lst in SITELINKS.values():
        for t, d1, d2, _u in lst:
            if len(t) > 25: erros.append(f'texto ({len(t)}): {t}')
            if len(d1) > 35: erros.append(f'desc ({len(d1)}): {d1}')
            if len(d2) > 35: erros.append(f'desc ({len(d2)}): {d2}')
    if erros:
        print('\n'.join(erros)); sys.exit('violações de limite')
    print('limites ok (texto ≤25, descrições ≤35).')


def main(modo):
    valida_limites()
    validate = (modo == 'validate')
    cid = env('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')
    h = headers_base(access_token())
    v = descobre_versao(h)
    url = f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:mutate'
    print(f'API {v} | customer {cid} | modo: {modo}\n')

    # vínculos de sitelink atuais (para remover)
    q = ("SELECT campaign.id, campaign_asset.resource_name FROM campaign_asset "
         "WHERE campaign.id IN (24136476223,24136476898) "
         "AND campaign_asset.field_type='SITELINK' AND campaign_asset.status!='REMOVED'")
    body = {'query': q}
    resp, err = http_json(f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:search', h, body)
    if err:
        print('FALHA ao ler sitelinks atuais:', err[1]); sys.exit(1)
    antigos = {}
    for r in resp.get('results', []):
        antigos.setdefault(r['campaign']['id'], []).append(r['campaignAsset']['resourceName'])

    for camp_id, nome in CAMP.items():
        ops = []
        n = 0
        # remove vínculos antigos (home)
        for rn in antigos.get(camp_id, []):
            ops.append({'campaignAssetOperation': {'remove': rn}})
        # cria novos assets + vincula
        for t, d1, d2, u in SITELINKS[camp_id]:
            n += 1
            arn = f'customers/{cid}/assets/-{n}'
            ops.append({'assetOperation': {'create': {
                'resourceName': arn, 'finalUrls': [u],
                'sitelinkAsset': {'linkText': t, 'description1': d1, 'description2': d2}}}})
            ops.append({'campaignAssetOperation': {'create': {
                'campaign': f'customers/{cid}/campaigns/{camp_id}',
                'asset': arn, 'fieldType': 'SITELINK'}}})
        payload = {'mutateOperations': ops, 'validateOnly': validate}
        resp, err = http_json(url, h, payload)
        if err:
            print(f'FALHA em [{nome}] (HTTP {err[0]}):', str(err[1])[:2000]); sys.exit(1)
        rem = len(antigos.get(camp_id, []))
        print(f'  [{nome}] {"VALIDADO" if validate else "APLICADO"}: '
              f'-{rem} sitelinks home, +{len(SITELINKS[camp_id])} por produto/categoria.')

    print('\n' + ('Ensaio OK — rode "execute".' if validate else
                  'Sitelinks efetivos aplicados nas 2 campanhas.'))


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: sitelinks_produtos.py validate|execute')
    main(sys.argv[1])
