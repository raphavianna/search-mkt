# Revisão de política — anúncios Biquíni + Hot Pant (2026-08-13)

## Diagnóstico real das reprovações (dado da conta, não suposição)
Consulta de `policy_summary` na conta: **nenhuma keyword reprovada**; **4 anúncios
reprovados**, todos por **`DESTINATION_NOT_CRAWLABLE`** (URL de destino não rastreável) —
**não** por conteúdo/termo. O termo "empina bumbum" passou na revisão de conteúdo.

Anúncios reprovados e correção aplicada (repontados p/ categoria real já aprovada):
| Ad group | URL antes (reprovada) | URL depois (rastreável) |
|---|---|---|
| `[011-A]-EMPINA-BUMBUM` | /feminino/biquini/marquinha/ | /feminino/biquini/ |
| `[011-H]-COMERCIAL` | /search/?q=biquini | /feminino/biquini/ |
| `[012-A]-MANGA-34` | /search/?q=hot+pant+manga | /feminino/biquini/hot-pant/ |
| `[012-G]-GENERICO` | /search/?q=hot+pant | /feminino/biquini/hot-pant/ |

> `/feminino/biquini/` e `/feminino/biquini/hot-pant/` já constam APROVADAS em outros
> ad groups (Google rastreou OK). As páginas `/search/?q=` provavelmente estão bloqueadas
> no robots.txt da loja (`Disallow: /search`) — daí o não-rastreável.

## Ad groups ainda em `/search/?q=` (aprovados hoje, mas em risco)
`[011-B]-CORTININHA`, `[011-C]-ASA-DELTA`, `[011-D]-SEM-BOJO`, `[012-E]-CROPPED`.
Recomendação: mover para categoria real rastreável (`/feminino/biquini/` ou
`/feminino/biquini/hot-pant/`) para evitar reprovação futura por rastreamento e melhorar QS.
Ideal: se a loja tiver subcategorias (`/feminino/biquini/cortininha/` etc.), usá-las.

## Revisão de termos x política de conteúdo (proativa)
Situação atual: **todos aprovados**. Avaliação de risco para reforço futuro:

| Termo/uso | Política que pode tocar | Risco | Recomendação |
|---|---|---|---|
| empina bumbum / levanta bumbum / "efeito que levanta" | Conteúdo sexual/sugestivo (ênfase em parte do corpo) | Baixo–Médio (hoje aprovado) | Manter "empina bumbum" como **nome de modelo** (termo de mercado). Suavizar o reforço na descrição: trocar "efeito que levanta"/"modelagem que levanta" por "modelagem que valoriza" / "caimento que valoriza" |
| fio dental, tanga, micro, cavado | Vestuário revelador | Baixo | OK para e-commerce de moda praia; manter |
| sem bojo | — | Nenhum | manter |

Nenhuma troca é obrigatória agora (nada reprovado por termo). As sugestões acima reduzem
risco caso a conta passe a revisar com mais rigor (ex.: anúncios personalizados).
