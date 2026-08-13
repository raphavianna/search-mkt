# search-mkt — Ferramenta de campanhas de Search da Use Zero Hora

Este repositório **é uma ferramenta, não uma campanha**. Ele serve para criar e operar
campanhas e projetos de search (Google Ads) de **qualquer categoria ou produto** da marca
Use Zero Hora (D2C surf/beachwear). O objetivo de toda campanha é **conversão (venda) no
site**, não tráfego.

## Estrutura do repositório
- **`master/`** — materiais reutilizáveis entre campanhas (esta pasta):
  - `00-specs-google-ads.md` — limites de caractere e requisitos de cada peça/extensão;
  - `padrao-nomenclatura.md` — nomenclatura de campanhas, ad groups e listas;
  - `checklist-lancamento.md` — checklist de qualidade antes de subir e antes de ativar;
  - `biblioteca-negativas.md` — negativas base da marca (colisão jornal Zero Hora + gerais);
  - `templates/` — modelos de `00-produtos.md`, `01-kws.md`, `02-ads.md`, `04-medicao.md`;
  - `templates-csv/` — modelos de CSV de importação do Google Ads Editor (cabeçalhos).
- **`campanhas/<slug>/`** — uma pasta por campanha: `00-produtos.md`, `01-kws.md`,
  `02-ads.md`, `03-csv/`, `04-medicao.md`.
- **`data/`** — bases fornecidas na mão (Excel/CSV), por campanha/tema, com nome datado e
  proveniência registrada.
- **`reports/`** — snapshots datados de Semrush/Similarweb e resumos de leitura das bases.

## Pipeline de campanha (uma etapa por vez)
- **Etapa 0 — Base de produto:** benefícios/atributos reais das URLs (WebFetch) → `00-produtos.md`.
- **Etapa 1 — Setup de KWs:** pesquisa por funil (Semrush BR), volume/CPC/competição,
  ad groups coesos, estrutura decidida por dados → `01-kws.md` + snapshot em `reports/`.
- **Etapa 2 — Ads e setup:** RSAs, extensões, negativas, setup e orçamento → `02-ads.md`
  + CSVs em `03-csv/`.
- **Etapa 3 — Medição e otimização:** plano de acompanhamento pós-lançamento → `04-medicao.md`.

## Regras de dados (resumo)
Toda métrica vem de chamada real de ferramenta nesta sessão, snapshot em `reports/`, ou
base em `data/` — nunca de memória. Registrar fonte, base e data. Copy de anúncio usa só
atributos que existem na página do produto. Ver `CLAUDE.md` para o contrato completo.

## Escopo atual
Campanhas de **Search** (texto). Arquitetura preparada para Shopping e Performance Max
(templates novos no master quando pedido), sem executá-los antes de pedido explícito.

O master evolui: aprendizado de campanha que sirva às próximas vira atualização de
template ou checklist.
