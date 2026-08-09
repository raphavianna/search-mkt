#!/usr/bin/env python3
"""Cliente REST mínimo da API do Google Ads — conta direta, sem MCC.

Sem dependências externas (somente stdlib). Credenciais via variáveis de
ambiente (ver README.md). Uso como módulo:

    from gads import GoogleAdsClient
    client = GoogleAdsClient.from_env()
    rows = client.search("SELECT campaign.name FROM campaign")

Uso na linha de comando (imprime JSON):

    python3 gads.py "SELECT campaign.name, campaign.status FROM campaign"
"""

import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

OAUTH_TOKEN_URL = "https://oauth2.googleapis.com/token"
API_HOST = "https://googleads.googleapis.com"
DEFAULT_API_VERSION = "v25"

ENV_VARS_OBRIGATORIAS = [
    "GOOGLE_ADS_DEVELOPER_TOKEN",
    "GOOGLE_ADS_CLIENT_ID",
    "GOOGLE_ADS_CLIENT_SECRET",
    "GOOGLE_ADS_REFRESH_TOKEN",
    "GOOGLE_ADS_CUSTOMER_ID",
]


class GoogleAdsError(Exception):
    """Erro de chamada à API, com o corpo da resposta para diagnóstico."""

    def __init__(self, status, body):
        self.status = status
        self.body = body
        super().__init__(f"HTTP {status}: {body}")


def _ssl_context():
    ctx = ssl.create_default_context()
    bundle = os.environ.get("SSL_CERT_FILE") or "/root/.ccr/ca-bundle.crt"
    if os.path.exists(bundle):
        ctx.load_verify_locations(cafile=bundle)
    return ctx


def _request(url, data=None, headers=None, method=None):
    req = urllib.request.Request(url, data=data, headers=headers or {}, method=method)
    try:
        with urllib.request.urlopen(req, context=_ssl_context(), timeout=60) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise GoogleAdsError(e.code, e.read().decode("utf-8", "replace")) from e


def variaveis_faltantes():
    return [v for v in ENV_VARS_OBRIGATORIAS if not os.environ.get(v)]


class GoogleAdsClient:
    def __init__(self, developer_token, client_id, client_secret, refresh_token,
                 customer_id, login_customer_id=None, api_version=None):
        self.developer_token = developer_token
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.customer_id = customer_id.replace("-", "")
        self.login_customer_id = (login_customer_id or "").replace("-", "") or None
        self.api_version = api_version or DEFAULT_API_VERSION
        self._access_token = None

    @classmethod
    def from_env(cls):
        faltantes = variaveis_faltantes()
        if faltantes:
            raise RuntimeError(
                "Variáveis de ambiente ausentes: " + ", ".join(faltantes)
                + " (ver integracao/google-ads/SETUP.md)"
            )
        return cls(
            developer_token=os.environ["GOOGLE_ADS_DEVELOPER_TOKEN"],
            client_id=os.environ["GOOGLE_ADS_CLIENT_ID"],
            client_secret=os.environ["GOOGLE_ADS_CLIENT_SECRET"],
            refresh_token=os.environ["GOOGLE_ADS_REFRESH_TOKEN"],
            customer_id=os.environ["GOOGLE_ADS_CUSTOMER_ID"],
            login_customer_id=os.environ.get("GOOGLE_ADS_LOGIN_CUSTOMER_ID"),
            api_version=os.environ.get("GOOGLE_ADS_API_VERSION"),
        )

    def obter_access_token(self):
        """Troca o refresh token por um access token (OAuth 2.0)."""
        if self._access_token:
            return self._access_token
        data = urllib.parse.urlencode({
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
        }).encode("utf-8")
        resp = _request(
            OAUTH_TOKEN_URL, data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )
        self._access_token = resp["access_token"]
        return self._access_token

    def _headers(self):
        headers = {
            "Authorization": f"Bearer {self.obter_access_token()}",
            "developer-token": self.developer_token,
            "Content-Type": "application/json",
        }
        # Conta direta: sem login-customer-id. Só entra se a operação um dia
        # migrar para MCC (GOOGLE_ADS_LOGIN_CUSTOMER_ID preenchida).
        if self.login_customer_id:
            headers["login-customer-id"] = self.login_customer_id
        return headers

    def listar_contas_acessiveis(self):
        """IDs de contas que o usuário do OAuth acessa diretamente."""
        url = f"{API_HOST}/{self.api_version}/customers:listAccessibleCustomers"
        resp = _request(url, headers=self._headers(), method="GET")
        return [r.split("/")[-1] for r in resp.get("resourceNames", [])]

    def mutate(self, entidade, operations, validate_only=True, customer_id=None):
        """Aplica operações de escrita em um recurso (ex.: 'campaigns').

        `validate_only=True` (padrão) só valida no servidor, sem gravar —
        é a simulação obrigatória antes de qualquer aplicação real.
        """
        cid = (customer_id or self.customer_id).replace("-", "")
        url = f"{API_HOST}/{self.api_version}/customers/{cid}/{entidade}:mutate"
        body = {"operations": operations, "validateOnly": bool(validate_only)}
        return _request(url, data=json.dumps(body).encode("utf-8"),
                        headers=self._headers())

    def renomear(self, entidade, ids_e_nomes, validate_only=True, customer_id=None):
        """Renomeia entidades. `ids_e_nomes`: lista de (id, novo_nome).

        Envia updateMask='name': por construção, nenhum outro campo da
        entidade pode ser alterado por esta chamada.
        """
        cid = (customer_id or self.customer_id).replace("-", "")
        ops = [
            {
                "update": {
                    "resourceName": f"customers/{cid}/{entidade}/{ent_id}",
                    "name": nome,
                },
                "updateMask": "name",
            }
            for ent_id, nome in ids_e_nomes
        ]
        return self.mutate(entidade, ops, validate_only=validate_only,
                           customer_id=customer_id)

    def search(self, query, customer_id=None):
        """Executa GAQL via googleAds:search e devolve a lista de resultados."""
        cid = (customer_id or self.customer_id).replace("-", "")
        url = f"{API_HOST}/{self.api_version}/customers/{cid}/googleAds:search"
        rows = []
        page_token = None
        while True:
            body = {"query": query}
            if page_token:
                body["pageToken"] = page_token
            resp = _request(url, data=json.dumps(body).encode("utf-8"),
                            headers=self._headers())
            rows.extend(resp.get("results", []))
            page_token = resp.get("nextPageToken")
            if not page_token:
                return rows


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    client = GoogleAdsClient.from_env()
    try:
        rows = client.search(sys.argv[1])
    except GoogleAdsError as e:
        print(f"Erro da API (HTTP {e.status}):\n{e.body}", file=sys.stderr)
        sys.exit(1)
    print(json.dumps(rows, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
