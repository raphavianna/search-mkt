#!/usr/bin/env python3
"""Divisão do grupo único de lycra em masculino / feminino / genérico.

Fonte única do plano: as estruturas abaixo geram **tanto os CSVs**
(registro auditável, no modelo oficial) **quanto a aplicação por API** —
os dois não podem divergir.

Uso (a partir de integracao/google-ads, com as variáveis de ambiente):
    python3 ../../manutencao/2026-08-09-lycra-split/plano.py            # CSVs + simulação
    python3 ../../manutencao/2026-08-09-lycra-split/plano.py --aplicar  # + grava na conta

Procedência da copy: as afirmações vêm do RSA que já roda na conta
(claims aprovados pela marca) e do contexto de marca do CLAUDE.md
(fabricação própria, envio em até 24h úteis, cores vibrantes). Nada foi
inferido de keyword — buscar "abertura para o polegar" não prova que o
produto tenha o recurso. Preço e promoção ficam de fora: exigem coleta
datada da página (Etapa 0), hoje bloqueada pela política de rede.
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
GRUPO_EXISTENTE_ID = "207497286628"
RSA_EXISTENTE_ID = "820176449671"

URL_MASC = "https://usezerohora.com.br/masculino/lycra-surf/"
URL_FEM = "https://usezerohora.com.br/feminino/lycra-surf1/"
# Genérico usa a masculina até existir uma coleção de lycra sem recorte
# de gênero (decisão do usuário em 2026-08-09).
URL_GEN = URL_MASC

GRUPO_MASC = "[006-A]-LYCRA-MASCULINA"
GRUPO_FEM = "[006-B]-LYCRA-FEMININA"
GRUPO_GEN = "[006-C]-LYCRA-GENERICO"

# (criterion_id, texto) — saem do grupo atual e entram no grupo do gênero
KWS_MASC = [
    ("349388089564", "lycra surf masculina"),
    ("1663507766063", "camisa de surfista masculina"),
    ("2421701992276", "camisa de surf masculina manga curta"),
    ("2496743000145", "camisa de lycra masculina uv50"),
]
KWS_FEM = [
    ("376947507286", "lycra surf feminina"),
    ("395352136238", "camiseta lycra feminina"),
    ("416638112773", "camisetas femininas surf"),
    ("417497928922", "camiseta lycra surf feminina"),
    ("418769937783", "camiseta para surf feminina"),
    ("430251980559", "blusa surf feminina"),
    ("2494012155976", "camiseta lycra feminina secagem rápida"),
    ("2494565019999", "camiseta lycra feminina para beach tennis"),
    ("2495418476768", "comprar camiseta lycra feminina"),
    ("2496336751605", "camiseta esportiva feminina proteção solar"),
    ("2496336752045", "camiseta lycra segunda pele feminina"),
    ("2496336753005", "camiseta lycra feminina modelagem anatômica"),
    ("2496721976850", "camisa de lycra feminina uv50"),
    ("2497386432191", "camiseta lycra feminina uv50"),
    ("2523706244324", "camiseta lycra feminina para corrida"),
]

COMUNS = [
    "Proteção UV Para o Surf",
    "Bloqueia Até 98% dos Raios",
    "Manga Longa e Manga Curta",
    "Lycra Para Esportes Aquáticos",
    "Para Surf, Praia e Piscina",
    "Fabricação Própria no Brasil",
    "Envio em Até 24h Úteis",
    "Use Zero Hora Surf Wear",
    "Compre no Site Oficial",
    "Cores Vibrantes no Mar",
    "Peça Agora, Receba em Casa",
]

RSA_MASC = {
    "titulos": [
        "Lycra de Surf Masculina",
        "Camiseta de Lycra Masculina",
        "Camisa UV Masculina de Surf",
        "Lycra Masculina Zero Hora",
    ] + COMUNS,
    "descricoes": [
        "Lycra masculina com proteção UV: bloqueia até 98% dos raios do sol. Peça no site.",
        "Camisetas de lycra para surf, praia e piscina. Manga longa e curta. Envio em 24h úteis.",
        "Fabricação própria no Brasil, nas cores vibrantes da Use Zero Hora. Receba em casa.",
        "Para surf, praia e esportes aquáticos. Compre direto da marca e receba em casa.",
    ],
    "path1": "lycra", "path2": "masculina", "url": URL_MASC,
}

RSA_FEM = {
    "titulos": [
        "Lycra de Surf Feminina",
        "Camiseta de Lycra Feminina",
        "Camisa UV Feminina de Surf",
        "Lycra Feminina Zero Hora",
    ] + COMUNS,
    "descricoes": [
        "Lycra feminina com proteção UV: bloqueia até 98% dos raios do sol. Peça no site.",
        "Camisetas de lycra para surf, praia e piscina. Manga longa e curta. Envio em 24h úteis.",
        "Fabricação própria no Brasil, nas cores vibrantes da Use Zero Hora. Receba em casa.",
        "Para surf, praia e esportes aquáticos. Compre direto da marca e receba em casa.",
    ],
    "path1": "lycra", "path2": "feminina", "url": URL_FEM,
}

# RSA que já roda: edição mínima — só os dois erros de grafia, a URL e os
# caminhos de exibição. Expandir de 9/3 para 15/4 fica para a Etapa 2,
# com dados de página.
RSA_GEN_CORRECOES = {
    "Camiseta de Lyrca Zero Hora": "Camiseta de Lycra Zero Hora",     # Lyrca -> Lycra
    "Para Surf e Esportes Áquaticos": "Para Surf e Esportes Aquáticos",  # acento
}


def validar_limites():
    erros = []
    for nome, rsa in (("MASCULINA", RSA_MASC), ("FEMININA", RSA_FEM)):
        if len(rsa["titulos"]) != 15:
            erros.append(f"{nome}: {len(rsa['titulos'])} títulos (esperado 15)")
        if len(rsa["descricoes"]) != 4:
            erros.append(f"{nome}: {len(rsa['descricoes'])} descrições (esperado 4)")
        if len(set(rsa["titulos"])) != len(rsa["titulos"]):
            erros.append(f"{nome}: títulos repetidos")
        for t in rsa["titulos"]:
            if len(t) > 30:
                erros.append(f"{nome}: título ({len(t)}) '{t}'")
        for d in rsa["descricoes"]:
            if len(d) > 90:
                erros.append(f"{nome}: descrição ({len(d)}) '{d}'")
        for p in ("path1", "path2"):
            if len(rsa[p]) > 15:
                erros.append(f"{nome}: {p} ({len(rsa[p])})")
    for texto in list(RSA_GEN_CORRECOES.values()):
        if len(texto) > 30:
            erros.append(f"GENERICO: título corrigido ({len(texto)}) '{texto}'")
    return erros


def header_of(nome):
    with open(os.path.join(OFICIAL, nome), encoding="utf-8-sig") as f:
        for row in csv.reader(f):
            if row and not row[0].lstrip().startswith("#"):
                return row


def escrever_csv(dest, template, linhas):
    hdr = header_of(template)
    with open(os.path.join(AQUI, dest), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(hdr)
        for d in linhas:
            faltando = [k for k in d if k not in hdr]
            assert not faltando, f"{dest}: colunas inexistentes {faltando}"
            w.writerow([d.get(c, "") for c in hdr])
    print(f"  {dest}: {len(linhas)} linhas")


def gerar_csvs():
    print("CSVs (registro auditável):")
    escrever_csv("01-grupos.csv", "ad_group_template.csv", [
        {"Row Type": "Ad group", "Action": "Edit", "Campaign ID": CAMPANHA_ID,
         "Campaign": CAMPANHA, "Ad group ID": GRUPO_EXISTENTE_ID,
         "Ad group": GRUPO_GEN},
        {"Row Type": "Ad group", "Action": "Add", "Campaign ID": CAMPANHA_ID,
         "Campaign": CAMPANHA, "Ad group": GRUPO_MASC,
         "Ad group type": "Standard", "Ad group status": "Enabled"},
        {"Row Type": "Ad group", "Action": "Add", "Campaign ID": CAMPANHA_ID,
         "Campaign": CAMPANHA, "Ad group": GRUPO_FEM,
         "Ad group type": "Standard", "Ad group status": "Enabled"},
    ])

    kws = []
    for grupo, lista in ((GRUPO_MASC, KWS_MASC), (GRUPO_FEM, KWS_FEM)):
        for _, texto in lista:
            kws.append({"Row Type": "Keyword", "Action": "Add",
                        "Campaign ID": CAMPANHA_ID, "Campaign": CAMPANHA,
                        "Ad group": grupo, "Keyword": texto,
                        "Type": "Phrase match", "Keyword status": "Enabled"})
    for crit_id, texto in KWS_MASC + KWS_FEM:
        kws.append({"Row Type": "Keyword", "Action": "Remove",
                    "Campaign ID": CAMPANHA_ID, "Campaign": CAMPANHA,
                    "Ad group ID": GRUPO_EXISTENTE_ID, "Ad group": GRUPO_GEN,
                    "Keyword ID": crit_id, "Keyword": texto})
    escrever_csv("02-keywords.csv", "keyword_template.csv", kws)

    linhas = []
    for grupo, rsa in ((GRUPO_MASC, RSA_MASC), (GRUPO_FEM, RSA_FEM)):
        d = {"Row Type": "Ad", "Action": "Add", "Ad status": "Enabled",
             "Campaign ID": CAMPANHA_ID, "Campaign": CAMPANHA,
             "Ad group": grupo, "Ad type": "Responsive search ad",
             "Path 1": rsa["path1"], "Path 2": rsa["path2"],
             "Final URL": rsa["url"]}
        for i, t in enumerate(rsa["titulos"], 1):
            d[f"Headline {i}"] = t
        for i, x in enumerate(rsa["descricoes"], 1):
            d[f"Description {i}"] = x
        linhas.append(d)
    escrever_csv("03-rsa.csv", "responsive_search_ad_template.csv", linhas)


def aplicar(gravar):
    c = GoogleAdsClient.from_env()
    cid = c.customer_id
    modo = "APLICAR" if gravar else "SIMULAÇÃO"
    print(f"\nAPI — conta {cid} | {modo}")

    def op(entidade, ops, rotulo):
        try:
            resp = c.mutate(entidade, ops, validate_only=not gravar)
        except GoogleAdsError as e:
            print(f"  FALHA em {rotulo} (HTTP {e.status}):\n{e.body[:900]}")
            sys.exit(1)
        print(f"  OK — {rotulo} ({len(ops)} op.)")
        return resp

    # 1. Renomear o grupo existente para GENERICO
    c.renomear("adGroups", [(GRUPO_EXISTENTE_ID, GRUPO_GEN)],
               validate_only=not gravar)
    print(f"  OK — grupo {GRUPO_EXISTENTE_ID} → {GRUPO_GEN}")

    # 2. Criar os dois grupos novos
    novos = [
        {"create": {"name": nome,
                    "campaign": f"customers/{cid}/campaigns/{CAMPANHA_ID}",
                    "status": "ENABLED", "type": "SEARCH_STANDARD"}}
        for nome in (GRUPO_MASC, GRUPO_FEM)
    ]
    resp = op("adGroups", novos, "criar grupos masculino e feminino")

    if not gravar:
        print("\nSimulação concluída — nada gravado. As etapas seguintes "
              "(keywords e anúncios) dependem dos IDs reais dos grupos "
              "novos, então só rodam com --aplicar.")
        return

    ids = [r["resourceName"].split("/")[-1] for r in resp["results"]]
    id_masc, id_fem = ids[0], ids[1]
    print(f"     {GRUPO_MASC} = {id_masc} | {GRUPO_FEM} = {id_fem}")

    # 3. Keywords nos grupos novos
    for grupo_id, lista in ((id_masc, KWS_MASC), (id_fem, KWS_FEM)):
        ops = [{"create": {"adGroup": f"customers/{cid}/adGroups/{grupo_id}",
                           "status": "ENABLED",
                           "keyword": {"text": texto, "matchType": "PHRASE"}}}
               for _, texto in lista]
        op("adGroupCriteria", ops, f"criar {len(ops)} KWs no grupo {grupo_id}")

    # 4. Remover as mesmas KWs do grupo genérico (evita competição interna)
    ops = [{"remove": f"customers/{cid}/adGroupCriteria/"
                      f"{GRUPO_EXISTENTE_ID}~{crit}"}
           for crit, _ in KWS_MASC + KWS_FEM]
    op("adGroupCriteria", ops, f"remover {len(ops)} KWs do grupo genérico")

    # 5. RSAs nos grupos novos
    for grupo_id, rsa in ((id_masc, RSA_MASC), (id_fem, RSA_FEM)):
        ops = [{"create": {
            "adGroup": f"customers/{cid}/adGroups/{grupo_id}",
            "status": "ENABLED",
            "ad": {"finalUrls": [rsa["url"]],
                   "responsiveSearchAd": {
                       "headlines": [{"text": t} for t in rsa["titulos"]],
                       "descriptions": [{"text": d} for d in rsa["descricoes"]],
                       "path1": rsa["path1"], "path2": rsa["path2"]}}}}]
        op("adGroupAds", ops, f"criar RSA no grupo {grupo_id}")

    # 6. Corrigir o RSA existente: URL, caminhos e as duas grafias erradas
    atual = c.search(
        "SELECT ad_group_ad.ad.responsive_search_ad.headlines, "
        "ad_group_ad.ad.responsive_search_ad.descriptions "
        f"FROM ad_group_ad WHERE ad_group_ad.ad.id = {RSA_EXISTENTE_ID}"
    )[0]["adGroupAd"]["ad"]["responsiveSearchAd"]
    titulos = [{"text": RSA_GEN_CORRECOES.get(h["text"], h["text"])}
               for h in atual["headlines"]]
    ops = [{"update": {
        "resourceName": f"customers/{cid}/ads/{RSA_EXISTENTE_ID}",
        "finalUrls": [URL_GEN],
        "responsiveSearchAd": {
            "headlines": titulos,
            "descriptions": [{"text": d["text"]} for d in atual["descriptions"]],
            "path1": "lycra", "path2": "surf"}},
        "updateMask": "finalUrls,responsiveSearchAd.headlines,"
                      "responsiveSearchAd.descriptions,"
                      "responsiveSearchAd.path1,responsiveSearchAd.path2"}]
    op("ads", ops, "corrigir RSA do grupo genérico (URL, caminhos, grafia)")

    print("\nReestruturação aplicada.")


def main():
    erros = validar_limites()
    if erros:
        print("Peças fora do limite — nada foi gerado:")
        for e in erros:
            print("  -", e)
        sys.exit(1)
    print("Limites de caracteres: OK (15 títulos ≤30 e 4 descrições ≤90 por RSA)\n")
    gerar_csvs()
    aplicar("--aplicar" in sys.argv)


if __name__ == "__main__":
    main()
