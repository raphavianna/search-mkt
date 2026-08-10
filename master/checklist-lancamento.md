# Checklist de lançamento — campanha de Search

Conferência obrigatória antes de importar e publicar. Item reprovado =
não sobe.

## Estrutura e dados

- [ ] `00-produtos.md` com preço/frete coletados e datados das páginas
- [ ] `01-kws.md` com fonte, base (ex.: Semrush BR) e data de cada métrica
- [ ] Decisão de estrutura (única vs. separadas) com racional numérico
- [ ] 5–20 KWs por ad group, um tema por grupo, match types registrados
- [ ] Negativas da campanha + biblioteca da marca aplicadas
- [ ] Awareness de CPC alto marcado como território de SEO (fora da campanha)

## Peças

- [ ] Toda peça com contagem declarada e dentro do limite (specs do master)
- [ ] 15 títulos e 4 descrições por RSA; pins só onde justificado
- [ ] Copy promete só o que a página sustenta; preço/promoção com data
- [ ] Entidade correta: "Use Zero Hora" = surf/beachwear (zero colisão com o jornal)
- [ ] URLs finais **https**, sem `www`, respondem 200 sem redirect e batem com o produto do grupo (nunca a home, salvo campanha institucional)
- [ ] **Extensões obrigatórias** preenchidas em `03-extensoes.md`: sitelinks (4+, cada um com 2 descrições), callouts (6+), snippet (1 cabeçalho + 3+ valores)
- [ ] Sitelinks apontam para páginas distintas entre si e da URL final
- [ ] Imagem avaliada; promoção/preço só se a página sustentar (com data)

## Setup

- [ ] Taxonomia do master aplicada: campanha `[NNN-CANAL]-TEMA`, grupos `[NNN-L]-SUBTEMA-INTENCAO` com o NNN da campanha-mãe
- [ ] `Final URL suffix` com UTM padrão preenchido (ou decisão registrada de não usar)
- [ ] Rede: Pesquisa Google; **parceiros de pesquisa e Display desligados**
- [ ] Localização: Brasil (ou recorte com racional); idioma português
- [ ] Lance inteligente (Maximizar conversões; tCPA/tROAS só com histórico do cluster) — manual exige justificativa escrita
- [ ] Orçamento derivado de CPC × volume do cluster, com a conta mostrada
- [ ] Medição conferida na conta (ação de conversão de compra ativa; auto-tagging)

## Subida (Google Ads Editor)

- [ ] CSVs gerados no modelo `master/templates-csv/` (todos os arquivos aplicáveis)
- [ ] Importação feita arquivo a arquivo, conferindo o mapeamento de colunas
- [ ] Revisão das mudanças propostas no Editor **antes** de "Manter"
- [ ] Erros/avisos do Editor zerados antes de "Postar"
- [ ] Pós-publicação: status das peças "Qualificado" (sem reprovação editorial)
