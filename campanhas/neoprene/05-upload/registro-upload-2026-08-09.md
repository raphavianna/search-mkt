# Registro de upload — Google Ads API (2026-08-09)

- **Conta**: customer `2614617888` | API v22 | script `upload_google_ads.py`
- **Fluxo**: `validate` (validateOnly, OK) → `execute`
- **Fonte das KWs**: `kw-planner/kw-consolidada-neoprene.csv` (revisão de
  2026-08-09, 323 KWs; subiram os 11 grupos ativos = 240 KWs; `concorrencia`
  e `fora-da-campanha` não subiram, por decisão registrada)

## Renomeação (2026-08-09, mesma data)

Após o upload, campanha e ad groups foram renomeados via API para o padrão
real da conta (`[NNN-TIPO]-NOME` / `[NNN-L]-TEMA`), observado nas campanhas
001–006 existentes. Mapa novo ↔ antigo abaixo. `master/nomenclatura.md`
atualizado com o padrão da conta.

## Campanha

- `[007-SEARCH]-NEOPRENE` (nome de criação: `[UZH] [Search] [Neoprene] [BR]`)
  — `customers/2614617888/campaigns/24115053024`
- **Status: PAUSED** (sem anúncios — Etapa 2 pendente; não ativar antes)
- Rede: só Pesquisa Google (sem parceiros, sem Display)
- Geo: Brasil (2076), opção presença | Idioma: português (1014)
- Lance: Maximizar conversões | Orçamento: R$30/dia (budget próprio,
  não compartilhado) — revisar valor antes de ativar
- 69 negativas de campanha em frase (jornal Zero Hora, DIY, atacado,
  emprego, marketplaces, tecido/matéria-prima, nichos fitness/ortopédico/
  pet, long john/wetsuit, infantil, trilha, pesca, 5mm; "borracha" e
  "mergulho" ficaram FORA das negativas — há KWs positivas com esses termos)

## Ad groups (todos ENABLED dentro da campanha pausada)

| Ad group (nome na conta) | Nome no repositório/planilha | ID | KWs |
|---|---|---|---|
| [007-A]-SAPATILHA-AQUATICA-COMPRA | sapatilha-aquatica-compra | 199159715756 | 45 |
| [007-B]-SAPATILHA-NEOPRENE-COMPRA | sapatilha-neoprene-compra | 199159715956 | 19 |
| [007-C]-SAPATILHA-AREIA-COMPRA | sapatilha-areia-compra | 199159715916 | 5 |
| [007-D]-CAMISETA-COMPRA | neoprene-camiseta-compra | 199159715436 | 66 |
| [007-E]-BERMUDA-NEOPRENE-COMPRA | neoprene-bermuda-compra | 199159715276 | 15 |
| [007-F]-BERMUDA-SURF-COMPRA | bermuda-surf-compra | 199159715236 | 9 |
| [007-G]-BERMUDA-NATACAO-COMPRA | bermuda-natacao-compra | 199159715196 | 14 |
| [007-H]-SURF-VESTUARIO-COMPRA | neoprene-surf-compra | 199159715716 | 13 |
| [007-I]-NATACAO-VESTUARIO-COMPRA | neoprene-natacao-compra | 199159715676 | 27 |
| [007-J]-CATEGORIA-COMPRA | neoprene-categoria-compra | 199159715476 | 23 |
| [007-K]-MARCA | neoprene-marca | 199159715516 | 4 |

Keywords: **240/240 criadas**, match conforme coluna "Match sugerido"
(frase para head terms, exata para cauda longa), sem partial failures.

## Pendências antes de ativar (checklist master)

1. **Etapa 2**: RSAs (15 títulos/4 descrições por grupo), sitelinks,
   callouts, snippets — a campanha não tem anúncios.
2. Conferir orçamento (R$30/dia é placeholder de lançamento) e a
   conversão primária (compra) na conta.
3. URLs finais por grupo (inclui decisão da página de destino do grupo
   categoria/surf/natação).
4. Revisão no Ads Editor/interface e ativação manual.
