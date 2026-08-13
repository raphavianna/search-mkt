# Registro — Padronização de nomenclatura de ad groups (2026-08-13)

- **Conta:** `2614617888` · **Método:** `05-upload/padroniza_adgroups.py execute`
  (`gads.renomear`, updateMask=`name`; só o nome muda). Ensaio `validate` OK antes.
- **Motivo:** alinhar ao padrão real da conta `[NNN-<LETRA>]-DESCRICAO(-COMPRA)`
  (ver `master/padrao-nomenclatura.md`). Auditoria pós-mudança: **41/41 ad groups
  ativos** conformes; nenhum fora do padrão.

## [011]-BIQUINI
| Antes | Depois |
|---|---|
| Biquíni \| Empina Bumbum | `[011-A]-EMPINA-BUMBUM-COMPRA` |
| Biquíni \| Cortininha | `[011-B]-CORTININHA-COMPRA` |
| Biquíni \| Asa Delta | `[011-C]-ASA-DELTA-COMPRA` |
| Biquíni \| Sem Bojo | `[011-D]-SEM-BOJO-COMPRA` |
| Biquíni \| Esportivo/Surf/Futevôlei | `[011-E]-ESPORTIVO-SURF-FUTEVOLEI-COMPRA` |
| Biquíni \| Fio Dental | `[011-F]-FIO-DENTAL-COMPRA` |
| Biquíni \| Genérico | `[011-G]-GENERICO` |
| Biquíni \| Comercial | `[011-H]-COMERCIAL-COMPRA` |

## [012]-HOT-PANT
| Antes | Depois |
|---|---|
| Hot Pant \| Manga 3/4 e Manga Longa | `[012-A]-MANGA-34-COMPRA` |
| Hot Pant \| Proteção Solar UV50 | `[012-B]-PROTECAO-UV50-COMPRA` |
| Hot Pant \| Surf | `[012-C]-SURF-COMPRA` |
| Hot Pant \| Top Nadador | `[012-D]-TOP-NADADOR-COMPRA` |
| Hot Pant \| Cropped | `[012-E]-CROPPED-COMPRA` |
| Hot Pant \| Fitness/Esporte | `[012-F]-FITNESS-ESPORTE-COMPRA` |
| Hot Pant \| Genérico | `[012-G]-GENERICO` |
| Hot Pant \| Comercial | `[012-H]-COMERCIAL-COMPRA` |

## [010]-SAIDA-DE-PRAIA (estava despadronizada: "AGn · Nome")
| Antes | Depois |
|---|---|
| AG0 · Saída de Praia Zero Hora | `[010-A]-SAIDA-DE-PRAIA-MARCA` |
| AG1 · Vestido Saída de Praia | `[010-B]-VESTIDO-SAIDA-PRAIA-COMPRA` |
| AG2 · Transparência / Tule | `[010-C]-TRANSPARENCIA-TULE-COMPRA` |
| AG3 · Saia de Praia | `[010-D]-SAIA-DE-PRAIA-COMPRA` |
| AG4 · Categoria Genérico | `[010-E]-CATEGORIA-GENERICO` |

> Demais campanhas (002–008) já estavam no padrão — não tocadas.
> Só o nome mudou: IDs, keywords, anúncios e URLs finais permanecem.
