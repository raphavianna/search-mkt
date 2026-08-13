#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Limpa o ad group [011-F]-FIO-DENTAL-COMPRA:
- REMOVE todas as keywords em correspondência AMPLA (adicionadas fora do fluxo).
- RECRIA em FRASE as que são on-theme (contêm "fio dental"), deduplicando.
- NEGATIVA "calcinha" (off-target) no ad group.
As amplas soltas sem "fio dental" (ex.: biquini pequeno/fino/cavados/calcinha) saem
e não são recriadas.

Uso: python3 limpa_fio_dental.py validate|execute
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'integracao', 'google-ads'))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

AG = '197525753725'  # [011-F]-FIO-DENTAL-COMPRA
NEGATIVAS_OFFTARGET = ['calcinha']


def main(modo):
    validate = (modo == 'validate')
    c = GoogleAdsClient.from_env()
    cid = c.customer_id

    rows = c.search(
        "SELECT ad_group_criterion.resource_name, ad_group_criterion.keyword.text, "
        "ad_group_criterion.keyword.match_type, ad_group_criterion.negative "
        f"FROM ad_group_criterion WHERE ad_group.id = {AG} "
        "AND ad_group_criterion.type = KEYWORD AND ad_group_criterion.status != 'REMOVED'")

    amplas, frases_existentes = [], set()
    for r in rows:
        crit = r['adGroupCriterion']
        if crit.get('negative'):
            continue
        kw = crit['keyword']
        if kw['matchType'] == 'BROAD':
            amplas.append((crit['resourceName'], kw['text']))
        elif kw['matchType'] == 'PHRASE':
            frases_existentes.add(kw['text'].lower())

    # on-theme = contém "fio dental"; recria em frase (dedupe vs frases existentes)
    recria, dropa = [], []
    for _rn, txt in amplas:
        if 'fio dental' in txt.lower():
            if txt.lower() not in frases_existentes:
                recria.append(txt); frases_existentes.add(txt.lower())
        else:
            dropa.append(txt)

    print(f'AMPLAS a remover: {len(amplas)}')
    print(f'  → recriar em FRASE (on-theme): {len(recria)}')
    print(f'  → dropar (off-target, sem "fio dental"): {len(dropa)} -> {dropa}')
    print(f'NEGATIVAS a adicionar: {NEGATIVAS_OFFTARGET}\n')

    ops = []
    for rn, _txt in amplas:                       # remove todas as amplas
        ops.append({'remove': rn})
    for txt in recria:                            # recria on-theme em frase
        ops.append({'create': {
            'adGroup': f'customers/{cid}/adGroups/{AG}', 'status': 'ENABLED',
            'keyword': {'text': txt, 'matchType': 'PHRASE'}}})
    for neg in NEGATIVAS_OFFTARGET:               # negativa off-target
        ops.append({'create': {
            'adGroup': f'customers/{cid}/adGroups/{AG}', 'negative': True,
            'keyword': {'text': neg, 'matchType': 'PHRASE'}}})

    try:
        c.mutate('adGroupCriteria', ops, validate_only=validate)
    except GoogleAdsError as e:
        print(f'FALHA: HTTP {e.status}\n{e.body[:4000]}'); sys.exit(1)

    print(f'{"VALIDAÇÃO OK — nada gravado" if validate else "APLICADO"}: '
          f'-{len(amplas)} amplas, +{len(recria)} frases, +{len(NEGATIVAS_OFFTARGET)} negativa(s).')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: limpa_fio_dental.py validate|execute')
    main(sys.argv[1])
