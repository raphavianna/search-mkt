# Integração Google Ads — conta direta (sem MCC)

Integração da conta Google Ads da Use Zero Hora a este repositório via
**API oficial do Google Ads (REST)**, autenticando **direto na conta**,
sem vincular a conta a nenhuma MCC.

## Arquitetura

```
Claude Code (web) ──► variáveis de ambiente (credenciais)
        │
        ├── gads.py            cliente REST (OAuth refresh + GAQL + mutate)
        ├── check_conexao.py   verificação de conexão e diagnóstico
        └── aplicar_rename.py  aplica renomeações dos CSVs de manutenção
                │
                ▼
   googleads.googleapis.com (REST, v21)
                │
                ▼
   Conta Google Ads da marca (customer ID direto)
```

Pontos de desenho:

- **Sem MCC na operação.** O OAuth é feito com o e-mail que administra a
  conta, e todas as chamadas usam o customer ID da própria conta. Nenhum
  header `login-customer-id` é enviado (a variável existe, mas fica vazia).
  A única aparição de MCC no processo é burocrática: o *developer token* da
  API só é emitido dentro do Centro de API de uma conta de administrador —
  mas essa MCC serve apenas de "portadora" do token e **não precisa (nem
  deve) ter a conta da marca vinculada a ela**. Detalhes no `SETUP.md`.
- **REST puro, sem dependências.** Os scripts usam somente a biblioteca
  padrão do Python (o ambiente do Code web é efêmero; nada de `pip install`
  nem gRPC, que sofre com proxy).
- **Credenciais só em variáveis de ambiente.** Nada de segredo em arquivo
  do repositório; o `.gitignore` reforça isso. No Code web, as variáveis
  são configuradas no ambiente da sessão (Settings do ambiente).

## Variáveis de ambiente

| Variável | Obrigatória | Descrição |
|---|---|---|
| `GOOGLE_ADS_DEVELOPER_TOKEN` | sim | Developer token do Centro de API |
| `GOOGLE_ADS_CLIENT_ID` | sim | OAuth client ID (Google Cloud) |
| `GOOGLE_ADS_CLIENT_SECRET` | sim | OAuth client secret |
| `GOOGLE_ADS_REFRESH_TOKEN` | sim | Refresh token do e-mail admin da conta |
| `GOOGLE_ADS_CUSTOMER_ID` | sim | ID da conta (10 dígitos, sem hífens) |
| `GOOGLE_ADS_LOGIN_CUSTOMER_ID` | não | Vazia = acesso direto (padrão). Só preencher se um dia a operação migrar para MCC |
| `GOOGLE_ADS_API_VERSION` | não | Padrão `v21` |

Modelo em `.env.example` (para uso local; no Code web use as variáveis do
ambiente).

## Uso

```bash
# diagnóstico completo da conexão (rode após configurar as variáveis)
python3 integracao/google-ads/check_conexao.py

# consulta GAQL avulsa
python3 integracao/google-ads/gads.py "SELECT campaign.name, campaign.status FROM campaign"
```

O `check_conexao.py` valida, nesta ordem: variáveis presentes → OAuth
(refresh do access token) → developer token (lista contas acessíveis) →
acesso à conta (nome, moeda, fuso, auto-tagging) → medição de conversão
(ações de conversão ativas) → campanhas existentes. Cada etapa reporta
sucesso ou o erro exato, para saber onde parou.

## O que esta integração habilita no fluxo de campanhas

- **Regra 7 de `<ferramentas_de_dados>` do CLAUDE.md**: dados de conta
  própria (termos de pesquisa, conversões, CPC real por KW) passam a vir
  por consulta GAQL, vencendo estimativas de ferramenta para o que já
  rodou na conta. Snapshots datados vão para `reports/`, como sempre.
- **Etapa 3 (medição)**: acompanhamento de termos de pesquisa, Quality
  Score, conversões por grupo direto da conta.
- A **criação** de campanhas continua pelo fluxo aprovado (CSVs no modelo
  de `master/templates-csv/`).

## Escrita via API

Liberada pelo usuário em 2026-08-09 para **manutenção** (a criação de
campanha segue por CSV). Regras:

1. **O CSV continua sendo a fonte auditável.** `aplicar_rename.py` lê os
   CSVs de `manutencao/` e executa o que está neles — a planilha
   versionada e a conta não divergem.
2. **Simulação obrigatória antes.** `client.mutate()` e
   `client.renomear()` nascem com `validate_only=True`; gravar exige
   passar a flag explicitamente (`--aplicar` no script).
3. **Escopo mínimo.** `renomear()` envia `updateMask=name` — por
   construção nenhum outro campo da entidade pode ser alterado.
4. **Conferência depois.** Reconsultar o estado na conta e validar
   contra a regra pretendida; salvar snapshot em `reports/` quando a
   mudança for relevante.
5. Operação destrutiva (remover, pausar campanha ativa) só com pedido
   explícito do usuário, nunca por iniciativa própria.

```bash
python3 aplicar_rename.py ../../manutencao/<pasta>/*.csv            # simula
python3 aplicar_rename.py ../../manutencao/<pasta>/*.csv --aplicar  # grava
```
