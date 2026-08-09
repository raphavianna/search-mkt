# Divisão do grupo de lycra + correção de URL — 2026-08-09

> **STATUS: APLICADO em 2026-08-09, via API** (`plano.py --aplicar`),
> após simulação (`validateOnly`) aprovada. Estado final conferido.

## Problema

A campanha `[006-SEARCH]-LYCRA` tinha **um único grupo com 47 keywords**
misturando intenções de gênero, e o anúncio apontava para
`http://www.usezerohora.com.br` — protocolo http, com `www` e levando à
**home**, não a uma página de lycra.

Classificação das 47 KWs: **15 femininas**, **4 masculinas**, **28
neutras**. Apontar tudo para a coleção masculina (única URL disponível a
princípio) mandaria as 15 femininas para a página errada — por isso a
correção real era dividir o grupo, não só trocar a URL.

## Estrutura aplicada

| Grupo | KWs | URL final | Caminhos |
|---|---|---|---|
| `[006-A]-LYCRA-MASCULINA` *(novo)* | 4 | `https://usezerohora.com.br/masculino/lycra-surf/` | `/lycra/masculina` |
| `[006-B]-LYCRA-FEMININA` *(novo)* | 15 | `https://usezerohora.com.br/feminino/lycra-surf1/` | `/lycra/feminina` |
| `[006-C]-LYCRA-GENERICO` *(era o grupo único)* | 28 | `https://usezerohora.com.br/masculino/lycra-surf/` | `/lycra/surf` |

O grupo original foi **renomeado**, não recriado: as 28 KWs neutras
mantêm histórico e Quality Score. As 19 KWs de gênero foram criadas nos
grupos novos e removidas do genérico (Google Ads não move keyword entre
grupos; recriar zera o histórico daquelas 19 — inevitável e esperado).

**Genérico usando a URL masculina** é decisão consciente do usuário
(2026-08-09), provisória até existir uma coleção de lycra sem recorte de
gênero. Quando existir, é trocar `URL_GEN` em `plano.py`.

## Defeitos corrigidos no anúncio que já rodava

| Antes | Depois |
|---|---|
| `Camiseta de Lyrca Zero Hora` | `Camiseta de Lycra Zero Hora` |
| `Para Surf e Esportes Áquaticos` | `Para Surf e Esportes Aquáticos` |
| URL `http://www.usezerohora.com.br` (home) | URL https da coleção |
| Caminhos `/use/zerohora` (redundante) | `/lycra/surf` |

## Procedência da copy dos RSAs novos

15 títulos e 4 descrições por grupo, todos dentro do limite (validação
automática no `plano.py` antes de gerar qualquer coisa). As afirmações
vêm de duas fontes, sem invenção:

- **RSA que já rodava na conta** (claims aprovados pela marca): proteção
  UV que bloqueia até 98% dos raios, manga longa e curta, surf/praia/
  piscina/esportes aquáticos, fabricação no Brasil, "peça agora, receba
  em casa";
- **Contexto de marca do CLAUDE.md**: fabricação própria, envio em até
  24h úteis, cores vibrantes.

**Nada foi inferido de keyword.** Existirem buscas por "abertura para o
polegar", "segunda pele" ou "beach tennis" não prova que o produto tenha
o recurso — essas KWs continuam sendo alvo, mas não viram promessa de
anúncio.

**Preço e promoção ficaram de fora**: exigem coleta datada da página
(Etapa 0), hoje impossível porque a política de rede do ambiente bloqueia
`usezerohora.com.br`.

## Pendências

- **Confirmar a URL feminina** `…/feminino/lycra-surf1/` — o `1` no final
  do slug chama atenção e não foi possível verificar por aqui (rede
  bloqueada). Se estiver errada, o anúncio do grupo B cai em 404 e será
  reprovado. Conferir no navegador.
- **RSA do genérico segue com 9 títulos e 3 descrições** (abaixo dos 15/4
  do checklist). Edição foi deliberadamente mínima — expandir é trabalho
  de Etapa 2, com dados de página.
- Os anúncios novos entram em revisão do Google (algumas horas).

## Como reproduzir / reverter

`plano.py` é a fonte única: as mesmas estruturas geram os CSVs
(`01-grupos.csv`, `02-keywords.csv`, `03-rsa.csv`, no modelo oficial) e a
aplicação por API — os dois não podem divergir.

```bash
cd integracao/google-ads
python3 ../../manutencao/2026-08-09-lycra-split/plano.py            # CSVs + simulação
python3 ../../manutencao/2026-08-09-lycra-split/plano.py --aplicar  # grava
```
