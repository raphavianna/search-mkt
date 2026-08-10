#!/usr/bin/env python3
"""Sitelinks da campanha [006-SEARCH]-LYCRA.

Só URLs confirmadas pelo usuário entram — o site está bloqueado pela
política de rede do ambiente, então inventar slug significaria arriscar
404 e reprovação do anúncio.

Desenho: 4 variantes de cor + a coleção do gênero oposto. Cor não
sustentou grupo de anúncio (as 8 KWs de cor tinham zero impressão e foram
removidas), mas é decisão real de compra — sitelink entrega o caminho
direto para a variante sem depender de volume de busca.

Vinculação **por grupo de anúncio**, não por campanha: assim o sitelink
da coleção nunca repete a URL final do próprio grupo, como manda o
checklist do master.

Uso (a partir de integracao/google-ads):
    python3 ../../manutencao/2026-08-09-lycra-sitelinks/plano.py
    python3 ../../manutencao/2026-08-09-lycra-sitelinks/plano.py --aplicar
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..",
                                "integracao", "google-ads"))
from gads import GoogleAdsClient, GoogleAdsError  # noqa: E402

G_MASC, G_FEM, G_GER = "204785138331", "204785138371", "207497286628"
NOME = {G_MASC: "[006-A]-UV-MASCULINA", G_FEM: "[006-B]-UV-FEMININA",
        G_GER: "[006-C]-UV-GERAL"}

P = "https://usezerohora.com.br/produtos/"
URL_MASC = "https://usezerohora.com.br/masculino/lycra-surf/"
URL_FEM = "https://usezerohora.com.br/feminino/lycra-surf1/"

# chave: (título ≤25, descrição 1 ≤35, descrição 2 ≤35, URL)
SITELINKS = {
    "preto": ("Camiseta UV Preta", "Manga longa com proteção UV50",
              "Preto liso, envio em 24h úteis",
              P + "camiseta-lycra-surf-uv50-manga-longa-preto-liso/"),
    "rosa": ("Camiseta UV Rosa", "Rosa liso, manga longa",
             "Proteção UV50, envio em 24h",
             P + "camiseta-lycra-surf-uv50-manga-longa-rosa-liso/"),
    "preto-amarelo": ("Preto com Amarelo", "Lycra bicolor de manga longa",
                      "Proteção UV50 para o surf",
                      P + "camiseta-lycra-surf-uv50-manga-longa-preto-com-amarelo-8zdld/"),
    "amarelo-preto": ("Amarelo com Preto", "Lycra bicolor de manga longa",
                      "Cores vibrantes no mar",
                      P + "camiseta-lycra-surf-uv50-manga-longa-amarelo-com-preto-t1cab/"),
    "col-masc": ("Lycra Masculina", "Coleção masculina de surf",
                 "Proteção UV para o mar", URL_MASC),
    "col-fem": ("Lycra Feminina", "Coleção feminina de surf",
                "Proteção UV para o mar", URL_FEM),
}

CORES = ["preto", "rosa", "preto-amarelo", "amarelo-preto"]
# Cada grupo recebe as 4 cores + a coleção que NÃO é a sua URL final.
POR_GRUPO = {
    G_MASC: CORES + ["col-fem"],
    G_FEM: CORES + ["col-masc"],
    G_GER: CORES + ["col-fem"],   # URL final do geral é a masculina
}

URL_FINAL_DO_GRUPO = {G_MASC: URL_MASC, G_FEM: URL_FEM, G_GER: URL_MASC}


def validar():
    erros = []
    for k, (t, d1, d2, url) in SITELINKS.items():
        if len(t) > 25:
            erros.append(f"{k}: título ({len(t)}) '{t}'")
        for d in (d1, d2):
            if len(d) > 35:
                erros.append(f"{k}: descrição ({len(d)}) '{d}'")
        if not url.startswith("https://"):
            erros.append(f"{k}: URL não é https")
    if len({s[3] for s in SITELINKS.values()}) != len(SITELINKS):
        erros.append("URLs repetidas entre sitelinks")
    for gid, chaves in POR_GRUPO.items():
        if len(chaves) < 4:
            erros.append(f"{NOME[gid]}: {len(chaves)} sitelinks (mínimo 4)")
        for k in chaves:
            if SITELINKS[k][3] == URL_FINAL_DO_GRUPO[gid]:
                erros.append(f"{NOME[gid]}: sitelink '{k}' repete a URL final")
    return erros


def main():
    erros = validar()
    if erros:
        print("Fora do padrão — nada aplicado:")
        [print("  -", e) for e in erros]
        sys.exit(1)

    print("Sitelinks (contagem de caracteres):")
    for k, (t, d1, d2, url) in SITELINKS.items():
        print(f"  '{t}' ({len(t)}) | '{d1}' ({len(d1)}) | '{d2}' ({len(d2)})")
    print("\nDistribuição por grupo:")
    for gid, chaves in POR_GRUPO.items():
        print(f"  {NOME[gid]}: {len(chaves)} — {', '.join(chaves)}")

    gravar = "--aplicar" in sys.argv
    c = GoogleAdsClient.from_env()
    cid = c.customer_id
    print(f"\nAPI — conta {cid} | {'APLICAR' if gravar else 'SIMULAÇÃO'}")

    ordem = list(SITELINKS)
    ops = [{"create": {"finalUrls": [SITELINKS[k][3]],
                       "sitelinkAsset": {"linkText": SITELINKS[k][0],
                                         "description1": SITELINKS[k][1],
                                         "description2": SITELINKS[k][2]}}}
           for k in ordem]
    try:
        resp = c.mutate("assets", ops, validate_only=not gravar)
    except GoogleAdsError as e:
        print(f"  FALHA (HTTP {e.status}):\n{e.body[:800]}")
        sys.exit(1)
    print(f"  OK — {len(ops)} sitelinks {'criados' if gravar else 'validados'}")

    if not gravar:
        print("\nSimulação concluída — nada gravado.")
        return

    rn = {k: r["resourceName"] for k, r in zip(ordem, resp["results"])}
    vinc = [{"create": {"adGroup": f"customers/{cid}/adGroups/{gid}",
                        "asset": rn[k], "fieldType": "SITELINK"}}
            for gid, chaves in POR_GRUPO.items() for k in chaves]
    try:
        c.mutate("adGroupAssets", vinc, validate_only=False)
    except GoogleAdsError as e:
        print(f"  FALHA ao vincular (HTTP {e.status}):\n{e.body[:800]}")
        sys.exit(1)
    print(f"  OK — {len(vinc)} vínculos de sitelink nos 3 grupos")


if __name__ == "__main__":
    main()
