# UTM no nível da conta — 2026-08-09

> **STATUS: APLICADO em 2026-08-09, via API.**

## O que foi feito

Cadastrado o **sufixo do URL final** no nível da conta (2614617888):

```
utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}
```

Antes: nenhum UTM em nenhum nível (conta, campanha, grupo, anúncio).
Depois: sufixo herdado por todas as campanhas, atuais e futuras.

## Por que não saiu em CSV

Configuração de **conta** não é entidade dos templates de upload em massa
(que cobrem campanha, grupo, KW, negativa, anúncio). Sem CSV possível,
foi aplicado por API — mesmo protocolo da renomeação: simulação
(`validateOnly`) antes, `updateMask` restrito ao campo alterado
(`finalUrlSuffix`) e conferência do estado final depois.

Campanhas novas criadas por CSV não precisam repetir o sufixo: herdam o
da conta. A coluna `Final URL suffix` do CSV de campanha fica reservada
para exceção justificada.

## Verificação pós-aplicação

| Campo da conta | Estado |
|---|---|
| `finalUrlSuffix` | sufixo acima, aplicado |
| `trackingUrlTemplate` | vazio (proposital — sufixo não altera a URL exibida nem arrisca quebrar a landing) |
| `autoTaggingEnabled` | `true` — **intocado**, segue alimentando a conversão de compra |

Pré-requisito atendido antes de aplicar: usuário testou e confirmou que a
plataforma da loja preserva parâmetros de query na navegação.

## Reversão

Se necessário, limpar com o mesmo mecanismo (`finalUrlSuffix` vazio,
`updateMask=finalUrlSuffix`). Não afeta histórico nem conversões.
