# Auditoria de entrega — [007-SEARCH]-NEOPRENE (2026-08-10)

Fonte: Google Ads API v22 (GAQL), conta 261-461-7888, somente leitura.
Script: `campanhas/neoprene/05-upload/auditoria_entrega.py`.

## O número que explica a entrega

Dia 2026-08-09 (primeiro dia servindo): **2 impressões**, IS 9,99%.

| Métrica | Valor | Leitura |
|---|---|---|
| Parcela de impressões (IS) | 9,99% | entrou em ~10% dos leilões elegíveis |
| **Perda por RANK** | **85,7%** | ← o gargalo: Ad Rank insuficiente |
| Perda por budget | 4,8% | orçamento NÃO é o limitador |

## O que foi descartado na varredura (tudo limpo)

- **Campanha**: ENABLED, SERVING, início 2026-08-09; primary status
  `LEARNING (BIDDING_STRATEGY_LEARNING)`.
- **Anúncios**: 11/11 APPROVED (review concluído). Ad strength: 10×
  AVERAGE, 1× GOOD (sapatilha-areia).
- **Ad groups**: 11/11 ELIGIBLE.
- **Geo**: Brasil (2076), presença — correto. Idioma pt.
- **Negativas**: 72 na campanha (as que subimos); **nenhuma lista
  compartilhada aplicada**; **nenhuma negativa de conta**; sem conflito
  negativa×positiva detectado (nenhuma KW com status "bloqueada por
  negativa").
- **Conversão**: ação "Compra (usezerohora.com.br/)" PURCHASE, primária,
  ativa. Auto-tagging on. Moeda BRL.
- **KWs**: 241 ativas; 19 de cauda em `RARELY_SERVED` (esperado — termos
  de volume ~zero, ficam adormecidos sem prejudicar o resto); **1 KW
  REMOVIDA: "sapatilha de neoprene" (590/mês)** — não foi removida pelos
  nossos scripts; provavelmente excluída na interface. Vale restaurar.

## Diagnóstico

A campanha **não está travada — está no início da curva, perdendo leilão
por Ad Rank**, pela combinação:

1. **Maximizar conversões em campanha recém-criada, sem histórico de
   conversão próprio**: o smart bidding entra conservador e "compra"
   pouquíssimo leilão enquanto aprende (`BIDDING_STRATEGY_LEARNING`).
   Com ~1 dia servindo (anúncios só aprovaram ao longo do dia 09), o
   sistema quase não deu lances.
2. **Quality Score ainda inexistente**: KWs novas, sem CTR histórico, em
   conta sem histórico na categoria calçado/neoprene (a conta roda
   poncho, lycra e maiô). Ad Rank = lance × qualidade; os dois começam
   baixos.
3. **Ad strength AVERAGE** na maioria dos grupos — alavanca menor, mas
   soma no rank.

Não há nenhum bloqueio estrutural (política, geo, negativa, budget,
elegibilidade). A demanda existe; a campanha ainda não está pagando o
preço de entrada do leilão.

## Recomendações (em ordem de impacto)

1. **Trocar o lance de largada**: Maximizar conversões → **Maximizar
   cliques com teto de CPC (R$0,60–0,80)** por 2–4 semanas. No leilão de
   texto vazio deste nicho (CPC ref. R$0,03–0,28), isso força entrada,
   compra volume barato, constrói CTR/QS e alimenta o pixel. Voltar para
   Maximizar conversões (depois tCPA) com ≥15–30 conversões/30d.
2. **Subir o budget para R$50/dia durante o aprendizado** — sinaliza
   apetite ao sistema de lances; hoje a perda por budget é pequena, mas
   com a torneira do rank aberta o teto de R$30 fica apertado.
3. **Restaurar a KW "sapatilha de neoprene"** (frase, 590/mês) no grupo
   [007-B].
4. **Ad strength**: subir de AVERAGE para GOOD/EXCELLENT nos grupos-chave
   (mais títulos ecoando as KWs de maior volume do grupo, ex.:
   "Sapatilha Aquática Masculina/Feminina" no [007-A]).
5. **Não mexer** em geo, negativas e estrutura — estão corretos; e não
   julgar a campanha antes de ~7 dias servindo de fato.

## Contexto da conta (7d)

| Campanha | Imp | Cliques | Custo |
|---|---|---|---|
| [001-PMAX]-PONCHO-FEMININO | 6.275 | 120 | R$144,07 |
| [004-SHOPPING]-MAIO | 1.652 | 21 | R$79,36 |
| [005-SHOPPING]-LYCRA | 1.279 | 34 | R$65,38 |
| [003-SHOPPING]-PONCHO | 551 | 13 | R$57,59 |
| [002-SEARCH]-INSTITUCIONAL | 834 | 25 | R$46,72 |
| [006-SEARCH]-LYCRA | 526 | 25 | R$44,79 |
| [007-SEARCH]-NEOPRENE | 2 | 0 | R$0,00 |

A conta inteira gira ~R$60/dia; a 007 com R$30/dia é o segundo maior
budget da conta quando destravar.
