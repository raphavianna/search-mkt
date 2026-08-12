# Resumo de leitura — Vendas da linha Biquíni + Hot Pant

- **Fonte:** `zerohora-painel/public/data/vendas.json` (base BaseMestre v6 + API BaseLinker `getOrders`).
- **Conexão:** repositório painel (zerohora-painel), integração BaseLinker — fonte indicada pelo usuário para captura de SKU/linha.
- **Período:** 2026-01-01 a 2026-08-11 (`manifest.versao_dados: 3`, gerado 2026-08-12).
- **Data de coleta:** 2026-08-12.
- **Escopo do recorte:** categorias `BIQUINI` e `HOT PANT`, apenas linhas `aprovado = true`.

## O que a base contém
19 campos por linha de venda, incluindo: `produto` (nome + variação Tamanho/Cor),
`categoria` (classificada, confiança ALTA), `preco_unitario`, `valor_total`,
`quantidade`, `canal_analitico`, `data`, `id_cliente` (hash, sem PII).

## Limitações (registradas para não virar erro silencioso)
1. **`sku` vem vazio** (limitação conhecida da origem NuvemShop/BaseLinker). A chave de
   produto usada aqui é o **nome do modelo** (normalizado, sem a variação Tamanho/Cor).
2. **Só demanda realizada.** A base mostra o que **vendeu**, não o catálogo completo —
   SKUs sem venda no período não aparecem. Catálogo total exigiria Nuvemshop (MCP não
   registrado nesta sessão) ou o site (bloqueado por egress nesta sessão).
3. **URL de página de produto não está na base** e o site está bloqueado por egress —
   as URLs finais dos anúncios ficam **pendentes de verificação** (ver 00-produtos.md).
4. **Sem margem** na base — usaremos **preço** como proxy de valor de conversão e
   sinalizaremos a limitação, conforme decidido.
5. **Agosto/2026 incompleto** (dados até 11/08): não comparar o mês cheio.

## Números que a base sustenta
- Linha Biquíni+Hot Pant: **335 unidades**, **R$ 33.546,37** no período (~4% das 8.223
  linhas totais da loja — a linha é pequena vs. PONCHO/MAIO/VESTIDO).
- **Sazonalidade:** pico em **jan/2026 (132 un)**, queda progressiva; jun–jul estáveis
  (~32–34 un/mês). Confirma padrão de verão brasileiro → **pacing crescente rumo a
  nov–fev**. Coleta em ago = baixa temporada.
- **Canal-mix da linha (un):** Mercado Livre Full 151 · Mercado Livre 95 ·
  **Site Próprio 59** · Shopee 29 · Shein 1.
- **Site Próprio (alvo de conversão da campanha):** 59 un / R$ 5.990,42 —
  Hot Pant 35 un/R$ 4.141 **vende mais que** Biquíni 24 un/R$ 1.849, e com ticket maior.
- **Faixa de preço real (preço unitário vendido):**
  - Biquíni: min R$ 65 · mediana **R$ 75** · max R$ 130.
  - Hot Pant: min R$ 70 · mediana **R$ 141** · max R$ 299.

## Decisões que esta base sustenta
- **Priorização de produto** por demanda real (best-sellers) e por ticket.
- **Segmentação Shopping** por faixa de preço/ticket e por campeão de venda (custom_label).
- **Pacing sazonal** de orçamento (baixa agora, escala no verão).
- **Split por canal:** o site converte hot pant a ticket alto — peso relevante para a
  campanha de conversão no site.

## O que esta base NÃO sustenta (precisa de outra fonte)
- **Volume de busca / CPC / concorrência** das keywords → exige Google Keyword Planner
  (API não disponível como MCP nesta sessão) ou Semrush BR (sem unidades de API nesta
  sessão). **Bloqueio ativo** — ver decisão pendente no fim da Etapa 0.
- **URLs finais, composição/material exatos, preço vigente e frete** → exige o site
  (bloqueado) ou Nuvemshop (MCP ausente).
