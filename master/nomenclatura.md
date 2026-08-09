# Padrão de nomenclatura — Google Ads (Use Zero Hora)

## Campanha

`[UZH] [Search] [<Categoria>] [<Recorte>] [BR]`

- `<Categoria>`: linha/categoria de produto (ex.: Neoprene, Poncho, Biquini).
- `<Recorte>`: opcional — intenção ou subestrutura quando houver mais de uma
  campanha por categoria (ex.: Marca, Genérico, Concorrência).
- Exemplos:
  - `[UZH] [Search] [Neoprene] [BR]`
  - `[UZH] [Search] [Neoprene] [Concorrencia] [BR]`

## Ad group

`<categoria>-<tema>-<intencao>`

- Minúsculas, sem acento, hífen como separador.
- `<intencao>`: `compra`, `consideracao`, `awareness`, `marca`, `concorrencia`.
- Exemplos: `neoprene-camiseta-compra`, `neoprene-categoria-consideracao`.

## Anúncios

`<ad group>-rsa-<n>` (ex.: `neoprene-camiseta-compra-rsa-1`).

## Listas de negativas compartilhadas

`[UZH] Negativas — <tema>` (ex.: `[UZH] Negativas — Marca/Jornal`).

## Slug de campanha no repositório

Pasta `campanhas/<slug>`: minúsculas, sem acento, hífens
(ex.: `neoprene`, `poncho-surf`). O slug aparece no snapshot de
`reports/` correspondente: `reports/<AAAA-MM-DD>-<slug>-<fonte>.md`.
