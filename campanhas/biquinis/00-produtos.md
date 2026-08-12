# Etapa 0 — Base de produto | Linha Biquíni + Hot Pant (Use Zero Hora)

- **Campanha:** biquinis · **Objetivo:** conversão (venda) no site da marca.
- **Fonte de linha/preço/demanda:** vendas reais BaseLinker (`vendas.json`), período
  2026-01-01 a 2026-08-11. Coleta: 2026-08-12. Ver `reports/2026-08-12-leitura-vendas-linha-biquini-hotpant.md`.
- **Atributos de produto:** extraídos dos **próprios títulos de produto da loja** na base
  de vendas (reais). Composição/material exatos, preço vigente e frete **não** foram
  verificados ao vivo (site bloqueado por egress) — marcados como *pendente de verificação*.
- **URL final:** *pendente* (site bloqueado; sem Nuvemshop nesta sessão) — padrão do site é
  `usezerohora.com.br/produtos/<slug>-<id>/`.

## Escopo da linha
Duas categorias, tratadas como **duas sub-linhas** com economia distinta:

| Sub-linha | Un vendidas | Receita | Ticket mediano | Papel na campanha |
|---|---|---|---|---|
| **Biquíni** | 164 | R$ 12.620,94 | R$ 75 | Volume de entrada, ticket menor |
| **Hot Pant** | 171 | R$ 20.925,43 | R$ 141 | Ticket alto, campeão no Site Próprio |

> Nota estratégica: no **Site Próprio** (alvo da campanha) o **Hot Pant** puxa a receita
> (35 un / R$ 4.141 vs. Biquíni 24 un / R$ 1.849). Peso de budget deve refletir isso.

---

## Sub-linha BIQUÍNI — modelos por demanda real

| # | Modelo | Un | Receita | Preço real | Atributos (do título) | Proposta de valor p/ anúncio |
|---|---|---|---|---|---|---|
| 1 | **Biquíni Empina Bumbum** | 106 | R$ 8.370 | R$ 67–80 | cortininha, sem bojo, efeito empina bumbum | Campeão de vendas. Modelagem que empina o bumbum, cortininha sem bojo. |
| 2 | Biquíni Asa Delta Bicolor | 20 | R$ 1.488 | R$ 65–130 | asa delta, bicolor, top alça fixa | Top asa delta bicolor, alça fixa que sustenta. |
| 3 | Biquíni Cortininha Premium Empina Bumbum Sem Bojo | 18 | R$ 1.229 | R$ 67–70 | cortininha premium, empina bumbum, sem bojo | Versão premium da cortininha campeã. |
| 4 | Biquíni/Sunkini Hot Pant Top Faixa (Surf/Piscina/Futevôlei) | 7 | R$ 484 | R$ 76–77 | top faixa, esporte, surf/piscina/futevôlei | Biquíni esportivo que fica no lugar no surf e no futevôlei. |
| 5 | Biquíni Asa Delta Top Fixo | 4 | R$ 320 | R$ 77–80 | asa delta, top fixo | Top fixo asa delta, sem escorregar. |
| 6 | Outros (Amanda, Fio Dental, Hot Pant Cós Alto, UV50 Nadador) | 9 | R$ 749 | R$ 67–100 | variações de modelagem | Cauda: subir por relevância, não por volume. |

**Territórios de KW da sub-linha (a validar com volume):** biquíni empina bumbum,
biquíni cortininha, biquíni sem bojo, biquíni asa delta, biquíni bicolor, biquíni
esportivo/futevôlei, biquíni fio dental.

## Sub-linha HOT PANT — modelos por demanda real

| # | Modelo | Un | Receita | Preço real | Atributos (do título) | Proposta de valor p/ anúncio |
|---|---|---|---|---|---|---|
| 1 | **Hot Pant Manga 3/4** | 60 | R$ 8.607 | R$ 134–150 | manga 3/4, surf, proteção solar | Campeão hot pant. Manga 3/4 com proteção solar para surf. |
| 2 | Hot Pant Top Nadador | 34 | R$ 2.858 | R$ 75–299 | top nadador, esporte | Top nadador esportivo, liberdade de braço. |
| 3 | Hot Pant Top Manga 3/4 | 26 | R$ 3.763 | R$ 130–150 | top + manga 3/4, surf | Conjunto top manga 3/4 para esporte na água. |
| 4 | Hot Pant Top Alças Esporte | 19 | R$ 1.484 | R$ 70–299 | top alças, esporte | Top de alças para treino e praia. |
| 5 | Hot Pant Top Cropped Manga 3/4 Surf UV50 | 24+ | R$ 4.500+ | R$ 133–150 | cropped, manga 3/4, UV50, surf | Cropped manga 3/4 com proteção UV50 de verdade. |
| 6 | Hot Pant Top Fixo (com/sem metal) | 7 | R$ 695 | R$ 77–100 | top fixo, com/sem metal | Top fixo, acabamento com ou sem metal. |

**Territórios de KW da sub-linha (a validar com volume):** hot pant, hot pant manga longa,
hot pant proteção solar / UV50, hot pant surf, conjunto hot pant, hot pant top nadador,
hot pant fitness, hot pant cropped.

---

## Diferenciais de marca (para callouts/descrições, a confirmar na página)
Fabricação própria · cores vibrantes que aparecem no mar e nas fotos · foco surf/beachwear ·
envio rápido (prazo *pendente de verificação na página*). **Não usar preço/frete em anúncio
até coletar da página com data.**

## Consistência de entidade
Marca = **Use Zero Hora** (surf/beachwear). Nas KWs de marca, blindar a colisão com o
**jornal Zero Hora** (GZH/RBS) via negativas (notícia, jornal, rbs, gzh, assinatura).

## ⛔ Bloqueio para a Etapa 1 (volume)
Ordenar keywords "por volume" exige uma fonte de volume viva. Nesta sessão: KW Planner
(sem MCP), Semrush BR (sem unidades de API), site (bloqueado). **Aguardando decisão do
usuário sobre a fonte de volume** antes de ordenar por volume. Enquanto isso, a
priorização de produto já está ancorada na **demanda real de vendas** acima.
