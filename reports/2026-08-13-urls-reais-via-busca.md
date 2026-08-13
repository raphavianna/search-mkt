# Captura de URLs reais da loja — via índice de busca (WebSearch)

- **Data:** 2026-08-13 · **Método:** WebSearch (índice de motores) sobre `usezerohora.com.br`.
- **Motivo:** site bloqueado por egress (WebFetch e curl falham); Nuvemshop sem credenciais.
  O índice de busca foi o único canal que retornou URLs reais do domínio.

## Descoberta de estrutura (corrige suposição anterior)
- As categorias vivem em **`/feminino/<categoria>/`**, `/masculino/<categoria>/` e
  `/roupas-e-acessorios/<pai>/<categoria>/`. **Os provisórios `/biquini` e `/hot-pant`
  usados no upload NÃO existem** (dariam 404).
- **Não há página de categoria dedicada de biquíni/hot pant** indexada (5+ buscas). Os itens
  de biquíni/hot pant aparecem como **produtos** e via a **página de busca** `/search/?q=<termo>`.

## URLs reais confirmadas
**Categorias:**
- Maiô: `https://usezerohora.com.br/feminino/maio/`
- Saída de praia (conjunto atoalhado): `https://usezerohora.com.br/feminino/saida-de-praia/conjunto-atoalhado/`
- Lycra surf (masculino): `https://usezerohora.com.br/masculino/lycra-surf/`
- Poncho: `https://usezerohora.com.br/roupas-e-acessorios/linha-surf/poncho/`

**Busca (LP dinâmica válida):** `https://usezerohora.com.br/search/?q=<termo>` (ex.: `?q=biquini+maio`).

**Produtos (biquíni/hot pant) — canônicos (sem `?variant`/`pf`):**
- `.../produtos/biquini-fio-dental-marquinha-cortininha-com-regulagens/`
- `.../produtos/biquini-hot-pant-cos-alto-com-top-fixo/`
- `.../produtos/biquini-sunkini-hot-pant-top-faixa-surf-piscina-futevolei/`
- `.../produtos/maio-biquini-hot-pant-top-nadador-esporte-protecao-uv50/`
- `.../produtos/maio-biquini-hot-pant-top-alcas-esporte-protecao-uv50/`
- `.../produtos/camiseta-lycra-surf-feminina-uv50-segunda-pele-surfnelas-dment/`

## Mapa aplicado por ad group
Ver `campanhas/biquinis/03-csv/links-reais-por-adgroup.csv`. Regra: ad group com produto
correspondente → página de produto real; genéricos/modelos sem produto exato → página de
busca do termo; marca/consideração → home.

## Limitações
- Sem o site ao vivo nem a API Nuvemshop, não dá para confirmar `finalUrls` byte a byte nem
  achar a URL exata do campeão "Hot Pant Cropped Manga 3/4 UV50" (existe, sem URL indexada).
- Páginas `/search/?q=` são válidas mas rendem Quality Score menor que uma categoria própria.
  **Recomendação:** criar categorias `/feminino/biquini/` e `/feminino/hot-pant/` na loja e
  reapontar os genéricos para elas (ganho de conversão e QS).
