# HANDOFF COMPLETO — Campanha Search + Shopping | Linha Biquíni & Hot Pant (Use Zero Hora)

> **Como usar este arquivo em outra conversa:** cole o bloco abaixo como primeira mensagem,
> anexando este mesmo arquivo. Ele é autocontido — traz estrutura, copy, keywords,
> extensões, negativas, Shopping, medição, guia de importação e os CSVs embutidos.

```
Você é um engenheiro de search marketing. Anexei o HANDOFF COMPLETO de uma campanha de
Google Ads (Search + Shopping) para a linha de biquínis + hot pants da Use Zero Hora,
orientada a conversão no site. A campanha já está estruturada e validada. Preciso que você:
1) Gere/entregue os CSVs de importação do Google Ads Editor a partir das seções embutidas;
2) Me guie na importação (tudo deve subir PAUSADO);
3) Antes de ativar, feche as pendências: URLs finais por ad group, volume/CPC do Semrush
   (reordenar KW por volume e calibrar orçamento) e custom_labels do feed de Shopping.
Mantenha português do Brasil e os limites de caractere do Google Ads.
```

---


# ETAPA 0 — BASE DE PRODUTO

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

---


# ETAPA 1 — KEYWORDS (SEED)

# Etapa 1 (parcial) — Lista SEED de keywords para rodar no Semrush

- **Campanha:** biquinis · **Objetivo:** conversão no site.
- **Status:** lista SEED **quebrada por ad group**, pronta para você colar no Semrush e
  puxar volume/CPC/concorrência (BR). O volume **ainda não está preenchido** — entra no
  retorno do Semrush. Ordenação final "por volume decrescente" acontece depois disso.
- **Total:** 118 keywords únicas · 18 ad groups · 3 campanhas de Search.
- **Arquivos:** `03-csv/kws-seed-biquinis.xlsx` (3 abas) · `03-csv/kws-seed-por-ag.csv` ·
  `03-csv/kws-seed-semrush-lotes.txt`.

## Como usar no Semrush
O `phrase_these` aceita **até 100 keywords por vez, separadas por `;`**. A aba
**"Lotes Semrush"** (e o `.txt`) já traz os 2 lotes prontos:
- **Lote 1:** 100 keywords · **Lote 2:** 18 keywords.
Cole cada lote no Keyword Overview / Bulk Analysis (database **BR**) e exporte
Volume, CPC, KD e Competição. Me devolve o export (ou coloca em `data/biquinis/`) que eu:
1. Preencho o volume em cada keyword;
2. **Ordeno cada ad group em volume decrescente** (requisito seu);
3. Consolido a estrutura final de ad groups **pelos dados** (volume × CPC × margem/preço),
   com racional numérico;
4. Sigo para a Etapa 2 (RSAs, extensões, Shopping, CSVs do Ads Editor).

## Abas do .xlsx
1. **KW por AG** — tabela completa: Campanha · Sub-linha · Ad Group · Intenção · Match sugerido · Keyword (com filtro).
2. **Todas as KW (colar SR)** — coluna única com as 118 keywords, para colagem direta.
3. **Lotes Semrush** — os 2 lotes já concatenados com `;`.

## Estrutura de ad groups (SEED)

### Campanha: Search - Biquínis
| Ad Group | Intenção | Nº KW |
|---|---|---|
| Biquíni \| Genérico | Consideração/Genérico | 10 |
| Biquíni \| Empina Bumbum (campeão 106 un) | Compra/Modelo | 8 |
| Biquíni \| Cortininha | Compra/Modelo | 7 |
| Biquíni \| Asa Delta | Compra/Modelo | 6 |
| Biquíni \| Sem Bojo | Compra/Atributo | 4 |
| Biquíni \| Esportivo/Surf/Futevôlei | Compra/Uso | 10 |
| Biquíni \| Fio Dental | Compra/Modelo | 3 |
| Biquíni \| Comercial | Fundo/Comercial | 9 |

### Campanha: Search - Hot Pant
| Ad Group | Intenção | Nº KW |
|---|---|---|
| Hot Pant \| Genérico | Consideração/Genérico | 7 |
| Hot Pant \| Manga 3/4 e Manga Longa (campeão 60 un) | Compra/Modelo | 7 |
| Hot Pant \| Proteção Solar UV50 | Compra/Atributo | 6 |
| Hot Pant \| Surf | Compra/Uso | 7 |
| Hot Pant \| Top Nadador | Compra/Modelo | 4 |
| Hot Pant \| Cropped | Compra/Modelo | 4 |
| Hot Pant \| Fitness/Esporte | Compra/Uso | 4 |
| Hot Pant \| Comercial | Fundo/Comercial | 8 |

### Campanha: Search - Marca e Consideração
| Ad Group | Intenção | Nº KW |
|---|---|---|
| Marca \| Use Zero Hora | Marca | 6 |
| Consideração \| Dúvidas (SEO) | Topo/SEO | 8 |

## Notas
- **Match sugerido = Frase** na maioria (equilíbrio alcance × intenção para conversão);
  os termos SEO/dúvida ficam em **Ampla** só para o Semrush medir o território — subir na
  mídia paga só se CPC/intenção justificarem.
- Sementes ancoradas nos **modelos reais de venda** (Etapa 0) + atributos reais dos títulos
  (empina bumbum, cortininha, asa delta, manga 3/4, UV50, nadador, cropped, surf).
- **Marca:** entidade Use Zero Hora (surf/beachwear); a colisão com o jornal Zero Hora será
  tratada por negativas na Etapa 2 (notícia, jornal, gzh, rbs, assinatura).
- Depois do retorno do Semrush, keywords irrelevantes que o volume revelar viram negativas;
  as relevantes de volume zero **sobem mesmo assim** (sua decisão), no fim da ordenação.

---


# ETAPA 2 — ANÚNCIOS, EXTENSÕES E SETUP

# Etapa 2 — Anúncios, extensões e setup | Campanha Biquínis + Hot Pant

- **Objetivo:** conversão no site. **Lance:** Maximizar conversões (todas as campanhas).
- **Contagem de caractere** ao lado de cada peça `(n/limite)`. Validado por script: **0 peças acima do limite**.
- **URLs finais:** provisórias por categoria — site bloqueado por egress; **verificar/ajustar para a página exata antes de importar**.
- **Preço/frete/prazo em copy:** não usados até verificação na página (regra de dados). Copy usa só atributos reais dos títulos de produto.

## Estrutura
3 campanhas de Search + 1 de Shopping. 18 ad groups de Search. Lance Maximizar conversões.

## Search - Biquínis
Caminhos de exibição: `biquini` (7/15) · `empina-bumbum` (13/15) — URL: /biquini (verificar)

### AG: Biquíni | Genérico
**Títulos (15):**
1. Biquíni Feminino da Marca (25/30) [fixado P1]
2. Biquíni de Praia e Surf (23/30)
3. Moda Praia Feminina (19/30)
4. Biquíni para o Verão (20/30)
5. Novos Modelos de Biquíni (24/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Biquínis da Use Zero Hora: fabricação própria e cores que aparecem no mar. (74/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Biquíni | Empina Bumbum
**Títulos (15):**
1. Biquíni Empina Bumbum (21/30) [fixado P1]
2. Cortininha Empina Bumbum (24/30)
3. Efeito que Levanta (18/30)
4. Empina Bumbum Sem Bojo (22/30)
5. Modelagem que Valoriza (22/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Peças para Surfar (17/30)
15. Estilo de Praia e Surf (22/30)

**Descrições (4):**
1. Biquíni empina bumbum cortininha, com modelagem que levanta e valoriza o corpo. (79/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Biquíni | Cortininha
**Títulos (15):**
1. Biquíni Cortininha (18/30) [fixado P1]
2. Cortininha Sem Bojo (19/30)
3. Cortininha Premium (18/30)
4. Alcinha Regulável (17/30)
5. Top Cortininha (14/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Biquíni cortininha da marca, com alcinha regulável e caimento que fica no lugar. (80/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Biquíni | Asa Delta
**Títulos (15):**
1. Biquíni Asa Delta (17/30) [fixado P1]
2. Top Asa Delta Fixo (18/30)
3. Asa Delta Bicolor (17/30)
4. Alça Fixa que Sustenta (22/30)
5. Top Asa Delta (13/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Biquíni asa delta com alça fixa que sustenta, em versões lisas e bicolor. (73/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Biquíni | Sem Bojo
**Títulos (15):**
1. Biquíni Sem Bojo (16/30) [fixado P1]
2. Top Sem Bojo (12/30)
3. Sem Enchimento (14/30)
4. Natural e Confortável (21/30)
5. Cortininha Sem Bojo (19/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Biquíni sem bojo, sem enchimento: leve, natural e confortável no corpo. (71/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Biquíni | Esportivo/Surf/Futevôlei
**Títulos (15):**
1. Biquíni para Surfar (19/30) [fixado P1]
2. Biquíni Esportivo (17/30)
3. Não Sai na Onda (15/30)
4. Biquíni de Futevôlei (20/30)
5. Top Fixo de Esporte (19/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Biquíni esportivo que não sai na onda: feito para surf, futevôlei e praia. (74/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Biquíni | Fio Dental
**Títulos (15):**
1. Biquíni Fio Dental (18/30) [fixado P1]
2. Fio Dental Cortininha (21/30)
3. Modelagem Cavada (16/30)
4. Tanga Fio Dental (16/30)
5. Marca de Sol Menor (18/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Biquíni fio dental cortininha, modelagem cavada que valoriza e marca menos. (75/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Biquíni | Comercial
**Títulos (15):**
1. Comprar Biquíni Online (22/30) [fixado P1]
2. Loja de Biquíni Online (22/30)
3. Biquíni Direto da Marca (23/30)
4. Comprar na Loja Oficial (23/30)
5. Biquíni com Envio Nacional (26/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Compre biquíni direto da Use Zero Hora, com envio para todo o Brasil. (69/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

## Search - Hot Pant
Caminhos de exibição: `hot-pant` (8/15) · `surf` (4/15) — URL: /hot-pant (verificar)

### AG: Hot Pant | Genérico
**Títulos (15):**
1. Hot Pant Feminino da Marca (26/30) [fixado P1]
2. Conjunto Hot Pant (17/30)
3. Hot Pant de Praia (17/30)
4. Moda Praia com Hot Pant (23/30)
5. Novos Modelos de Hot Pant (25/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Hot pant da Use Zero Hora: beachwear de fabricação própria, feito para o mar. (77/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Hot Pant | Manga 3/4 e Manga Longa
**Títulos (15):**
1. Hot Pant Manga 3/4 (18/30) [fixado P1]
2. Hot Pant Manga Longa (20/30)
3. Conjunto Manga 3/4 (18/30)
4. Top Manga 3/4 de Surf (21/30)
5. Cobre e Protege do Sol (22/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Hot pant manga 3/4 com proteção solar, feito para surfar sem se preocupar. (74/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Hot Pant | Proteção Solar UV50
**Títulos (15):**
1. Hot Pant Proteção UV50 (22/30) [fixado P1]
2. Proteção Solar UV50 (19/30)
3. Roupa com Proteção UV (21/30)
4. Protege na Água (15/30)
5. Feito para o Sol Forte (22/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Hot pant com proteção solar UV50 de verdade, para horas de sol dentro da água. (78/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Hot Pant | Surf
**Títulos (15):**
1. Hot Pant para Surfar (20/30) [fixado P1]
2. Roupa de Surf Feminina (22/30)
3. Conjunto de Surf (16/30)
4. Não Sai na Onda (15/30)
5. Feito para o Surf (17/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Hot pant de surf feminino: fica no lugar na onda e protege do sol e do atrito. (78/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Hot Pant | Top Nadador
**Títulos (15):**
1. Hot Pant Top Nadador (20/30) [fixado P1]
2. Top Nadador de Esporte (22/30)
3. Liberdade nos Braços (20/30)
4. Top Nadador Feminino (20/30)
5. Feito para o Movimento (22/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Hot pant top nadador: recorte esportivo que dá liberdade de braço na água. (74/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Hot Pant | Cropped
**Títulos (15):**
1. Hot Pant Cropped (16/30) [fixado P1]
2. Top Cropped de Surf (19/30)
3. Cropped Manga 3/4 (17/30)
4. Conjunto Cropped (16/30)
5. Estilo e Proteção (17/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Hot pant cropped manga 3/4: estilo com proteção, do surf à beira da piscina. (76/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Hot Pant | Fitness/Esporte
**Títulos (15):**
1. Hot Pant Fitness (16/30) [fixado P1]
2. Hot Pant de Academia (20/30)
3. Hot Pant de Esporte (19/30)
4. Do Treino à Praia (17/30)
5. Segunda Pele no Corpo (21/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Hot pant fitness que vai do treino à praia, como uma segunda pele no corpo. (75/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Hot Pant | Comercial
**Títulos (15):**
1. Comprar Hot Pant Online (23/30) [fixado P1]
2. Loja de Hot Pant (16/30)
3. Hot Pant Direto da Marca (24/30)
4. Comprar na Loja Oficial (23/30)
5. Conjunto com Envio Nacional (27/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Compre hot pant direto da Use Zero Hora, com envio para todo o Brasil. (70/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

## Search - Marca e Consideração
Caminhos de exibição: `use-zero-hora` (13/15) · `surf` (4/15) — URL: / (verificar)

### AG: Marca | Use Zero Hora
**Títulos (15):**
1. Use Zero Hora Oficial (21/30) [fixado P1]
2. Loja Oficial da Marca (21/30)
3. Surf e Beachwear (16/30)
4. Biquíni e Hot Pant (18/30)
5. Direto de Quem Fabrica (22/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Use Zero Hora: surf e beachwear de fabricação própria. Compre na loja oficial. (78/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

### AG: Consideração | Dúvidas (SEO)
**Títulos (15):**
1. Biquíni ou Hot Pant? (20/30) [fixado P1]
2. Qual Usar para Surfar (21/30)
3. Guia para Escolher (18/30)
4. Feito para o Surf (17/30)
5. Modelos para o Mar (18/30)
6. Fabricação Própria (18/30)
7. Feito para o Mar (16/30)
8. Direto da Marca (15/30)
9. Envio para Todo o Brasil (24/30)
10. Cores que Saem na Foto (22/30)
11. Moda Praia e Surf (17/30)
12. Beachwear com Assinatura (24/30)
13. Compre Online Agora (19/30)
14. Modelagem que Valoriza (22/30)
15. Peças para Surfar (17/30)

**Descrições (4):**
1. Não sabe qual escolher para surfar? Conheça os modelos da Use Zero Hora. (72/90)
2. Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora. (79/90)
3. Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto. (75/90)
4. Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo. (76/90)

## Extensões (compartilhadas)
**Sitelinks (título ≤25 · 2 descrições ≤35):**
- **Biquínis** (8/25) — Empina bumbum e cortininha (26/35) · Modelos que valorizam o corpo (29/35)
- **Hot Pants** (9/25) — Manga 3/4 e proteção UV50 (25/35) · Feito para surfar sem sol (25/35)
- **Novidades** (9/25) — Últimos lançamentos da marca (28/35) · Moda praia e surf feminina (26/35)
- **Trocas e Envio** (14/25) — Envio para todo o Brasil (24/35) · Troca fácil pelo site (21/35)
- **Quem Somos** (10/25) — Marca de surf e beachwear (25/35) · Fabricação própria desde 2023 (29/35)

**Frases de destaque / callouts (≤25):**
- Fabricação própria (18/25)
- Envio para todo o Brasil (24/25)
- Cores que saem na foto (22/25)
- Feito para surfar (17/25)
- Proteção solar UV50 (19/25)
- Modelagem que valoriza (22/25)
- Direto da marca (15/25)
- Troca fácil (11/25)

**Snippets estruturados (valores ≤25):**
- **Tipos:** Biquíni (7/25) · Hot pant (8/25) · Cortininha (10/25) · Asa delta (9/25) · Top nadador (11/25) · Fio dental (10/25)
- **Estilos:** Empina bumbum (13/25) · Manga 3/4 (9/25) · Sem bojo (8/25) · Cropped (7/25) · Proteção UV50 (13/25) · Esportivo (9/25)

## Negativas (lista compartilhada nas campanhas)
- **Marca/Jornal (colisão):** jornal, jornais, noticia, noticias, notícia, notícias, gzh, rbs, clicrbs, assinar, assinatura, jornal zero hora, zero hora jornal, edição, previsão do tempo
- **DIY/Tutorial:** molde, moldes, molde de biquini, como fazer, passo a passo, croche, crochê, costurar, costura, apostila, pdf, papel, de eva, feltro, para colorir, desenho, tutorial
- **Baixa intenção:** gratis, grátis, download, usado, usada, brecho, brechó, aluguel, alugar, atacado, revenda, segunda mao, segunda mão
- **Fora do alvo:** infantil, criança, crianca, bebe, bebê, masculino, boneca, roupa de boneca

## Campanha de Shopping
**Shopping - Biquíni & Hot Pant** · Lance: Maximizar conversões · feed assumido existente (não gerado).
Subdivisão de grupos de produto por custom_label:
- `custom_label_0` — sub-linha: biquini / hot_pant
- `custom_label_1` — campeão de venda: empina_bumbum / hotpant_manga_34 / demais
- `custom_label_2` — faixa de preço: ate_90 / 91_150 / 151_mais
- `custom_label_3` — estação: alta_verao (pacing)
- Negativas: mesma lista de negativas de Marca/Jornal + DIY + Baixa intenção.
- **Auditoria de título do feed** recomendada: em Shopping o título é o sinal de relevância — garantir que os títulos dos SKUs da linha tragam modelo + atributo (ex.: 'Hot Pant Manga 3/4 Proteção UV50').

## Setup e orçamento
- **Rede:** só Pesquisa (sem Display; sem parceiros de pesquisa no lançamento).
- **Local:** Brasil. **Idioma:** Português. **Dispositivos:** todos (fashion é mobile-first).
- **Estratégia de lance:** Maximizar conversões nas 4 campanhas. **Graduação:** ao acumular conversões suficientes por campanha/grupo, migrar para tCPA/tROAS derivado do ticket/margem (registrar gatilho na Etapa 3).
- **Orçamento diário provisório (baixa temporada, calibrar com CPC do Semrush):**
  | Campanha | R$/dia | Racional |
  |---|---|---|
  | Shopping | 25 | maior conversão em D2C; cobre catálogo inteiro |
  | Search - Hot Pant | 12 | ticket alto (mediana R$141) e campeão no Site Próprio |
  | Search - Biquínis | 8 | volume de entrada, ticket menor (R$75) |
  | Search - Marca | 5 | defende a marca; barato e alta conversão |
  | **Total** | **50** | provisório; escala no pacing sazonal |
- **Pacing sazonal** (base: pico jan = 132 un, ago = vale). Escalar o orçamento: set +30%, out +60%, **nov 2x (Black Friday)**, **dez–jan 3–4x (pico verão)**, fev retorno gradual. Reduzir na baixa (mar–ago).

> Números absolutos de orçamento são **provisórios** (sem CPC vivo nesta sessão). O **split** entre campanhas é ancorado em dado real (canal-mix e ticket da Etapa 0). Calibrar os valores quando o volume/CPC do Semrush chegar.

---


# ETAPA 3 — MEDIÇÃO E OTIMIZAÇÃO

# Etapa 3 — Medição e otimização | Campanha Biquínis + Hot Pant

Objetivo: venda no site. Todo indicador aqui é lido para **conversão e ROAS**, não cliques.

## 0. Pré-lançamento (destravar antes de subir)
- [ ] **Conversão configurada** na conta (compra + valor da conversão dinâmico via tag/GA4).
      Sem valor de conversão, Maximizar conversões otimiza por *quantidade*; para migrar a
      tROAS depois, o valor precisa estar vindo correto.
- [ ] **URLs finais** trocadas para a página exata de cada ad group (hoje provisórias —
      site estava bloqueado). Cada grupo aponta para a página que converte o termo.
- [ ] **Volume/CPC do Semrush** aplicado: reordenar keywords por volume decrescente e
      recalibrar o orçamento absoluto (hoje provisório).
- [ ] **Feed do Shopping** com `custom_label_0..3` preenchidos (sub-linha, campeão, faixa
      de preço, estação) e títulos auditados (modelo + atributo).

## 1. O que acompanhar (cadência)
| Métrica | Onde | Cadência | Gatilho de ação |
|---|---|---|---|
| Conversões e ROAS por campanha/ad group/grupo de produto | Google Ads | Semanal | Realocar budget para o que converte |
| Termos de pesquisa | Relatório de termos | 2x/semana no 1º mês, depois semanal | Negativar irrelevante; subir termo bom como KW |
| Quality Score (por KW) | Google Ads | Quinzenal | QS<5: revisar match copy↔LP↔keyword |
| CPA e ticket por sub-linha | Ads + Etapa 0 | Semanal | CPA > margem: pausar/reduzir |
| Share de perda por orçamento/rank | Métricas de leilão | Quinzenal | Perda alta no verão: subir budget (pacing) |
| Cobertura do feed / reprovações | Merchant Center | Semanal | Corrigir SKU reprovado |

## 2. Mineração de termos de pesquisa (proteção de conversão)
- Rodar 2x/semana no primeiro mês. Negativar de imediato: colisão com jornal Zero Hora
  (notícia, gzh, rbs, assinatura), DIY (molde, croche, como fazer), baixa intenção
  (grátis, usado, aluguel) e fora do alvo (infantil, masculino).
- Termo com conversão e ainda não mapeado → subir como keyword no ad group certo.

## 3. Poda e expansão de keywords
- **Poda:** KW com gasto ≥ 1–2× o CPA-alvo e **zero** conversão em ~4 semanas → pausar
  ou passar a negativa. Exceção: KW relevante de volume zero mantida (decisão do projeto),
  mas com lance/observação controlados.
- **Expansão:** clusters que batem meta de ROAS → abrir ad group próprio, testar Exata,
  puxar novos termos relacionados (Semrush) na próxima rodada.

## 4. Teste de RSA
- Manter 1 RSA por ad group com ≥ "Boa"/"Excelente" no Índice de otimização.
- A cada ~4 semanas trocar os 2–3 títulos de pior associação; nunca fixar a ponto de
  matar combinações (pino só no título-âncora de keyword/modelo).
- Comparar RSA por *conversões*, não por CTR isolado.

## 5. Gatilho de graduação de lance
- **Maximizar conversões → tCPA:** quando a campanha acumular ~**15–30 conversões/mês**
  estáveis, fixar tCPA em torno do CPA médio dos últimos 30 dias.
- **tCPA → tROAS:** quando o valor de conversão estiver confiável e houver histórico por
  grupo, migrar a tROAS derivado do ticket/margem (hot pant suporta alvo maior que biquíni).

## 6. Pacing sazonal (revisar mensal)
Base real (Etapa 0): pico jan (132 un), vale ago. Subir budget: set +30%, out +60%,
**nov 2× (Black Friday)**, **dez–jan 3–4× (pico)**, fev retorno gradual, mar–ago baixa.
Revisar no fim de cada mês contra a curva real do ano.

## 7. Backlog de dados a fechar
- Volume/CPC/KD (Semrush BR) → ordenação e orçamento definitivos.
- Margem por SKU (hoje proxy = preço) → tROAS por sub-linha.
- Catálogo completo + URLs (Nuvemshop/site) → cobertura total e LP exata.

---


# GUIA DE IMPORTAÇÃO (GOOGLE ADS EDITOR)

# Guia de importação — Google Ads Editor (subir PAUSADO)

> **Importante:** esta sessão **não tem conexão de escrita com o Google Ads**. A publicação
> é feita por você no **Google Ads Editor** a partir dos CSVs em `03-csv/`. As 4 campanhas
> já estão marcadas **`Status = Paused`** — sobem pausadas, sem gastar, prontas para ativar.

## Antes de importar (checklist mínimo)
- [ ] **URLs finais** — os CSVs usam URL provisória de categoria (site estava bloqueado).
      Ajuste `Final URL` em `rsas.csv` para a página exata de cada ad group.
- [ ] **Volume/CPC** — opcional para subir pausado; necessário antes de ativar (calibra
      orçamento e ordenação). Rode a lista no Semrush.
- [ ] **Feed do Shopping** — preencha `custom_label_0..3` no Merchant Center conforme
      `shopping-grupos-produto.csv` e audite os títulos.

## Ordem de importação no Ads Editor
1. Abra o **Google Ads Editor** conectado à conta da marca → **Account → Import → From file**.
2. Importe nesta ordem (o Editor casa por nome de campanha/ad group):
   1. `campanhas.csv` (cria as 4 campanhas — já **Paused**)
   2. `grupos.csv` (ad groups)
   3. `keywords.csv` (palavras-chave + match)
   4. `negativas.csv` (lista compartilhada de negativas → associe às 4 campanhas)
   5. `rsas.csv` (anúncios responsivos — confira `Final URL`)
   6. `sitelinks.csv`, `callouts.csv`, `snippets.csv` (extensões → associe às campanhas)
   7. `shopping-grupos-produto.csv` (referência para montar a subdivisão de grupos no Shopping)
3. Revise o painel de **erros/avisos** do Editor (limites de caractere já validados aqui).
4. **Post changes** → tudo sobe **pausado**.

## Para ativar depois (quando fechar as pendências)
- Troque `Status` da campanha para **Enabled** (ou ative na interface do Google Ads).
- Comece pelas de maior conversão esperada: **Shopping** e **Search - Hot Pant**.
- Acompanhe pelo `04-medicao.md`.

## Observações
- Estratégia de lance: **Maximizar conversões** (exige conversão configurada na conta).
- Orçamentos são **provisórios** (baixa temporada); o `02-ads.md` traz o pacing sazonal.
- Snippets/sitelinks/callouts podem exigir recriação manual como *assets* na interface,
  dependendo da versão do Editor — os CSVs servem de fonte fiel do conteúdo.

---


# PROVENIÊNCIA DOS DADOS

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

---


# CSVs EMBUTIDOS (para importar no Google Ads Editor)

Cada bloco abaixo é um CSV completo. Salve com o nome indicado e importe na ordem do guia.


## `campanhas.csv`

```csv
Campaign,Campaign Type,Networks,Bid Strategy Type,Daily Budget (BRL) provisório,Locations,Languages,Status
Search - Biquínis,Search,Google search,Maximize conversions,8,Brazil,Portuguese,Paused
Search - Hot Pant,Search,Google search,Maximize conversions,12,Brazil,Portuguese,Paused
Search - Marca e Consideração,Search,Google search,Maximize conversions,5,Brazil,Portuguese,Paused
Shopping - Biquíni & Hot Pant,Shopping,Google search,Maximize conversions,25,Brazil,Portuguese,Paused
```

## `grupos.csv`

```csv
Campaign,Ad Group,Default Max CPC,Status
Search - Biquínis,Biquíni | Genérico,,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,,Enabled
Search - Biquínis,Biquíni | Cortininha,,Enabled
Search - Biquínis,Biquíni | Asa Delta,,Enabled
Search - Biquínis,Biquíni | Sem Bojo,,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,,Enabled
Search - Biquínis,Biquíni | Fio Dental,,Enabled
Search - Biquínis,Biquíni | Comercial,,Enabled
Search - Hot Pant,Hot Pant | Genérico,,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,,Enabled
Search - Hot Pant,Hot Pant | Surf,,Enabled
Search - Hot Pant,Hot Pant | Top Nadador,,Enabled
Search - Hot Pant,Hot Pant | Cropped,,Enabled
Search - Hot Pant,Hot Pant | Fitness/Esporte,,Enabled
Search - Hot Pant,Hot Pant | Comercial,,Enabled
Search - Marca e Consideração,Marca | Use Zero Hora,,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),,Enabled
```

## `keywords.csv`

```csv
Campaign,Ad Group,Keyword,Match Type,Status
Search - Biquínis,Biquíni | Genérico,biquíni,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,biquini,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,biquíni feminino,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,biquíni moda praia,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,biquíni de praia,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,biquíni verão,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,biquíni 2026,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,biquíni cavado,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,moda praia feminina,Phrase,Enabled
Search - Biquínis,Biquíni | Genérico,biquíni tanga,Phrase,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,biquíni empina bumbum,Phrase,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,biquíni empina bumbum,Exact,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,biquini que empina o bumbum,Phrase,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,biquíni cortininha empina bumbum,Phrase,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,biquíni empina bumbum sem bojo,Phrase,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,biquíni levanta bumbum,Phrase,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,biquíni cavado empina bumbum,Phrase,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,biquíni lifting,Phrase,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,comprar biquíni empina bumbum,Phrase,Enabled
Search - Biquínis,Biquíni | Cortininha,biquíni cortininha,Phrase,Enabled
Search - Biquínis,Biquíni | Cortininha,biquíni cortininha,Exact,Enabled
Search - Biquínis,Biquíni | Cortininha,biquíni cortininha sem bojo,Phrase,Enabled
Search - Biquínis,Biquíni | Cortininha,biquíni cortininha premium,Phrase,Enabled
Search - Biquínis,Biquíni | Cortininha,top cortininha,Phrase,Enabled
Search - Biquínis,Biquíni | Cortininha,biquíni cortininha regulável,Phrase,Enabled
Search - Biquínis,Biquíni | Cortininha,biquíni cortininha fio duplo,Phrase,Enabled
Search - Biquínis,Biquíni | Cortininha,biquíni cortininha bojo removível,Phrase,Enabled
Search - Biquínis,Biquíni | Asa Delta,biquíni asa delta,Phrase,Enabled
Search - Biquínis,Biquíni | Asa Delta,biquíni asa delta,Exact,Enabled
Search - Biquínis,Biquíni | Asa Delta,top asa delta,Phrase,Enabled
Search - Biquínis,Biquíni | Asa Delta,biquíni asa delta bicolor,Phrase,Enabled
Search - Biquínis,Biquíni | Asa Delta,biquíni asa delta top fixo,Phrase,Enabled
Search - Biquínis,Biquíni | Asa Delta,biquíni asa delta alça fixa,Phrase,Enabled
Search - Biquínis,Biquíni | Asa Delta,top asa delta fixo,Phrase,Enabled
Search - Biquínis,Biquíni | Sem Bojo,biquíni sem bojo,Phrase,Enabled
Search - Biquínis,Biquíni | Sem Bojo,top sem bojo,Phrase,Enabled
Search - Biquínis,Biquíni | Sem Bojo,biquíni sem enchimento,Phrase,Enabled
Search - Biquínis,Biquíni | Sem Bojo,biquíni sem bojo cortininha,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,biquíni esportivo,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,biquíni para surfar,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,biquíni de surf,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,biquíni futevôlei,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,biquíni que não sai,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,biquíni fixo esporte,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,top de surf feminino,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,sunkini,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,biquíni para praia esportiva,Phrase,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,biquíni que não cai no mar,Phrase,Enabled
Search - Biquínis,Biquíni | Fio Dental,biquíni fio dental,Phrase,Enabled
Search - Biquínis,Biquíni | Fio Dental,biquíni fio dental cortininha,Phrase,Enabled
Search - Biquínis,Biquíni | Fio Dental,biquíni tanga fio dental,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,comprar biquíni,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,biquíni online,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,loja de biquíni,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,biquíni preço,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,biquíni barato,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,biquíni frete grátis,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,biquíni promoção,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,biquíni loja online,Phrase,Enabled
Search - Biquínis,Biquíni | Comercial,biquíni onde comprar,Phrase,Enabled
Search - Hot Pant,Hot Pant | Genérico,hot pant,Phrase,Enabled
Search - Hot Pant,Hot Pant | Genérico,hotpant,Phrase,Enabled
Search - Hot Pant,Hot Pant | Genérico,hot pant feminino,Phrase,Enabled
Search - Hot Pant,Hot Pant | Genérico,hot pant praia,Phrase,Enabled
Search - Hot Pant,Hot Pant | Genérico,hot pant moda praia,Phrase,Enabled
Search - Hot Pant,Hot Pant | Genérico,conjunto hot pant,Phrase,Enabled
Search - Hot Pant,Hot Pant | Genérico,hot pant biquíni,Phrase,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,hot pant manga 3/4,Phrase,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,hot pant manga 3/4,Exact,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,hot pant manga longa,Phrase,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,hot pant manga,Phrase,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,hot pant top manga 3/4,Phrase,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,conjunto hot pant manga longa,Phrase,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,hot pant manga 3/4 surf,Phrase,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,conjunto hot pant manga 3/4,Phrase,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,hot pant proteção solar,Phrase,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,hot pant proteção solar,Exact,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,hot pant uv50,Phrase,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,hot pant com proteção uv,Phrase,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,roupa com proteção solar praia,Phrase,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,hot pant fps,Phrase,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,hot pant proteção uv50,Phrase,Enabled
Search - Hot Pant,Hot Pant | Surf,hot pant surf,Phrase,Enabled
Search - Hot Pant,Hot Pant | Surf,hot pant surf,Exact,Enabled
Search - Hot Pant,Hot Pant | Surf,hot pant para surfar,Phrase,Enabled
Search - Hot Pant,Hot Pant | Surf,roupa de surf feminina,Phrase,Enabled
Search - Hot Pant,Hot Pant | Surf,conjunto surf feminino,Phrase,Enabled
Search - Hot Pant,Hot Pant | Surf,hot pant surf feminino,Phrase,Enabled
Search - Hot Pant,Hot Pant | Surf,roupa para surfar feminina,Phrase,Enabled
Search - Hot Pant,Hot Pant | Surf,lycra de surf feminina,Phrase,Enabled
Search - Hot Pant,Hot Pant | Top Nadador,hot pant top nadador,Phrase,Enabled
Search - Hot Pant,Hot Pant | Top Nadador,top nadador,Phrase,Enabled
Search - Hot Pant,Hot Pant | Top Nadador,top nadador esporte,Phrase,Enabled
Search - Hot Pant,Hot Pant | Top Nadador,hot pant nadador feminino,Phrase,Enabled
Search - Hot Pant,Hot Pant | Cropped,hot pant cropped,Phrase,Enabled
Search - Hot Pant,Hot Pant | Cropped,cropped manga 3/4,Phrase,Enabled
Search - Hot Pant,Hot Pant | Cropped,top cropped surf,Phrase,Enabled
Search - Hot Pant,Hot Pant | Cropped,conjunto cropped praia,Phrase,Enabled
Search - Hot Pant,Hot Pant | Fitness/Esporte,hot pant fitness,Phrase,Enabled
Search - Hot Pant,Hot Pant | Fitness/Esporte,hot pant academia,Phrase,Enabled
Search - Hot Pant,Hot Pant | Fitness/Esporte,hot pant esporte,Phrase,Enabled
Search - Hot Pant,Hot Pant | Fitness/Esporte,short hot pant fitness,Phrase,Enabled
Search - Hot Pant,Hot Pant | Comercial,comprar hot pant,Phrase,Enabled
Search - Hot Pant,Hot Pant | Comercial,hot pant online,Phrase,Enabled
Search - Hot Pant,Hot Pant | Comercial,loja de hot pant,Phrase,Enabled
Search - Hot Pant,Hot Pant | Comercial,hot pant preço,Phrase,Enabled
Search - Hot Pant,Hot Pant | Comercial,hot pant barato,Phrase,Enabled
Search - Hot Pant,Hot Pant | Comercial,hot pant frete grátis,Phrase,Enabled
Search - Hot Pant,Hot Pant | Comercial,conjunto hot pant preço,Phrase,Enabled
Search - Hot Pant,Hot Pant | Comercial,hot pant onde comprar,Phrase,Enabled
Search - Marca e Consideração,Marca | Use Zero Hora,use zero hora,Phrase,Enabled
Search - Marca e Consideração,Marca | Use Zero Hora,use zero hora biquíni,Phrase,Enabled
Search - Marca e Consideração,Marca | Use Zero Hora,use zero hora hot pant,Phrase,Enabled
Search - Marca e Consideração,Marca | Use Zero Hora,zero hora surf,Phrase,Enabled
Search - Marca e Consideração,Marca | Use Zero Hora,zero hora beachwear,Phrase,Enabled
Search - Marca e Consideração,Marca | Use Zero Hora,use zero hora moda praia,Phrase,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),qual o melhor biquíni para surfar,Broad,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),como escolher biquíni,Broad,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),melhor biquíni para praia,Broad,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),o que é hot pant,Broad,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),para que serve hot pant,Broad,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),hot pant serve para surf,Broad,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),biquíni ou hot pant para surfar,Broad,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),qual roupa usar para surfar feminina,Broad,Enabled
```

## `negativas.csv`

```csv
Shared Set,Keyword,Match Type,Grupo
Negativas Biquíni & Hot Pant,jornal,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,jornais,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,noticia,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,noticias,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,notícia,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,notícias,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,gzh,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,rbs,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,clicrbs,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,assinar,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,assinatura,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,jornal zero hora,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,zero hora jornal,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,edição,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,previsão do tempo,Phrase,Marca/Jornal (colisão)
Negativas Biquíni & Hot Pant,molde,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,moldes,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,molde de biquini,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,como fazer,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,passo a passo,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,croche,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,crochê,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,costurar,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,costura,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,apostila,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,pdf,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,papel,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,de eva,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,feltro,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,para colorir,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,desenho,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,tutorial,Phrase,DIY/Tutorial
Negativas Biquíni & Hot Pant,gratis,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,grátis,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,download,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,usado,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,usada,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,brecho,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,brechó,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,aluguel,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,alugar,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,atacado,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,revenda,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,segunda mao,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,segunda mão,Phrase,Baixa intenção
Negativas Biquíni & Hot Pant,infantil,Phrase,Fora do alvo
Negativas Biquíni & Hot Pant,criança,Phrase,Fora do alvo
Negativas Biquíni & Hot Pant,crianca,Phrase,Fora do alvo
Negativas Biquíni & Hot Pant,bebe,Phrase,Fora do alvo
Negativas Biquíni & Hot Pant,bebê,Phrase,Fora do alvo
Negativas Biquíni & Hot Pant,masculino,Phrase,Fora do alvo
Negativas Biquíni & Hot Pant,boneca,Phrase,Fora do alvo
Negativas Biquíni & Hot Pant,roupa de boneca,Phrase,Fora do alvo
```

## `rsas.csv`

```csv
Campaign,Ad Group,Headline 1,Headline 1 position,Headline 2,Headline 2 position,Headline 3,Headline 3 position,Headline 4,Headline 4 position,Headline 5,Headline 5 position,Headline 6,Headline 6 position,Headline 7,Headline 7 position,Headline 8,Headline 8 position,Headline 9,Headline 9 position,Headline 10,Headline 10 position,Headline 11,Headline 11 position,Headline 12,Headline 12 position,Headline 13,Headline 13 position,Headline 14,Headline 14 position,Headline 15,Headline 15 position,Description 1,Description 2,Description 3,Description 4,Path 1,Path 2,Final URL,Status
Search - Biquínis,Biquíni | Genérico,Biquíni Feminino da Marca,1,Biquíni de Praia e Surf,,Moda Praia Feminina,,Biquíni para o Verão,,Novos Modelos de Biquíni,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,Biquínis da Use Zero Hora: fabricação própria e cores que aparecem no mar.,Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,biquini,empina-bumbum,https://usezerohora.com.br/biquini,Enabled
Search - Biquínis,Biquíni | Empina Bumbum,Biquíni Empina Bumbum,1,Cortininha Empina Bumbum,,Efeito que Levanta,,Empina Bumbum Sem Bojo,,Modelagem que Valoriza,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Peças para Surfar,,Estilo de Praia e Surf,,"Biquíni empina bumbum cortininha, com modelagem que levanta e valoriza o corpo.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,biquini,empina-bumbum,https://usezerohora.com.br/biquini,Enabled
Search - Biquínis,Biquíni | Cortininha,Biquíni Cortininha,1,Cortininha Sem Bojo,,Cortininha Premium,,Alcinha Regulável,,Top Cortininha,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Biquíni cortininha da marca, com alcinha regulável e caimento que fica no lugar.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,biquini,empina-bumbum,https://usezerohora.com.br/biquini,Enabled
Search - Biquínis,Biquíni | Asa Delta,Biquíni Asa Delta,1,Top Asa Delta Fixo,,Asa Delta Bicolor,,Alça Fixa que Sustenta,,Top Asa Delta,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Biquíni asa delta com alça fixa que sustenta, em versões lisas e bicolor.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,biquini,empina-bumbum,https://usezerohora.com.br/biquini,Enabled
Search - Biquínis,Biquíni | Sem Bojo,Biquíni Sem Bojo,1,Top Sem Bojo,,Sem Enchimento,,Natural e Confortável,,Cortininha Sem Bojo,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Biquíni sem bojo, sem enchimento: leve, natural e confortável no corpo.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,biquini,empina-bumbum,https://usezerohora.com.br/biquini,Enabled
Search - Biquínis,Biquíni | Esportivo/Surf/Futevôlei,Biquíni para Surfar,1,Biquíni Esportivo,,Não Sai na Onda,,Biquíni de Futevôlei,,Top Fixo de Esporte,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Biquíni esportivo que não sai na onda: feito para surf, futevôlei e praia.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,biquini,empina-bumbum,https://usezerohora.com.br/biquini,Enabled
Search - Biquínis,Biquíni | Fio Dental,Biquíni Fio Dental,1,Fio Dental Cortininha,,Modelagem Cavada,,Tanga Fio Dental,,Marca de Sol Menor,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Biquíni fio dental cortininha, modelagem cavada que valoriza e marca menos.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,biquini,empina-bumbum,https://usezerohora.com.br/biquini,Enabled
Search - Biquínis,Biquíni | Comercial,Comprar Biquíni Online,1,Loja de Biquíni Online,,Biquíni Direto da Marca,,Comprar na Loja Oficial,,Biquíni com Envio Nacional,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Compre biquíni direto da Use Zero Hora, com envio para todo o Brasil.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,biquini,empina-bumbum,https://usezerohora.com.br/biquini,Enabled
Search - Hot Pant,Hot Pant | Genérico,Hot Pant Feminino da Marca,1,Conjunto Hot Pant,,Hot Pant de Praia,,Moda Praia com Hot Pant,,Novos Modelos de Hot Pant,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Hot pant da Use Zero Hora: beachwear de fabricação própria, feito para o mar.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,hot-pant,surf,https://usezerohora.com.br/hot-pant,Enabled
Search - Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,Hot Pant Manga 3/4,1,Hot Pant Manga Longa,,Conjunto Manga 3/4,,Top Manga 3/4 de Surf,,Cobre e Protege do Sol,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Hot pant manga 3/4 com proteção solar, feito para surfar sem se preocupar.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,hot-pant,surf,https://usezerohora.com.br/hot-pant,Enabled
Search - Hot Pant,Hot Pant | Proteção Solar UV50,Hot Pant Proteção UV50,1,Proteção Solar UV50,,Roupa com Proteção UV,,Protege na Água,,Feito para o Sol Forte,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Hot pant com proteção solar UV50 de verdade, para horas de sol dentro da água.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,hot-pant,surf,https://usezerohora.com.br/hot-pant,Enabled
Search - Hot Pant,Hot Pant | Surf,Hot Pant para Surfar,1,Roupa de Surf Feminina,,Conjunto de Surf,,Não Sai na Onda,,Feito para o Surf,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,Hot pant de surf feminino: fica no lugar na onda e protege do sol e do atrito.,Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,hot-pant,surf,https://usezerohora.com.br/hot-pant,Enabled
Search - Hot Pant,Hot Pant | Top Nadador,Hot Pant Top Nadador,1,Top Nadador de Esporte,,Liberdade nos Braços,,Top Nadador Feminino,,Feito para o Movimento,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,Hot pant top nadador: recorte esportivo que dá liberdade de braço na água.,Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,hot-pant,surf,https://usezerohora.com.br/hot-pant,Enabled
Search - Hot Pant,Hot Pant | Cropped,Hot Pant Cropped,1,Top Cropped de Surf,,Cropped Manga 3/4,,Conjunto Cropped,,Estilo e Proteção,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Hot pant cropped manga 3/4: estilo com proteção, do surf à beira da piscina.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,hot-pant,surf,https://usezerohora.com.br/hot-pant,Enabled
Search - Hot Pant,Hot Pant | Fitness/Esporte,Hot Pant Fitness,1,Hot Pant de Academia,,Hot Pant de Esporte,,Do Treino à Praia,,Segunda Pele no Corpo,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Hot pant fitness que vai do treino à praia, como uma segunda pele no corpo.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,hot-pant,surf,https://usezerohora.com.br/hot-pant,Enabled
Search - Hot Pant,Hot Pant | Comercial,Comprar Hot Pant Online,1,Loja de Hot Pant,,Hot Pant Direto da Marca,,Comprar na Loja Oficial,,Conjunto com Envio Nacional,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,"Compre hot pant direto da Use Zero Hora, com envio para todo o Brasil.",Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,hot-pant,surf,https://usezerohora.com.br/hot-pant,Enabled
Search - Marca e Consideração,Marca | Use Zero Hora,Use Zero Hora Oficial,1,Loja Oficial da Marca,,Surf e Beachwear,,Biquíni e Hot Pant,,Direto de Quem Fabrica,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,Use Zero Hora: surf e beachwear de fabricação própria. Compre na loja oficial.,Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,use-zero-hora,surf,https://usezerohora.com.br/,Enabled
Search - Marca e Consideração,Consideração | Dúvidas (SEO),Biquíni ou Hot Pant?,1,Qual Usar para Surfar,,Guia para Escolher,,Feito para o Surf,,Modelos para o Mar,,Fabricação Própria,,Feito para o Mar,,Direto da Marca,,Envio para Todo o Brasil,,Cores que Saem na Foto,,Moda Praia e Surf,,Beachwear com Assinatura,,Compre Online Agora,,Modelagem que Valoriza,,Peças para Surfar,,Não sabe qual escolher para surfar? Conheça os modelos da Use Zero Hora.,Fabricação própria e cores que aparecem no mar. Compre direto da Use Zero Hora.,Beachwear feito para surfar: fica no lugar na água e ainda sai bem na foto.,Moda praia da marca com envio para todo o Brasil. Compre online agora mesmo.,use-zero-hora,surf,https://usezerohora.com.br/,Enabled
```

## `sitelinks.csv`

```csv
Sitelink Text,Description 1,Description 2,Final URL
Biquínis,Empina bumbum e cortininha,Modelos que valorizam o corpo,https://usezerohora.com.br/
Hot Pants,Manga 3/4 e proteção UV50,Feito para surfar sem sol,https://usezerohora.com.br/
Novidades,Últimos lançamentos da marca,Moda praia e surf feminina,https://usezerohora.com.br/
Trocas e Envio,Envio para todo o Brasil,Troca fácil pelo site,https://usezerohora.com.br/
Quem Somos,Marca de surf e beachwear,Fabricação própria desde 2023,https://usezerohora.com.br/
```

## `callouts.csv`

```csv
Callout text
Fabricação própria
Envio para todo o Brasil
Cores que saem na foto
Feito para surfar
Proteção solar UV50
Modelagem que valoriza
Direto da marca
Troca fácil
```

## `snippets.csv`

```csv
Header,Values (; )
Tipos,Biquíni; Hot pant; Cortininha; Asa delta; Top nadador; Fio dental
Estilos,Empina bumbum; Manga 3/4; Sem bojo; Cropped; Proteção UV50; Esportivo
```

## `shopping-grupos-produto.csv`

```csv
Campaign,Subdivision level,Attribute,Value,Observação
Shopping - Biquíni & Hot Pant,0,custom_label_0,biquini,sub-linha
Shopping - Biquíni & Hot Pant,0,custom_label_0,hot_pant,sub-linha
Shopping - Biquíni & Hot Pant,1,custom_label_1,empina_bumbum,campeão biquíni (106 un)
Shopping - Biquíni & Hot Pant,1,custom_label_1,hotpant_manga_34,campeão hot pant (60 un)
Shopping - Biquíni & Hot Pant,1,custom_label_1,Everything else,demais modelos
Shopping - Biquíni & Hot Pant,2,custom_label_2,ate_90,faixa preço biquíni
Shopping - Biquíni & Hot Pant,2,custom_label_2,91_150,faixa preço
Shopping - Biquíni & Hot Pant,2,custom_label_2,151_mais,ticket alto hot pant
```

## `kws-seed-por-ag.csv`

```csv
campanha,sub_linha,ad_group,intencao,match_sugerido,keyword
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquíni
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquini
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquíni feminino
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquíni moda praia
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquíni de praia
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquíni verão
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquíni 2026
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquíni cavado
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,moda praia feminina
Search - Biquínis,Biquíni,Biquíni | Genérico,Consideração/Genérico,Frase,biquíni tanga
Search - Biquínis,Biquíni,Biquíni | Empina Bumbum,Compra/Modelo,Frase,biquíni empina bumbum
Search - Biquínis,Biquíni,Biquíni | Empina Bumbum,Compra/Modelo,Frase,biquini que empina o bumbum
Search - Biquínis,Biquíni,Biquíni | Empina Bumbum,Compra/Modelo,Frase,biquíni cortininha empina bumbum
Search - Biquínis,Biquíni,Biquíni | Empina Bumbum,Compra/Modelo,Frase,biquíni empina bumbum sem bojo
Search - Biquínis,Biquíni,Biquíni | Empina Bumbum,Compra/Modelo,Frase,biquíni levanta bumbum
Search - Biquínis,Biquíni,Biquíni | Empina Bumbum,Compra/Modelo,Frase,biquíni cavado empina bumbum
Search - Biquínis,Biquíni,Biquíni | Empina Bumbum,Compra/Modelo,Frase,biquíni lifting
Search - Biquínis,Biquíni,Biquíni | Empina Bumbum,Compra/Modelo,Frase,comprar biquíni empina bumbum
Search - Biquínis,Biquíni,Biquíni | Cortininha,Compra/Modelo,Frase,biquíni cortininha
Search - Biquínis,Biquíni,Biquíni | Cortininha,Compra/Modelo,Frase,biquíni cortininha sem bojo
Search - Biquínis,Biquíni,Biquíni | Cortininha,Compra/Modelo,Frase,biquíni cortininha premium
Search - Biquínis,Biquíni,Biquíni | Cortininha,Compra/Modelo,Frase,top cortininha
Search - Biquínis,Biquíni,Biquíni | Cortininha,Compra/Modelo,Frase,biquíni cortininha regulável
Search - Biquínis,Biquíni,Biquíni | Cortininha,Compra/Modelo,Frase,biquíni cortininha fio duplo
Search - Biquínis,Biquíni,Biquíni | Cortininha,Compra/Modelo,Frase,biquíni cortininha bojo removível
Search - Biquínis,Biquíni,Biquíni | Asa Delta,Compra/Modelo,Frase,biquíni asa delta
Search - Biquínis,Biquíni,Biquíni | Asa Delta,Compra/Modelo,Frase,top asa delta
Search - Biquínis,Biquíni,Biquíni | Asa Delta,Compra/Modelo,Frase,biquíni asa delta bicolor
Search - Biquínis,Biquíni,Biquíni | Asa Delta,Compra/Modelo,Frase,biquíni asa delta top fixo
Search - Biquínis,Biquíni,Biquíni | Asa Delta,Compra/Modelo,Frase,biquíni asa delta alça fixa
Search - Biquínis,Biquíni,Biquíni | Asa Delta,Compra/Modelo,Frase,top asa delta fixo
Search - Biquínis,Biquíni,Biquíni | Sem Bojo,Compra/Atributo,Frase,biquíni sem bojo
Search - Biquínis,Biquíni,Biquíni | Sem Bojo,Compra/Atributo,Frase,top sem bojo
Search - Biquínis,Biquíni,Biquíni | Sem Bojo,Compra/Atributo,Frase,biquíni sem enchimento
Search - Biquínis,Biquíni,Biquíni | Sem Bojo,Compra/Atributo,Frase,biquíni sem bojo cortininha
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,biquíni esportivo
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,biquíni para surfar
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,biquíni de surf
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,biquíni futevôlei
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,biquíni que não sai
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,biquíni fixo esporte
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,top de surf feminino
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,sunkini
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,biquíni para praia esportiva
Search - Biquínis,Biquíni,Biquíni | Esportivo/Surf/Futevôlei,Compra/Uso,Frase,biquíni que não cai no mar
Search - Biquínis,Biquíni,Biquíni | Fio Dental,Compra/Modelo,Frase,biquíni fio dental
Search - Biquínis,Biquíni,Biquíni | Fio Dental,Compra/Modelo,Frase,biquíni fio dental cortininha
Search - Biquínis,Biquíni,Biquíni | Fio Dental,Compra/Modelo,Frase,biquíni tanga fio dental
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,comprar biquíni
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,biquíni online
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,loja de biquíni
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,biquíni preço
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,biquíni barato
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,biquíni frete grátis
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,biquíni promoção
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,biquíni loja online
Search - Biquínis,Biquíni,Biquíni | Comercial,Fundo/Comercial,Frase,biquíni onde comprar
Search - Hot Pant,Hot Pant,Hot Pant | Genérico,Consideração/Genérico,Frase,hot pant
Search - Hot Pant,Hot Pant,Hot Pant | Genérico,Consideração/Genérico,Frase,hotpant
Search - Hot Pant,Hot Pant,Hot Pant | Genérico,Consideração/Genérico,Frase,hot pant feminino
Search - Hot Pant,Hot Pant,Hot Pant | Genérico,Consideração/Genérico,Frase,hot pant praia
Search - Hot Pant,Hot Pant,Hot Pant | Genérico,Consideração/Genérico,Frase,hot pant moda praia
Search - Hot Pant,Hot Pant,Hot Pant | Genérico,Consideração/Genérico,Frase,conjunto hot pant
Search - Hot Pant,Hot Pant,Hot Pant | Genérico,Consideração/Genérico,Frase,hot pant biquíni
Search - Hot Pant,Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,Compra/Modelo,Frase,hot pant manga 3/4
Search - Hot Pant,Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,Compra/Modelo,Frase,hot pant manga longa
Search - Hot Pant,Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,Compra/Modelo,Frase,hot pant manga
Search - Hot Pant,Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,Compra/Modelo,Frase,hot pant top manga 3/4
Search - Hot Pant,Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,Compra/Modelo,Frase,conjunto hot pant manga longa
Search - Hot Pant,Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,Compra/Modelo,Frase,hot pant manga 3/4 surf
Search - Hot Pant,Hot Pant,Hot Pant | Manga 3/4 e Manga Longa,Compra/Modelo,Frase,conjunto hot pant manga 3/4
Search - Hot Pant,Hot Pant,Hot Pant | Proteção Solar UV50,Compra/Atributo,Frase,hot pant proteção solar
Search - Hot Pant,Hot Pant,Hot Pant | Proteção Solar UV50,Compra/Atributo,Frase,hot pant uv50
Search - Hot Pant,Hot Pant,Hot Pant | Proteção Solar UV50,Compra/Atributo,Frase,hot pant com proteção uv
Search - Hot Pant,Hot Pant,Hot Pant | Proteção Solar UV50,Compra/Atributo,Frase,roupa com proteção solar praia
Search - Hot Pant,Hot Pant,Hot Pant | Proteção Solar UV50,Compra/Atributo,Frase,hot pant fps
Search - Hot Pant,Hot Pant,Hot Pant | Proteção Solar UV50,Compra/Atributo,Frase,hot pant proteção uv50
Search - Hot Pant,Hot Pant,Hot Pant | Surf,Compra/Uso,Frase,hot pant surf
Search - Hot Pant,Hot Pant,Hot Pant | Surf,Compra/Uso,Frase,hot pant para surfar
Search - Hot Pant,Hot Pant,Hot Pant | Surf,Compra/Uso,Frase,roupa de surf feminina
Search - Hot Pant,Hot Pant,Hot Pant | Surf,Compra/Uso,Frase,conjunto surf feminino
Search - Hot Pant,Hot Pant,Hot Pant | Surf,Compra/Uso,Frase,hot pant surf feminino
Search - Hot Pant,Hot Pant,Hot Pant | Surf,Compra/Uso,Frase,roupa para surfar feminina
Search - Hot Pant,Hot Pant,Hot Pant | Surf,Compra/Uso,Frase,lycra de surf feminina
Search - Hot Pant,Hot Pant,Hot Pant | Top Nadador,Compra/Modelo,Frase,hot pant top nadador
Search - Hot Pant,Hot Pant,Hot Pant | Top Nadador,Compra/Modelo,Frase,top nadador
Search - Hot Pant,Hot Pant,Hot Pant | Top Nadador,Compra/Modelo,Frase,top nadador esporte
Search - Hot Pant,Hot Pant,Hot Pant | Top Nadador,Compra/Modelo,Frase,hot pant nadador feminino
Search - Hot Pant,Hot Pant,Hot Pant | Cropped,Compra/Modelo,Frase,hot pant cropped
Search - Hot Pant,Hot Pant,Hot Pant | Cropped,Compra/Modelo,Frase,cropped manga 3/4
Search - Hot Pant,Hot Pant,Hot Pant | Cropped,Compra/Modelo,Frase,top cropped surf
Search - Hot Pant,Hot Pant,Hot Pant | Cropped,Compra/Modelo,Frase,conjunto cropped praia
Search - Hot Pant,Hot Pant,Hot Pant | Fitness/Esporte,Compra/Uso,Frase,hot pant fitness
Search - Hot Pant,Hot Pant,Hot Pant | Fitness/Esporte,Compra/Uso,Frase,hot pant academia
Search - Hot Pant,Hot Pant,Hot Pant | Fitness/Esporte,Compra/Uso,Frase,hot pant esporte
Search - Hot Pant,Hot Pant,Hot Pant | Fitness/Esporte,Compra/Uso,Frase,short hot pant fitness
Search - Hot Pant,Hot Pant,Hot Pant | Comercial,Fundo/Comercial,Frase,comprar hot pant
Search - Hot Pant,Hot Pant,Hot Pant | Comercial,Fundo/Comercial,Frase,hot pant online
Search - Hot Pant,Hot Pant,Hot Pant | Comercial,Fundo/Comercial,Frase,loja de hot pant
Search - Hot Pant,Hot Pant,Hot Pant | Comercial,Fundo/Comercial,Frase,hot pant preço
Search - Hot Pant,Hot Pant,Hot Pant | Comercial,Fundo/Comercial,Frase,hot pant barato
Search - Hot Pant,Hot Pant,Hot Pant | Comercial,Fundo/Comercial,Frase,hot pant frete grátis
Search - Hot Pant,Hot Pant,Hot Pant | Comercial,Fundo/Comercial,Frase,conjunto hot pant preço
Search - Hot Pant,Hot Pant,Hot Pant | Comercial,Fundo/Comercial,Frase,hot pant onde comprar
Search - Marca e Consideração,Marca,Marca | Use Zero Hora,Marca,Frase,use zero hora
Search - Marca e Consideração,Marca,Marca | Use Zero Hora,Marca,Frase,use zero hora biquíni
Search - Marca e Consideração,Marca,Marca | Use Zero Hora,Marca,Frase,use zero hora hot pant
Search - Marca e Consideração,Marca,Marca | Use Zero Hora,Marca,Frase,zero hora surf
Search - Marca e Consideração,Marca,Marca | Use Zero Hora,Marca,Frase,zero hora beachwear
Search - Marca e Consideração,Marca,Marca | Use Zero Hora,Marca,Frase,use zero hora moda praia
Search - Marca e Consideração,Ambas,Consideração | Dúvidas (SEO),Topo/SEO,Ampla,qual o melhor biquíni para surfar
Search - Marca e Consideração,Ambas,Consideração | Dúvidas (SEO),Topo/SEO,Ampla,como escolher biquíni
Search - Marca e Consideração,Ambas,Consideração | Dúvidas (SEO),Topo/SEO,Ampla,melhor biquíni para praia
Search - Marca e Consideração,Ambas,Consideração | Dúvidas (SEO),Topo/SEO,Ampla,o que é hot pant
Search - Marca e Consideração,Ambas,Consideração | Dúvidas (SEO),Topo/SEO,Ampla,para que serve hot pant
Search - Marca e Consideração,Ambas,Consideração | Dúvidas (SEO),Topo/SEO,Ampla,hot pant serve para surf
Search - Marca e Consideração,Ambas,Consideração | Dúvidas (SEO),Topo/SEO,Ampla,biquíni ou hot pant para surfar
Search - Marca e Consideração,Ambas,Consideração | Dúvidas (SEO),Topo/SEO,Ampla,qual roupa usar para surfar feminina
```

## `kws-seed-semrush-lotes.txt`

```text
# LOTE 1 (100 kw)
biquíni;biquini;biquíni feminino;biquíni moda praia;biquíni de praia;biquíni verão;biquíni 2026;biquíni cavado;moda praia feminina;biquíni tanga;biquíni empina bumbum;biquini que empina o bumbum;biquíni cortininha empina bumbum;biquíni empina bumbum sem bojo;biquíni levanta bumbum;biquíni cavado empina bumbum;biquíni lifting;comprar biquíni empina bumbum;biquíni cortininha;biquíni cortininha sem bojo;biquíni cortininha premium;top cortininha;biquíni cortininha regulável;biquíni cortininha fio duplo;biquíni cortininha bojo removível;biquíni asa delta;top asa delta;biquíni asa delta bicolor;biquíni asa delta top fixo;biquíni asa delta alça fixa;top asa delta fixo;biquíni sem bojo;top sem bojo;biquíni sem enchimento;biquíni sem bojo cortininha;biquíni esportivo;biquíni para surfar;biquíni de surf;biquíni futevôlei;biquíni que não sai;biquíni fixo esporte;top de surf feminino;sunkini;biquíni para praia esportiva;biquíni que não cai no mar;biquíni fio dental;biquíni fio dental cortininha;biquíni tanga fio dental;comprar biquíni;biquíni online;loja de biquíni;biquíni preço;biquíni barato;biquíni frete grátis;biquíni promoção;biquíni loja online;biquíni onde comprar;hot pant;hotpant;hot pant feminino;hot pant praia;hot pant moda praia;conjunto hot pant;hot pant biquíni;hot pant manga 3/4;hot pant manga longa;hot pant manga;hot pant top manga 3/4;conjunto hot pant manga longa;hot pant manga 3/4 surf;conjunto hot pant manga 3/4;hot pant proteção solar;hot pant uv50;hot pant com proteção uv;roupa com proteção solar praia;hot pant fps;hot pant proteção uv50;hot pant surf;hot pant para surfar;roupa de surf feminina;conjunto surf feminino;hot pant surf feminino;roupa para surfar feminina;lycra de surf feminina;hot pant top nadador;top nadador;top nadador esporte;hot pant nadador feminino;hot pant cropped;cropped manga 3/4;top cropped surf;conjunto cropped praia;hot pant fitness;hot pant academia;hot pant esporte;short hot pant fitness;comprar hot pant;hot pant online;loja de hot pant;hot pant preço

# LOTE 2 (18 kw)
hot pant barato;hot pant frete grátis;conjunto hot pant preço;hot pant onde comprar;use zero hora;use zero hora biquíni;use zero hora hot pant;zero hora surf;zero hora beachwear;use zero hora moda praia;qual o melhor biquíni para surfar;como escolher biquíni;melhor biquíni para praia;o que é hot pant;para que serve hot pant;hot pant serve para surf;biquíni ou hot pant para surfar;qual roupa usar para surfar feminina
```

---

_Arquivo gerado a partir do repositório raphavianna/search-mkt, branch claude/zero-hora-bikini-campaign-3zznh3. Fontes: vendas reais BaseLinker (jan–ago/2026). Pendências de go-live: URLs finais, volume/CPC (Semrush), custom_labels do feed._