#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cria a [008-SHOPPING]-NEOPRENE (pausada) filtrada nos 11 produtos da linha.

Padrão da conta (verificado 2026-08-10): Shopping standard, Maximizar valor
da conversão, prioridade 1, budgets R$15-25/dia.

Uso: python3 shopping_008.py validate|execute
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from upload_google_ads import access_token, headers_base, descobre_versao, http_json, env

MERCHANT_ID = '5507430207'
BUDGET_MICROS = 15_000_000  # R$15/dia, padrão das shopping da conta
CAMPANHA = '[008-SHOPPING]-NEOPRENE'
AD_GROUP = '[008-A]-NEOPRENE-COMPRA'

ITEM_IDS = [
    '1569492206', '1569492207', '1569492210', '1569492211',  # camiseta P M G GG
    '1569492227', '1569492228', '1569492229', '1569492230',  # bermuda P M G GG
    '1569492220', '1569492221', '1569492222',                # sapatilha 34-37 38-41 42-44
]


def ops_fase_a(cid):
    budget_rn = f'customers/{cid}/campaignBudgets/-1'
    camp_rn = f'customers/{cid}/campaigns/-2'
    return [
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
            'advertisingChannelType': 'SHOPPING',
            'campaignBudget': budget_rn,
            'maximizeConversionValue': {},
            'shoppingSetting': {
                'merchantId': MERCHANT_ID,
                'campaignPriority': 1,
                'enableLocal': False,
            },
            'containsEuPoliticalAdvertising': 'DOES_NOT_CONTAIN_EU_POLITICAL_ADVERTISING',
        }}},
    ], camp_rn


def ops_fase_b(cid, camp_real):
    ag_rn = f'customers/{cid}/adGroups/-3'
    return [
        {'adGroupOperation': {'create': {
            'resourceName': ag_rn,
            'name': AD_GROUP,
            'campaign': camp_real,
            'status': 'ENABLED',
            'type': 'SHOPPING_PRODUCT_ADS',
        }}},
        {'adGroupAdOperation': {'create': {
            'adGroup': ag_rn,
            'status': 'ENABLED',
            'ad': {'shoppingProductAd': {}},
        }}},
    ], ag_rn


def ops_fase_c(cid, ag_real):
    raiz = f'customers/{cid}/adGroupCriteria/{ag_real.split("/")[-1]}~-10'
    ops = [{'adGroupCriterionOperation': {'create': {
        'resourceName': raiz,
        'adGroup': ag_real,
        'status': 'ENABLED',
        'listingGroup': {'type': 'SUBDIVISION'},
    }}}]
    for iid in ITEM_IDS:
        ops.append({'adGroupCriterionOperation': {'create': {
            'adGroup': ag_real,
            'status': 'ENABLED',
            'cpcBidMicros': '500000',
            'listingGroup': {
                'type': 'UNIT',
                'parentAdGroupCriterion': raiz,
                'caseValue': {'productItemId': {'value': iid}},
            },
        }}})
    # "tudo o mais" excluído — a campanha só anuncia a linha neoprene
    ops.append({'adGroupCriterionOperation': {'create': {
        'adGroup': ag_real,
        'negative': True,
        'listingGroup': {
            'type': 'UNIT',
            'parentAdGroupCriterion': raiz,
            'caseValue': {'productItemId': {}},
        },
    }}})
    return ops


def main(modo):
    cid = env('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')
    h = headers_base(access_token())
    v = descobre_versao(h)
    url = f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:mutate'
    print(f'API {v} | customer {cid} | modo: {modo}')

    lote_a, camp_rn = ops_fase_a(cid)
    lote_b, ag_rn = ops_fase_b(cid, camp_rn)

    if modo == 'validate':
        ops = lote_a + lote_b + ops_fase_c(cid, ag_rn)
        resp, err = http_json(url, h, {'mutateOperations': ops, 'validateOnly': True})
        if err:
            print('FALHA NA VALIDAÇÃO:')
            print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000])
            sys.exit(1)
        print(f'VALIDAÇÃO OK — campanha + ad group + {len(ITEM_IDS)} produtos '
              f'+ exclusão do restante. Nada foi gravado.')
        return

    resp, err = http_json(url, h, {'mutateOperations': lote_a})
    if err:
        print('FALHA fase A:'); print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000]); sys.exit(1)
    camp_real = resp['mutateOperationResponses'][1]['campaignResult']['resourceName']
    print(f'fase A ok — campanha PAUSADA: {camp_real}')

    lote_b, ag_rn = ops_fase_b(cid, camp_real)
    resp, err = http_json(url, h, {'mutateOperations': lote_b})
    if err:
        print('FALHA fase B:'); print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000]); sys.exit(1)
    ag_real = resp['mutateOperationResponses'][0]['adGroupResult']['resourceName']
    print(f'fase B ok — ad group: {ag_real}')

    resp, err = http_json(url, h, {'mutateOperations': ops_fase_c(cid, ag_real)})
    if err:
        print('FALHA fase C:'); print(json.dumps(err[1], indent=2, ensure_ascii=False)[:6000]); sys.exit(1)
    print(f'fase C ok — listing groups: {len(ITEM_IDS)} produtos incluídos, restante excluído')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: shopping_008.py validate|execute')
    main(sys.argv[1])
