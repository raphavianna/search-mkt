#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Corrige os 3 sitelinks ainda apontando para /search/?q= (e suaviza desc1).
Atualiza diretamente os assets via AssetService:mutate (updateMask).

  407254494838  "Empina Bumbum"      → /feminino/biquini/  + desc1 "Modelagem que valoriza"
  407254495465  "Biquíni Cortininha" → /feminino/biquini/
  407254497592  "Manga 3/4 e Longa"  → /feminino/biquini/hot-pant/

Uso: python3 corrige_sitelinks.py validate|execute
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'integracao', 'google-ads'))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

BASE = 'https://usezerohora.com.br'

# (asset_id, label, nova_url, nova_desc1 ou None para manter)
CORRECOES = [
    ('407254494838', 'Empina Bumbum',      BASE + '/feminino/biquini/',           'Modelagem que valoriza'),
    ('407254495465', 'Biquíni Cortininha', BASE + '/feminino/biquini/',           None),
    ('407254497592', 'Manga 3/4 e Longa',  BASE + '/feminino/biquini/hot-pant/', None),
]


def main(modo):
    validate = (modo == 'validate')
    c = GoogleAdsClient.from_env()
    cid = c.customer_id

    ops = []
    print(f'{len(CORRECOES)} sitelinks a corrigir:\n')
    for aid, label, nova_url, nova_desc1 in CORRECOES:
        rn = f'customers/{cid}/assets/{aid}'
        update = {'resourceName': rn, 'finalUrls': [nova_url]}
        mask_parts = ['final_urls']
        if nova_desc1:
            update['sitelinkAsset'] = {'description1': nova_desc1}
            mask_parts.append('sitelink_asset.description1')
        print(f'  "{label}"')
        print(f'    url → {nova_url}')
        if nova_desc1:
            print(f'    desc1 → "{nova_desc1}"')
        ops.append({'update': update, 'updateMask': ','.join(mask_parts)})

    print()
    try:
        c.mutate('assets', ops, validate_only=validate)
        print(f'{"VALIDAÇÃO OK — nada gravado" if validate else "APLICADO"}: '
              f'{len(ops)} sitelink(s) corrigidos.')
    except GoogleAdsError as e:
        print(f'FALHA: HTTP {e.status}\n{e.body[:4000]}')
        sys.exit(1)

    if validate:
        print('Rode "execute" para aplicar.')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: corrige_sitelinks.py validate|execute')
    main(sys.argv[1])
