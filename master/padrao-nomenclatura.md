# Padrão de nomenclatura

Nomes consistentes entre campanhas facilitam relatório, automação e leitura no Ads Editor.

## Slug de campanha (pasta)
`campanhas/<slug>/` — slug curto, minúsculo, sem acento, sem espaço (ex.: `biquinis`,
`neoprene`, `poncho`). Um slug por linha/projeto de campanha.

## Campanha (Google Ads)
`<Rede> - <Linha/Tema>` — ex.: `Search - Biquínis`, `Search - Hot Pant`,
`Search - Marca e Consideração`, `Shopping - Biquíni & Hot Pant`.
- Rede: `Search` ou `Shopping` (PMax só quando pedido).
- Uma campanha por eixo de controle de budget/lance (linha, marca, consideração).

## Ad group
`<Linha> | <Tema/Intenção>` — pipe com espaços. Um tema por grupo, 5–20 KWs.
Ex.: `Biquíni | Empina Bumbum`, `Hot Pant | Proteção Solar UV50`, `Marca | Use Zero Hora`.

## Listas compartilhadas
- Negativas: `Negativas <Linha/Tema>` — ex.: `Negativas Biquíni & Hot Pant`.

## Extensões
Nível recomendado: campanha (ou conta, quando genéricas da marca). Sitelinks/callouts/
snippets podem ser compartilhados entre campanhas da mesma linha.

## Convenção de arquivos da campanha
`00-produtos.md` · `01-kws.md` · `02-ads.md` · `03-csv/` · `04-medicao.md`.
Snapshots de ferramenta em `reports/AAAA-MM-DD-<descricao>.md`.
Bases recebidas em `data/<slug>/AAAA-MM-DD-<origem>.<ext>`.
