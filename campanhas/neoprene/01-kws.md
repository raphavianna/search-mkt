# [007-SEARCH]-NEOPRENE — Etapa 1: KWs e estrutura

> **Status: PLANO PRONTO — aguarda Etapa 0 para subir.** A estrutura, as
> keywords e as negativas abaixo estão fechadas e podem ser aplicadas; o
> que falta é a copy dos anúncios, que depende dos atributos das páginas
> de produto (ver "Bloqueios" no fim).
> **Fonte:** API Google Ads, conta 2614617888, `search_term_view`
> acumulado — coleta de 2026-08-09/10.
> **Semrush: dado indisponível** — saldo de créditos da API zerado
> (`ERROR 132 :: API UNITS BALANCE IS ZERO`). Sem volume de mercado nem
> CPC estimado; o dimensionamento abaixo usa **CPC observado na própria
> conta**, que pela regra 7 do CLAUDE.md vence estimativa de ferramenta
> de qualquer forma — mas com amostra pequena, declarada como tal.

## 1. O que a conta já sabe sobre neoprene

Nenhuma campanha de Search de neoprene existe ainda, mas as campanhas de
Shopping e a de lycra **já captaram demanda de neoprene por engano**:
**63 termos distintos, 91 impressões, 3 cliques**.

Os 3 cliques dizem muito, porque neoprene é clique caro:

| Termo | Cliques | Custo |
|---|---:|---:|
| bota neoprene | 1 | R$ 6,74 |
| roupa termica praia | 1 | R$ 2,27 |
| camisa neoprene | 1 | R$ 1,84 |

CPC médio observado: **R$ 3,62** — mais que o dobro do CPC médio da conta
(R$ 1,49). Amostra de 3 cliques, então serve para dimensionar orçamento,
não para prever performance.

## 2. Achado principal: o mercado diz "térmica", não "neoprene"

Mesmo padrão da lycra (onde a demanda estava em "proteção UV", não em
"lycra"). Aqui, um bloco inteiro de buscas usa **"térmica"**:

| Termo | Impressões |
|---|---:|
| camisa termica maresia | 5 |
| camisa termica | 3 |
| roupa termica natacao feminina | 3 |
| camisa termica surf feminina | 2 |
| camisa termica surf / praia / praia masculina | 3 |
| blusa termica feminina / masculina / piscina | 3 |
| roupa termica praia *(gerou clique)* | 1 |
| camiseta termica · roupa termica para calor | 2 |

**~22 impressões em linguagem "térmica"**, contra ~15 em "neoprene" puro
para o mesmo produto (camisa). Quem compra chama de camisa térmica; quem
vende chama de neoprene. A campanha precisa falar as duas.

> Isso já virou regra no master (`tracking-urls.md` guarda a lição
> equivalente): antes de fechar keyword set, conferir no relatório de
> termos **com que palavra o comprador nomeia o produto**.

## 3. Concorrentes que já aparecem

| Marca | Impressões | Onde |
|---|---:|---|
| Mormaii | 6 | camisa neoprene mormaii (4), sapatilha neoprene mormaii, mormaii neoprene |
| Fiber | 8 | sapatilha fiber (3), fiber sapatilha de treino (2), + variações |
| Maresia | 5 | camisa termica maresia |
| Decathlon · Kaisan · Xterra | 3 | sapatilha fiber decathlon, kaisan macaquinho, xterra wetsuits outlet |

Mormaii e Maresia são as âncoras da categoria no Brasil; Fiber domina o
vocabulário de sapatilha. Todos entram como **negativa** (mesma decisão
da campanha 006 — nenhum clique veio deles).

## 4. Estrutura — 3 grupos, um por produto

Aplicando o mesmo critério validado na 006: **grupo novo só se mudar a
página de destino.** Aqui os três produtos têm páginas distintas, então o
corte é natural e não há fragmentação artificial.

| Grupo | Produto | URL final |
|---|---|---|
| `[007-A]-CAMISA-NEOPRENE` | Camiseta de neoprene Cabo Frio | `/produtos/camiseta-neoprene-cabo-frio-17xyv/` |
| `[007-B]-BERMUDA-NEOPRENE` | Bermuda de neoprene Joaquina | `/produtos/bermuda-neoprene-joaquina-7x5hp/` |
| `[007-C]-SAPATILHA-NEOPRENE` | Sapatilha esportiva de neoprene | `/produtos/sapatilha-esportiva-neoprene-xlgci/` |

### Keywords por grupo

✱ = termo real da conta (demanda comprovada). Correspondência: **exata**
nos que já geraram clique, **frase** no resto.

**A — CAMISA-NEOPRENE** (camiseta Cabo Frio)
✱ `[camisa neoprene]` *(clique)* · ✱ camisa neoprene 2mm · ✱ camiseta
neoprene · ✱ regata neoprene · camisa de neoprene · camiseta de neoprene ·
blusa de neoprene · camisa de neoprene surf · **linguagem térmica:**
✱ camisa termica surf · ✱ camisa termica praia · ✱ camisa termica surf
feminina · ✱ camiseta termica · ✱ blusa termica masculina · ✱ blusa
termica feminina

**B — BERMUDA-NEOPRENE** (bermuda Joaquina)
✱ bermuda de neoprene · ✱ bermuda neoprene · ✱ bermuda neoprene natação ·
✱ bermuda de neoprene para natação · bermuda de neoprene masculina ·
short de neoprene · bermuda termica · bermuda para surf neoprene

**C — SAPATILHA-NEOPRENE** (sapatilha esportiva)
✱ `[bota neoprene]` *(clique, R$ 6,74)* · ✱ sapatilha neoprene adulto ·
✱ sapatilha aquática masculina · ✱ sapatilhas aquática · ✱ sapatilha de
banho · ✱ scarpette neoprene · ✱ sapatilha esportiva · sapatilha de
neoprene · bota de neoprene surf · sapatilha aquática feminina ·
sapatilha para beach tennis

### Fora do escopo (não vira keyword)

`macaquinho` (13 impressões: academia, fitness, levanta bumbum) — é
body de ginástica, categoria errada que a conta vem captando. Vai para
negativa, não para keyword. Idem `wetsuit`/`long john`: são roupa
completa de mergulho/surf, produto que a marca não tem.

## 5. Negativas da campanha

**Concorrente:** mormaii · maresia · fiber · decathlon · kaisan · xterra ·
seaway · lupo

**Categoria errada:** macaquinho · academia · fitness · musculação ·
levanta bumbum · wetsuit · long john · mergulho · cilindro · pesca ·
capa de piscina · maiô · biquíni

**Cruzada com a 006:** `lycra` e `proteção uv` ficam **fora** da 007 (e
`neoprene` já está negativado na 006) — as duas campanhas não disputam o
mesmo leilão.

Somam-se às permanentes de `master/negativas-biblioteca.md`.

## 6. Setup proposto

| Item | Valor | Racional |
|---|---|---|
| Nome | `[007-SEARCH]-NEOPRENE` | próximo sequencial livre |
| Rede | Pesquisa Google (sem parceiros, sem Display) | padrão do master |
| Local / idioma | Brasil / pt | |
| UTM | herdado da conta | já aplicado no `finalUrlSuffix` |
| Lance | **Maximizar cliques, teto R$ 4,00** | campanha nova, 0 conversões — mesma lógica validada na 006; teto acima do da lycra porque o CPC observado em neoprene é R$ 3,62 |
| Orçamento | **R$ 15,00/dia** | ~4 cliques/dia ao CPC observado; iguala a 006 e cabe no gasto atual da conta (R$ 991/mês) |

Revisar o orçamento quando houver conversão medida — hoje a conta não
captura valor de transação (ver `campanhas/lycra/01-kws.md`, item 1.4), o
que impede julgar retorno.

## 7. Extensões

Callouts e snippet da 006 são reaproveitáveis (são da marca, não da
linha). **Sitelinks precisam ser próprios**: os três produtos da linha
apontando uns para os outros — camiseta, bermuda e sapatilha — que é
venda cruzada natural dentro da mesma linha.

## Bloqueios para subir

1. **Etapa 0 não pôde ser feita.** A política de rede do ambiente bloqueia
   `usezerohora.com.br` (403 no proxy), então não foi possível coletar
   preço, espessura do neoprene, tamanhos, cores nem diferenciais das três
   páginas. **Sem isso não há copy de anúncio**: a regra do projeto é que
   o anúncio só promete o que a página sustenta.
   → Liberar o domínio no **Acesso à rede** do ambiente, ou colar o
   conteúdo das três páginas.
2. **Semrush sem créditos** — impede dimensionar volume de mercado. Não
   bloqueia a subida (a conta tem sinal próprio), mas o orçamento fica
   com margem de erro maior até haver dado.
