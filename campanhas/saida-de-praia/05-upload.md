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

### 1. URL final (alterada)

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

## Pendências antes de ativar

- [ ] Confirmar a URL final — decidir entre a categoria única e URLs por subcategoria
- [ ] Extensões não vinham no CSV e **não foram criadas**: sitelinks (4+), callouts (6+),
      snippets estruturados. A Etapa 2 do master pede essas peças
- [ ] Conferir a aprovação editorial dos 5 RSAs (status ainda `UNKNOWN`, análise pendente)
- [ ] Ativar a campanha (`status: ENABLED`) quando os itens acima estiverem fechados
