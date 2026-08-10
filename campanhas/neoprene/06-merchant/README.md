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

## Desfecho (2026-08-10)

**Feed manual desnecessário**: a busca "neoprene" no Merchant confirmou os
3 produtos **já sincronizados via API Content** (plataforma do e-commerce),
aprovados e em estoque — 11 variações (camiseta P/M/G/GG, bermuda P/M/G/GG,
sapatilha 34-37/38-41/42-44), IDs 1569492206–1569492230, cor Preto.
Preços no Merchant em 2026-08-10: camiseta R$399,99 (de R$499,99), bermuda
R$299,99 (de R$399,99), sapatilha R$79,99 (de R$179,90).
O `feed-neoprene.tsv` fica arquivado como referência; NÃO subir (criaria
fonte duplicada).

**Campanha criada**: `[008-SHOPPING]-NEOPRENE` (ID 24123512324), PAUSADA —
Shopping standard, Maximizar valor da conversão, R$15/dia, prioridade 1,
merchant 5507430207. Ad group `[008-A]-NEOPRENE-COMPRA`
(ID 200137485978) com listing group filtrado nos 11 item IDs e o restante
do catálogo excluído. Script: `../05-upload/shopping_008.py`.

**Atenção**: 7 variações (bermuda + sapatilha) estão `ELIGIBLE_LIMITED`
no Merchant — conferir a aba "Requer atenção" (provável falta de atributo
de vestuário ou GTIN); a camiseta está `ELIGIBLE` pleno.

## PMax (2026-08-10)

**`[009-PMAX]-NEOPRENE`** (ID 24128612776) criada via API, **PAUSADA** —
Performance Max feed-only (anúncios gerados do Merchant, sem assets
obrigatórios), Maximizar valor da conversão, R$15/dia, merchant
5507430207. Asset group `[009-A]-NEOPRENE` (ID 6739198789) com listing
group filter nos 11 item IDs e restante do catálogo excluído. Script:
`../05-upload/pmax_009.py`.

**Regra de convivência (prioridade de veiculação)**: PMax > Shopping
padrão para os mesmos produtos. Manter **apenas uma** ativa:
- 009 ativa → 008 fica pausada (senão a PMax engole a Shopping);
- preferindo controle manual/CPC barato no início, ativar a 008 e manter
  a 009 pausada.
Recomendação: ativar a 009 (padrão da conta é PMax na linha principal,
ex.: poncho) e deixar a 008 como plano B de controle.

**Correção 2026-08-10**: a 009 nasceu sem segmentação (Locais: todos os
países). Aplicados via API: geo Brasil (2076) + idiomas português (1014)
e inglês (1000), espelhando a [001-PMAX]-PONCHO-FEMININO. Lição
incorporada: PMax via API exige criar os campaign criteria de geo/idioma
explicitamente (não herda default como a UI sugere).

## Cópia de conteúdo 007 → 009 (2026-08-10)

- **Sitelinks (4)** e **callouts (9 assets com os textos da campanha; um
  texto tinha asset duplicado pré-existente na conta)** vinculados à
  [009-PMAX]-NEOPRENE via campaign assets — mesmos assets da 007, sem
  duplicação de conteúdo.
- **KWs → temas de pesquisa**: PMax não usa keywords; os 25 termos-cabeça
  da 007 entraram como search themes no asset group [009-A] (limite do
  Google: 25/grupo) — sapatilha (aquática/neoprene/náutica/praia/beach
  tennis/futevôlei/cachoeira), meia/bota, camiseta/camisa térmica,
  bermuda (neoprene/surf/natação), roupa de neoprene/surf/natação,
  segunda pele, conjunto.
