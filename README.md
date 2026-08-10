# search-mkt — Ferramenta de campanhas de Search da Use Zero Hora

Repositório-ferramenta para criação e manutenção de campanhas de Search
Marketing (Google Ads) da **Use Zero Hora** (usezerohora.com.br), marca D2C
brasileira de surf/beachwear. Objetivo de toda campanha: **conversão (venda)
no site**.

## Estrutura

- `master/` — materiais reutilizáveis entre campanhas: specs de limites de
  caracteres do Google Ads, templates dos arquivos de campanha, templates
  CSV do Google Ads Editor, checklist de lançamento, padrão de nomenclatura
  e biblioteca de negativas da marca.
- `campanhas/<slug>/` — uma pasta por campanha: `00-produtos.md`,
  `01-kws.md`, `02-ads.md`, `03-csv/`, `04-medicao.md`.
- `data/` — bases fornecidas na mão (Excel/CSV), com nome datado e
  proveniência registrada.
- `reports/` — snapshots datados de Semrush/Similarweb e resumos de leitura
  das bases recebidas.

## Pipeline de campanha

0. **Base de produto** — coleta dos benefícios e atributos reais das
   páginas de produto.
1. **Setup de KWs** — pesquisa por funil (demanda geral, compra,
   consideração, awareness, concorrência, negativas) com dados reais
   (Semrush BR / Similarweb / bases próprias). Decisão de estrutura de
   campanha registrada com racional numérico.
2. **Ads e setup** — RSAs, extensões e CSVs de importação do Ads Editor.
3. **Medição e otimização** — plano pós-lançamento.

Regras completas de operação: ver `CLAUDE.md`.
