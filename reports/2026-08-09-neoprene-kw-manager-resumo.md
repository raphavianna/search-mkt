# Resumo de leitura — base recebida: export Keyword Manager (Semrush)

- **Arquivo original**: `data/neoprene/2026-08-09-neoprene-list-semrush-keyword-manager.csv`
- **Proveniência**: enviado pelo usuário nesta sessão (2026-08-09), export
  do Keyword Manager do Semrush, database `br`, lista curada
  "neoprene_list". Datas de referência: as do Semrush na data do export.
- **Conteúdo**: 298 KWs com Volume, KD, CPC (USD), densidade competitiva,
  intenção, SERP features, trend e concorrentes por keyword. Tópicos da
  lista: natação/triathlon (64), camisas de neoprene surf (36),
  bermudas/shorts (28), roupas completas/long johns (12), mergulho (11) e
  147 sem tópico (inclui o cluster sapatilha e a expansão da sessão).

## O que a base muda em relação à sessão

1. **Valida a expansão "n/c"** da sessão com métricas reais — destaques:
   "sapatilha beach tennis" + "sapatilha para beach tennis" (1.600 cada!),
   "sapatilha para cachoeira" (590), "meia neoprene" (390), "meia de
   neoprene" (320), "meia aquatica" (260), "camisa neoprene surf" (140),
   "sapatilha para mar" (140), "use zero hora" (50).
2. **Novos clusters trazidos pelo usuário**: natação (bermuda/roupa),
   surf vestuário, mergulho, long johns — parte aproveitável, parte
   fora do produto (roupa fechada) → classificação registrada no
   consolidado.
3. CPC em **USD** neste export (coluna "CPC (USD)"); vários termos de
   cauda com CPC 0.00 = sem dado de leilão.

## Decisões que a base sustenta

- Consolidado único em
  `campanhas/neoprene/kw-planner/kw-consolidada-neoprene.csv` (336 KWs,
  3 fontes deduplicadas: 298 do arquivo + lista colada pelo usuário +
  lista da sessão), com grupo, match sugerido e observação.
- Novos ad groups: `sapatilha-areia-compra` (beach tennis/futevolei,
  ~3.2k/mês), `bermuda-surf-compra` (~5.6k), `bermuda-natacao-compra`
  (~4.5k), `neoprene-surf-compra` (~6k), `neoprene-natacao-compra` (~7k),
  `neoprene-concorrencia` (criado a pedido, com recomendação de NÃO
  ativar mantida).
- 85 KWs marcadas `fora-da-campanha (observacao)` com motivo (produto
  não vendido, infantil, acessórios, lojas, marcas) — ficam registradas,
  não sobem na campanha sem decisão explícita.

## Limitações

- Trend e SERP features não incorporados ao consolidado (disponíveis no
  original em `data/`).
- Conflito de fontes (regra 7): para KWs presentes nas duas coletas
  Semrush, valem os números do export (mesma fonte, curadoria mais
  recente); divergências são pequenas (ex.: camiseta neoprene 210 vs 260).
