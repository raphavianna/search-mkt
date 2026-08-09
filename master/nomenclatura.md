# Padrão de nomenclatura — taxonomia oficial

Taxonomia definida em 2026-08-09 (aprovação do usuário): **números para
campanhas, letras para ad groups — e o ad group sempre carrega o número
da campanha-mãe**. Assim qualquer relatório (termos de pesquisa, GAQL,
planilha exportada) liga grupo ↔ campanha só pelo nome, e a ordenação
alfabética agrupa tudo junto.

## Campanha

```
[NNN-CANAL]-TEMA
```

- `NNN`: sequencial único da conta, 3 dígitos, nunca reutilizado
  (próximo livre em 2026-08-09: **007**);
- `CANAL`: `SEARCH` | `SHOPPING` | `PMAX`;
- `TEMA`: linha/categoria em caixa alta, hífens no lugar de espaços.

Ex.: `[007-SEARCH]-NEOPRENE`

## Ad group

```
[NNN-L]-SUBTEMA-INTENCAO
```

- `NNN`: **o mesmo número da campanha-mãe** (elo do grupo com a campanha);
- `L`: letra sequencial dentro da campanha (`A`, `B`, `C`…);
- `SUBTEMA`: produto/cluster do grupo;
- `INTENCAO`: `COMPRA` | `CONSIDERACAO` | `MARCA` | `CONCORRENTE` |
  `GENERICO`.

Ex. — campanha `[007-SEARCH]-NEOPRENE`:

```
[007-A]-CAMISETA-COMPRA
[007-B]-BERMUDA-COMPRA
[007-C]-SAPATILHA-COMPRA
[007-D]-NEOPRENE-GENERICO
```

Regras de preenchimento:

- O tema não se repete no grupo quando já está na campanha — o elo é o
  número. Em `[004-SHOPPING]-MAIO`, os grupos são `[004-A]-LANCAMENTOS-…`,
  não `[004-A]-MAIO-LANCAMENTOS-…`.
- Não repetir o canal no tema (`[003-SHOPPING]-PONCHO`, nunca
  `[003-SHOPPING]-PONCHO-SHOPPING`).
- Sem espaços: hífen sempre, inclusive depois do colchete.
- **Shopping**: grupo é recorte de produto, então a intenção é `COMPRA`
  por padrão (anúncio de produto é fundo de funil).

## Grupo de ativos (Performance Max)

```
[NNN-L]-SUBTEMA
```

Ex.: `[001-A]-PONCHO-FEMININO`. Não há upload em massa para grupos de
ativos — renomeação pela interface.

## Estado da base instalada

Auditoria de 2026-08-09 encontrou padrões mistos (`Grupo de anúncios 1`
default, `[001-MAIO-LANCAMENTOS]` dentro da campanha **004**, canal e
tema invertidos em 004/005/006). O de-para completo e os CSVs de
renomeação estão em `manutencao/2026-08-09-taxonomia/`.

Renomear **não apaga histórico de performance** (a métrica segue o ID),
mas quebra relatórios salvos, regras automatizadas e painéis que filtrem
**por nome** — conferir esses depois de aplicar.

## Arquivos de campanha (repositório)

- Slug da pasta: `campanhas/<tema-curto>/` em minúsculas (ex.:
  `campanhas/neoprene/`);
- CSVs de subida: `03-csv/NN-entidade.csv`, mesmos nomes dos templates do
  master (`01-campanhas.csv`, `02-grupos-de-anuncio.csv`, ...).

## Ativos e listas

- Lista de negativas compartilhada (quando criada na conta):
  `NEG-MARCA-UZH` (biblioteca da marca) e `NEG-NNN-<TEMA>` (por campanha);
- Rótulos (labels), quando usados: `UZH-<TEMA>-<AAAA-MM>`.
