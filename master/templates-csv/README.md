# Templates CSV — formato canônico de subida (prioridade de upload)

**Regra:** toda subida de campanha é entregue como conjunto de CSVs neste
modelo, preenchidos pela ferramenta (Etapa 2) e importados em massa no
Google Ads. Montagem manual na interface, campanha a campanha, não é o
fluxo padrão — só com pedido explícito.

## Proveniência

- `google-oficial/` — **modelos oficiais de upload em massa do Google
  Ads** (interface web), baixados da conta e enviados pelo usuário em
  **2026-08-09**. São a fonte de verdade dos cabeçalhos; não editar.
- Arquivos `01-…csv` a `05-…csv` — versões prontas-para-preencher,
  geradas a partir dos oficiais (cabeçalho idêntico, extração
  programática) com uma linha de exemplo comentada (`#`).

## Arquivos e ordem de subida

| Ordem | Arquivo | Entidade | Origem oficial |
|---|---|---|---|
| 1 | `01-campanhas.csv` | Campanhas | `campaign_template.csv` |
| 2 | `02-grupos-de-anuncio.csv` | Ad groups | `ad_group_template.csv` |
| 3 | `03-palavras-chave.csv` | Keywords | `keyword_template.csv` |
| 4 | `04-negativas.csv` | Negativas (campanha e grupo, via coluna `Level`) | `ad_group_negative_keyword_template.csv` |
| 5 | `05-rsa.csv` | Anúncios responsivos de pesquisa | `responsive_search_ad_template.csv` |

`responsive_display_ad_template.csv` fica arquivado, mas **fora do escopo
atual** (Search apenas; Display/PMax só com pedido explícito).

## Como preencher (regras do formato)

- 1ª linha = cabeçalho, intocável. Linhas começando com `#` são ignoradas
  no upload (as de exemplo devem ser apagadas no arquivo final da
  campanha).
- `Action` = `Add` para criação; `Edit`/`Remove` para manutenção.
- Valores de lista respeitam EXATAMENTE os suportados pelo template
  oficial (em inglês): `Type` = `Exact match` | `Phrase match` |
  `Broad match`; `Campaign type` = `Search`; `Networks` = `Google search`
  (parceiros de pesquisa e Display desligados por padrão);
  `Bid strategy type` = `Maximize Conversions` (tCPA/tROAS via colunas
  `Target CPA`/`Target ROAS` quando decidido);
  `Budget type` = `Daily`; `Language` = `pt`; `Location` = `Brazil`.
- Nomes de campanha/grupo seguem `master/nomenclatura.md`; textos de RSA
  respeitam `master/specs-limites-google-ads.md` (conferência de contagem
  antes de gerar o CSV).
- Encoding UTF-8; decimal com ponto (`50.00`).

## Como subir

1. Google Ads (web) → **Ferramentas e configurações → Ações em massa →
   Uploads**.
2. Enviar os arquivos na ordem da tabela (campanha antes de grupo, grupo
   antes de KW/anúncio).
3. **Sempre usar a pré-visualização** do upload e revisar as mudanças
   propostas antes de aplicar.
4. Conferir erros/avisos do relatório de upload; erro zerado é critério
   do checklist de lançamento.

## Lacunas conhecidas (completar quando formos usar)

Ainda sem modelo oficial arquivado: **sitelinks, callouts, snippets
estruturados** e demais ativos (promoção, preço, imagem). Ao precisar:
baixar os templates de ativos na mesma tela de Uploads da conta e
arquivá-los em `google-oficial/` (mesmo fluxo), criando as versões
prontas correspondentes. Até lá, ativos podem ser subidos pela interface
com os textos do `02-ads.md` — única exceção aceita à regra do CSV.
