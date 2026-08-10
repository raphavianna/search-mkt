# URLs finais e tracking — padrão da marca

Baseado na auditoria da conta em 2026-08-09
(`reports/2026-08-09-google-ads-auditoria-urls-tracking.md`).

> **Estado atual da conta (2026-08-09):** auto-tagging **ativo** e sufixo
> de UTM **aplicado no nível da conta** (abaixo), depois do teste de
> preservação de parâmetros aprovado pelo usuário. Nenhum tracking
> template em uso — proposital.

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
  sessão. **Testado e aprovado pelo usuário em 2026-08-09.**

### Por que IDs e não nomes

`{campaignid}`/`{adgroupid}` entregam número, não nome legível. A troca é
deliberada: o ID **não quebra quando a campanha é renomeada** (como
aconteceu na taxonomia de 2026-08-09) e não exige manutenção por
campanha. Nomes legíveis exigiriam sufixo fixo campanha a campanha, que
volta a divergir a cada renomeação. Quem lê relatório dentro do
ecossistema Google não é afetado: o GA4 recebe nome de campanha pelo
`gclid`. Se o painel da loja precisar de nome legível, o caminho é sufixo
por campanha — mudança consciente, com o custo de manutenção assumido.

### Comportamento fora da Pesquisa

`{keyword}` só resolve em campanhas de Pesquisa. Em Shopping e PMax o
parâmetro chega vazio (`utm_term=`), o que é esperado e inofensivo —
`utm_source`, `utm_medium`, `utm_campaign` e `utm_content` seguem
preenchidos.

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

## Caso resolvido — campanha 006 (referência de método)

`[006-SEARCH]-LYCRA` apontava para `http://www.usezerohora.com.br` (http,
`www`, home) com um grupo único de 47 KWs misturando gênero. **Resolvido
em 2026-08-09** dividindo em três grupos, cada um com a URL da sua
coleção — ver `manutencao/2026-08-09-lycra-split/`.

Lição que virou regra: **URL errada raramente se resolve trocando a URL**.
Quando um grupo mistura intenções (gênero, categoria, estágio de funil),
nenhuma URL única serve — o conserto é dividir o grupo. Antes de corrigir
uma URL, classifique as keywords do grupo e confira se elas apontam para
o mesmo destino.

## Limitação do ambiente

O ambiente do Claude Code web usado neste projeto tem política de rede
que **bloqueia `usezerohora.com.br`** (403 no proxy). Consequência: não é
possível conferir URL (status, redirect) nem coletar conteúdo de página
de produto por aqui — o que a **Etapa 0 exige**. Antes da Etapa 0,
liberar o domínio nas configurações de rede do ambiente ou fornecer o
conteúdo das páginas por outro meio.
