# Registro — Expansão de keywords por COR (2026-08-13)

- **Conta:** `2614617888` · **Método:** `05-upload/expansao_cores.py execute`
  (adGroupCriteria:mutate, correspondência **Frase**; dedupe vs. existentes; dry-run OK antes).
- **Fonte das cores:** base de vendas BaseLinker/painel
  (`zerohora-painel/public/data/vendas.json`, período 2026-01-01→08-11) — cores reais
  vendidas por categoria (campo `produto` → `Cor:`).

## Cores disponíveis no catálogo (por unidades vendidas)
- **Biquíni:** Preto 35 · Coral 28 · Onça 27 · Verde 22 · Rosa 16 · (cauda: Laranja Neon, Oceano, Amarelo, Marrom)
- **Hot Pant:** Preto 53 · Ocean 29 · Gelo 26 · Coral 24 · Rosa 8 · Cereja 3 · Verde 2
- KW usa termos pesquisáveis: biquíni → preto/coral/onça/verde/rosa (+amarelo/laranja no genérico);
  hot pant → preto/coral/rosa/verde/azul (Ocean→azul). "Gelo/Cereja" (nomes de marketing) não viraram KW.

## Resultado: +76 keywords (Frase) em 15 ad groups
Reforço nos grupos magros (Fio Dental, Sem Bojo, Top Nadador, Cropped, Fitness) e cobertura
de cor nos demais. Padrão: `<termo do ad group> <cor>` (ex.: `biquíni fio dental coral`,
`hot pant cropped azul`). UV50 (`[012-B]`) não recebeu cor (grupo de atributo).

Contagem de keywords por ad group após a expansão: ver GAQL na sessão (Biquíni+Hot Pant = 219,
sendo 180 Frase, 6 Exata, 33 Ampla).

## Observação — 33 keywords AMPLAS no Fio Dental (não subidas por este script)
O grupo `[011-F]-FIO-DENTAL-COMPRA` contém 33 keywords em **correspondência ampla**
(ex.: "biquini calcinha", "biquini pequeno", "calcinha de biquini", "micro fio dental")
adicionadas **fora deste script** — provável expansão manual no Keyword Planner da interface.
Risco: ampla em campanha Maximize Conversions abre muito o alcance e pode gastar em termos
frouxos. **Recomendação:** revisar essas amplas — converter as boas para Frase e podar as
off-target (calcinha/pequeno/micro se não forem o alvo), ou apoiar em negativas.
