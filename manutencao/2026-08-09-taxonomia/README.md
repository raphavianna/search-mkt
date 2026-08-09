# Renomeação para a taxonomia oficial — 2026-08-09

Alinha a base instalada ao padrão de `master/nomenclatura.md`. Só muda
**nome**: nenhum lance, orçamento, status, KW ou anúncio é tocado.
Identificação por **ID** (a coluna `Campaign ID` / `Ad group ID` é o que
garante renomear a entidade existente em vez de criar uma nova).

Dados de origem: consulta GAQL na conta 2614617888 em 2026-08-09.

## Ordem de subida (obrigatória)

1. `01-campanhas-rename.csv`
2. `02-grupos-rename.csv`

Campanhas primeiro: o arquivo de grupos já traz o **novo** nome da
campanha na coluna `Campaign`. Subir fora de ordem faz o nome não bater.

Caminho: **Ferramentas e configurações → Ações em massa → Uploads**.
Sempre usar a **pré-visualização** antes de aplicar.

## De-para — campanhas

| ID | Nome atual | Nome novo | Motivo |
|---|---|---|---|
| 23916468618 | `[001-PMAX]-PONCHO-FEMININO` | *(sem mudança)* | já conforme |
| 24120633838 | `[002-SEARCH]-INSTITUCIONAL SEARCH` | `[002-SEARCH]-INSTITUCIONAL` | espaço no nome e "SEARCH" repetido |
| 24110155431 | `[003-SHOPPING] PONCHO-SHOPPING` | `[003-SHOPPING]-PONCHO` | espaço após o colchete; "SHOPPING" repetido |
| 24120681592 | `[004-MAIO]-SHOPPING` | `[004-SHOPPING]-MAIO` | canal e tema invertidos |
| 24110345733 | `[005-LYCRA]-SHOPPING` | `[005-SHOPPING]-LYCRA` | canal e tema invertidos |
| 24110422707 | `006-LYCRA-SEARCH` | `[006-SEARCH]-LYCRA` | sem colchetes e invertido |

## De-para — grupos de anúncio

| ID | Campanha | Nome atual | Nome novo | Motivo |
|---|---|---|---|---|
| 201520465560 | 002 | `Grupo de anúncios 1` | `[002-A]-INSTITUCIONAL-MARCA` | nome default; as 12 KWs são todas de marca ("use zero hora", "zerohora surf") → intenção MARCA |
| 207493793508 | 003 | `PONCHO-01` | `[003-A]-PONCHO-COMPRA` | sequencial numérico virou letra |
| 199784258140 | 004 | `[001-MAIO-LANCAMENTOS]` | `[004-A]-LANCAMENTOS-COMPRA` | **prefixo 001 não correspondia à campanha-mãe (004)** |
| 200672357444 | 004 | `[001-MAIO-AON]` | `[004-B]-AON-COMPRA` | idem; segundo grupo da campanha → letra B |
| 198568929066 | 005 | `[005-LYCRA-SHOPPING]` | `[005-A]-LYCRA-COMPRA` | faltava a letra; "SHOPPING" já está na campanha |
| 207497286628 | 006 | `006-A-LYCRA-GERAL` | `[006-A]-LYCRA-GENERICO` | colchetes + vocabulário oficial de intenção |

O tema (MAIO, PONCHO, LYCRA) sai do nome do grupo quando já está na
campanha — o elo é o número. `AON` foi preservado como subtema por ser
termo interno da operação; se significar outra coisa, é só ajustar.

## Passo manual — grupo de ativos da PMax

O Google não oferece upload em massa para **grupos de ativos**. Renomear
pela interface:

| Campanha | Atual | Novo |
|---|---|---|
| `[001-PMAX]-PONCHO-FEMININO` | `001 - PONCHO FEMININO` | `[001-A]-PONCHO-FEMININO` |

## Conferência após aplicar

- A pré-visualização deve mostrar **5 campanhas alteradas** e
  **6 grupos alterados**, todas do tipo "nome". Se aparecer criação de
  campanha ou grupo, **cancelar** — sinal de ID errado ou ordem trocada.
- Renomear **não apaga histórico de performance** (a métrica segue o ID).
- Verificar depois: relatórios salvos, regras automatizadas, scripts e
  painéis que filtrem campanha **por nome** — esses precisam do nome novo.
