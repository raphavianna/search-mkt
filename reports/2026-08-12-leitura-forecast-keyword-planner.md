# Resumo de leitura — Forecast do Google Keyword Planner (linha Biquíni + Hot Pant)

- **Fonte:** Google Ads / Keyword Planner — *Keyword Forecasts* (export do usuário).
- **Arquivo original:** `Keyword_Forecasts_20260812_at_20_37_19.csv` (UTF-16), arquivado em
  `data/biquinis/2026-08-12-keyword-forecasts-google-planner.csv` (convertido p/ UTF-8).
- **Data de coleta:** 2026-08-12. **Janela do forecast:** 1–30 de setembro de 2026 (mês).
- **Estratégia simulada:** Maximize Conversions · Rede: Google Search · Local: Brasil (ID 2076).

## O que a base contém (e o que NÃO contém)
- **Contém:** forecast **agregado da campanha inteira** (todas as ~118 KWs juntas, rotuladas
  "Campaign1"), com segmentação por **dispositivo** e por **local**. É o nível "Total da campanha".
- **NÃO contém:** linhas **por keyword** nem por ad group (as colunas `Ad Group` e `Keyword`
  vêm vazias). Portanto **não dá para ordenar KW por volume individual a partir deste arquivo**.

## Números que a base sustenta (mês de setembro/2026)
| Métrica | Total | Desktop | Smartphone | Tablet |
|---|--:|--:|--:|--:|
| Cliques est. | 4.419,53 | 448,67 | 3.921,02 | 49,84 |
| Impressões est. | 78.684,38 | 7.339,49 | 71.077,15 | 267,74 |
| Custo est. (R$) | 649,80 | 91,30 | 551,58 | 6,92 |
| CTR est. | 5,6% | 6,1% | 5,5% | 18,6% |
| **CPC médio est. (R$)** | **0,15** | 0,20 | 0,14 | 0,14 |

- **Conversões est.:** 30/mês · **Conv. rate:** 0,68% · **CPA médio est.:** R$ 22,00.
- **Orçamento diário sugerido pelo Google:** **R$ 21,66/dia** (× 30 ≈ R$ 649,80/mês).

## Leituras
1. **CPC médio da linha é baixíssimo: R$ 0,15.** Keywords de nicho, pouca disputa paga →
   favorece Maximize Conversions e permite volume de clique com orçamento modesto.
2. **Mobile domina:** smartphone = 89% dos cliques est. Confirma fashion mobile-first →
   manter todos os dispositivos, criativos/LP mobile-first.
3. **CPA est. R$ 22 << ticket** (Biquíni mediana R$ 75; Hot Pant R$ 141). Margem larga entre
   custo de aquisição e ticket → sustenta migração futura a **tROAS** (Etapa 3).
4. **Escopo = só Search.** O forecast não inclui Shopping; o orçamento de Shopping segue
   provisório por outra lógica (catálogo D2C).

## Decisões que esta base sustenta
- **Calibrar o orçamento das 3 campanhas de Search** com âncora no número do Google
  (≈ R$ 22/dia no total para o conjunto Search em setembro), mantendo o split por
  ticket/demanda da Etapa 0. Ver `campanhas/biquinis/02-ads.md`.
- Usar **CPC R$ 0,15** como referência de custo da linha (nível campanha).

## O que esta base NÃO sustenta (precisa de outra fonte)
- **Volume/CPC por keyword** (para ordenar cada ad group por volume) → exige:
  (a) **Semrush BR** (`phrase_these`, consome créditos), ou
  (b) re-exportar o Keyword Planner em **nível de keyword** (aba de métricas históricas /
      tabela de palavras do plano: busca mensal média + lance de topo por termo).
