# Master — materiais reutilizáveis de campanhas de Search

Este repositório é a **ferramenta de campanhas de search da Use Zero Hora**.
Esta pasta guarda tudo que é genérico e reutilizável entre campanhas; o que
é específico de uma campanha vive em `campanhas/<slug>/`.

## Conteúdo

| Arquivo/pasta | O que é |
|---|---|
| `specs-limites-google-ads.md` | Limites de caracteres e regras editoriais de cada peça |
| `extensoes-ativos.md` | Extensões obrigatórias por campanha e critérios de escolha |
| `nomenclatura.md` | Taxonomia oficial de campanhas, grupos e ativos |
| `tracking-urls.md` | Padrão de URL final e UTM (sufixo do URL final) |
| `checklist-lancamento.md` | Conferência obrigatória antes de subir qualquer campanha |
| `negativas-biblioteca.md` | Negativas permanentes da marca (aplicar em toda campanha) |
| `templates/` | Modelos dos arquivos de campanha (`00-produtos`, `01-kws`, `02-ads`, `03-extensoes`, `04-medicao`) |
| `templates-csv/` | **Modelos de upload do Google Ads Editor — formato canônico de subida** |

## Regra de ouro do upload

Toda subida de campanha é entregue como **conjunto completo de CSVs no
modelo de `templates-csv/`**, pronto para importação no Google Ads Editor.
Montagem manual na interface, campanha a campanha, não é o fluxo padrão —
só acontece com pedido explícito. Detalhes em `templates-csv/README.md`.

## Evolução

O master evolui: aprendizado de campanha que sirva às próximas vira
atualização de template, spec ou checklist — no mesmo commit da campanha ou
em commit próprio.
