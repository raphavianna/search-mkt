#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aplica as URLs reais (via índice de busca) nos ad groups das campanhas
[011]-BIQUINI e [012]-HOT-PANT e REMOVE a [013]-MARCA (marca já coberta pela
[002-SEARCH]-INSTITUCIONAL existente).

Fonte das URLs: ../03-csv/links-reais-por-adgroup.csv (só as 2 campanhas).
Atualiza `ad.final_urls` de cada RSA (AdService) e remove a campanha 013.

Uso:
  python3 aplicar_urls_reais.py validate   # ensaio (validateOnly; nada muda)
  python3 aplicar_urls_reais.py execute     # aplica de verdade (campanhas seguem PAUSED)
"""
import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'integracao', 'google-ads'))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

BASE = os.path.dirname(os.path.abspath(__file__))
CSV_MAP = os.path.join(BASE, '..', '03-csv', 'links-reais-por-adgroup.csv')

CAMP_BIQUINI = '24136476223'
CAMP_HOTPANT = '24136476898'
CAMP_MARCA_REMOVER = '24136476661'   # [013]-MARCA — redundante, remover
CAMPS_MANTER = (CAMP_BIQUINI, CAMP_HOTPANT)


def carrega_map():
    """ad_group.name -> URL real (só campanhas de Biquíni e Hot Pant)."""
    m = {}
    for r in csv.DictReader(open(CSV_MAP, encoding='utf-8')):
        if r['Campaign'] in ('Search - Biquínis', 'Search - Hot Pant'):
            m[r['Ad Group']] = r['Final URL (real; via índice de busca)'].strip()
    return m


def main(modo):
    validate = (modo == 'validate')
    c = GoogleAdsClient.from_env()
    url_por_ag = carrega_map()

    # 1) descobrir os anúncios (RSA) de cada ad group nas 2 campanhas
    q = ("SELECT campaign.id, ad_group.name, ad_group_ad.ad.resource_name, "
         "ad_group_ad.ad.final_urls FROM ad_group_ad "
         f"WHERE campaign.id IN ({CAMP_BIQUINI},{CAMP_HOTPANT})")
    rows = c.search(q)
    ops = []
    plano = []
    for r in rows:
        ag = r['adGroup']['name']
        ad_rn = r['adGroupAd']['ad']['resourceName']
        atual = (r['adGroupAd']['ad'].get('finalUrls') or ['—'])[0]
        nova = url_por_ag.get(ag)
        if not nova:
            print(f'AVISO: sem URL no mapa para ad group "{ag}" — pulando')
            continue
        plano.append((ag, atual, nova))
        ops.append({
            'update': {'resourceName': ad_rn, 'finalUrls': [nova]},
            'updateMask': 'final_urls',
        })

    print(f'{len(ops)} anúncios a atualizar (de {len(rows)} encontrados):')
    for ag, atual, nova in plano:
        print(f'  {ag}\n      de:  {atual}\n      para: {nova}')

    # 2) aplicar updates de URL (AdService)
    try:
        c.mutate('ads', ops, validate_only=validate)
        print(f'\n[URLs] {"VALIDAÇÃO OK — nada gravado" if validate else "aplicadas na conta"} '
              f'({len(ops)} anúncios).')
    except GoogleAdsError as e:
        print(f'FALHA ao atualizar URLs: HTTP {e.status}\n{e.body[:4000]}')
        sys.exit(1)

    # 3) remover a campanha de marca redundante
    rem = [{'remove': f'customers/{c.customer_id}/campaigns/{CAMP_MARCA_REMOVER}'}]
    try:
        c.mutate('campaigns', rem, validate_only=validate)
        print(f'[Marca] [013]-MARCA {"validada p/ remoção (nada gravado)" if validate else "REMOVIDA da conta"}.')
    except GoogleAdsError as e:
        print(f'FALHA ao remover [013]-MARCA: HTTP {e.status}\n{e.body[:4000]}')
        sys.exit(1)

    if validate:
        print('\nEnsaio concluído. Rode "execute" para aplicar de verdade.')
    else:
        print('\nPronto: URLs reais aplicadas em Biquíni + Hot Pant; [013]-MARCA removida. '
              'Campanhas seguem PAUSED.')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: aplicar_urls_reais.py validate|execute')
    main(sys.argv[1])
