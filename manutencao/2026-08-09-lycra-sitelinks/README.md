# Sitelinks da campanha [006-SEARCH]-LYCRA — 2026-08-09

> **STATUS: APLICADO em 2026-08-09, via API** (`plano.py --aplicar`),
> após simulação aprovada. Com isso a campanha passa a cumprir o
> checklist de extensões do master: **5 sitelinks por grupo**, 6 frases
> de destaque e 1 snippet estruturado.

## A ideia por trás do desenho

As 8 keywords de cor ("camiseta lycra rosa com preto", "manga longa
preta", "bicolor"…) foram **removidas na reestruturação por terem zero
impressão** — não têm volume de busca. Mas cor é decisão real de compra
de lycra. Sitelink resolve exatamente isso: entrega o caminho direto para
a variante **sem depender de volume de busca**, ocupando espaço no
anúncio em vez de espaço na lista de keywords.

Por isso 4 dos 6 sitelinks são variantes de cor.

## Sitelinks criados

| Título | Descrições | Destino |
|---|---|---|
| Camiseta UV Preta | Manga longa com proteção UV50 · Preto liso, envio em 24h úteis | produto preto liso |
| Camiseta UV Rosa | Rosa liso, manga longa · Proteção UV50, envio em 24h | produto rosa liso |
| Preto com Amarelo | Lycra bicolor de manga longa · Proteção UV50 para o surf | produto preto/amarelo |
| Amarelo com Preto | Lycra bicolor de manga longa · Cores vibrantes no mar | produto amarelo/preto |
| Lycra Masculina | Coleção masculina de surf · Proteção UV para o mar | `/masculino/lycra-surf/` |
| Lycra Feminina | Coleção feminina de surf · Proteção UV para o mar | `/feminino/lycra-surf1/` |

Todos dentro do limite (título ≤25, descrições ≤35), validado por script
antes de qualquer chamada.

## Vinculação por grupo, não por campanha

| Grupo | Sitelinks | Coleção incluída |
|---|---:|---|
| `[006-A]-UV-MASCULINA` | 5 | Feminina (a masculina é a URL final) |
| `[006-B]-UV-FEMININA` | 5 | Masculina (a feminina é a URL final) |
| `[006-C]-UV-GERAL` | 5 | Feminina (usa a URL masculina como final) |

O checklist do master exige que **sitelink não repita a URL final do
anúncio**. No nível da campanha isso seria impossível de garantir, porque
cada grupo tem uma URL final diferente. No nível do grupo, cada um recebe
a coleção do gênero oposto — o que ainda vira venda cruzada.

## UV50: claim agora sustentado

As quatro URLs de produto trazem **`uv50` no próprio slug**. Nos anúncios
eu tinha evitado "UV 50+" de propósito, por ser especificação técnica não
verificada (o site está bloqueado pela rede do ambiente). O slug é a
marca nomeando o próprio produto, então o claim passa a ter lastro — e
está usado nas descrições dos sitelinks.

**Pendente de decisão:** trocar um título de cada RSA por "Proteção
UV50", que casa direto com as keywords `camiseta uv 50 feminina`,
`camisa fator de proteção uv 50` e `camisa de lycra masculina uv50`, hoje
sem título correspondente. Não aplicado — mexer em copy de anúncio de
novo reinicia a revisão do Google, então fica para aprovação do usuário.

## Reproduzir

```bash
cd integracao/google-ads
python3 ../../manutencao/2026-08-09-lycra-sitelinks/plano.py            # simula
python3 ../../manutencao/2026-08-09-lycra-sitelinks/plano.py --aplicar  # grava
```

Não há CSV: o Google não oferece template de upload em massa para
ativos — é a exceção já prevista no `CLAUDE.md`.
