# Specs — limites de caracteres e regras das peças (Google Ads, Search)

Referência obrigatória da Etapa 2. **Peça acima do limite é defeito, não
detalhe**: toda peça entregue declara a contagem ao lado e é conferida
antes da entrega. Contagem inclui espaços.

## RSA (anúncio responsivo de pesquisa)

| Peça | Limite | Quantidade |
|---|---|---|
| Título (headline) | **30** caracteres | 15 por anúncio |
| Descrição | **90** caracteres | 4 por anúncio |
| Caminho de exibição (path) | **15** caracteres | 2 |
| URL final | — | 1 (página de produto/categoria real) |

- Pins (posição fixa) só quando necessários — ex.: título de marca fixado
  na posição 1. Pin demais degrada o Ad Strength.
- Cobertura mínima dos 15 títulos: KW do grupo (Quality Score), benefício,
  prova/diferencial, preço/oferta (se estável e coletado com data), CTA de
  conversão.
- Regras editoriais: sem "!" em título; sem CAIXA ALTA integral em palavra
  (exceto sigla real); sem pontuação/símbolos repetidos; sem emoji; sem
  número de telefone no texto; promessa só do que a página sustenta.

## Extensões (ativos)

| Ativo | Limites | Mínimo/recomendado |
|---|---|---|
| Sitelink | título **25**; 2 descrições de **35** cada; URL final | mínimo 2, recomendado 4+ por campanha |
| Frase de destaque (callout) | **25** | mínimo 2, recomendado 6+ |
| Snippet estruturado | valores de **25** cada | 1 cabeçalho + mínimo 3 valores |
| Promoção | ocasião + item ≤ **20**; exige datas e valor | quando houver promoção real na página |
| Preço | cabeçalho **25**; descrição **25** por item; 3–8 itens | quando preços estáveis |
| Imagem | 1:1 (1200×1200) e 1,91:1 (1200×628); sem logo/texto sobreposto | 4+ quando houver ativo aprovado |

- Cabeçalho de snippet vem da lista fixa do Google (usar em pt-BR):
  "Tipos", "Estilos", "Marcas", "Modelos", "Serviços", "Cursos",
  "Destaques", "Comodidades", "Destinos", "Bairros", "Seguros",
  "Programas de graduação", "Shows".
- Sitelinks apontam para páginas distintas entre si e da URL final do
  anúncio (categoria, produtos irmãos, quem somos, trocas/frete).

## Keywords

- Match types usados: exata `[kw]`, frase `"kw"`, ampla `kw` — a escolha é
  registrada por KW no `01-kws.md`, com racional.
- 5–20 KWs por ad group; um tema por grupo.
- Negativas: além das da campanha, aplicar sempre a biblioteca da marca
  (`master/negativas-biblioteca.md`).

## Conferência de contagem

Contagem de caracteres feita por script/ferramenta, não no olho. No
`02-ads.md`, toda peça aparece como `texto (NN)`. CSV final não leva a
contagem — só o texto.
