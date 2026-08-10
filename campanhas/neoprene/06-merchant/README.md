# Feed Merchant Center — linha neoprene

- **Merchant Center vinculado à conta Ads**: ID `5507430207` (link ativo,
  confirmado via API em 2026-08-10). Há um segundo vínculo `469097391`
  com tipo UNKNOWN.
- **Arquivo**: `feed-neoprene.tsv` — formato TSV oficial do Merchant
  Center, 9 linhas (3 produtos × 3 variações de tamanho, agrupadas por
  `item_group_id`). Descrições e atributos vêm dos infográficos oficiais
  (00-produtos.md); grade P–G usada só como variação de feed (exigência
  do Merchant p/ vestuário no Brasil), não em copy de anúncio.

## Bloqueio de API registrado

O refresh token do ambiente tem escopo apenas da Google Ads API; a
Content API do Merchant respondeu `403 insufficient authentication
scopes` (2026-08-10). Sem novo consentimento OAuth com escopo
`https://www.googleapis.com/auth/content`, o envio programático não é
possível — o caminho é upload manual do TSV ou re-autorização.

## Campos pendentes (marcados `PREENCHER` no TSV)

| Campo | Por quê está pendente |
|---|---|
| `price` (por variação) | preço não coletável (site bloqueado por rede) e não fornecido |
| `image_link` | URLs das imagens dos produtos |
| `color` | cor não confirmada (fotos mostram preto; não assumido) |
| `identifier_exists` | marcado `no` (sem GTIN — confirmar se as peças têm código de barras) |
| `availability` | assumido `in stock` — confirmar |

## Como subir (manual, ~2 min)

Merchant Center (conta 5507430207) → Produtos → Feeds → Adicionar feed
primário → Brasil / Português → Upload de arquivo → enviar
`feed-neoprene.tsv` (após preencher os campos pendentes).

## Observação de uso

Feed do Merchant **não pluga em campanha de Search de texto** (a
[007-SEARCH]-NEOPRENE segue independente). Ele habilita: campanha
**Shopping** dedicada (seria `[008-SHOPPING]-NEOPRENE`, seguindo o padrão
da conta), inclusão da linha na PMax existente, e listagens orgânicas do
Shopping. Criação da campanha Shopping só com pedido explícito (escopo do
repositório).
