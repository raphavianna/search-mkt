# Diagnóstico de conexão — conta Google Ads Use Zero Hora

- **Fonte:** API Google Ads (REST v21), conta própria, via `integracao/google-ads/check_conexao.py`
- **Data de coleta:** 2026-08-09
- **Modo:** conta direta (sem MCC / sem `login-customer-id`)
- **Resultado:** conexão validada de ponta a ponta (6/6 etapas OK)

## Conta

| Campo | Valor |
|---|---|
| Nome | * Use Zero Hora |
| Customer ID | 2614617888 |
| Moeda | BRL |
| Fuso | America/Sao_Paulo |
| Auto-tagging | ativo |
| Medição de conversão | CONVERSION_TRACKING_MANAGED_BY_SELF |

## Ações de conversão ativas

| Ação | Tipo | Principal |
|---|---|---|
| Compra (usezerohora.com.br/) | WEBPAGE_CODELESS | sim |

→ Confirma a premissa do CLAUDE.md: a conta mede compra no site; lances
inteligentes (Maximizar conversões / tCPA / tROAS) são o padrão.

## Campanhas existentes na coleta

| Campanha | Canal | Status |
|---|---|---|
| [001-PMAX]-PONCHO-FEMININO | PERFORMANCE_MAX | ENABLED |
| [002-SEARCH]-INSTITUCIONAL SEARCH | SEARCH | ENABLED |
| [003-SHOPPING] PONCHO-SHOPPING | SHOPPING | ENABLED |
| [004-MAIO]-SHOPPING | SHOPPING | ENABLED |
| [005-LYCRA]-SHOPPING | SHOPPING | ENABLED |
| 006-LYCRA-SEARCH | SEARCH | ENABLED |

Observações para as próximas etapas:

- A conta tem histórico real de Search/Shopping/PMax → dados de conta
  própria (termos de pesquisa, CPC real, conversões) estão disponíveis via
  GAQL e vencem estimativas de ferramenta para o que já rodou (regra 7 de
  `<ferramentas_de_dados>`).
- Nomenclatura vigente na conta mistura padrões (`[00X-TIPO]-TEMA` com e
  sem colchetes) — considerar no padrão de nomenclatura do master.
- O usuário OAuth acessa também a conta 9193560742 (MCC emissora do
  developer token; fora da operação).
