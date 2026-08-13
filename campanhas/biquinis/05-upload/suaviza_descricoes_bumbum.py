#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Suaviza descrições dos RSAs em [011-A]-EMPINA-BUMBUM-COMPRA (e qualquer
outro ad group das campanhas [011]/[012] que contenha as frases-alvo).

Substituições:
  "modelagem que levanta" → "modelagem que valoriza"
  "efeito que levanta"   → "caimento que valoriza"

Mantém o pinning existente. Aplica somente onde as frases-alvo forem
encontradas; demais descrições ficam intactas.

Uso: python3 suaviza_descricoes_bumbum.py validate|execute
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'integracao', 'google-ads'))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

CAMP_IDS = ('24136476223', '24136476898')  # [011]-BIQUINI, [012]-HOT-PANT

SUBSTITUICOES = [
    # mais específica primeiro — evita redundância ("valoriza e valoriza")
    ('modelagem que levanta e valoriza', 'modelagem que realça e valoriza'),
    ('modelagem que levanta', 'modelagem que valoriza'),
    ('efeito que levanta',    'caimento que valoriza'),
]


def suaviza(texto):
    t = texto
    for antes, depois in SUBSTITUICOES:
        t = t.replace(antes, depois)
    return t


def main(modo):
    validate = (modo == 'validate')
    c = GoogleAdsClient.from_env()

    ids = ','.join(CAMP_IDS)
    rows = c.search(
        "SELECT ad_group.name, ad_group_ad.ad.resource_name, "
        "ad_group_ad.ad.responsive_search_ad.descriptions "
        f"FROM ad_group_ad WHERE campaign.id IN ({ids}) "
        "AND ad_group_ad.status != 'REMOVED' "
        "AND ad_group_ad.ad.type = 'RESPONSIVE_SEARCH_AD'")

    ops = []
    for r in rows:
        ag_nome = r['adGroup']['name']
        ad_rn = r['adGroupAd']['ad']['resourceName']
        rsa = r['adGroupAd']['ad'].get('responsiveSearchAd', {})
        descs = rsa.get('descriptions', [])

        novas, alteradas = [], []
        for d in descs:
            txt_antes = d['text']
            txt_depois = suaviza(txt_antes)
            novo_d = {'text': txt_depois}
            if 'pinnedField' in d:
                novo_d['pinnedField'] = d['pinnedField']
            novas.append(novo_d)
            if txt_antes != txt_depois:
                alteradas.append((txt_antes, txt_depois))

        if not alteradas:
            continue

        print(f'[{ag_nome}]  {ad_rn}')
        for antes, depois in alteradas:
            print(f'  "{antes}"')
            print(f'  → "{depois}"')

        ops.append({
            'update': {
                'resourceName': ad_rn,
                'responsiveSearchAd': {'descriptions': novas},
            },
            'updateMask': 'responsive_search_ad.descriptions',
        })

    if not ops:
        print('Nenhuma frase-alvo encontrada nas descrições — nada a fazer.'); sys.exit(0)

    print(f'\n{len(ops)} RSA(s) com descrições a suavizar.\n')

    try:
        c.mutate('ads', ops, validate_only=validate)
        print(f'{"VALIDAÇÃO OK — nada gravado" if validate else "APLICADO"}: '
              f'{len(ops)} RSA(s) atualizados.')
    except GoogleAdsError as e:
        print(f'FALHA: HTTP {e.status}\n{e.body[:4000]}'); sys.exit(1)

    if validate:
        print('Rode "execute" para aplicar.')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: suaviza_descricoes_bumbum.py validate|execute')
    main(sys.argv[1])
