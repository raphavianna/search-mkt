# Renomeação para a taxonomia oficial — 2026-08-09

> **STATUS: APLICADO em 2026-08-09, via API** (a pedido do usuário), com
> `integracao/google-ads/aplicar_rename.py` lendo estes mesmos CSVs.
> Simulação (`validateOnly`) aprovada antes da gravação; estado final
> conferido por consulta contra a regex da taxonomia — 13/13 conformes.

Alinha a base instalada ao padrão de `master/nomenclatura.md`. Só muda
**nome**: nenhum lance, orçamento, status, KW ou anúncio é tocado.
Identificação por **ID** (a coluna `Campaign ID` / `Ad group ID` é o que
garante renomear a entidade existente em vez de criar uma nova).

Dados de origem: consulta GAQL na conta 2614617888 em 2026-08-09.

## Como foi aplicado

```bash
cd integracao/google-ads
python3 aplicar_rename.py ../../manutencao/2026-08-09-taxonomia/*.csv            # simula
python3 aplicar_rename.py ../../manutencao/2026-08-09-taxonomia/*.csv --aplicar  # grava
```

O script envia `updateMask=name`: por construção, nenhum outro campo
pode ser alterado, mesmo que o CSV tenha valor em outra coluna.

**Alternativa manual** (se preferir a interface): subir em
**Ferramentas e configurações → Ações em massa → Uploads**, nesta ordem —
`01-campanhas-rename.csv` e depois `02-grupos-rename.csv` (o arquivo de
grupos já traz o **novo** nome da campanha na coluna `Campaign`; fora de
ordem o nome não bate). Sempre usar a pré-visualização.

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

## Grupo de ativos da PMax — aplicado por API

| Campanha | Atual | Novo |
|---|---|---|
| `[001-PMAX]-PONCHO-FEMININO` | `001 - PONCHO FEMININO` | `[001-A]-PONCHO-FEMININO` |

Não existe upload em massa para **grupos de ativos**, então pela via CSV
isso seria um passo manual na interface. Pela API foi aplicado junto com
o resto (`assetGroups`), o que fecha 100% da taxonomia — vantagem real
da via API sobre a planilha neste caso.

## Conferência (feita em 2026-08-09)

- Estado final consultado na conta e validado contra a regex da
  taxonomia: **13/13 conformes** (6 campanhas, 6 grupos de anúncio,
  1 grupo de ativos), incluindo o elo número-do-grupo ↔ campanha-mãe.
- Renomear **não apaga histórico de performance** (a métrica segue o ID).
- **Pendente do usuário:** revisar relatórios salvos, regras
  automatizadas, scripts e painéis que filtrem campanha **por nome** —
  esses precisam ser atualizados para os nomes novos.
