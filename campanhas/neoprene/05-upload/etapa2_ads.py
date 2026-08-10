#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Etapa 2 — RSAs e extensões da campanha [007-SEARCH]-NEOPRENE.

Copy baseada exclusivamente em 00-produtos.md (infográficos de 2026-08-09).
Regras: sem preço, sem grade de roupa; numeração 34-44 da sapatilha liberada.

Uso:
  python3 etapa2_ads.py check      # valida limites de caracteres e gera 02-ads.md + CSVs
  python3 etapa2_ads.py validate   # validateOnly na API (nada é gravado)
  python3 etapa2_ads.py execute    # cria RSAs + extensões na conta (campanha segue PAUSED)
"""
import csv
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from upload_google_ads import access_token, headers_base, descobre_versao, http_json, env

BASE = os.path.dirname(os.path.abspath(__file__))
CAMPAIGN_ID = '24115053024'

URL_SAPATILHA = 'https://usezerohora.com.br/produtos/sapatilha-esportiva-neoprene-xlgci/'
URL_CAMISETA = 'https://usezerohora.com.br/produtos/camiseta-neoprene-cabo-frio-17xyv/'
URL_BERMUDA = 'https://usezerohora.com.br/produtos/bermuda-neoprene-joaquina-7x5hp/'
URL_HOME = 'https://usezerohora.com.br/'

D_SAPATILHA = [
    'Sapatilha de neoprene com solado antiderrapante e isolamento térmico. Do 34 ao 44.',
    'Três tecidos técnicos: solado de alta aderência, neoprene 1,5mm e punho elástico.',
    'Secagem rápida e leveza para praia, pedras, surf e esportes na água. Use Zero Hora.',
    'Proteção e aderência da areia ao costão. Compre direto da marca brasileira de surf.',
]
D_CAMISETA = [
    'Camiseta em neoprene Span/Flex 1,5mm com mangas de poliamida UV50. Térmica no mar.',
    'Elasticidade 360° para remar e surfar sem limitar o movimento. Resiste a cloro e sal.',
    'Enfrente a água fria com conforto térmico e toque macio na pele. Compre da marca.',
    'Feita para o surf: leve, flexível e durável. Use Zero Hora, marca brasileira de surf.',
]
D_BERMUDA = [
    'Bermuda de neoprene com cordão interno no cós: ajuste firme sem apertar na água.',
    'Fica no lugar em cada manobra. Etiqueta emborrachada resiste à água salgada e ao sol.',
    'Visual clean do mar para o dia a dia. Feita para a rotina de quem vive o surf.',
    'Compre direto da Use Zero Hora, marca brasileira de surf e beachwear.',
]

GRUPOS = {
    '199159715756': {  # [007-A]
        'nome': '[007-A]-SAPATILHA-AQUATICA-COMPRA',
        'url': URL_SAPATILHA, 'paths': ('neoprene', 'sapatilha'),
        'titulos': [
            'Sapatilha Aquática', 'Sapatilha Para Praia e Mar', 'Sapatilha Náutica',
            'Tênis Aquático de Neoprene', 'Solado Antiderrapante',
            'Aderência da Areia à Pedra', 'Isolamento Térmico', 'Secagem Rápida',
            'Leve e Confortável', 'Numeração do 34 ao 44', '3 Tecidos Técnicos',
            'Para Surf, SUP e Piscina', 'Use Zero Hora', 'Compre Direto da Marca',
            'Marca Brasileira de Surf'],
        'descricoes': D_SAPATILHA,
    },
    '199159715956': {  # [007-B]
        'nome': '[007-B]-SAPATILHA-NEOPRENE-COMPRA',
        'url': URL_SAPATILHA, 'paths': ('neoprene', 'sapatilha'),
        'titulos': [
            'Sapatilha de Neoprene', 'Meia de Neoprene', 'Bota de Surf em Neoprene',
            'Neoprene Nylon 1,5mm', 'Punho Elástico Duplo', 'Solado Antiderrapante',
            'Isolamento Térmico', 'Secagem Rápida', 'Aderência e Segurança',
            'Numeração do 34 ao 44', 'Proteção Dentro da Água', 'Leve e Flexível',
            'Use Zero Hora', 'Compre Direto da Marca', 'Feita Para o Surf'],
        'descricoes': D_SAPATILHA,
    },
    '199159715916': {  # [007-C]
        'nome': '[007-C]-SAPATILHA-AREIA-COMPRA',
        'url': URL_SAPATILHA, 'paths': ('neoprene', 'beach-tennis'),
        'titulos': [
            'Sapatilha Para Beach Tennis', 'Sapatilha Para Futevôlei',
            'Jogue na Areia Quente', 'Proteja os Pés na Areia',
            'Solado Antiderrapante', 'Leve e Confortável', 'Secagem Rápida',
            'Sapatilha Esportiva', 'Numeração do 34 ao 44', 'Sapatilha de Neoprene',
            'Aderência e Estabilidade', 'Do Jogo Para o Mar', 'Use Zero Hora',
            'Compre Direto da Marca', 'Marca Brasileira de Surf'],
        'descricoes': [
            'Sapatilha de neoprene com solado antiderrapante e isolamento térmico. Do 34 ao 44.',
            'Três tecidos técnicos: solado de alta aderência, neoprene 1,5mm e punho elástico.',
            'Secagem rápida e leveza para beach tennis, futevôlei e areia quente.',
            'Proteção e aderência para jogar na areia. Compre direto da marca brasileira.',
        ],
    },
    '199159715436': {  # [007-D]
        'nome': '[007-D]-CAMISETA-COMPRA',
        'url': URL_CAMISETA, 'paths': ('neoprene', 'camiseta'),
        'titulos': [
            'Camiseta de Neoprene', 'Camisa de Neoprene', 'Neoprene Span/Flex 1,5mm',
            'Mangas com Proteção UV50', 'Conforto Térmico no Mar', 'Elasticidade 360°',
            'Camisa Térmica Para Surf', 'Enfrente a Água Fria',
            'Resistente a Cloro e Sal', 'Toque Macio na Pele', 'Camiseta Cabo Frio',
            'Leve e Flexível', 'Use Zero Hora', 'Compre Direto da Marca',
            'Feita Para o Surf'],
        'descricoes': D_CAMISETA,
    },
    '199159715276': {  # [007-E]
        'nome': '[007-E]-BERMUDA-NEOPRENE-COMPRA',
        'url': URL_BERMUDA, 'paths': ('neoprene', 'bermuda'),
        'titulos': [
            'Bermuda de Neoprene', 'Bermuda Neoprene Joaquina', 'Cordão Interno no Cós',
            'Ajuste Firme Sem Apertar', 'Fica no Lugar na Manobra',
            'Resiste à Água Salgada', 'Visual Clean', 'Feita Para o Surf',
            'Etiqueta Emborrachada', 'Do Mar Para o Dia a Dia',
            'Conforto Dentro da Água', 'Não Descasca Nem Racha', 'Use Zero Hora',
            'Compre Direto da Marca', 'Marca Brasileira de Surf'],
        'descricoes': D_BERMUDA,
    },
    '199159715236': {  # [007-F]
        'nome': '[007-F]-BERMUDA-SURF-COMPRA',
        'url': URL_BERMUDA, 'paths': ('neoprene', 'bermuda'),
        'titulos': [
            'Bermuda de Surf', 'Bermuda Para Surfar', 'Bermuda de Neoprene',
            'Firme em Cada Onda', 'Cordão Interno no Cós', 'Ajuste Sem Apertar',
            'Resiste à Água Salgada', 'Feita Para o Surf', 'Conforto na Remada',
            'Visual Clean', 'Do Mar Para o Dia a Dia', 'Etiqueta Emborrachada',
            'Use Zero Hora', 'Compre Direto da Marca', 'Marca Brasileira de Surf'],
        'descricoes': D_BERMUDA,
    },
    '199159715196': {  # [007-G]
        'nome': '[007-G]-BERMUDA-NATACAO-COMPRA',
        'url': URL_BERMUDA, 'paths': ('neoprene', 'natacao'),
        'titulos': [
            'Bermuda Para Natação', 'Short Para Natação', 'Bermuda de Neoprene',
            'Treine em Águas Abertas', 'Conforto Total no Treino',
            'Cordão Interno no Cós', 'Ajuste Firme Sem Apertar',
            'Fica no Lugar no Treino', 'Resistente ao Uso Intenso', 'Visual Clean',
            'Etiqueta Emborrachada', 'Da Piscina ao Mar', 'Use Zero Hora',
            'Compre Direto da Marca', 'Marca Brasileira de Surf'],
        'descricoes': [
            'Bermuda de neoprene com cordão interno no cós: ajuste firme sem apertar na água.',
            'Conforto total para treinos na piscina e em águas abertas. Fica no lugar.',
            'Etiqueta emborrachada resistente à água salgada, ao sol e ao uso intenso.',
            'Compre direto da Use Zero Hora, marca brasileira de surf e beachwear.',
        ],
    },
    '199159715716': {  # [007-H]
        'nome': '[007-H]-SURF-VESTUARIO-COMPRA',
        'url': URL_CAMISETA, 'paths': ('neoprene', 'surf'),
        'titulos': [
            'Roupa de Surf', 'Roupa Para Surfar', 'Camiseta de Neoprene',
            'Camisa Térmica Para Surf', 'Neoprene Span/Flex 1,5mm',
            'Mangas com Proteção UV50', 'Conforto Térmico no Mar',
            'Elasticidade 360°', 'Surfe na Água Fria', 'Bermuda e Camiseta de Surf',
            'Feita Para o Surf', 'Resistente ao Sal', 'Use Zero Hora',
            'Compre Direto da Marca', 'Marca Brasileira de Surf'],
        'descricoes': [
            'Roupa de surf em neoprene: camiseta térmica 1,5mm com mangas UV50 e bermuda.',
            'Elasticidade 360° para remar e surfar sem limitar o movimento. Resiste ao sal.',
            'Enfrente a água fria com conforto térmico e toque macio na pele. Compre da marca.',
            'Feita para o surf: leve, flexível e durável. Use Zero Hora, marca brasileira de surf.',
        ],
    },
    '199159715676': {  # [007-I]
        'nome': '[007-I]-NATACAO-VESTUARIO-COMPRA',
        'url': URL_CAMISETA, 'paths': ('neoprene', 'natacao'),
        'titulos': [
            'Roupa Para Natação', 'Roupa de Neoprene', 'Camisa Neoprene Natação',
            'Conforto Térmico na Água', 'Neoprene Span/Flex 1,5mm',
            'Elasticidade 360°', 'Resistente ao Cloro', 'Treine em Águas Abertas',
            'Camiseta Térmica', 'Toque Macio na Pele', 'Proteção UV50 nas Mangas',
            'Nade Sem Sentir Frio', 'Use Zero Hora', 'Compre Direto da Marca',
            'Marca Brasileira de Surf'],
        'descricoes': [
            'Camisa de neoprene para natação: conforto térmico, elasticidade e resistência.',
            'Treine na piscina ou em águas abertas sem sentir frio. Neoprene Span/Flex 1,5mm.',
            'Resistente ao cloro, ao sal e ao uso intenso. Mantém cor e performance.',
            'Compre direto da Use Zero Hora, marca brasileira de surf e beachwear.',
        ],
    },
    '199159715476': {  # [007-J]
        'nome': '[007-J]-CATEGORIA-COMPRA',
        'url': URL_CAMISETA, 'paths': ('neoprene', 'linha'),
        'titulos': [
            'Roupa de Neoprene', 'Linha Neoprene Completa', 'Camiseta, Bermuda, Sapatilha',
            'Neoprene Span/Flex 1,5mm', 'Conforto Térmico no Mar',
            'Elasticidade e Liberdade', 'Feita Para o Surf',
            'Resistente à Água Salgada', 'Neoprene Para Surf e Mar', 'Secagem Rápida',
            'Tecidos Técnicos', 'Do Mar Para o Dia a Dia', 'Use Zero Hora',
            'Compre Direto da Marca', 'Marca Brasileira de Surf'],
        'descricoes': [
            'Linha neoprene Use Zero Hora: camiseta, bermuda e sapatilha para o mar.',
            'Tecidos técnicos com conforto térmico, elasticidade e resistência ao sal.',
            'Feita para o surf e para esportes na água. Performance em cada detalhe.',
            'Compre direto da Use Zero Hora, marca brasileira de surf e beachwear.',
        ],
    },
    '199159715516': {  # [007-K]
        'nome': '[007-K]-MARCA',
        'url': URL_HOME, 'paths': ('neoprene', 'oficial'),
        'pin_titulo_1': True,
        'titulos': [
            'Use Zero Hora', 'Site Oficial Use Zero Hora', 'Neoprene Use Zero Hora',
            'Linha Neoprene Completa', 'Camiseta, Bermuda, Sapatilha',
            'Marca Brasileira de Surf', 'Compre Direto da Marca', 'Feita Para o Surf',
            'Surf e Beachwear', 'Conforto Térmico no Mar', 'Sapatilha de Neoprene',
            'Bermuda de Neoprene', 'Camiseta de Neoprene', 'Etiqueta Emborrachada',
            'Performance e Qualidade'],
        'descricoes': [
            'Use Zero Hora: marca brasileira de surf e beachwear. Conheça a linha neoprene.',
            'Camiseta, bermuda e sapatilha de neoprene. Performance e qualidade em cada detalhe.',
            'Conforto térmico, elasticidade e resistência à água salgada. Feita para o surf.',
            'Compre direto da marca no site oficial da Use Zero Hora.',
        ],
    },
}

SITELINKS = [
    ('Sapatilha de Neoprene', 'Solado antiderrapante', 'Numeração do 34 ao 44', URL_SAPATILHA),
    ('Camiseta de Neoprene', 'Neoprene 1,5mm e mangas UV50', 'Conforto térmico no mar', URL_CAMISETA),
    ('Bermuda de Neoprene', 'Cordão interno no cós', 'Feita para o surf', URL_BERMUDA),
    ('Site Use Zero Hora', 'Marca brasileira de surf', 'Compre direto da marca', URL_HOME),
]
CALLOUTS = [
    'Secagem Rápida', 'Solado Antiderrapante', 'Proteção UV50', 'Neoprene 1,5mm',
    'Feito Para o Surf', 'Elasticidade 360°', 'Etiqueta Emborrachada', 'Marca Brasileira',
]
SNIPPET = ('Tipos', ['Camiseta', 'Bermuda', 'Sapatilha', 'Meia de Neoprene'])


def valida():
    erros = []
    for gid, g in GRUPOS.items():
        assert len(g['titulos']) == 15, f"{g['nome']}: {len(g['titulos'])} títulos"
        assert len(g['descricoes']) == 4, f"{g['nome']}: {len(g['descricoes'])} descrições"
        if len(set(g['titulos'])) != 15:
            erros.append(f"{g['nome']}: título duplicado")
        for t in g['titulos']:
            if len(t) > 30:
                erros.append(f"{g['nome']} título ({len(t)}): {t}")
        for d in g['descricoes']:
            if len(d) > 90:
                erros.append(f"{g['nome']} descrição ({len(d)}): {d}")
        for p in g['paths']:
            if len(p) > 15:
                erros.append(f"{g['nome']} path ({len(p)}): {p}")
    for t, d1, d2, _u in SITELINKS:
        if len(t) > 25: erros.append(f"sitelink título ({len(t)}): {t}")
        if len(d1) > 35: erros.append(f"sitelink desc ({len(d1)}): {d1}")
        if len(d2) > 35: erros.append(f"sitelink desc ({len(d2)}): {d2}")
    for c in CALLOUTS:
        if len(c) > 25: erros.append(f"callout ({len(c)}): {c}")
    for v in SNIPPET[1]:
        if len(v) > 25: erros.append(f"snippet valor ({len(v)}): {v}")
    if erros:
        print('\n'.join(erros))
        sys.exit(f'{len(erros)} violações de limite')
    print('limites ok: 11 grupos × (15 títulos ≤30 + 4 descrições ≤90), '
          f'{len(SITELINKS)} sitelinks, {len(CALLOUTS)} callouts, snippet.')


def gera_docs():
    md = ['# [Campanha Neoprene] 02 — Ads e setup de campanha', '',
          '> Copy baseada em `00-produtos.md` (infográficos de 2026-08-09).',
          '> Regras aplicadas: sem preço, sem grade de roupa; numeração 34–44 da',
          '> sapatilha liberada. Contagens verificadas por script',
          '> (`05-upload/etapa2_ads.py check`). Subida via API em 2026-08-09 —',
          '> ver `05-upload/registro-upload-2026-08-09.md`.', '',
          '## Setup da campanha', '',
          '- **Nome**: `[007-SEARCH]-NEOPRENE` (ID 24115053024) — **PAUSED**',
          '- Rede: Pesquisa Google (sem parceiros/Display) | Geo: Brasil (presença) | Idioma: pt',
          '- Lance: Maximizar conversões | Orçamento: R$30/dia (revisar antes de ativar)', '']
    for gid, g in GRUPOS.items():
        md += [f"## Ad group `{g['nome']}` (ID {gid})", '',
               f"- **URL final**: {g['url']}",
               f"- **Caminhos**: `/{g['paths'][0]}` ({len(g['paths'][0])}) `/{g['paths'][1]}` ({len(g['paths'][1])})",
               f"- **Pin**: {'título 1 fixado na posição 1 (marca)' if g.get('pin_titulo_1') else 'nenhum'}",
               '', 'Títulos (máx. 30):', '',
               '| # | Título | Chars |', '|---|---|---|']
        md += [f'| {i} | {t} | {len(t)} |' for i, t in enumerate(g['titulos'], 1)]
        md += ['', 'Descrições (máx. 90):', '', '| # | Descrição | Chars |', '|---|---|---|']
        md += [f'| {i} | {d} | {len(d)} |' for i, d in enumerate(g['descricoes'], 1)]
        md += ['']
    md += ['## Extensões da campanha', '',
           '### Sitelinks (título ≤25; descrições ≤35)', '',
           '| Título (n) | Desc 1 (n) | Desc 2 (n) | URL final |', '|---|---|---|---|']
    md += [f'| {t} ({len(t)}) | {d1} ({len(d1)}) | {d2} ({len(d2)}) | {u} |'
           for t, d1, d2, u in SITELINKS]
    md += ['', '### Callouts (≤25)', '', '| Callout | Chars |', '|---|---|']
    md += [f'| {c} | {len(c)} |' for c in CALLOUTS]
    md += ['', '### Snippet estruturado', '',
           f"- Cabeçalho: {SNIPPET[0]}",
           '- Valores: ' + ', '.join(f'`{v}` ({len(v)})' for v in SNIPPET[1]), '']
    open(os.path.join(BASE, '..', '02-ads.md'), 'w', encoding='utf-8').write('\n'.join(md))

    csvdir = os.path.join(BASE, '..', '03-csv')
    os.makedirs(csvdir, exist_ok=True)
    with open(os.path.join(csvdir, 'rsa.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Campaign', 'Ad Group', 'Ad type'] +
                   [f'Headline {i}' for i in range(1, 16)] + ['Headline 1 position'] +
                   [f'Description {i}' for i in range(1, 5)] +
                   ['Path 1', 'Path 2', 'Final URL', 'Ad Status'])
        for g in GRUPOS.values():
            w.writerow(['[007-SEARCH]-NEOPRENE', g['nome'], 'Responsive search ad'] +
                       g['titulos'] + (['1'] if g.get('pin_titulo_1') else ['']) +
                       g['descricoes'] + [g['paths'][0], g['paths'][1], g['url'], 'Enabled'])
    with open(os.path.join(csvdir, 'sitelinks.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Campaign', 'Sitelink text', 'Sitelink description line 1',
                    'Sitelink description line 2', 'Final URL'])
        for t, d1, d2, u in SITELINKS:
            w.writerow(['[007-SEARCH]-NEOPRENE', t, d1, d2, u])
    with open(os.path.join(csvdir, 'callouts.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Campaign', 'Callout text'])
        for c in CALLOUTS:
            w.writerow(['[007-SEARCH]-NEOPRENE', c])
    with open(os.path.join(csvdir, 'snippets.csv'), 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['Campaign', 'Structured snippet header', 'Structured snippet values'])
        w.writerow(['[007-SEARCH]-NEOPRENE', SNIPPET[0], '; '.join(SNIPPET[1])])
    print('02-ads.md e 03-csv/ gerados.')


def ops_ads(cid):
    ops = []
    for gid, g in GRUPOS.items():
        heads = []
        for i, t in enumerate(g['titulos'], 1):
            h = {'text': t}
            if i == 1 and g.get('pin_titulo_1'):
                h['pinnedField'] = 'HEADLINE_1'
            heads.append(h)
        ops.append({'adGroupAdOperation': {'create': {
            'adGroup': f'customers/{cid}/adGroups/{gid}',
            'status': 'ENABLED',
            'ad': {
                'finalUrls': [g['url']],
                'responsiveSearchAd': {
                    'headlines': heads,
                    'descriptions': [{'text': d} for d in g['descricoes']],
                    'path1': g['paths'][0],
                    'path2': g['paths'][1],
                },
            },
        }}})
    return ops


def ops_assets(cid):
    camp = f'customers/{cid}/campaigns/{CAMPAIGN_ID}'
    ops, links = [], []
    n = 1
    for t, d1, d2, u in SITELINKS:
        rn = f'customers/{cid}/assets/-{n}'; n += 1
        ops.append({'assetOperation': {'create': {
            'resourceName': rn, 'finalUrls': [u],
            'sitelinkAsset': {'linkText': t, 'description1': d1, 'description2': d2}}}})
        links.append((rn, 'SITELINK'))
    for c in CALLOUTS:
        rn = f'customers/{cid}/assets/-{n}'; n += 1
        ops.append({'assetOperation': {'create': {
            'resourceName': rn, 'calloutAsset': {'calloutText': c}}}})
        links.append((rn, 'CALLOUT'))
    rn = f'customers/{cid}/assets/-{n}'
    ops.append({'assetOperation': {'create': {
        'resourceName': rn,
        'structuredSnippetAsset': {'header': SNIPPET[0], 'values': SNIPPET[1]}}}})
    links.append((rn, 'STRUCTURED_SNIPPET'))
    for rn, ft in links:
        ops.append({'campaignAssetOperation': {'create': {
            'campaign': camp, 'asset': rn, 'fieldType': ft}}})
    return ops


def api(modo):
    cid = env('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')
    h = headers_base(access_token())
    v = descobre_versao(h)
    url = f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:mutate'
    print(f'API {v} | customer {cid} | modo: {modo}')

    if modo == 'validate':
        payload = {'mutateOperations': ops_assets(cid) + ops_ads(cid), 'validateOnly': True}
        resp, err = http_json(url, h, payload)
        if err:
            print('FALHA NA VALIDAÇÃO:')
            print(json.dumps(err[1], indent=2, ensure_ascii=False)[:8000])
            sys.exit(1)
        print('VALIDAÇÃO OK — 11 RSAs + extensões. Nada foi gravado.')
        return

    resp, err = http_json(url, h, {'mutateOperations': ops_assets(cid)})
    if err:
        print('FALHA assets:'); print(json.dumps(err[1], indent=2, ensure_ascii=False)[:8000]); sys.exit(1)
    print(f"assets ok — {len(resp['mutateOperationResponses'])} operações "
          f"({len(SITELINKS)} sitelinks + {len(CALLOUTS)} callouts + 1 snippet + vínculos)")

    resp, err = http_json(url, h, {'mutateOperations': ops_ads(cid), 'partialFailure': True})
    if err:
        print('FALHA RSAs:'); print(json.dumps(err[1], indent=2, ensure_ascii=False)[:8000]); sys.exit(1)
    criados = sum(1 for r in resp['mutateOperationResponses'] if r)
    print(f'RSAs ok — {criados}/11 criados')
    if resp.get('partialFailureError'):
        print(json.dumps(resp['partialFailureError'], indent=2, ensure_ascii=False)[:8000])


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] not in ('check', 'validate', 'execute'):
        sys.exit('uso: etapa2_ads.py check|validate|execute')
    valida()
    if sys.argv[1] == 'check':
        gera_docs()
    else:
        api(sys.argv[1])
