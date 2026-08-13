# Registro de upload — Campanha Biquíni + Hot Pant (Search) via Google Ads API

- **Data:** 2026-08-13 · **Conta:** `2614617888` (* Use Zero Hora) · **API:** REST v25.
- **Método:** `05-upload/upload_biquinis.py execute` (mesma integração de
  `integracao/google-ads/`, `googleAds:mutate` com resource names temporários, atômico por campanha).
- **Estado:** todas as campanhas nascem **PAUSED**. Sem gasto até revisão e ativação manual.
- **Ensaio:** `validate` (validateOnly) passou nas 3 campanhas antes do `execute`.

## Campanhas criadas
| Campanha | ID | Orçamento/dia | Lance | Status | Ad groups | Keywords | RSAs | Negativas | Assets |
|---|---|--:|---|---|--:|--:|--:|--:|--:|
| `[011-SEARCH]-BIQUINI` | 24136476223 | R$ 7 | Maximize Conversions | PAUSED | 8 | 60 | 8 | 53 | 15 |
| `[012-SEARCH]-HOT-PANT` | 24136476898 | R$ 11 | Maximize Conversions | PAUSED | 8 | 50 | 8 | 53 | 15 |
| `[013-SEARCH]-MARCA` | 24136476661 | R$ 4 | Maximize Conversions | PAUSED | 2 | 14 | 2 | 53 | 15 |

- **Rede:** só Pesquisa Google (sem parceiros/Display). **Geo:** Brasil (presença). **Idioma:** pt (1014).
- **Assets por campanha:** 5 sitelinks + 8 callouts + 2 snippets estruturados vinculados.
- **Negativas:** lista compartilhada (53 frases: colisão jornal Zero Hora + DIY + baixa intenção + fora do alvo) aplicada às 3 campanhas.
- **Orçamento:** calibrado pelo forecast do Keyword Planner (CPC R$ 0,15; conjunto Search ~R$ 22/dia), split por ticket/demanda.

## Pendências antes de ATIVAR (não ativar sem fechar)
- [ ] **URLs finais por ad group** — hoje provisórias de categoria (`/biquini`, `/hot-pant`, `/`).
      Trocar pela página exata que converte cada termo (ver `03-csv/links-sugeridos-por-adgroup.csv`).
- [ ] **Ordenação por volume/keyword** — forecast do Planner é agregado; volume por termo
      exige Semrush BR ou re-export do Planner em nível de keyword.
- [ ] Conferir na interface o Índice de otimização dos RSAs e reprovações de política.

## Como ativar (quando fechar as pendências)
Trocar `campaign.status` para `ENABLED` (interface ou API). Começar pela de maior
conversão esperada (Hot Pant, ticket alto). Acompanhar por `04-medicao.md`.

## Reproduzir / reverter
- Reproduzir: `python3 campanhas/biquinis/05-upload/upload_biquinis.py validate|execute`.
- Reverter (se preciso): remover as campanhas por ID via `campaign.status = REMOVED` na conta.
