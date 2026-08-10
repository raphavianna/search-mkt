#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria a [009-PMAX]-NEOPRENE (pausada), feed-only, filtrada nos 11 produtos.

Padrão da conta: [001-PMAX]-PONCHO-FEMININO. Feed-only = anúncios gerados a
partir do Merchant (sem assets de imagem/texto obrigatórios), como uma
Smart Shopping. Uso: python3 pmax_009.py validate|execute
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from upload_google_ads import access_token, headers_base, descobre_versao, http_json, env

MERCHANT_ID = '5507430207'
BUDGET_MICROS = 15_000_000
CAMPANHA = '[009-PMAX]-NEOPRENE'
ASSET_GROUP = '[009-A]-NEOPRENE'
URL_FINAL = 'https://usezerohora.com.br/'

ITEM_IDS = [
    '1569492206', '1569492207', '1569492210', '1569492211',
    '1569492227', '1569492228', '1569492229', '1569492230',
    '1569492220', '1569492221', '1569492222',
]


def monta_ops(cid):
    budget_rn = f'customers/{cid}/campaignBudgets/-1'
    camp_rn = f'customers/{cid}/campaigns/-2'
    ag_rn = f'customers/{cid}/assetGroups/-3'
    ops = [
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
            'advertisingChannelType': 'PERFORMANCE_MAX',
            'campaignBudget': budget_rn,
            'maximizeConversionValue': {},
            'shoppingSetting': {'merchantId': MERCHANT_ID},
            'containsEuPoliticalAdvertising': 'DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING',
        }}},
        {'assetGroupOperation': {'create': {
            'resourceName': ag_rn,
            'campaign': camp_rn,
            'name': ASSET_GROUP,
            'finalUrls': [URL_FINAL],
            'status': 'ENABLED',
        }}},
    ]
    raiz = f'customers/{cid}/assetGroupListingGroupFilters/-3~-10'
    ops.append({'assetGroupListingGroupFilterOperation': {'create': {
        'resourceName': raiz,
        'assetGroup': ag_rn,
        'type': 'SUBDIVISION',
        'listingSource': 'SHOPPING',
    }}})
    for i, iid in enumerate(ITEM_IDS, 11):
        ops.append({'assetGroupListingGroupFilterOperation': {'create': {
            'resourceName': f'customers/{cid}/assetGroupListingGroupFilters/-3~-{i+10}',
            'assetGroup': ag_rn,
            'type': 'UNIT_INCLUDED',
            'listingSource': 'SHOPPING',
            'parentListingGroupFilter': raiz,
            'caseValue': {'productItemId': {'value': iid}},
        }}})
    ops.append({'assetGroupListingGroupFilterOperation': {'create': {
        'resourceName': f'customers/{cid}/assetGroupListingGroupFilters/-3~-99',
        'assetGroup': ag_rn,
        'type': 'UNIT_EXCLUDED',
        'listingSource': 'SHOPPING',
        'parentListingGroupFilter': raiz,
        'caseValue': {'productItemId': {}},
    }}})
    return ops


def main(modo):
    cid = env('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')
    h = headers_base(access_token())
    v = descobre_versao(h)
    url = f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:mutate'
    print(f'API {v} | customer {cid} | modo: {modo}')
    ops = monta_ops(cid)
    payload = {'mutateOperations': ops}
    if modo == 'validate':
        payload['validateOnly'] = True
    resp, err = http_json(url, h, payload)
    if err:
        print('FALHA:')
        print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000])
        sys.exit(1)
    if modo == 'validate':
        print(f'VALIDAÇÃO OK — campanha + asset group + {len(ITEM_IDS)} produtos '
              f'+ exclusão do restante. Nada foi gravado.')
    else:
        rs = resp['mutateOperationResponses']
        print('criado:')
        print(' ', rs[1]['campaignResult']['resourceName'])
        print(' ', rs[2]['assetGroupResult']['resourceName'])
        print(f'  listing group filters: {len(ITEM_IDS)} incluídos + restante excluído')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: pmax_009.py validate|execute')
    main(sys.argv[1])
