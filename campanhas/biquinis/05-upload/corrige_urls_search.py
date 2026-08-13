#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Move os 4 ad groups ainda apontando para /search/?q= para URLs rastreáveis.
Preventivo: esses grupos estão aprovados hoje mas têm o mesmo risco dos 4 já
corrigidos (robots.txt provavelmente bloqueia /search/).

Ad groups:
  [011-B]-CORTININHA-COMPRA (198539014545) → /feminino/biquini/
  [011-C]-ASA-DELTA-COMPRA  (199510871175) → /feminino/biquini/
  [011-D]-SEM-BOJO-COMPRA   (198461972839) → /feminino/biquini/
  [012-E]-CROPPED-COMPRA    (199510875095) → /feminino/biquini/hot-pant/

Uso: python3 corrige_urls_search.py validate|execute
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'integracao', 'google-ads'))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

BASE_URL = 'https://usezerohora.com.br'

# ad_group_id → URL rastreável de destino
MAPA = {
    '198539014545': BASE_URL + '/feminino/biquini/',           # [011-B]-CORTININHA-COMPRA
    '199510871175': BASE_URL + '/feminino/biquini/',           # [011-C]-ASA-DELTA-COMPRA
    '198461972839': BASE_URL + '/feminino/biquini/',           # [011-D]-SEM-BOJO-COMPRA
    '199510875095': BASE_URL + '/feminino/biquini/hot-pant/',  # [012-E]-CROPPED-COMPRA
}


def main(modo):
    validate = (modo == 'validate')
    c = GoogleAdsClient.from_env()

    ids = ','.join(MAPA)
    rows = c.search(
        "SELECT ad_group.id, ad_group.name, ad_group_ad.ad.resource_name, "
        "ad_group_ad.ad.final_urls FROM ad_group_ad "
        f"WHERE ad_group.id IN ({ids}) AND ad_group_ad.status != 'REMOVED'")

    ops, plano = [], []
    for r in rows:
        ag_id = r['adGroup']['id']
        ag_nome = r['adGroup']['name']
        ad_rn = r['adGroupAd']['ad']['resourceName']
        atual = (r['adGroupAd']['ad'].get('finalUrls') or ['—'])[0]
        nova = MAPA[ag_id]
        plano.append((ag_nome, atual, nova))
        ops.append({
            'update': {'resourceName': ad_rn, 'finalUrls': [nova]},
            'updateMask': 'final_urls',
        })

    print(f'{len(ops)} anúncio(s) a atualizar:\n')
    for nome, atual, nova in plano:
        print(f'  {nome}')
        print(f'    de:   {atual}')
        print(f'    para: {nova}')

    if not ops:
        print('Nenhum anúncio encontrado nos ad groups alvo.'); sys.exit(0)

    try:
        c.mutate('ads', ops, validate_only=validate)
        print(f'\n{"VALIDAÇÃO OK — nada gravado" if validate else "APLICADO"}: '
              f'{len(ops)} anúncio(s) movidos para URLs rastreáveis.')
    except GoogleAdsError as e:
        print(f'FALHA: HTTP {e.status}\n{e.body[:4000]}'); sys.exit(1)

    if validate:
        print('Rode "execute" para aplicar.')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: corrige_urls_search.py validate|execute')
    main(sys.argv[1])
