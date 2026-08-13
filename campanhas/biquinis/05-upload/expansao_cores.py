#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Expansão de keywords por COR, ancorada nas cores reais do catálogo
(base de vendas BaseLinker/painel — `zerohora-painel/public/data/vendas.json`,
período 2026-01→08). Combina o termo de cada ad group com as cores disponíveis.

Cores por categoria (searchable; nomes de marketing mapeados p/ termo de busca):
  Biquíni : preto, coral, onça, verde, rosa (+ amarelo, laranja no genérico)
  Hot Pant: preto, coral, rosa, verde, azul   (Ocean→azul)

Adiciona como FRASE, deduplicando contra o que já existe no ad group.

Uso:
  python3 expansao_cores.py validate   # ensaio (validateOnly)
  python3 expansao_cores.py execute     # aplica (partialFailure ativado)
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'integracao', 'google-ads'))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

CORES_BIQUINI = ['preto', 'coral', 'onça', 'verde', 'rosa']
CORES_BIQUINI_GEN = CORES_BIQUINI + ['amarelo', 'laranja']
CORES_HOTPANT = ['preto', 'coral', 'rosa', 'verde', 'azul']

# ad group id -> lista de frases-base (cada uma recebe " {cor}")
BASES = {
    # [011]-BIQUINI
    '198863640909': (['biquíni empina bumbum'], CORES_BIQUINI),         # A
    '198539014545': (['biquíni cortininha'], CORES_BIQUINI),            # B
    '199510871175': (['biquíni asa delta'], CORES_BIQUINI),             # C
    '198461972839': (['biquíni sem bojo'], CORES_BIQUINI),              # D (magro)
    '198461972879': (['biquíni esportivo'], CORES_BIQUINI),             # E
    '197525753725': (['biquíni fio dental'], CORES_BIQUINI),            # F (magro)
    '199510870215': (['biquíni'], CORES_BIQUINI_GEN),                   # G
    '198539015225': (['comprar biquíni'], CORES_BIQUINI),               # H
    # [012]-HOT-PANT
    '199510873375': (['hot pant manga longa'], CORES_HOTPANT),          # A
    # B (UV50) — atributo; sem expansão por cor
    '199510874375': (['hot pant surf'], CORES_HOTPANT),                 # C
    '198863644269': (['hot pant top nadador'], CORES_HOTPANT),          # D (magro)
    '199510875095': (['hot pant cropped'], CORES_HOTPANT),              # E (magro)
    '198863644549': (['hot pant fitness'], CORES_HOTPANT),              # F (magro)
    '199510872935': (['hot pant'], CORES_HOTPANT),                      # G
    '199510875335': (['comprar hot pant'], CORES_HOTPANT),              # H
}


def main(modo):
    validate = (modo == 'validate')
    c = GoogleAdsClient.from_env()
    cid = c.customer_id

    # keywords já existentes por ad group (para dedupe)
    ids = ','.join(BASES)
    existentes = {}
    for r in c.search(
        "SELECT ad_group.id, ad_group_criterion.keyword.text FROM ad_group_criterion "
        f"WHERE ad_group.id IN ({ids}) AND ad_group_criterion.type = KEYWORD "
        "AND ad_group_criterion.negative = false"):
        g = r['adGroup']['id']
        existentes.setdefault(g, set()).add(
            r['adGroupCriterion']['keyword']['text'].lower())

    ops, plano = [], []
    for gid, (bases, cores) in BASES.items():
        novas = []
        for base in bases:
            for cor in cores:
                kw = f'{base} {cor}'
                if kw.lower() in existentes.get(gid, set()):
                    continue
                novas.append(kw)
                ops.append({'create': {
                    'adGroup': f'customers/{cid}/adGroups/{gid}',
                    'status': 'ENABLED',
                    'keyword': {'text': kw, 'matchType': 'PHRASE'}}})
        if novas:
            plano.append((gid, novas))

    nomes = {r['adGroup']['id']: r['adGroup']['name']
             for r in c.search(f"SELECT ad_group.id, ad_group.name FROM ad_group WHERE ad_group.id IN ({ids})")}
    print(f'{len(ops)} novas keywords por cor em {len(plano)} ad groups:\n')
    for gid, novas in plano:
        print(f'  {nomes.get(gid, gid)} (+{len(novas)}): ' + ' · '.join(novas))

    try:
        resp = c.mutate('adGroupCriteria', ops, validate_only=validate)
    except GoogleAdsError as e:
        print(f'\nFALHA: HTTP {e.status}\n{e.body[:4000]}')
        sys.exit(1)

    if validate:
        print(f'\nVALIDAÇÃO OK — {len(ops)} keywords. Nada gravado. Rode "execute".')
    else:
        print(f'\nExpansão aplicada — {len(ops)} novas keywords por cor adicionadas.')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: expansao_cores.py validate|execute')
    main(sys.argv[1])
