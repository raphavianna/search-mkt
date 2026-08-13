#!/usr/bin/env python3
"""Aplica via API as renomeações descritas nos CSVs de manutenção.

Os CSVs de `manutencao/` continuam sendo a fonte auditável: este script
apenas executa o que está neles, em vez de exigir upload manual. Só a
coluna de nome é aplicada (updateMask='name') — nenhum outro campo da
entidade pode ser alterado por aqui, mesmo que o CSV tenha valor nele.

Uso:
    python3 aplicar_rename.py <arquivo.csv> [<arquivo.csv> ...]      # simula
    python3 aplicar_rename.py <arquivo.csv> [...] --aplicar          # grava

Sem `--aplicar` roda em validateOnly: o Google valida tudo e não grava
nada. Rode sempre a simulação antes.
"""

import csv
import sys

from gads import GoogleAdsClient, GoogleAdsError

# Row Type do CSV → (recurso da API, coluna de ID, coluna de nome)
ENTIDADES = {
    "campaign": ("campaigns", "Campaign ID", "Campaign"),
    "ad group": ("adGroups", "Ad group ID", "Ad group"),
    "asset group": ("assetGroups", "Asset group ID", "Asset group"),
}


def ler(caminho):
    """Extrai (recurso, [(id, novo_nome)]) das linhas Action=Edit do CSV."""
    grupos = {}
    with open(caminho, newline="", encoding="utf-8-sig") as f:
        for linha in csv.DictReader(f):
            row_type = (linha.get("Row Type") or "").strip().lower()
            if row_type.startswith("#") or row_type not in ENTIDADES:
                continue
            if (linha.get("Action") or "").strip().lower() != "edit":
                continue
            recurso, col_id, col_nome = ENTIDADES[row_type]
            ent_id = (linha.get(col_id) or "").strip()
            nome = (linha.get(col_nome) or "").strip()
            if not ent_id:
                raise SystemExit(
                    f"{caminho}: linha sem '{col_id}' — renomear exige o ID "
                    "(sem ele o upload criaria uma entidade nova)."
                )
            if not nome:
                raise SystemExit(f"{caminho}: linha {ent_id} sem nome novo.")
            grupos.setdefault(recurso, []).append((ent_id, nome))
    return grupos


def main():
    args = [a for a in sys.argv[1:] if a != "--aplicar"]
    aplicar = "--aplicar" in sys.argv
    if not args:
        print(__doc__)
        sys.exit(2)

    client = GoogleAdsClient.from_env()
    print(f"Conta {client.customer_id} | API {client.api_version} | "
          f"modo: {'APLICAR (grava)' if aplicar else 'SIMULAÇÃO (não grava)'}")

    total = 0
    for caminho in args:
        print(f"\n{caminho}")
        for recurso, itens in ler(caminho).items():
            for ent_id, nome in itens:
                print(f"  {recurso[:-1]} {ent_id} → {nome}")
            try:
                client.renomear(recurso, itens, validate_only=not aplicar)
            except GoogleAdsError as e:
                print(f"  FALHA (HTTP {e.status}):\n{e.body}", file=sys.stderr)
                sys.exit(1)
            print(f"  OK — {len(itens)} {recurso} "
                  f"{'renomeados' if aplicar else 'validados'}")
            total += len(itens)

    if aplicar:
        print(f"\n{total} entidade(s) renomeada(s).")
    else:
        print(f"\n{total} entidade(s) validada(s), nada gravado. "
              "Repita com --aplicar para gravar.")


if __name__ == "__main__":
    main()
