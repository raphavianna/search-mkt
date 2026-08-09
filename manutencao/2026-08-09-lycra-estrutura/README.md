# Reestruturação da campanha [006-SEARCH]-LYCRA — 2026-08-09

> **STATUS: APLICADO em 2026-08-09, via API** (`plano.py --aplicar`),
> após simulação aprovada nos 7 passos. Estado final conferido.
> Diagnóstico completo em `campanhas/lycra/01-kws.md`.

## Princípio de desenho

Campanha **nova**, R$ 15/dia, 0 conversões, gastando 2,5% do orçamento.
Com pouco dado, fragmentar custa mais do que rende — mas por um motivo
específico: **o lance inteligente aprende no nível da campanha, então
mais grupos não diluem o lance; o RSA aprende por anúncio**, e é aí que a
fragmentação machuca. Cada grupo a mais divide as impressões entre mais
anúncios e atrasa o aprendizado de combinação de títulos.

Daí **3 grupos, não 8**. O corte usado é a **página de destino** — o
único eixo que muda para onde o clique vai, e o que mais pesa em conversão
(cair na página do gênero errado é abandono garantido). Cor, manga,
tecnologia e modalidade não mudam página nem argumento: viram variação
dentro dos 15 títulos do RSA, que o Google já escolhe conforme a busca.

## Estrutura final

| Grupo | KWs | Correspondência | Página |
|---|---:|---|---|
| `[006-A]-UV-MASCULINA` | 11 | 10 frase, 1 exata | `/masculino/lycra-surf/` |
| `[006-B]-UV-FEMININA` | 20 | 20 frase | `/feminino/lycra-surf1/` |
| `[006-C]-UV-GERAL` | 24 | 22 frase, 2 exata | `/masculino/lycra-surf/` * |

\* provisório, até existir coleção de lycra sem recorte de gênero.

O eixo dos nomes mudou de **LYCRA para UV** porque é assim que o mercado
busca: 5 dos 6 cliques em termos relevantes vieram de linguagem de
proteção solar, e a KW campeã de impressões é "camisa uv surf" (55% do
total). O produto continua o mesmo — mudou o vocabulário com que a
campanha fala com o comprador.

## O que foi aplicado (7 passos)

| # | Ação | Volume |
|---|---|---|
| 1 | Negativas de campanha (concorrente + categoria errada) | **49** |
| 2 | Renomeação dos 3 grupos para o eixo UV | 3 |
| 3 | Keywords novas, colhidas de termos de pesquisa reais | **27** |
| 4 | Remoção de keywords com zero impressão desde o início | **19** |
| 5 | RSAs de 15 títulos e 4 descrições, um por grupo | 3 |
| 6 | Extensões: 6 frases de destaque + 1 snippet estruturado | 7 |
| 7 | Lance: Maximizar conversões → **Maximizar cliques**, teto R$ 2,50 | 1 |

Limpeza posterior: os 2 RSAs da divisão anterior (grupos A e B) foram
removidos. Tinham copy quase idêntica à nova e, neste volume, dois
anúncios parecidos por grupo só dividem o aprendizado.

## As duas decisões que mais devem mover o ponteiro

**1. A troca de lance é o destravamento.** Maximizar conversões numa
campanha com **zero conversões** não tem sinal para aprender: o Google
liça de forma conservadora, e é por isso que a campanha gastava 2,5% do
orçamento. Maximizar cliques com teto de R$ 2,50 (CPC médio atual
R$ 1,72) compra o tráfego que gera o dado. Continua sendo lance
automático — o padrão do CLAUDE.md (nada de CPC manual) segue de pé, e a
justificativa fica registrada aqui.

Escada combinada: **Maximizar cliques** → **Maximizar conversões** (a
partir de ~15 conversões/mês na campanha) → **tROAS** (só depois de
corrigir o valor de conversão).

**2. As 49 negativas param a sangria de relevância.** 47,6% das
impressões caíam em marca de concorrente (UV Line, Litoraneus, Tempestal,
Lupo, Decathlon) com **zero clique**, e 14,1% em categoria errada (pesca,
maiô, natação, ciclismo, wetsuit). Não custava dinheiro, mas derrubava o
CTR — e CTR é o que define o Índice de Qualidade, que define o preço do
clique nos termos que importam.

Inclui negativa de **"neoprene"**, para a campanha 007 não canibalizar
esta quando entrar.

## Extensões — de zero para sete

A conta **inteira** não tinha nenhuma extensão. São ganho de CTR sem
custo adicional e obrigatórias pelo `master/extensoes-ativos.md`.

- **Frases de destaque (6):** Bloqueia Até 98% do Sol · Fabricação
  Própria · Envio em 24h Úteis · Manga Longa e Curta · Cores Vibrantes ·
  Compra no Site Oficial
- **Snippet estruturado:** cabeçalho "Tipos" — Manga Longa, Manga Curta,
  Masculina, Feminina, Proteção UV

**Sitelinks ficaram de fora**: exigem URL verificada e o site está
bloqueado pela política de rede do ambiente. É a primeira coisa a fazer
quando a rede liberar — 4 sitelinks é o item que falta para a campanha
cumprir o checklist inteiro.

## Procedência da copy

Mesma regra da divisão anterior: só claims que a marca já anunciava
(proteção UV bloqueando até 98% dos raios, manga longa e curta,
surf/praia/piscina, fabricação no Brasil) e contexto de marca do
CLAUDE.md (fabricação própria, envio em até 24h úteis, cores vibrantes).

**"UV 50+" foi deliberadamente evitado** apesar de aparecer nas
keywords: é especificação técnica (UPF) que a marca não afirma nos
anúncios atuais e que não foi possível verificar na página. Buscar por um
termo não prova que o produto o tenha.

## Pendências

- **Sitelinks** (4+), quando a rede liberar a verificação de URLs;
- **Página de lycra sem recorte de gênero**, para o grupo C sair da URL
  masculina provisória;
- **Valor de conversão** (item 1.4 do diagnóstico) — a conta conta
  compras mas não captura receita, o que trava tROAS e impede avaliar
  lucratividade. Maior prioridade da conta, fora desta campanha.

## Reproduzir

```bash
cd integracao/google-ads
python3 ../../manutencao/2026-08-09-lycra-estrutura/plano.py            # CSVs + simulação
python3 ../../manutencao/2026-08-09-lycra-estrutura/plano.py --aplicar  # grava
```

`plano.py` é fonte única: as mesmas estruturas geram os CSVs no modelo
oficial e a aplicação por API, com validação de limites antes de tudo.
