# Padrão de nomenclatura — taxonomia oficial

Taxonomia definida em 2026-08-09 (aprovação do usuário): **números para
campanhas, letras para ad groups — e o ad group sempre carrega o número
da campanha-mãe**. Assim qualquer relatório (termos de pesquisa, GAQL,
planilha exportada) liga grupo ↔ campanha só pelo nome, e a ordenação
alfabética agrupa tudo junto.

## Campanha

```
[NNN-CANAL]-TEMA
```

- `NNN`: sequencial único da conta, 3 dígitos, nunca reutilizado
  (próximo livre em 2026-08-09: **007**);
- `CANAL`: `SEARCH` | `SHOPPING` | `PMAX`;
- `TEMA`: linha/categoria em caixa alta, hífens no lugar de espaços.

Ex.: `[007-SEARCH]-NEOPRENE`

## Ad group

```
[NNN-L]-SUBTEMA-INTENCAO
```

- `NNN`: **o mesmo número da campanha-mãe** (elo do grupo com a campanha);
- `L`: letra sequencial dentro da campanha (`A`, `B`, `C`…);
- `SUBTEMA`: produto/cluster do grupo;
- `INTENCAO`: `COMPRA` | `CONSIDERACAO` | `MARCA` | `CONCORRENTE` |
  `GENERICO`.

Ex. — campanha `[007-SEARCH]-NEOPRENE`:

```
[007-A]-CAMISETA-COMPRA
[007-B]-BERMUDA-COMPRA
[007-C]-SAPATILHA-COMPRA
[007-D]-NEOPRENE-GENERICO
```

## Estado da base instalada (auditoria 2026-08-09, em `reports/`)

A conta tem padrões mistos: `006-A-LYCRA-GERAL` (já quase no padrão),
`[001-MAIO-LANCAMENTOS]` dentro da campanha 004 (número não bate),
`Grupo de anúncios 1` (default), `PONCHO-01`. **Campanhas novas nascem na
taxonomia oficial; renomear a base instalada só com pedido explícito**
(renomear não apaga histórico de performance, mas muda relatórios e
regras salvas que filtram por nome).

## Arquivos de campanha (repositório)

- Slug da pasta: `campanhas/<tema-curto>/` em minúsculas (ex.:
  `campanhas/neoprene/`);
- CSVs de subida: `03-csv/NN-entidade.csv`, mesmos nomes dos templates do
  master (`01-campanhas.csv`, `02-grupos-de-anuncio.csv`, ...).

## Ativos e listas

- Lista de negativas compartilhada (quando criada na conta):
  `NEG-MARCA-UZH` (biblioteca da marca) e `NEG-NNN-<TEMA>` (por campanha);
- Rótulos (labels), quando usados: `UZH-<TEMA>-<AAAA-MM>`.
