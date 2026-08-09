# Auditoria — URLs finais e parâmetros de tracking da conta

- **Fonte:** API Google Ads (REST **v25**), conta própria (2614617888)
- **Data de coleta:** 2026-08-09
- **Escopo:** customer, 6 campanhas ativas, 6 ad groups, anúncios ativos

## Achados

### Tracking

| Nível | Tracking template | Final URL suffix |
|---|---|---|
| Conta (customer) | — | — |
| Campanhas (todas) | — | — |
| Ad groups (todos) | — | — |
| Anúncios (todos) | — | — |

- **Auto-tagging: ATIVO** → atribuição Google Ads ↔ GA4 funciona via
  `gclid`. É o que sustenta a medição de conversão atual.
- **Nenhum UTM configurado em nenhum nível.** Consequência: plataformas
  que leem UTM (painel da loja, planilhas próprias, qualquer analytics
  não-Google) enxergam o tráfego pago sem origem estruturada.

### URLs finais (anúncios de Search; Shopping usa o feed)

| Campanha > grupo | URL final | Problema |
|---|---|---|
| 006-LYCRA-SEARCH > 006-A-LYCRA-GERAL | `http://www.usezerohora.com.br` | **http** (não https) + variante **www** + aponta para a **home**, não para a categoria lycra |
| [002-SEARCH]-INSTITUCIONAL > Grupo de anúncios 1 (2 RSAs) | `https://usezerohora.com.br` | home — aceitável para institucional/marca |

### Nomenclatura observada (insumo da taxonomia)

Padrões mistos nos ad groups: `006-A-LYCRA-GERAL` (número da campanha +
letra — padrão bom), `[001-MAIO-LANCAMENTOS]` e `[001-MAIO-AON]` dentro
da campanha **004** (número não bate com a campanha-mãe),
`Grupo de anúncios 1` (nome default), `PONCHO-01`,
`[005-LYCRA-SHOPPING]`.

## Situação das recomendações (atualizado 2026-08-09, fim do dia)

| # | Recomendação | Status |
|---|---|---|
| 1 | URL da campanha 006 | **não aplicada** — grupo mistura gênero (15 fem. × 4 masc. × 28 neutras) e só há a URL masculina; correção real é dividir o grupo |
| 2 | UTM no nível da conta | **aplicada** (`manutencao/2026-08-09-tracking-utm/`) |
| 3 | Taxonomia de nomes | **aplicada** (`reports/2026-08-09-google-ads-renomeacao-aplicada.md`) |

## Recomendações (texto original da auditoria)

1. **URL da 006-LYCRA-SEARCH:** trocar para a URL canônica https da
   categoria lycra (ex.: página de coleção), não a home — relevância e
   Quality Score. Corrige junto o http/www (hoje depende de redirect).
2. **UTM padrão via "Sufixo do URL final" no nível da CONTA** (não muda
   URL exibida, não afeta gclid):
   `utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}`
   — ValueTrack preenche os IDs automaticamente. Pré-requisito: conferir
   se a plataforma da loja preserva/lê UTMs. Campanhas novas do
   repositório já podem nascer com o sufixo via coluna `Final URL suffix`
   do CSV.
3. **Nomenclatura:** taxonomia padronizada registrada em
   `master/nomenclatura.md` (campanhas numeradas, grupos com número da
   campanha + letra). Renomear a base instalada é seguro para o histórico
   de performance, mas só com pedido explícito.

## Nota técnica

Durante a auditoria o Google passou a bloquear a versão **v21** da API
(`UNSUPPORTED_VERSION`). Sondagem: v22–v25 aceitas, v26+ inexistentes.
Cliente atualizado para **v25** como padrão (maior sobrevida).
