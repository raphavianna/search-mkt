# [Campanha <tema>] Etapa 2 — Ads e setup

> Toda peça declara a contagem ao lado: `texto (NN)`. Limites em
> `master/specs-limites-google-ads.md`. Peça acima do limite é defeito.
> Preço/promoção/frete só se coletados da página, com data.

## Setup da campanha

| Item | Valor | Racional |
|---|---|---|
| Nome | `[NNN-SEARCH]-<TEMA>` | nomenclatura do master |
| Rede | Pesquisa Google (sem parceiros, sem Display) | |
| Localização / idioma | Brasil / pt | |
| Estratégia de lance | Maximizar conversões <ou tCPA/tROAS> | <dado> |
| Orçamento diário | R$ <valor> | CPC médio × cliques estimados do cluster: <conta> |

## RSA — <NOME-DO-GRUPO | INTENCAO>

URL final: <url> · Caminhos: `/<path1>` (NN) `/<path2>` (NN)

**Títulos (15 × ≤30):**

| # | Título | NN | Pin |
|---|---|---|---|
| 1 | | | |

**Descrições (4 × ≤90):**

| # | Descrição | NN |
|---|---|---|
| 1 | | |

<!-- repetir por ad group -->

## Sitelinks (4+ · título ≤25 · descrições ≤35)

| Título | NN | Desc 1 | NN | Desc 2 | NN | URL |
|---|---|---|---|---|---|---|

## Callouts (6+ · ≤25)

| Texto | NN |
|---|---|

## Snippet estruturado (cabeçalho da lista fixa · valores ≤25)

Cabeçalho: <Tipos/Estilos/...>

| Valor | NN |
|---|---|

## Extensões adicionais (se aplicável)

<Promoção / preço / imagem — com requisitos atendidos e data de coleta.>

## Geração dos CSVs

Após aprovação deste arquivo: gerar `03-csv/01-…` a `05-…` no modelo
`master/templates-csv/` e rodar o checklist de lançamento.
