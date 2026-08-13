# Registro — Correção preventiva de URLs + suavização de descrições (2026-08-13)

## Contexto
Continuação do `registro-politica-2026-08-13.md`: os 4 anúncios com
`DESTINATION_NOT_CRAWLABLE` foram corrigidos. Este registro cobre as ações
preventivas para os grupos que ainda usavam `/search/?q=` e a suavização
das descrições RSA com "levanta".

---

## Tarefa 1 — URLs dos 4 ad groups em risco movidas para rastreáveis

**Script:** `corrige_urls_search.py execute`
**Validação prévia:** OK (dry-run confirmou 4 anúncios + URLs corretas)

| Ad group | URL antes | URL depois |
|---|---|---|
| `[011-B]-CORTININHA-COMPRA` | /search/?q=cortininha | /feminino/biquini/ |
| `[011-C]-ASA-DELTA-COMPRA` | /search/?q=asa+delta | /feminino/biquini/ |
| `[011-D]-SEM-BOJO-COMPRA` | /search/?q=biquini+sem+bojo | /feminino/biquini/ |
| `[012-E]-CROPPED-COMPRA` | /search/?q=hot+pant+cropped | /feminino/biquini/hot-pant/ |

**Situação após:** todos os anúncios das campanhas [011] e [012] apontam para
URLs rastreáveis (`/feminino/biquini/` ou `/feminino/biquini/hot-pant/`).
Zero exposição a `DESTINATION_NOT_CRAWLABLE`.

---

## Tarefa 2 — Suavização de descrição RSA em [011-A]-EMPINA-BUMBUM-COMPRA

**Script:** `suaviza_descricoes_bumbum.py execute`
**Regra de substituição (mais específica primeiro, para evitar redundância):**
1. `"modelagem que levanta e valoriza"` → `"modelagem que realça e valoriza"`
2. `"modelagem que levanta"` → `"modelagem que valoriza"`
3. `"efeito que levanta"` → `"caimento que valoriza"`

**Alteração aplicada:**

| Campo | Antes | Depois |
|---|---|---|
| Descrição (RSA `820710582438`) | "…com modelagem que levanta e valoriza o corpo." | "…com modelagem que realça e valoriza o corpo." |

O termo "empina bumbum" permanece (é nome de modelo, aprovado). Apenas o
reforço verbal na descrição foi suavizado.

---

## Tarefa 3 — Sitelinks com /search/?q= e "Modelagem que levanta" (mesma sessão)

**Script:** `corrige_sitelinks.py execute`
Assets atualizados via AssetService:mutate (updateMask `final_urls` + `sitelink_asset.description1`).

| Sitelink | Asset ID | URL antes | URL depois | desc1 antes | desc1 depois |
|---|---|---|---|---|---|
| "Biquíni Cortininha" (BIQUINI) | 407254495465 | `/search/?q=cortininha` | `/feminino/biquini/` | — | — |
| "Empina Bumbum" (BIQUINI) | 407254494838 | `/search/?q=empina+bumbum` | `/feminino/biquini/` | "Modelagem que levanta" | "Modelagem que valoriza" |
| "Manga 3/4 e Longa" (HOT-PANT) | 407254497592 | `/search/?q=hot+pant+manga` | `/feminino/biquini/hot-pant/` | — | — |

Verificação pós-execute: URLs e desc1 confirmados via GAQL.

**Estado final:** zero URLs `/search/?q=` em anúncios ou sitelinks de [011] e [012].
Zero descrições com "levanta" em anúncios ou sitelinks.
