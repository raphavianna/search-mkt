#!/usr/bin/env python3
"""Reestruturação best-in-class da campanha [006-SEARCH]-LYCRA.

Contexto que define o desenho: campanha nova, R$15/dia, 0 conversões,
gastando 2,5% do orçamento. Com pouco dado, fragmentar custa mais do que
rende — o lance inteligente aprende no nível da campanha, mas **o RSA
aprende por anúncio**, então cada grupo a mais dilui o aprendizado de
combinação de títulos. Daí 3 grupos, não 8: o corte é a página de
destino, único eixo que muda para onde o clique vai.

Uso (a partir de integracao/google-ads):
    python3 ../../manutencao/2026-08-09-lycra-estrutura/plano.py
    python3 ../../manutencao/2026-08-09-lycra-estrutura/plano.py --aplicar
"""

import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "integracao", "google-ads"))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

AQUI = os.path.dirname(os.path.abspath(__file__))
OFICIAL = os.path.join(AQUI, "..", "..", "master", "templates-csv", "google-oficial")

CAMPANHA_ID = "24110422707"
CAMPANHA = "[006-SEARCH]-LYCRA"
G_MASC_ID, G_FEM_ID, G_GER_ID = "204785138331", "204785138371", "207497286628"
RSA_GER_ID = "820176449671"

URL_MASC = "https://usezerohora.com.br/masculino/lycra-surf/"
URL_FEM = "https://usezerohora.com.br/feminino/lycra-surf1/"
URL_GER = URL_MASC  # provisório até existir coleção sem recorte de gênero

RENOMEAR = [
    (G_MASC_ID, "[006-A]-UV-MASCULINA"),
    (G_FEM_ID, "[006-B]-UV-FEMININA"),
    (G_GER_ID, "[006-C]-UV-GERAL"),
]

# ✱ = colhida de termo de pesquisa real da conta (demanda comprovada)
KWS_NOVAS = {
    G_MASC_ID: [
        ("camisa uv masculina", "PHRASE"),
        ("camiseta uv masculina", "PHRASE"),
        ("blusa de proteção uv masculina", "PHRASE"),
        ("camiseta masculina de surf", "PHRASE"),
        ("camisa de lycra surf masculina", "PHRASE"),
        ("camiseta manga longa uv 50+ masculina", "EXACT"),
        ("camiseta com proteção solar masculina", "PHRASE"),
    ],
    G_FEM_ID: [
        ("blusa uv feminina", "PHRASE"),
        ("camisa uv feminina", "PHRASE"),
        ("blusa com proteção uv feminina", "PHRASE"),
        ("blusa com filtro solar feminina", "PHRASE"),
        ("camisa com proteção solar feminina", "PHRASE"),
        ("camiseta proteção solar feminina", "PHRASE"),
        ("camiseta feminina uv", "PHRASE"),
        ("camiseta uv 50 feminina", "PHRASE"),
        ("camiseta surf feminina", "PHRASE"),
        ("blusa surfista feminina", "PHRASE"),
    ],
    G_GER_ID: [
        ("camiseta uv", "EXACT"),
        ("blusa proteção uv", "EXACT"),
        ("roupa com proteção uv", "PHRASE"),
        ("roupa uva uvb", "PHRASE"),
        ("camisa proteção uv", "PHRASE"),
        ("camisetas com proteção uv", "PHRASE"),
        ("camiseta proteção uv manga longa", "PHRASE"),
        ("camisa manga longa proteção uv", "PHRASE"),
        ("camiseta para sol uv", "PHRASE"),
        ("camisa fator de proteção uv 50", "PHRASE"),
    ],
}

# Zero impressão desde o início: atributo/cor/modalidade sem volume.
# A cauda passa a ser colhida de termos de pesquisa (Etapa 3).
KWS_REMOVER = {
    G_GER_ID: [
        "camiseta lycra azul com preto", "camiseta lycra rosa com preto",
        "camiseta lycra preto com verde", "camiseta lycra surf bicolor",
        "camiseta lycra manga longa branca", "camiseta lycra manga longa azul",
        "camiseta lycra manga longa verde", "camiseta lycra manga longa preta",
        "camiseta lycra surf com dedal",
        "camiseta lycra com abertura para o polegar",
        "camiseta lycra surf secagem rápida",
        "camiseta lycra surf para stand up paddle",
        "camiseta lycra surf para natação", "camisetas surferas",
    ],
    G_FEM_ID: [
        "camiseta lycra feminina secagem rápida",
        "camiseta lycra feminina para beach tennis",
        "camiseta lycra segunda pele feminina",
        "camiseta lycra feminina modelagem anatômica",
        "camiseta lycra feminina para corrida",
    ],
}

NEG_CONCORRENTE = [
    "uv line", "uvline", "litoraneus", "litorânea", "litorâneos", "tempestal",
    "extreme uv", "uv action", "uv life", "uv motion", "dboaswim", "freesurf",
    "uvbeach", "brasil swim", "magah", "seaway", "lupo", "decathlon",
    "loja outside", "smolder", "surfstore", "teahupoo", "uaradei", "abreus",
    "faca na rede", "beach e fit",
]
NEG_CATEGORIA = [
    "pesca", "maiô", "maio", "maiôs", "natação", "natacao", "biquíni",
    "biquini", "kimono", "wetsuit", "neoprene", "bermuda", "calção", "calcao",
    "swimsuit", "térmica", "termica", "tecido", "bike", "ciclismo",
    "camisetas de corrida", "rayos", "swim",
]

COMUNS = [
    "Bloqueia Até 98% dos Raios",
    "Manga Longa e Manga Curta",
    "Para Surf, Praia e Piscina",
    "Fabricação Própria no Brasil",
    "Envio em Até 24h Úteis",
    "Use Zero Hora Surf Wear",
    "Compre no Site Oficial",
    "Cores Vibrantes no Mar",
    "Peça Agora, Receba em Casa",
]
DESC_COMUNS = [
    "Camisetas para surf, praia e piscina. Manga longa e curta. Envio em até 24h úteis.",
    "Fabricação própria no Brasil, nas cores vibrantes da Use Zero Hora. Receba em casa.",
    "Para surf, praia e esportes aquáticos. Compre direto da marca e receba em casa.",
]

RSAS = {
    G_MASC_ID: {
        "titulos": ["Camisa UV Masculina", "Camiseta com Proteção UV",
                    "Blusa UV Masculina de Surf", "Roupa com Proteção UV",
                    "Lycra de Surf Masculina", "Camiseta Manga Longa UV"] + COMUNS,
        "descricoes": ["Camisa com proteção UV masculina: bloqueia até 98% dos raios do sol."] + DESC_COMUNS,
        "path1": "protecao-uv", "path2": "masculina", "url": URL_MASC,
    },
    G_FEM_ID: {
        "titulos": ["Camisa UV Feminina", "Blusa com Proteção UV",
                    "Blusa UV Feminina de Surf", "Camiseta UV Feminina",
                    "Lycra de Surf Feminina", "Camiseta Manga Longa UV"] + COMUNS,
        "descricoes": ["Blusa com proteção UV feminina: bloqueia até 98% dos raios do sol."] + DESC_COMUNS,
        "path1": "protecao-uv", "path2": "feminina", "url": URL_FEM,
    },
    G_GER_ID: {
        "titulos": ["Camiseta com Proteção UV", "Roupa com Proteção UV",
                    "Blusa com Proteção UV", "Camisa UV Para Surf",
                    "Lycra de Surf Zero Hora", "Camiseta Manga Longa UV"] + COMUNS,
        "descricoes": ["Roupa com proteção UV que bloqueia até 98% dos raios do sol. Peça no site."] + DESC_COMUNS,
        "path1": "protecao-uv", "path2": "surf", "url": URL_GER,
    },
}

CALLOUTS = [
    "Bloqueia Até 98% do Sol", "Fabricação Própria",
    "Envio em 24h Úteis", "Manga Longa e Curta",
    "Cores Vibrantes", "Compra no Site Oficial",
]
SNIPPET = ("Tipos", ["Manga Longa", "Manga Curta", "Masculina", "Feminina",
                     "Proteção UV"])

# Campanha nova com 0 conversões: Maximizar conversões não tem sinal para
# aprender e por isso subliça (2,5% do orçamento). Maximizar cliques com
# teto compra o dado que falta. Continua sendo lance automático — o padrão
# do CLAUDE.md (nada de CPC manual) segue respeitado.
LANCE = {"biddingStrategyType": "TARGET_SPEND",
         "maximizeConversions": None, "targetSpend": {"cpcBidCeilingMicros": "2500000"}}


def validar():
    erros = []
    for gid, rsa in RSAS.items():
        if len(rsa["titulos"]) != 15:
            erros.append(f"{gid}: {len(rsa['titulos'])} títulos")
        if len(rsa["descricoes"]) != 4:
            erros.append(f"{gid}: {len(rsa['descricoes'])} descrições")
        if len(set(rsa["titulos"])) != 15:
            erros.append(f"{gid}: títulos repetidos")
        erros += [f"{gid}: título ({len(t)}) '{t}'" for t in rsa["titulos"] if len(t) > 30]
        erros += [f"{gid}: descrição ({len(d)}) '{d}'" for d in rsa["descricoes"] if len(d) > 90]
        erros += [f"{gid}: {p} ({len(rsa[p])})" for p in ("path1", "path2") if len(rsa[p]) > 15]
    erros += [f"callout ({len(x)}) '{x}'" for x in CALLOUTS if len(x) > 25]
    erros += [f"snippet ({len(v)}) '{v}'" for v in SNIPPET[1] if len(v) > 25]
    if len(CALLOUTS) < 6:
        erros.append("callouts abaixo do mínimo de 6")
    if len(SNIPPET[1]) < 3:
        erros.append("snippet abaixo do mínimo de 3 valores")
    return erros


def header_of(nome):
    with open(os.path.join(OFICIAL, nome), encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            if row and not row[0].lstrip().startswith("#"):
                return row


def csv_out(dest, template, linhas):
    hdr = header_of(template)
    with open(os.path.join(AQUI, dest), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        for d in linhas:
            assert not [k for k in d if k not in hdr], f"{dest}: coluna inválida"
            w.writerow([d.get(c, "") for c in hdr])
    print(f"  {dest}: {len(linhas)} linhas")


NOMES = dict(RENOMEAR)
MATCH_CSV = {"PHRASE": "Phrase match", "EXACT": "Exact match", "BROAD": "Broad match"}


def gerar_csvs():
    print("CSVs (registro auditável):")
    csv_out("01-grupos.csv", "ad_group_template.csv", [
        {"Row Type": "Ad group", "Action": "Edit", "Campaign ID": CAMPANHA_ID,
         "Campaign": CAMPANHA, "Ad group ID": gid, "Ad group": nome}
        for gid, nome in RENOMEAR])

    kws = []
    for gid, lista in KWS_NOVAS.items():
        for texto, match in lista:
            kws.append({"Row Type": "Keyword", "Action": "Add",
                        "Campaign ID": CAMPANHA_ID, "Campaign": CAMPANHA,
                        "Ad group ID": gid, "Ad group": NOMES[gid],
                        "Keyword": texto, "Type": MATCH_CSV[match],
                        "Keyword status": "Enabled"})
    for gid, lista in KWS_REMOVER.items():
        for texto in lista:
            kws.append({"Row Type": "Keyword", "Action": "Remove",
                        "Campaign ID": CAMPANHA_ID, "Campaign": CAMPANHA,
                        "Ad group ID": gid, "Ad group": NOMES[gid],
                        "Keyword": texto})
    csv_out("02-keywords.csv", "keyword_template.csv", kws)

    csv_out("03-negativas.csv", "ad_group_negative_keyword_template.csv", [
        {"Row Type": "Negative keyword", "Action": "Add", "Level": "Campaign",
         "Campaign ID": CAMPANHA_ID, "Campaign": CAMPANHA,
         "Negative keyword": t, "Type": "Phrase match",
         "Keyword status": "Enabled"}
        for t in NEG_CONCORRENTE + NEG_CATEGORIA])

    linhas = []
    for gid, rsa in RSAS.items():
        d = {"Row Type": "Ad", "Action": "Add", "Ad status": "Enabled",
             "Campaign ID": CAMPANHA_ID, "Campaign": CAMPANHA,
             "Ad group ID": gid, "Ad group": NOMES[gid],
             "Ad type": "Responsive search ad", "Path 1": rsa["path1"],
             "Path 2": rsa["path2"], "Final URL": rsa["url"]}
        for i, t in enumerate(rsa["titulos"], 1):
            d[f"Headline {i}"] = t
        for i, x in enumerate(rsa["descricoes"], 1):
            d[f"Description {i}"] = x
        linhas.append(d)
    csv_out("04-rsa.csv", "responsive_search_ad_template.csv", linhas)


def aplicar(gravar):
    c = GoogleAdsClient.from_env()
    cid = c.customer_id
    print(f"\nAPI — conta {cid} | {'APLICAR' if gravar else 'SIMULAÇÃO'}")
    vo = not gravar

    def op(ent, ops, rot):
        try:
            r = c.mutate(ent, ops, validate_only=vo)
        except GoogleAdsError as e:
            print(f"  FALHA em {rot} (HTTP {e.status}):\n{e.body[:800]}")
            sys.exit(1)
        print(f"  OK — {rot} ({len(ops)} op.)")
        return r

    # 1. Negativas (efeito imediato no CTR, risco zero)
    ops = [{"create": {"campaign": f"customers/{cid}/campaigns/{CAMPANHA_ID}",
                       "negative": True,
                       "keyword": {"text": t, "matchType": "PHRASE"}}}
           for t in NEG_CONCORRENTE + NEG_CATEGORIA]
    op("campaignCriteria", ops, f"{len(ops)} negativas de campanha")

    # 2. Renomear os grupos para o novo eixo (UV, não lycra)
    c.renomear("adGroups", RENOMEAR, validate_only=vo)
    print(f"  OK — renomear {len(RENOMEAR)} grupos")

    # 3. Keywords novas
    ops = [{"create": {"adGroup": f"customers/{cid}/adGroups/{gid}",
                       "status": "ENABLED",
                       "keyword": {"text": t, "matchType": m}}}
           for gid, lista in KWS_NOVAS.items() for t, m in lista]
    op("adGroupCriteria", ops, f"{len(ops)} keywords novas")

    # 4. Remover as sem impressão (precisa do criterion_id, buscado agora)
    alvo = {(gid, t) for gid, lista in KWS_REMOVER.items() for t in lista}
    ops = []
    for r in c.search("SELECT ad_group.id, ad_group_criterion.criterion_id, "
                      "ad_group_criterion.keyword.text FROM keyword_view "
                      f"WHERE campaign.id = {CAMPANHA_ID} "
                      "AND ad_group_criterion.status != 'REMOVED'"):
        chave = (r["adGroup"]["id"], r["adGroupCriterion"]["keyword"]["text"])
        if chave in alvo:
            ops.append({"remove": f"customers/{cid}/adGroupCriteria/"
                                  f"{chave[0]}~{r['adGroupCriterion']['criterionId']}"})
    if ops:
        op("adGroupCriteria", ops, f"remover {len(ops)} KWs sem impressão")

    # 5. RSAs — os dois novos entram como versão 2; o antigo (9 títulos) é
    #    substituído por um de 15, então o grupo geral deixa de rodar com
    #    anúncio abaixo do padrão do checklist.
    ops = [{"create": {"adGroup": f"customers/{cid}/adGroups/{gid}",
                       "status": "ENABLED",
                       "ad": {"finalUrls": [rsa["url"]],
                              "responsiveSearchAd": {
                                  "headlines": [{"text": t} for t in rsa["titulos"]],
                                  "descriptions": [{"text": d} for d in rsa["descricoes"]],
                                  "path1": rsa["path1"], "path2": rsa["path2"]}}}}
           for gid, rsa in RSAS.items()]
    op("adGroupAds", ops, f"criar {len(ops)} RSAs de 15 títulos")

    if gravar:
        op("adGroupAds", [{"remove": f"customers/{cid}/adGroupAds/"
                                     f"{G_GER_ID}~{RSA_GER_ID}"}],
           "remover o RSA antigo de 9 títulos")

    # 6. Extensões — a conta inteira não tinha nenhuma. Sitelink fica de
    #    fora: exige URL verificada e o site está bloqueado por rede.
    ops = [{"create": {"calloutAsset": {"calloutText": t}}} for t in CALLOUTS]
    ops.append({"create": {"structuredSnippetAsset":
                           {"header": SNIPPET[0], "values": SNIPPET[1]}}})
    resp = op("assets", ops, f"criar {len(CALLOUTS)} callouts + 1 snippet")

    if gravar:
        nomes = [r["resourceName"] for r in resp["results"]]
        vinculos = [{"create": {"campaign": f"customers/{cid}/campaigns/{CAMPANHA_ID}",
                                "asset": rn, "fieldType": "CALLOUT"}}
                    for rn in nomes[:len(CALLOUTS)]]
        vinculos.append({"create": {"campaign": f"customers/{cid}/campaigns/{CAMPANHA_ID}",
                                    "asset": nomes[-1],
                                    "fieldType": "STRUCTURED_SNIPPET"}})
        op("campaignAssets", vinculos, "vincular extensões à campanha")

    # 7. Lance: destravar alcance para a campanha conseguir gerar dado
    ops = [{"update": {"resourceName": f"customers/{cid}/campaigns/{CAMPANHA_ID}",
                       **{k: v for k, v in LANCE.items() if v is not None}},
            "updateMask": "biddingStrategyType,targetSpend.cpcBidCeilingMicros"}]
    op("campaigns", ops, "trocar lance para Maximizar cliques (teto R$2,50)")

    print("\nConcluído." if gravar else "\nSimulação concluída — nada gravado.")


def main():
    erros = validar()
    if erros:
        print("Peças fora do padrão — nada gerado:")
        [print("  -", e) for e in erros]
        sys.exit(1)
    print("Validação: 3 RSAs com 15 títulos ≤30 e 4 descrições ≤90; "
          f"{len(CALLOUTS)} callouts ≤25; snippet com {len(SNIPPET[1])} valores\n")
    gerar_csvs()
    aplicar("--aplicar" in sys.argv)


if __name__ == "__main__":
    main()
