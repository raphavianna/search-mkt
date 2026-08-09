# URLs finais e tracking — padrão da marca

Baseado na auditoria da conta em 2026-08-09
(`reports/2026-08-09-google-ads-auditoria-urls-tracking.md`): a conta tem
**auto-tagging ativo** e **nenhum UTM** em nenhum nível.

## Como as duas camadas convivem

| Camada | Para que serve | Estado |
|---|---|---|
| **Auto-tagging (`gclid`)** | Atribuição Google Ads ↔ GA4. É o que alimenta a conversão de compra da conta | ativo — **não desligar** |
| **UTM (sufixo do URL final)** | Leitura por qualquer ferramenta que não seja Google (painel da loja, planilhas, BI) | ausente — recomendado |

As duas coexistem sem conflito: o `gclid` é anexado pelo Google no
clique; o sufixo é anexado à URL final. Usar UTM **não** substitui nem
prejudica o auto-tagging.

## Padrão de UTM (sufixo do URL final)

```
utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_content={adgroupid}&utm_term={keyword}
```

- Usa **ValueTrack**: o Google preenche `{campaignid}`, `{adgroupid}` e
  `{keyword}` no clique — nada manual, nada que quebre ao renomear
  campanha.
- Cadastrar preferencialmente **no nível da conta** (vale para tudo,
  inclusive Shopping/PMax). Campanhas novas do repositório também podem
  nascer com ele pela coluna `Final URL suffix` do CSV de campanha.
- **Sufixo, não template de rastreamento**: sufixo não altera a URL
  exibida no anúncio e não corre risco de quebrar a landing page como um
  tracking template mal montado.
- **Pré-requisito antes de aplicar**: confirmar que a plataforma da loja
  preserva parâmetros de query na navegação (alguns temas descartam
  parâmetros em redirect). Teste: abrir a URL do produto com o sufixo
  colado e verificar se os parâmetros sobrevivem e se o GA4 registra a
  sessão.

## Regras de URL final

- Sempre **https** e **sem `www`** (domínio canônico
  `usezerohora.com.br`), para não depender de redirect — redirect custa
  latência e pode perder parâmetro.
- URL do anúncio aponta para a **página mais específica** que responde à
  intenção do grupo: produto para grupo de produto, coleção/categoria
  para grupo genérico. **Home só em campanha institucional/marca.**
- Toda URL final e de sitelink responde **200 sem redirect** antes de
  subir (item do checklist).
- Sitelinks nunca repetem a URL final do anúncio nem uns aos outros.

## Pendência conhecida na conta

`006-LYCRA-SEARCH` usa `http://www.usezerohora.com.br` — http, com `www`
e apontando para a home. Corrigir para a URL https da categoria lycra.
Aguardando decisão do usuário (não aplicado).
