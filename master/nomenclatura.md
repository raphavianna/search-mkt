# Padrão de nomenclatura — Google Ads (Use Zero Hora)

> Padrão observado na conta real (customer 261-461-7888) em 2026-08-09 e
> adotado como master. Exemplos vivos: `[001-PMAX]-PONCHO-FEMININO`,
> `[002-SEARCH]-INSTITUCIONAL`, `[006-SEARCH]-LYCRA`.

## Campanha

`[NNN-TIPO]-NOME`

- `NNN`: sequencial de 3 dígitos, único na conta (próximo número livre =
  maior existente + 1; conferir na conta antes de criar).
- `TIPO`: `SEARCH`, `SHOPPING`, `PMAX`.
- `NOME`: categoria/linha em MAIÚSCULAS, sem acento, hífen como separador
  (ex.: `NEOPRENE`, `PONCHO-FEMININO`, `INSTITUCIONAL`).
- Exemplos: `[006-SEARCH]-LYCRA`, `[007-SEARCH]-NEOPRENE`.

## Ad group

`[NNN-L]-TEMA(-SUFIXO)`

- `NNN`: o mesmo número da campanha-mãe.
- `L`: letra sequencial dentro da campanha (A, B, C…).
- `TEMA`: MAIÚSCULAS sem acento (ex.: `SAPATILHA-AQUATICA`, `UV-FEMININA`).
- `SUFIXO`: `COMPRA` para grupos de intenção de compra; `MARCA` para grupo
  de marca (ex.: `[002-A]-INSTITUCIONAL-MARCA`); omitir quando o tema já
  descreve (ex.: `[006-A]-UV-MASCULINA`).
- Exemplos: `[007-A]-SAPATILHA-AQUATICA-COMPRA`, `[007-K]-MARCA`.

## Anúncios

`[NNN-L]-RSA-<n>` (ex.: `[007-A]-RSA-1`).

## Listas de negativas compartilhadas

`[UZH] Negativas — <tema>` (ex.: `[UZH] Negativas — Marca/Jornal`).

## Slug de campanha no repositório

Pasta `campanhas/<slug>`: minúsculas, sem acento, hífens (ex.: `neoprene`).
Snapshots: `reports/<AAAA-MM-DD>-<slug>-<fonte>.md`.

## Histórico

- 2026-08-09: padrão `[UZH] [Search] [...] [BR]` (proposta inicial deste
  repositório) substituído pelo padrão real da conta, acima. A campanha
  neoprene foi renomeada na conta para `[007-SEARCH]-NEOPRENE`.
