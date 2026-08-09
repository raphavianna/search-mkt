# Extensões (ativos) — obrigatórias em toda campanha de Search

Extensão não é enfeite: ocupa mais área do resultado, dá caminhos
alternativos de clique e entra na fórmula do Ad Rank. **Campanha de
Search sem sitelinks, callouts e snippets não passa no checklist de
lançamento.**

## Obrigatoriedade por ativo

| Ativo | Status | Mínimo | Nível |
|---|---|---|---|
| Sitelinks | **obrigatório** | 4 (idealmente 6) | campanha |
| Frases de destaque (callouts) | **obrigatório** | 6 | campanha |
| Snippets estruturados | **obrigatório** | 1 cabeçalho + 3 valores | campanha |
| Imagem | **recomendado** | 4 imagens | campanha |
| Promoção | condicional | — | campanha |
| Preço | condicional | 3 itens | campanha |
| Local / Chamada / Formulário | **não usar** | — | — |

Condicionais: **Promoção** só com promoção real e vigente na página
(coletada com data, com data de término cadastrada); **Preço** só com
preços estáveis por 30+ dias. Marca D2C sem loja física e sem SAC por
telefone não usa Local nem Chamada; formulário de lead não faz sentido
para venda direta no site.

## Sitelinks — como escolher os 4+ (padrão da marca)

Sitelink não repete a URL final do anúncio nem os outros sitelinks. O
conjunto padrão, por ordem de prioridade:

1. **Categoria da campanha** (ex.: "Linha Neoprene") — a coleção do tema;
2. **Produto irmão** (ex.: "Bermuda de Neoprene") — outro produto da linha;
3. **Prova/segurança da compra** (ex.: "Trocas e Devoluções", "Envio em 24h");
4. **Marca** (ex.: "Quem Somos", "Nossa História") — sustenta a entidade
   Use Zero Hora surf/beachwear;
5. **Mais vendidos** / **Novidades** — quando existirem páginas próprias.

Cada sitelink: título ≤25, duas descrições ≤35 cada (as duas sempre —
sitelink com uma descrição só perde área de exibição), URL final própria
respondendo 200.

## Callouts — o que entra

Diferenciais reais e verificáveis na página, sem clichê publicitário
("qualidade incrível" está proibido). Fontes típicas: envio em 24h úteis,
fabricação própria, fotos reais, trocas facilitadas, parcelamento,
material técnico. ≤25 caracteres cada.

## Snippets estruturados

Cabeçalho da lista fixa do Google (pt-BR): "Tipos", "Estilos", "Marcas",
"Modelos", "Serviços", "Destaques", "Comodidades" (lista completa em
`specs-limites-google-ads.md`). Valores ≤25, mínimo 3, todos do mesmo
conjunto lógico. Ex.: `Tipos: Camiseta de neoprene; Bermuda de neoprene;
Sapatilha de neoprene`.

## Onde isso entra no pipeline

- **Etapa 2** produz os textos de todos os ativos no `02-ads.md`, com
  contagem de caracteres declarada, junto com os RSAs.
- **Subida:** o Google não disponibilizou (na conta, em 2026-08-09)
  template de upload em massa para ativos — **os ativos são cadastrados
  pela interface**, com os textos já prontos do `02-ads.md`. Esta é a
  única exceção autorizada à regra do CSV. Se um template de ativos
  aparecer na tela de Uploads, arquivar em
  `master/templates-csv/google-oficial/` e migrar a subida para CSV.
- **Checklist de lançamento** verifica a presença dos três obrigatórios.
