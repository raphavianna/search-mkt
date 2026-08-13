#!/usr/bin/env python3
"""Diagnóstico de conexão com a conta Google Ads (conta direta, sem MCC).

Valida em sequência: variáveis de ambiente → OAuth → developer token →
acesso à conta → medição de conversão → campanhas. Cada etapa reporta OK
ou o erro exato, para localizar onde a configuração parou.

Uso: python3 integracao/google-ads/check_conexao.py
"""

import sys

from gads import GoogleAdsClient, GoogleAdsError, variaveis_faltantes


def etapa(n, titulo):
    print(f"\n[{n}/6] {titulo}")


def ok(msg):
    print(f"  OK — {msg}")


def falha(msg, dica=None):
    print(f"  FALHA — {msg}")
    if dica:
        print(f"  → {dica}")
    print("\nDiagnóstico interrompido. Corrija e rode de novo.")
    sys.exit(1)


def main():
    print("Diagnóstico da integração Google Ads — Use Zero Hora")

    etapa(1, "Variáveis de ambiente")
    faltantes = variaveis_faltantes()
    if faltantes:
        falha(
            "ausentes: " + ", ".join(faltantes),
            "Cadastre no ambiente do Claude Code web (SETUP.md, passo 5). "
            "Se acabou de cadastrar, inicie uma sessão nova.",
        )
    client = GoogleAdsClient.from_env()
    modo = "conta direta (sem login-customer-id)" if not client.login_customer_id \
        else f"via MCC {client.login_customer_id}"
    ok(f"todas presentes; conta {client.customer_id}, modo {modo}, "
       f"API {client.api_version}")

    etapa(2, "OAuth — refresh do access token")
    try:
        client.obter_access_token()
    except GoogleAdsError as e:
        falha(f"HTTP {e.status}: {e.body}",
              "invalid_grant = refresh token expirado/revogado → SETUP.md passo 4.")
    ok("access token obtido")

    etapa(3, "Developer token — contas acessíveis pelo usuário do OAuth")
    try:
        contas = client.listar_contas_acessiveis()
    except GoogleAdsError as e:
        falha(f"HTTP {e.status}: {e.body}",
              "DEVELOPER_TOKEN_NOT_APPROVED = solicite Acesso básico no "
              "Centro de API (SETUP.md passo 2).")
    ok(f"{len(contas)} conta(s) acessível(is): {', '.join(contas) or '—'}")
    if client.customer_id not in contas:
        print(f"  AVISO — {client.customer_id} não está na lista; o e-mail do "
              "OAuth pode não ter acesso direto a essa conta. Seguindo mesmo "
              "assim (a consulta abaixo dá o veredito).")

    etapa(4, "Acesso à conta — dados básicos")
    try:
        rows = client.search(
            "SELECT customer.descriptive_name, customer.currency_code, "
            "customer.time_zone, customer.auto_tagging_enabled, "
            "customer.conversion_tracking_setting.conversion_tracking_status "
            "FROM customer"
        )
    except GoogleAdsError as e:
        falha(f"HTTP {e.status}: {e.body}",
              "USER_PERMISSION_DENIED = e-mail do OAuth sem acesso à conta ou "
              "customer ID errado (SETUP.md, Erros comuns).")
    c = rows[0]["customer"] if rows else {}
    ok(f"'{c.get('descriptiveName', '?')}' | moeda {c.get('currencyCode', '?')} "
       f"| fuso {c.get('timeZone', '?')} "
       f"| auto-tagging {'ativo' if c.get('autoTaggingEnabled') else 'INATIVO'}")
    status_conv = (c.get("conversionTrackingSetting") or {}) \
        .get("conversionTrackingStatus", "?")
    print(f"  Medição de conversão (status da conta): {status_conv}")

    etapa(5, "Ações de conversão ativas")
    try:
        rows = client.search(
            "SELECT conversion_action.name, conversion_action.type, "
            "conversion_action.status, conversion_action.primary_for_goal "
            "FROM conversion_action WHERE conversion_action.status = 'ENABLED'"
        )
    except GoogleAdsError as e:
        falha(f"HTTP {e.status}: {e.body}")
    if rows:
        ok(f"{len(rows)} ação(ões) de conversão ativa(s):")
        for r in rows:
            ca = r["conversionAction"]
            marca = " [principal]" if ca.get("primaryForGoal") else ""
            print(f"    - {ca.get('name')} ({ca.get('type')}){marca}")
        print("  → Premissa do CLAUDE.md confirmada: lances inteligentes são o padrão.")
    else:
        print("  AVISO — nenhuma ação de conversão ativa encontrada; revisar a "
              "premissa de lances inteligentes antes de lançar campanha.")

    etapa(6, "Campanhas existentes")
    try:
        rows = client.search(
            "SELECT campaign.name, campaign.status, "
            "campaign.advertising_channel_type FROM campaign "
            "ORDER BY campaign.status"
        )
    except GoogleAdsError as e:
        falha(f"HTTP {e.status}: {e.body}")
    if rows:
        ok(f"{len(rows)} campanha(s) na conta:")
        for r in rows:
            cp = r["campaign"]
            print(f"    - {cp.get('name')} | {cp.get('advertisingChannelType')} "
                  f"| {cp.get('status')}")
    else:
        ok("nenhuma campanha na conta (conta limpa para a campanha inaugural)")

    print("\nConexão validada de ponta a ponta. Integração pronta para uso.")


if __name__ == "__main__":
    main()
