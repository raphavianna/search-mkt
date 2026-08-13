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

## Ad group (padrão REAL da conta)
`[NNN-<LETRA>]-DESCRICAO(-COMPRA)` — **maiúsculas, sem acento, separado por hífen**,
onde `NNN` = número da campanha e `<LETRA>` = A, B, C… na ordem dos grupos.
Sufixo `-COMPRA` nos grupos de intenção de compra; grupos de marca/genérico podem
omiti-lo (ex.: `-MARCA`, `-GENERICO`). Um tema por grupo, 5–20 KWs.
Ex.: `[011-A]-EMPINA-BUMBUM-COMPRA`, `[012-B]-PROTECAO-UV50-COMPRA`,
`[007-K]-MARCA`, `[006-C]-UV-GERAL`.

> Sem acento e sem barra: "Manga 3/4" vira `MANGA-34`; "Proteção" vira `PROTECAO`.
> Este é o padrão vigente na conta (campanhas 002–012). O formato antigo
> "`<Tema> | <intenção>`" ou "`AGn · Nome`" está **descontinuado** — padronizar
> qualquer grupo que ainda apareça assim.

## Listas compartilhadas
- Negativas: `Negativas <Linha/Tema>` — ex.: `Negativas Biquíni & Hot Pant`.

## Extensões
Nível recomendado: campanha (ou conta, quando genéricas da marca). Sitelinks/callouts/
snippets podem ser compartilhados entre campanhas da mesma linha.

## Convenção de arquivos da campanha
`00-produtos.md` · `01-kws.md` · `02-ads.md` · `03-csv/` · `04-medicao.md`.
Snapshots de ferramenta em `reports/AAAA-MM-DD-<descricao>.md`.
Bases recebidas em `data/<slug>/AAAA-MM-DD-<origem>.<ext>`.
