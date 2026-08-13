# Setup de credenciais — passo a passo (100% pelo navegador)

Roteiro para obter as 5 credenciais da integração sem depender de rodar
nada em máquina local. Tempo estimado: 30–45 min (+ espera de aprovação do
developer token, quando for a primeira vez).

Antes de começar, tenha claro **qual e-mail administra a conta Google Ads
da marca** — é com ele que você fará login nos passos 3 e 4.

---

## 1. Customer ID da conta (`GOOGLE_ADS_CUSTOMER_ID`)

1. Entre em [ads.google.com](https://ads.google.com) com o e-mail admin.
2. O ID aparece no canto superior direito, no formato `XXX-XXX-XXXX`.
3. Anote **sem hífens** (ex.: `1234567890`).

## 2. Developer token (`GOOGLE_ADS_DEVELOPER_TOKEN`)

Aqui está a única esquina onde uma MCC aparece — e ela é só a "portadora"
do token. **A conta da marca NÃO será vinculada a essa MCC.** O Google só
emite developer token dentro do Centro de API de uma conta de
administrador; qual MCC emite o token é irrelevante para quais contas ele
acessa (o acesso vem do OAuth do passo 4, que é o da conta direta).

- **Se você já tem uma MCC** (mesmo vazia, ex.: da tentativa anterior):
  entre nela → **Administrador → Centro de API** → copie o token.
- **Se não tem nenhuma**: crie uma MCC nova e gratuita em
  [ads.google.com/home/tools/manager-accounts](https://ads.google.com/home/tools/manager-accounts)
  (pode usar o mesmo e-mail; é só um contêiner, não pede cartão nem cria
  campanha). Depois: **Administrador → Centro de API** → aceite os termos
  → o token aparece.
- Nível de acesso: o token nasce como **Acesso de teste** (não lê contas
  reais). No próprio Centro de API, solicite **Acesso básico**
  (formulário curto; aprovação típica em 1–3 dias úteis). Para ler a conta
  da marca, precisamos do Acesso básico.

> Se a trava anterior foi essa ("não consegui integrar a MCC"): não é
> preciso vincular, conceder acesso nem aceitar convite de MCC nenhuma.
> Só copiar o token que ela emite.

## 3. OAuth Client (`GOOGLE_ADS_CLIENT_ID` + `GOOGLE_ADS_CLIENT_SECRET`)

1. Acesse [console.cloud.google.com](https://console.cloud.google.com)
   com o e-mail admin e crie um projeto (ex.: `uzh-search-mkt`).
2. **APIs e serviços → Biblioteca** → ative **Google Ads API**.
3. **APIs e serviços → Tela de permissão OAuth**:
   - Tipo de usuário: **Externo** → modo **Teste** (não precisa publicar);
   - Adicione o e-mail admin como **usuário de teste**.
4. **APIs e serviços → Credenciais → Criar credenciais → ID do cliente
   OAuth**:
   - Tipo: **Aplicativo da Web**;
   - URIs de redirecionamento autorizados:
     `https://developers.google.com/oauthplayground`
     (é isso que permite gerar o refresh token só com o navegador);
   - Salve o **Client ID** e o **Client secret**.

## 4. Refresh token (`GOOGLE_ADS_REFRESH_TOKEN`)

Via **OAuth 2.0 Playground** — sem rodar nada local:

1. Abra
   [developers.google.com/oauthplayground](https://developers.google.com/oauthplayground).
2. Engrenagem (⚙️, canto direito) → marque **Use your own OAuth
   credentials** → cole Client ID e Client secret do passo 3.
3. No passo 1 do Playground, em "Input your own scopes", digite:
   `https://www.googleapis.com/auth/adwords`
4. **Authorize APIs** → faça login com o **e-mail admin da conta** →
   autorize (vai avisar que o app está em teste; prossiga).
5. No passo 2, clique **Exchange authorization code for tokens**.
6. Copie o **Refresh token** exibido.

> Atenção: com a tela de permissão em modo Teste, o refresh token expira
> em ~7 dias. Para token permanente, publique o app na tela de permissão
> ("Em produção" — para uso próprio não há revisão bloqueante com o escopo
> do Ads) e gere o refresh token de novo no Playground.

## 5. Configurar as variáveis no Claude Code web

No [claude.ai/code](https://claude.ai/code): abra as configurações do
**ambiente** deste projeto (Environment → Environment variables) e cadastre:

```
GOOGLE_ADS_DEVELOPER_TOKEN=...
GOOGLE_ADS_CLIENT_ID=...apps.googleusercontent.com
GOOGLE_ADS_CLIENT_SECRET=...
GOOGLE_ADS_REFRESH_TOKEN=...
GOOGLE_ADS_CUSTOMER_ID=1234567890
```

(`GOOGLE_ADS_LOGIN_CUSTOMER_ID` fica sem cadastrar — é isso que garante o
modo "conta direta".)

Sessões novas do ambiente já nascem com as variáveis. Na sessão em que
cadastrar, pode ser preciso iniciar uma nova sessão para elas valerem.

## 6. Validar

Peça na sessão (ou rode):

```bash
python3 integracao/google-ads/check_conexao.py
```

Saída esperada: todas as etapas com `OK`, incluindo a lista de ações de
conversão ativas (confirma a premissa de lances inteligentes do
CLAUDE.md). Qualquer falha vem com o erro exato da API e a dica do passo
a revisar.

---

## Erros comuns

| Erro | Causa provável | Correção |
|---|---|---|
| `invalid_grant` no OAuth | Refresh token expirado (app em modo Teste) ou revogado | Repita o passo 4; para acabar com a expiração, publique o app |
| `DEVELOPER_TOKEN_NOT_APPROVED` | Token ainda em Acesso de teste | Solicite Acesso básico no Centro de API |
| `USER_PERMISSION_DENIED` | O e-mail do OAuth não tem acesso à conta do `GOOGLE_ADS_CUSTOMER_ID` | Confirme o e-mail usado no Playground; confira o customer ID |
| `PERMISSION_DENIED` genérico na API | Google Ads API não ativada no projeto do Cloud | Passo 3.2 |
| `unauthorized_client` | Redirect URI do Playground não cadastrada no client | Passo 3.4 |
