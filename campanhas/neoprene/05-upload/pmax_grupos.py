#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quebra a PMax 009 em 4 grupos de recursos: geral (existente, renomeado),
sapatilha, camiseta e bermuda — copy da 007, URL do produto, temas por cluster.
Imagens: banner + quadrada existentes como placeholder (usuário troca na mão)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from upload_google_ads import access_token, headers_base, descobre_versao, http_json, env

CAMP_ID = '24128612776'
AG_GERAL = '6739295430'
SQUARE_ID = '404749410353'

URL_SAP = 'https://usezerohora.com.br/produtos/sapatilha-esportiva-neoprene-xlgci/'
URL_CAM = 'https://usezerohora.com.br/produtos/camiseta-neoprene-cabo-frio-17xyv/'
URL_BER = 'https://usezerohora.com.br/produtos/bermuda-neoprene-joaquina-7x5hp/'

GRUPOS = {
    '[009-B]-SAPATILHA': {
        'url': URL_SAP,
        'itens': ['1569492220', '1569492221', '1569492222'],
        'titulos': ['Sapatilha Aquática', 'Sapatilha de Neoprene', 'Sapatilha Náutica',
                    'Meia de Neoprene', 'Solado Antiderrapante', 'Isolamento Térmico',
                    'Secagem Rápida', 'Numeração do 34 ao 44', '3 Tecidos Técnicos',
                    'Aderência da Areia à Pedra', 'Para Surf, SUP e Piscina',
                    'Leve e Confortável', 'Use Zero Hora', 'Compre Direto da Marca',
                    'Marca Brasileira de Surf'],
        'longos': ['Sapatilha com solado antiderrapante e isolamento térmico. Do 34 ao 44.',
                   'Sapatilha de neoprene para praia, pedras, surf e esportes na água. Use Zero Hora.',
                   'Três tecidos técnicos: solado de alta aderência, neoprene 1,5mm e punho elástico.'],
        'descs': ['Sapatilha de neoprene antiderrapante. Do 34 ao 44.',
                  'Três tecidos técnicos: solado de alta aderência, neoprene 1,5mm e punho elástico.',
                  'Secagem rápida e leveza para praia, pedras, surf e esportes na água. Use Zero Hora.',
                  'Proteção e aderência da areia ao costão. Compre direto da marca brasileira de surf.'],
        'temas': ['sapatilha aquatica', 'sapatilha aquatica feminina', 'sapatilha aquatica masculina',
                  'sapatilha nautica', 'sapatilha para praia', 'sapatilha de neoprene',
                  'meia de neoprene', 'meia de surf', 'bota de surf', 'bota de neoprene',
                  'tenis aquatico', 'sapato aquatico', 'sapatilha antiderrapante',
                  'sapatilha para piscina', 'sapatilha para agua', 'sapatilha de mergulho',
                  'sapatilha para pedras', 'sapatilha para cachoeira', 'sapatilha para rio',
                  'sapatilha para beach tennis', 'sapatilha para futevolei', 'sapatilha para areia',
                  'sapatilha esportiva', 'sapatilha para surf', 'calcado aquatico'],
    },
    '[009-C]-CAMISETA': {
        'url': URL_CAM,
        'itens': ['1569492206', '1569492207', '1569492210', '1569492211'],
        'titulos': ['Camiseta de Neoprene', 'Camisa de Neoprene', 'Neoprene Span/Flex 1,5mm',
                    'Mangas com Proteção UV50', 'Conforto Térmico no Mar', 'Elasticidade 360°',
                    'Camisa Térmica Para Surf', 'Enfrente a Água Fria', 'Resistente a Cloro e Sal',
                    'Toque Macio na Pele', 'Camiseta Cabo Frio', 'Leve e Flexível',
                    'Use Zero Hora', 'Compre Direto da Marca', 'Feita Para o Surf'],
        'longos': ['Camiseta em neoprene Span/Flex 1,5mm com mangas de poliamida UV50. Térmica no mar.',
                   'Elasticidade 360° para remar e surfar sem limitar o movimento. Resiste a cloro e sal.',
                   'Enfrente a água fria com conforto térmico e toque macio na pele. Use Zero Hora.'],
        'descs': ['Camiseta térmica de neoprene 1,5mm. Compre da marca.',
                  'Camiseta em neoprene Span/Flex 1,5mm com mangas de poliamida UV50. Térmica no mar.',
                  'Elasticidade 360° para remar e surfar sem limitar o movimento. Resiste a cloro e sal.',
                  'Feita para o surf: leve, flexível e durável. Use Zero Hora, marca brasileira de surf.'],
        'temas': ['camiseta de neoprene', 'camisa de neoprene', 'camisa neoprene surf',
                  'camisa termica para surf', 'camiseta termica para agua fria',
                  'blusa de neoprene', 'camisa neoprene manga longa', 'segunda pele neoprene',
                  'camisa neoprene natacao', 'jaqueta de neoprene', 'camiseta neoprene masculina',
                  'camiseta neoprene feminina', 'camisa de borracha surf', 'top de neoprene',
                  'roupa para agua fria', 'camiseta para surf', 'segunda pele para surf'],
    },
    '[009-D]-BERMUDA': {
        'url': URL_BER,
        'itens': ['1569492227', '1569492228', '1569492229', '1569492230'],
        'titulos': ['Bermuda de Neoprene', 'Bermuda Neoprene Joaquina', 'Bermuda de Surf',
                    'Bermuda Para Natação', 'Cordão Interno no Cós', 'Ajuste Firme Sem Apertar',
                    'Fica no Lugar na Manobra', 'Resiste à Água Salgada', 'Visual Clean',
                    'Feita Para o Surf', 'Etiqueta Emborrachada', 'Do Mar Para o Dia a Dia',
                    'Use Zero Hora', 'Compre Direto da Marca', 'Marca Brasileira de Surf'],
        'longos': ['Bermuda de neoprene com cordão interno no cós: ajuste firme sem apertar na água.',
                   'Fica no lugar em cada manobra. Etiqueta emborrachada resiste à água salgada e ao sol.',
                   'Da piscina ao mar: bermuda de neoprene feita para o surf e para o treino.'],
        'descs': ['Bermuda de neoprene feita para o surf. Compre da marca.',
                  'Bermuda de neoprene com cordão interno no cós: ajuste firme sem apertar na água.',
                  'Fica no lugar em cada manobra. Etiqueta emborrachada resiste à água salgada e ao sol.',
                  'Visual clean do mar para o dia a dia. Feita para a rotina de quem vive o surf.'],
        'temas': ['bermuda de neoprene', 'bermuda de surf', 'bermuda para surfar',
                  'bermuda para natacao', 'short de natacao', 'bermuda surfista', 'short surf',
                  'bermuda termica para agua', 'bermuda de flutuacao', 'shorts neoprene',
                  'bermuda para aguas abertas', 'bermuda para remada', 'bermuda masculina surf'],
    },
}


def valida():
    for nome, g in GRUPOS.items():
        assert len(g['titulos']) == 15 and len(set(g['titulos'])) == 15, nome
        assert all(len(t) <= 30 for t in g['titulos']), [t for t in g['titulos'] if len(t) > 30]
        assert all(len(t) <= 90 for t in g['longos']), nome
        assert len(g['descs'][0]) <= 60, (nome, len(g['descs'][0]))
        assert all(len(d) <= 90 for d in g['descs'][1:]), nome
        assert len(g['temas']) <= 25, nome
    print('limites ok')


def main():
    valida()
    cid = env('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')
    h = headers_base(access_token())
    v = descobre_versao(h)
    murl = f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:mutate'
    surl = f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:search'
    CAMP = f'customers/{cid}/campaigns/{CAMP_ID}'
    SQUARE = f'customers/{cid}/assets/{SQUARE_ID}'

    resp, err = http_json(surl, h, {'query': """
        SELECT asset.resource_name FROM asset
        WHERE asset.name = 'UZH Neoprene banner 1200x628'"""})
    if err or not resp.get('results'):
        sys.exit('banner não encontrado')
    BANNER = resp['results'][0]['asset']['resourceName']
    print(f'banner: {BANNER}')

    for nome, g in GRUPOS.items():
        asset_ops, link_ops = [], []
        n = [2]
        AG = f'customers/{cid}/assetGroups/-1'

        def novo_texto(texto):
            rn = f'customers/{cid}/assets/-{n[0]}'; n[0] += 1
            asset_ops.append({'assetOperation': {'create': {'resourceName': rn, 'textAsset': {'text': texto}}}})
            return rn

        def link(rn, ft):
            link_ops.append({'assetGroupAssetOperation': {'create': {'assetGroup': AG, 'asset': rn, 'fieldType': ft}}})

        for t in g['titulos']: link(novo_texto(t), 'HEADLINE')
        for t in g['longos']: link(novo_texto(t), 'LONG_HEADLINE')
        for d in g['descs']: link(novo_texto(d), 'DESCRIPTION')
        link(BANNER, 'MARKETING_IMAGE')
        link(SQUARE, 'SQUARE_MARKETING_IMAGE')

        ag_op = [{'assetGroupOperation': {'create': {
            'resourceName': AG, 'campaign': CAMP, 'name': nome,
            'finalUrls': [g['url']], 'status': 'ENABLED'}}}]

        lgf = []
        raiz = f'customers/{cid}/assetGroupListingGroupFilters/-1~-500'
        lgf.append({'assetGroupListingGroupFilterOperation': {'create': {
            'resourceName': raiz, 'assetGroup': AG, 'type': 'SUBDIVISION', 'listingSource': 'SHOPPING'}}})
        for i, iid in enumerate(g['itens']):
            lgf.append({'assetGroupListingGroupFilterOperation': {'create': {
                'resourceName': f'customers/{cid}/assetGroupListingGroupFilters/-1~-{600+i}',
                'assetGroup': AG, 'type': 'UNIT_INCLUDED', 'listingSource': 'SHOPPING',
                'parentListingGroupFilter': raiz, 'caseValue': {'productItemId': {'value': iid}}}}})
        lgf.append({'assetGroupListingGroupFilterOperation': {'create': {
            'resourceName': f'customers/{cid}/assetGroupListingGroupFilters/-1~-999',
            'assetGroup': AG, 'type': 'UNIT_EXCLUDED', 'listingSource': 'SHOPPING',
            'parentListingGroupFilter': raiz, 'caseValue': {'productItemId': {}}}}})

        resp, err = http_json(murl, h, {'mutateOperations': asset_ops + ag_op + link_ops + lgf})
        if err:
            print(f'FALHA {nome}:'); print(json.dumps(err[1], indent=2, ensure_ascii=False)[:3000]); sys.exit(1)
        novo = [r for r in resp['mutateOperationResponses'] if r.get('assetGroupResult')][0]['assetGroupResult']['resourceName']
        print(f'{nome}: {novo} ({len(g["itens"])} produtos)')

        ops2 = [{'assetGroupSignalOperation': {'create': {
            'assetGroup': novo, 'searchTheme': {'text': t}}}} for t in g['temas']]
        resp, err = http_json(murl, h, {'mutateOperations': ops2})
        if err:
            print(f'FALHA temas {nome}:'); print(json.dumps(err[1], indent=2, ensure_ascii=False)[:2000]); sys.exit(1)
        print(f'  {len(g["temas"])} search themes')

    resp, err = http_json(murl, h, {'mutateOperations': [{'assetGroupOperation': {
        'update': {'resourceName': f'customers/{cid}/assetGroups/{AG_GERAL}',
                   'name': '[009-A]-NEOPRENE-GERAL'},
        'updateMask': 'name'}}]})
    print('grupo geral renomeado' if not err else json.dumps(err[1])[:500])


if __name__ == '__main__':
    main()
