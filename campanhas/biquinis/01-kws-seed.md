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
