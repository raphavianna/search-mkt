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
