# Guia de importação — Google Ads Editor (subir PAUSADO)

> **Importante:** esta sessão **não tem conexão de escrita com o Google Ads**. A publicação
> é feita por você no **Google Ads Editor** a partir dos CSVs em `03-csv/`. As 4 campanhas
> já estão marcadas **`Status = Paused`** — sobem pausadas, sem gastar, prontas para ativar.

## Antes de importar (checklist mínimo)
- [ ] **URLs finais** — os CSVs usam URL provisória de categoria (site estava bloqueado).
      Ajuste `Final URL` em `rsas.csv` para a página exata de cada ad group.
- [ ] **Volume/CPC** — opcional para subir pausado; necessário antes de ativar (calibra
      orçamento e ordenação). Rode a lista no Semrush.
- [ ] **Feed do Shopping** — preencha `custom_label_0..3` no Merchant Center conforme
      `shopping-grupos-produto.csv` e audite os títulos.

## Ordem de importação no Ads Editor
1. Abra o **Google Ads Editor** conectado à conta da marca → **Account → Import → From file**.
2. Importe nesta ordem (o Editor casa por nome de campanha/ad group):
   1. `campanhas.csv` (cria as 4 campanhas — já **Paused**)
   2. `grupos.csv` (ad groups)
   3. `keywords.csv` (palavras-chave + match)
   4. `negativas.csv` (lista compartilhada de negativas → associe às 4 campanhas)
   5. `rsas.csv` (anúncios responsivos — confira `Final URL`)
   6. `sitelinks.csv`, `callouts.csv`, `snippets.csv` (extensões → associe às campanhas)
   7. `shopping-grupos-produto.csv` (referência para montar a subdivisão de grupos no Shopping)
3. Revise o painel de **erros/avisos** do Editor (limites de caractere já validados aqui).
4. **Post changes** → tudo sobe **pausado**.

## Para ativar depois (quando fechar as pendências)
- Troque `Status` da campanha para **Enabled** (ou ative na interface do Google Ads).
- Comece pelas de maior conversão esperada: **Shopping** e **Search - Hot Pant**.
- Acompanhe pelo `04-medicao.md`.

## Observações
- Estratégia de lance: **Maximizar conversões** (exige conversão configurada na conta).
- Orçamentos são **provisórios** (baixa temporada); o `02-ads.md` traz o pacing sazonal.
- Snippets/sitelinks/callouts podem exigir recriação manual como *assets* na interface,
  dependendo da versão do Editor — os CSVs servem de fonte fiel do conteúdo.
