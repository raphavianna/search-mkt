# Upload — Campanha Saída de Praia

**Data do upload:** 2026-08-12
**Conta:** `* Use Zero Hora` — ID `2614617888` (BRL, America/Sao_Paulo, conta de produção)
**Método:** Google Ads API v22, `GoogleAdsService.Mutate` atômico (70 operações, `validateOnly` aprovado antes da execução)
**Fonte:** `03-csv/GoogleAds_Editor_Import_Saida_de_Praia.csv` (recebido do usuário)

## Identificadores criados

| Objeto | ID |
|---|---|
| Campanha | `24122214177` |
| Orçamento | `15785355813` |

## O que subiu

| Item | Quantidade |
|---|---|
| Grupos de anúncios | 5 |
| Keywords | 26 |
| RSAs | 5 (15 títulos + 4 descrições cada) |
| Negativas de campanha | 30 |

Grupos: `AG0 · Saída de Praia Zero Hora` (3 kws), `AG1 · Vestido Saída de Praia` (5),
`AG2 · Transparência / Tule` (4), `AG3 · Saia de Praia` (4), `AG4 · Categoria Genérico` (10).

## Configuração aplicada

- **Status: `PAUSED`** — nada veicula nem gasta até alguém ativar manualmente.
- Tipo: Search | Estratégia: Maximizar conversões | Orçamento: R$ 30,00/dia
- Rede: apenas Pesquisa Google — parceiros de pesquisa **off**, display **off**
- Local: Brasil (`geoTargetConstants/2076`) | Idioma: português (`languageConstants/1014`)
- Declaração de publicidade política da UE: não contém (obrigatório na v22)

Rede, local e idioma **não vinham no CSV** — foram definidos conforme o padrão master
do repositório (Etapa 2 de `<pipeline_de_campanha>`).

## Divergências entre o CSV e a conta — decisões tomadas

### 1. URL final (alterada — depois refinada por subcategoria)

> **Atualização 2026-08-12:** o usuário forneceu as 5 URLs reais de subcategoria e as
> URLs finais foram remapeadas. Ver "Remapeamento de URLs e extensões" no fim do arquivo.
> A seção abaixo registra a decisão original do upload.

O CSV apontava para `usezerohora.lojavirtualnuvem.com.br` (subdomínio interno da
Nuvemshop), em 4 caminhos: `/saida-de-praia`, `/saida-de-praia/vestido`,
`/saida-de-praia/transparencia`, `/saida-de-praia/saia`.

Dados que contradizem o CSV, coletados da própria conta em 2026-08-12:

- Os **16 anúncios já existentes** na conta usam `usezerohora.com.br`. Nenhum usa o
  subdomínio da Nuvemshop.
- A ação de conversão ativa — `Compra (usezerohora.com.br/)`, tipo PURCHASE, primária —
  está registrada em `usezerohora.com.br`. Mandar tráfego para outro domínio arrisca
  não registrar conversão, o que inviabilizaria a estratégia Maximizar conversões.
- Das 4 URLs do CSV, a única página de saída de praia comprovadamente existente na
  conta é `https://usezerohora.com.br/feminino/saida-de-praia/` (usada pela campanha
  `[004-SHOPPING]-MAIO` e por sitelinks). Os caminhos `/saida-de-praia/vestido`,
  `/transparencia` e `/saia` não aparecem em lugar nenhum da conta.

**Decisão:** os 5 grupos apontam para `https://usezerohora.com.br/feminino/saida-de-praia/`.

**Limitação declarada:** o proxy de rede desta sessão bloqueia `usezerohora.com.br` e
`usezerohora.lojavirtualnuvem.com.br`, então **nenhuma URL foi verificada por requisição
HTTP**. A escolha se apoia em dados da conta, não em checagem da página. Se existirem de
fato subcategorias por tipo de peça (vestido/transparência/saia), vale trocar as URLs
por grupo antes de ativar — ganho de relevância e Quality Score.

### 2. Nome da campanha (alterado)

CSV: `ZH | Search | Saída de Praia`. A conta segue `[00N-CANAL]-PRODUTO`
(`[009-PMAX]-NEOPRENE` era o último). Subiu como **`[010-SEARCH]-SAIDA-DE-PRAIA`**
para manter a numeração sequencial dos relatórios.

## Validação de limites de caracteres

CSV conferido antes do upload: **0 violações** em 75 títulos (≤30), 20 descrições (≤90)
e 10 caminhos de exibição (≤15).

---

# Remapeamento de URLs e extensões — 2026-08-12

O usuário confirmou que as subcategorias existem e forneceu as 5 URLs reais. Segundo
mutate atômico de 33 operações (`validateOnly` aprovado antes de executar).

## URLs finais por grupo

| Grupo | URL final |
|---|---|
| AG0 · Saída de Praia Zero Hora | `/feminino/saida-de-praia/` |
| AG1 · Vestido Saída de Praia | `/feminino/saida-de-praia/vestido-manga-longa/` |
| AG2 · Transparência / Tule | `/feminino/saida-de-praia/` |
| AG3 · Saia de Praia | `/feminino/saida-de-praia/saia/` |
| AG4 · Categoria Genérico | `/feminino/saida-de-praia/` |

Base: `https://usezerohora.com.br`.

Racional do mapeamento:

- **AG1 → `vestido-manga-longa`**: 2 das 5 keywords do grupo pedem comprimento
  explicitamente (`vestido saída de praia longo`, `saída de praia manga longa`) e
  nenhuma pede regata. `vestido-regata` fica coberta por sitelink. Se o volume
  justificar, vale quebrar o AG1 em dois grupos (manga longa × regata) e dar a cada um
  a sua URL — hoje `vestido de praia feminino` e `vestido saída de praia`, que são
  genéricas, caem em manga longa.
- **AG2 → categoria mãe**: não existe subcategoria de transparência/tule; as peças com
  transparência estão espalhadas pelos tipos.
- **AG0 (marca) e AG4 (genérico) → categoria mãe**: intenção ampla, a categoria cobre
  todo o sortimento.

## Extensões criadas (nível de campanha)

**5 sitelinks** — texto ≤25, descrições ≤35 cada:

| Texto | Descrição 1 | Descrição 2 | Destino |
|---|---|---|---|
| Vestido Manga Longa | Vestidos longos para a praia | Pronta entrega Zero Hora | `/vestido-manga-longa/` |
| Vestido Regata | Vestidos regata de praia | Loja oficial Zero Hora | `/vestido-regata/` |
| Saia de Praia | Saias em tule e transparência | A partir de R$49,99 | `/saia/` |
| Conjunto Atoalhado | Conjuntos em tecido atoalhado | Pronta entrega Zero Hora | `/conjunto-atoalhado/` |
| Shorts de Praia | Shorts de praia femininos | Loja oficial Zero Hora | `/shorts/` |

**8 callouts** (≤25): Pronta Entrega · Loja Oficial Zero Hora · A Partir de R$49,99 ·
Envio para Todo o Brasil · Fabricação Própria · Compra Online Segura ·
Novos Modelos 2026 · Modelos com Transparência

**1 snippet estruturado** — `Tipos`: Vestido Manga Longa, Vestido Regata, Saia de Praia,
Conjunto Atoalhado, Shorts de Praia

**Procedência da copy das extensões:** as afirmações reaproveitam claims que já estavam
no CSV aprovado (pronta entrega, loja oficial, a partir de R$49,99, transparência) mais
`fabricação própria` e `envio para todo o Brasil`, que vêm do contexto de marca do
`CLAUDE.md`. Nenhuma página foi lida — o proxy da sessão bloqueia o domínio. **Preço e
prazo mudam: reconfirmar `A Partir de R$49,99` e `Envio para Todo o Brasil` na loja
antes de ativar.**

## Status editorial dos anúncios

AG0, AG2 e AG4 voltaram `APPROVED`. AG1 e AG3 voltaram a `UNKNOWN` — esperado, porque
editar a URL final de um anúncio dispara nova análise do Google.

## Pendências antes de ativar

- [ ] Reconfirmar na loja os claims de preço (`A partir de R$49,99`) e envio
- [ ] Conferir aprovação editorial de AG1 e AG3 (reanálise em andamento) e dos sitelinks
- [ ] Avaliar quebrar o AG1 em manga longa × regata
- [ ] Ativar a campanha (`status: ENABLED`) quando o acima estiver fechado
