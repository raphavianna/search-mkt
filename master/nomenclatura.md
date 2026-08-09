# Padrão de nomenclatura

Segue e regulariza a convenção já vigente na conta (inventário de
2026-08-09 em `reports/`): `[001-PMAX]-PONCHO-FEMININO`,
`[003-SHOPPING] PONCHO-SHOPPING` etc. — com as inconsistências corrigidas
(sempre com colchetes e hífen, sem espaço).

## Campanha

```
[NNN-CANAL]-TEMA
```

- `NNN`: sequencial da conta (3 dígitos; próximo livre na criação — em
  2026-08-09 o próximo era 007);
- `CANAL`: `SEARCH` | `SHOPPING` | `PMAX`;
- `TEMA`: linha/categoria em caixa alta, hífens no lugar de espaços.
- Ex.: `[007-SEARCH]-NEOPRENE`.

## Ad group

```
TEMA-SUBTEMA | INTENCAO
```

- `INTENCAO`: `COMPRA` | `CONSIDERACAO` | `MARCA` | `CONCORRENTE` |
  `GENERICO`;
- Ex.: `CAMISETA-NEOPRENE | COMPRA`, `NEOPRENE-GENERICO | CONSIDERACAO`.

## Arquivos de campanha (repositório)

- Slug da pasta: `campanhas/<tema-curto>/` em minúsculas (ex.:
  `campanhas/neoprene/`);
- CSVs de subida: `03-csv/NN-entidade.csv`, mesmos nomes dos templates do
  master (`01-campanhas.csv`, `02-grupos-de-anuncio.csv`, ...).

## Ativos e listas

- Lista de negativas compartilhada (quando criada na conta):
  `NEG-MARCA-UZH` (biblioteca da marca) e `NEG-<TEMA>` (por campanha);
- Rótulos (labels), quando usados: `UZH-<TEMA>-<AAAA-MM>`.
