# Renomeação para a taxonomia oficial — APLICADA

- **Fonte:** API Google Ads (REST v25), conta 2614617888
- **Data de aplicação:** 2026-08-09
- **Como:** `integracao/google-ads/aplicar_rename.py` lendo os CSVs de
  `manutencao/2026-08-09-taxonomia/` (+ grupo de ativos por API)
- **Escopo:** somente nome (`updateMask=name`)
- **Resultado:** 13 entidades renomeadas, 13/13 conformes na conferência

## Estado final conferido na conta

| Campanha | Grupo | Conforme |
|---|---|---|
| `[001-PMAX]-PONCHO-FEMININO` | `[001-A]-PONCHO-FEMININO` *(grupo de ativos)* | sim |
| `[002-SEARCH]-INSTITUCIONAL` | `[002-A]-INSTITUCIONAL-MARCA` | sim |
| `[003-SHOPPING]-PONCHO` | `[003-A]-PONCHO-COMPRA` | sim |
| `[004-SHOPPING]-MAIO` | `[004-A]-LANCAMENTOS-COMPRA` | sim |
| `[004-SHOPPING]-MAIO` | `[004-B]-AON-COMPRA` | sim |
| `[005-SHOPPING]-LYCRA` | `[005-A]-LYCRA-COMPRA` | sim |
| `[006-SEARCH]-LYCRA` | `[006-A]-LYCRA-GENERICO` | sim |

Validação automática: regex da taxonomia para campanha e grupo + elo
número-do-grupo ↔ campanha-mãe. Todas as campanhas seguem `ENABLED`.

## Procedimento executado

1. Coleta dos IDs por GAQL (renomear por ID, nunca por nome).
2. Geração dos CSVs a partir dos cabeçalhos oficiais.
3. **Simulação** (`validateOnly=true`) das 11 operações de CSV → sem erro.
4. Aplicação (`validateOnly=false`).
5. Grupo de ativos da PMax: simulação + aplicação (não há CSV oficial
   para essa entidade; via API foi possível fechar 100%).
6. Reconsulta do estado final e validação contra a taxonomia.

## Pendências abertas (não aplicadas)

- **UTM**: conta sem sufixo de URL final em qualquer nível. Padrão
  proposto em `master/tracking-urls.md`; depende de testar se a
  plataforma da loja preserva parâmetros de query.
- **URL da `[006-SEARCH]-LYCRA`**: aponta para
  `http://www.usezerohora.com.br` (http, com `www`, e para a home).
  Aguardando a URL da coleção de lycra.
- **Do lado do usuário**: atualizar relatórios salvos, regras
  automatizadas e painéis que filtrem campanha por nome.
