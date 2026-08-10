# [Campanha <tema>] Etapa 3 — Medição e otimização

> Dados de conta própria via API (`integracao/google-ads/`) vencem
> estimativas de ferramenta para o que rodou na conta. Snapshots datados
> em `reports/`.

## Rotina de acompanhamento

| Frequência | O quê | Onde/consulta | Gatilho de ação |
|---|---|---|---|
| Semanal | Termos de pesquisa | search_term_view | termo irrelevante recorrente → negativa |
| Semanal | Conversões e custo/conv. por grupo | ad_group | grupo sem conv. com gasto > X × CPA alvo → revisar |
| Quinzenal | Quality Score por KW | keyword_view | QS ≤ 4 → revisar anúncio/página |
| Mensal | Ad Strength e combinações de RSA | ad | peça fraca → testar substituição |

## Critérios de poda e expansão

- **Poda:** <regra objetiva, ex.: KW com N cliques e 0 conversão>
- **Expansão:** <termo de pesquisa convertendo → vira KW exata no grupo>
- **Lance:** <quando migrar Maximizar conversões → tCPA/tROAS, com o
  histórico mínimo definido>

## Testes de RSA

| Hipótese | Peça alterada | Métrica de decisão | Início | Resultado |
|---|---|---|---|---|

## Registro de mudanças

| Data | Mudança | Racional | Efeito observado |
|---|---|---|---|
