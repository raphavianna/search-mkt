# Specs — Limites de caracteres do Google Ads (Search)

Referência para toda peça de texto. **Peça acima do limite é defeito.**
Contagem inclui espaços e pontuação.

## Anúncio responsivo de pesquisa (RSA)

| Elemento | Quantidade | Limite (caracteres) |
|---|---|---|
| Títulos (headlines) | 3–15 (usar 15) | 30 |
| Descrições | 2–4 (usar 4) | 90 |
| Caminho de exibição (path) | 2 | 15 cada |
| URL final | 1 por anúncio | — |

Regras:
- Sem ponto de exclamação em título; no máx. 1 por descrição.
- Sem CAPS LOCK integral, sem emoji, sem repetição de pontuação.
- Pins só quando necessários (ex.: título de marca fixado na posição 1);
  cada pin reduz as combinações e tende a reduzir o desempenho.
- Cobrir no conjunto: KW do grupo, benefício, prova/diferencial,
  preço/oferta (se estável e coletado da página), CTA de conversão.

## Extensões (recursos)

| Recurso | Quantidade mínima | Limites |
|---|---|---|
| Sitelinks | 4 por campanha | Título 25; 2 descrições de 35 cada; URL final |
| Frases de destaque (callouts) | 6 por campanha | 25 cada |
| Snippets estruturados | 1 cabeçalho + 3+ valores | Valores 25 cada; cabeçalho de lista oficial (ex.: Tipos, Estilos, Marcas) |
| Extensão de promoção | quando aplicável | Item 20; requer datas/ocasião e valor |
| Extensão de preço | quando aplicável | 3–8 itens; título 25; descrição 25 |
| Extensão de imagem | quando aplicável | 1:1 (1200×1200) e 1,91:1 (1200×628); sem logo/texto sobreposto |

## Keywords

- Match types: exata `[kw]`, frase `"kw"`, ampla `kw`.
- Negativas: por campanha e/ou lista compartilhada; exata/frase/ampla.

## Verificação obrigatória

Toda peça entregue declara a contagem ao lado, ex.:
`Camiseta de Neoprene UZH (26)`. Conferir programaticamente (ex.:
`python -c "print(len('texto'))"`), não no olho.
