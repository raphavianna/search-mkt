# [006-SEARCH]-LYCRA — Etapa 1: diagnóstico e estrutura proposta

> **Status: PROPOSTA — nada aplicado.** Aguarda decisão do usuário.
> **Fontes:** API Google Ads (conta 2614617888), coleta de 2026-08-09 —
> `keyword_view`, `search_term_view` e `campaign` (acumulado da campanha e
> últimos 30 dias da conta). Snapshot dos termos em
> `reports/2026-08-09-lycra-termos-de-pesquisa.md`.
> Semrush **não foi consultado** nesta rodada: dado de conta própria vence
> estimativa de ferramenta para o que já rodou (regra 7 do CLAUDE.md), e
> ele basta para a decisão de estrutura. Semrush entra para dimensionar
> volume de mercado dos termos novos, antes de definir orçamento.

## 1. Diagnóstico — o que os números dizem

| Métrica (acumulado da campanha) | Valor |
|---|---|
| Impressões | 208 |
| Cliques | 14 (CTR 6,73%) |
| Custo | R$ 24,07 (CPC médio R$ 1,72) |
| Conversões | **0** |
| Orçamento diário | R$ 15,00 |
| Gasto médio/dia (últimos 30d) | **R$ 0,37 — 2,5% do orçamento** |

Quatro achados, em ordem de impacto:

**1.1 — A campanha não tem alcance, não tem problema de orçamento.**
Gasta 2,5% do que pode. Das 47 keywords, **34 nunca tiveram uma única
impressão** — são cauda longa hiperespecífica em correspondência de frase
("camiseta lycra rosa com preto", "camiseta lycra surf com dedal",
"camiseta lycra surf para stand up paddle"). Elas não têm volume de busca
no Brasil. A estrutura atual dá a *ilusão* de cobertura.

**1.2 — O mercado não procura "lycra". Procura "proteção UV".**
Dos 6 cliques em termos relevantes, **5 vieram de linguagem de proteção
solar**, não de surf:

| Termo que gerou clique | Custo |
|---|---|
| blusa proteção uv | R$ 4,43 |
| camiseta uv | R$ 2,84 |
| roupa anti uva e uvb | R$ 1,99 |
| roupa uva uvb | R$ 1,37 |
| camiseta manga longa uv 50+ masculina | R$ 1,26 |
| lycra surf | R$ 0,90 |

A KW campeã de impressão é **"camisa uv surf" (115 impr, 55% do total)** —
de novo, linguagem UV. O keyword set está escrito no vocabulário da
marca ("lycra de surf"), não no do comprador ("camisa com proteção UV").

**1.3 — Quase metade das impressões vai para marca de concorrente.**

| Categoria do termo | Impressões | % | Cliques |
|---|---:|---:|---:|
| **Marca de concorrente** | 98 | **47,6%** | 0 |
| Relevante | 79 | 38,3% | 6 |
| Categoria errada | 29 | 14,1% | 0 |

Concorrentes que aparecem: UV Line/UVLine (38 impr), Litoraneus (19),
Tempestal, Extreme UV, UV Action, UV Life, DBoaSwim, Freesurf, UVBeach,
Brasil Swim, Magah, Seaway, Lupo, Decathlon. Categoria errada: pesca,
maiô/natação, ciclismo, corrida, kimono, wetsuit, neoprene, espanhol
("ropa anti rayos uva").

Não custa dinheiro (0 cliques), mas **derruba o CTR e, com ele, o Índice
de Qualidade** — que é o que define quanto se paga por clique nos termos
que importam. A correspondência de frase do Google está esticando o
sentido até nome de loja concorrente.

**1.4 — Achado crítico, fora do escopo de estrutura: a conta não mede
receita.** Nos últimos 30 dias a conta registrou **11,7 conversões com
R$ 9,08 de valor total** — cerca de R$ 0,78 por "compra". A ação de
conversão é do tipo `WEBPAGE_CODELESS` (regra de URL), que **conta a
compra mas não captura o valor da transação**.

Consequências práticas: o ROAS de 0,01x é artefato de medição, não
realidade; **tROAS e Maximizar valor de conversão são inviáveis**; e não
há como dizer se o CPA de R$ 84,84 da conta é lucrativo ou ruinoso sem
saber o ticket médio. **Corrigir isso vale mais que qualquer
reestruturação desta campanha** — é pré-requisito para otimizar por
margem em vez de por volume.

## 2. O que o diagnóstico implica

O pedido foi granularidade por característica de keyword. A resposta
honesta: **granularidade não é o gargalo — alcance e vocabulário são.**
Fatiar 208 impressões em 8 grupos temáticos produziria oito grupos sem
dado nenhum, e lance inteligente não aprende com isso.

A estrutura abaixo é desenhada para **onde a campanha vai chegar** depois
da correção de vocabulário, com granularidade justificada por dois
critérios objetivos — e só eles:

- **A característica exige página de destino diferente?** (gênero exige)
- **A característica exige ângulo de copy diferente?** (surfista × pessoa
  buscando proteção solar exige)

Cor, manga, tecnologia e modalidade **não** passam nesses testes: mesma
página, mesmo argumento. Viram variação dentro do RSA (que já escolhe o
título conforme a busca) e alvo de colheita de termos, não grupo próprio.

## 3. Estrutura proposta — 4 grupos

| Grupo | Característica | Página | Ângulo do RSA |
|---|---|---|---|
| `[006-A]-UV-MASCULINA` | proteção solar + masculino | `/masculino/lycra-surf/` | proteção UV para homem |
| `[006-B]-UV-FEMININA` | proteção solar + feminino | `/feminino/lycra-surf1/` | proteção UV para mulher |
| `[006-C]-UV-GENERICO` | proteção solar sem gênero | geral (masc. por ora) | proteção UV, benefício puro |
| `[006-D]-LYCRA-SURF` | linguagem de surfista | geral (masc. por ora) | performance no mar, surf |

Ou seja: os três grupos de gênero que já existem **mudam de eixo** — de
"lycra" para "proteção UV", que é onde está a demanda — e o vocabulário
de surf ganha grupo próprio, porque fala com outra pessoa.

### Sementes por grupo

Marcadas com ✱ as colhidas de **termos de pesquisa reais da conta** (têm
demanda comprovada); as demais já são keywords ativas.

**A — UV-MASCULINA**
✱ camisa uv masculina · ✱ camiseta uv masculina · ✱ camiseta manga longa
uv 50+ masculina · ✱ blusa de proteção uv masculina · ✱ camiseta
masculina de surf · ✱ camisa de lycra surf masculina · lycra surf
masculina · camisa de lycra masculina uv50 · camisa de surfista masculina

**B — UV-FEMININA**
✱ blusa uv feminina · ✱ camisa uv feminina · ✱ blusa com proteção uv
feminina · ✱ blusa feminina proteção uv · ✱ blusa com filtro solar
feminina · ✱ camisa com proteção solar feminina · ✱ camiseta proteção
solar feminina · ✱ camiseta feminina uv · ✱ camiseta uv 50 feminina ·
✱ camiseta surf feminina · ✱ camiseta feminina manga longa uv surf ·
✱ blusa surfista feminina · camiseta lycra feminina · lycra surf feminina

**C — UV-GENERICO**
✱ camiseta uv · ✱ blusa proteção uv · ✱ roupa com proteção uv · ✱ roupa
uva uvb · ✱ camisa proteção uv · ✱ camisetas com proteção uv · ✱ camiseta
proteção uv manga longa · ✱ camisa fator de proteção uv 50 · ✱ camisa
manga longa proteção uv · ✱ camiseta para sol uv · camisa uv surf ·
camiseta de proteção solar para surf · camiseta lycra surf uv50

**D — LYCRA-SURF**
✱ lycra surf · ✱ camisa de lycra surf · ✱ camisa lycra surf · ✱ camisa
para surf lycra · ✱ camisa surf uv · ✱ surf tee · camisa surf · camiseta
surfista · blusa de surf · camisetas lycra surf · comprar camiseta lycra
surf · camiseta lycra surf unissex

### O que sai

As **34 keywords sem impressão** (cores, dedal/polegar, segunda pele,
modelagem anatômica, bicolor, stand up paddle, natação, beach tennis,
corrida) saem da campanha. Não custam nada hoje, mas não entregam
alcance e poluem a gestão. A cauda passa a ser capturada pela
correspondência dos termos-núcleo mais colheita mensal de termos de
pesquisa (Etapa 3) — que é como cauda longa deve ser tratada.

## 4. Correspondências (match types)

| Camada | Correspondência | Por quê |
|---|---|---|
| Termos-núcleo com clique comprovado | **Exata** | protege o que já funciona do desvio semântico |
| Sementes colhidas de termos reais | **Frase** | cobertura com controle |
| 2–3 termos amplos por grupo | **Ampla** | só depois de negativas em pé e conversão medindo |

Hoje são 47 KWs, todas em frase — foi assim que "camisa uv surf" acabou
concorrendo com "uv line". Ampla **só entra na fase 3**, depois da lista
de negativas e do valor de conversão corrigido; ampla sem sinal de
conversão é queima de orçamento.

## 5. Negativas a aplicar

**Marca de concorrente** (frase): uv line · uvline · litoraneus ·
litorânea · tempestal · extreme uv · uv action · uv life · uv motion ·
dboaswim · freesurf · uvbeach · brasil swim · magah · seaway · lupo ·
decathlon · outside · smolder · surfstore · teahupoo · uaradei · abreus ·
faca na rede · beach e fit

> Decisão consciente a tomar: negativar (recomendado agora) **ou** montar
> uma campanha de conquista dedicada, com orçamento e copy comparativa
> próprios. O que não funciona é o estado atual — termo de concorrente
> caindo no grupo genérico, sem copy que responda a ele.

**Categoria errada** (frase): pesca · maiô · maio · natação · biquíni ·
kimono · wetsuit · neoprene¹ · bermuda · calção · swimsuit · térmica ·
tecido · ciclismo · bike · rayos² · camisetas de corrida

¹ Neoprene sai desta campanha porque ganha campanha própria
(`[007-SEARCH]-NEOPRENE`) — negativa cruzada evita canibalização.
² Espanhol: `ropa anti rayos uva` apareceu; negativar o idioma.

Somam-se às permanentes de `master/negativas-biblioteca.md`.

## 6. Lances e orçamento

O orçamento de R$ 15/dia **não é o limitante** (usa 2,5%). Não mexer nele
até o alcance crescer.

| Fase | Gatilho | Estratégia |
|---|---|---|
| 1 — comprar dado | agora | **Maximizar cliques com limite de CPC de R$ 2,50** (CPC médio atual R$ 1,72) |
| 2 — otimizar | ≥ 15 conversões/mês na campanha | **Maximizar conversões** |
| 3 — otimizar por margem | valor de conversão corrigido + histórico | **tROAS** |

Maximizar conversões hoje é otimizar com zero sinal na campanha; o padrão
do CLAUDE.md (lance inteligente) continua respeitado — Maximizar cliques
é estratégia automática, não lance manual, e a justificativa fica
registrada aqui.

## 7. Ordem de execução sugerida

1. **Negativas** (concorrente + categoria errada) — isolada, efeito
   imediato no CTR, risco zero;
2. **Keywords novas** nos 4 grupos + remoção das 34 sem impressão;
3. **Renomeação** dos grupos para o novo eixo e criação do `[006-D]`;
4. **RSAs** por grupo, com o vocabulário do grupo nos títulos;
5. **Troca da estratégia de lance** para Maximizar cliques;
6. **Fora desta campanha, prioridade máxima:** corrigir o valor de
   conversão (item 1.4).

Os passos 1–5 saem como CSV no modelo do master e podem ser aplicados por
API, como as manutenções anteriores.
