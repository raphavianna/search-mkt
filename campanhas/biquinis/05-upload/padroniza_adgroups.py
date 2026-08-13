#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Padroniza a nomenclatura dos ad groups para o padrão da conta
`[NNN-<LETRA>]-DESCRICAO(-COMPRA)` (maiúsculas, sem acento, hífen).

Alcance:
- [011]-BIQUINI e [012]-HOT-PANT (criadas nesta sessão, ainda no formato "Tema | ...").
- [010]-SAIDA-DE-PRAIA (formato antigo "AGn · Nome" — despadronizado).

Renomeia só o campo `name` (gads.renomear usa updateMask='name'). Nada além do
nome é tocado; IDs, keywords, anúncios e URLs permanecem.

Uso:
  python3 padroniza_adgroups.py validate   # ensaio (validateOnly)
  python3 padroniza_adgroups.py execute     # aplica os renames
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', '..', '..', 'integracao', 'google-ads'))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

# id do ad group -> novo nome padronizado
RENAMES = {
    # [011]-BIQUINI (ordem por prioridade/campeão)
    '198863640909': '[011-A]-EMPINA-BUMBUM-COMPRA',
    '198539014545': '[011-B]-CORTININHA-COMPRA',
    '199510871175': '[011-C]-ASA-DELTA-COMPRA',
    '198461972839': '[011-D]-SEM-BOJO-COMPRA',
    '198461972879': '[011-E]-ESPORTIVO-SURF-FUTEVOLEI-COMPRA',
    '197525753725': '[011-F]-FIO-DENTAL-COMPRA',
    '199510870215': '[011-G]-GENERICO',
    '198539015225': '[011-H]-COMERCIAL-COMPRA',
    # [012]-HOT-PANT
    '199510873375': '[012-A]-MANGA-34-COMPRA',
    '199510874095': '[012-B]-PROTECAO-UV50-COMPRA',
    '199510874375': '[012-C]-SURF-COMPRA',
    '198863644269': '[012-D]-TOP-NADADOR-COMPRA',
    '199510875095': '[012-E]-CROPPED-COMPRA',
    '198863644549': '[012-F]-FITNESS-ESPORTE-COMPRA',
    '199510872935': '[012-G]-GENERICO',
    '199510875335': '[012-H]-COMERCIAL-COMPRA',
    # [010]-SAIDA-DE-PRAIA (despadronizado "AGn · ...")
    '198426814959': '[010-A]-SAIDA-DE-PRAIA-MARCA',
    '198426814999': '[010-B]-VESTIDO-SAIDA-PRAIA-COMPRA',
    '205940800264': '[010-C]-TRANSPARENCIA-TULE-COMPRA',
    '198426815479': '[010-D]-SAIA-DE-PRAIA-COMPRA',
    '205940800304': '[010-E]-CATEGORIA-GENERICO',
}


def main(modo):
    validate = (modo == 'validate')
    c = GoogleAdsClient.from_env()

    # mostra de/para (nome atual via GAQL)
    ids = ','.join(RENAMES)
    atuais = {r['adGroup']['id']: r['adGroup']['name']
              for r in c.search(f"SELECT ad_group.id, ad_group.name FROM ad_group "
                                f"WHERE ad_group.id IN ({ids})")}
    print(f'{len(RENAMES)} ad groups a padronizar:\n')
    for gid, novo in RENAMES.items():
        print(f'  {atuais.get(gid, "?"):42} ->  {novo}')

    try:
        c.renomear('adGroups', list(RENAMES.items()), validate_only=validate)
    except GoogleAdsError as e:
        print(f'\nFALHA: HTTP {e.status}\n{e.body[:4000]}')
        sys.exit(1)

    if validate:
        print('\nVALIDAÇÃO OK — nada gravado. Rode "execute" para aplicar.')
    else:
        print('\nRenomeações aplicadas na conta.')


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('validate', 'execute'):
        sys.exit('uso: padroniza_adgroups.py validate|execute')
    main(sys.argv[1])
