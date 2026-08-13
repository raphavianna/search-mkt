# Checklist de lançamento

## A) Qualidade da campanha (antes de gerar CSV)
- [ ] Cada ad group tem 1 tema só e 5–20 KWs coesas.
- [ ] Cada KW tem match sugerido, intenção e ad group de destino.
- [ ] RSA por ad group: 15 títulos (≤30), 4 descrições (≤90), 2 paths (≤15); ≥1 título com a KW.
- [ ] Pins só onde necessário (título-âncora de marca/modelo).
- [ ] Extensões: ≥4 sitelinks (≤25 / 2×≤35), ≥6 callouts (≤25), ≥1 snippet (valores ≤25).
- [ ] **Contagem de caractere validada** — 0 peças acima do limite (rodar o validador).
- [ ] Negativas base da marca aplicadas (colisão jornal Zero Hora + gerais) + negativas da campanha.
- [ ] Copy só com atributos reais da página (Etapa 0). Preço/frete só se coletados e datados.
- [ ] Entidade correta: Use Zero Hora (surf/beachwear), não o jornal.

## B) Antes de IMPORTAR no Ads Editor (subir PAUSADO)
- [ ] Todas as campanhas com `Status = Paused` no `campanhas.csv`.
- [ ] Nomenclatura conforme `master/padrao-nomenclatura.md`.
- [ ] Ordem de import: campanhas → grupos → keywords → negativas → RSAs → extensões → (Shopping ref).
- [ ] Rede só Pesquisa (sem Display; sem parceiros de pesquisa no lançamento), salvo racional.

## C) Antes de ATIVAR (destravar pendências)
- [ ] **Conversão configurada** na conta (compra + valor dinâmico via tag/GA4).
- [ ] **URLs finais** por ad group trocadas para a página exata que converte o termo.
- [ ] **Volume/CPC (Semrush BR)** aplicado: KWs reordenadas por volume; orçamento calibrado
      por CPC × volume do cluster, com racional numérico.
- [ ] **Shopping:** `custom_label_0..3` preenchidos no feed e títulos auditados (modelo + atributo).
- [ ] Estratégia de lance: Maximizar conversões (padrão); gatilho de graduação a tCPA/tROAS registrado.
- [ ] Ativar primeiro as de maior conversão esperada (Shopping e a de ticket alto).
