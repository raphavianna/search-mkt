#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Auditoria de entrega da [007-SEARCH]-NEOPRENE — somente leitura (GAQL)."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from upload_google_ads import access_token, headers_base, descobre_versao, http_json, env

CAMP = '24115053024'


def busca(surl, h, q):
    resp, err = http_json(surl, h, {'query': q})
    if err:
        print(f'  [erro na query] {json.dumps(err[1])[:400]}')
        return []
    return resp.get('results', [])


def main():
    cid = env('GOOGLE_ADS_CUSTOMER_ID').replace('-', '')
    h = headers_base(access_token())
    v = descobre_versao(h)
    surl = f'https://googleads.googleapis.com/{v}/customers/{cid}/googleAds:search'
    print(f'== AUDITORIA {CAMP} | API {v} ==')

    print('\n-- 1. Campanha: status, serving, lance, budget --')
    for r in busca(surl, h, f"""
        SELECT campaign.status, campaign.serving_status, campaign.primary_status,
               campaign.primary_status_reasons, campaign.bidding_strategy_type,
               campaign.start_date, campaign_budget.amount_micros,
               campaign.network_settings.target_google_search,
               campaign.network_settings.target_search_network,
               campaign.geo_target_type_setting.positive_geo_target_type
        FROM campaign WHERE campaign.id = {CAMP}"""):
        c = r['campaign']
        print(json.dumps({
            'status': c.get('status'), 'serving': c.get('servingStatus'),
            'primary': c.get('primaryStatus'), 'motivos': c.get('primaryStatusReasons'),
            'lance': c.get('biddingStrategyType'), 'inicio': c.get('startDate'),
            'budget_dia_R$': int(r['campaignBudget']['amountMicros']) / 1e6,
            'geo_type': c.get('geoTargetTypeSetting', {}).get('positiveGeoTargetType'),
        }, ensure_ascii=False, indent=2))

    print('\n-- 2. Métricas por dia (14d) + impression share --')
    for r in busca(surl, h, f"""
        SELECT segments.date, metrics.impressions, metrics.clicks, metrics.cost_micros,
               metrics.search_impression_share, metrics.search_budget_lost_impression_share,
               metrics.search_rank_lost_impression_share
        FROM campaign WHERE campaign.id = {CAMP} AND segments.date DURING LAST_14_DAYS
        ORDER BY segments.date"""):
        m = r['metrics']
        print(f"  {r['segments']['date']}: imp={m.get('impressions', 0)} "
              f"cliques={m.get('clicks', 0)} custo=R${int(m.get('costMicros', 0))/1e6:.2f} "
              f"IS={m.get('searchImpressionShare', '-')} "
              f"perda_budget={m.get('searchBudgetLostImpressionShare', '-')} "
              f"perda_rank={m.get('searchRankLostImpressionShare', '-')}")

    print('\n-- 3. Ad groups: status primário --')
    for r in busca(surl, h, f"""
        SELECT ad_group.name, ad_group.status, ad_group.primary_status,
               ad_group.primary_status_reasons
        FROM ad_group WHERE campaign.id = {CAMP} ORDER BY ad_group.name"""):
        g = r['adGroup']
        print(f"  {g['name']}: {g.get('primaryStatus')} {g.get('primaryStatusReasons', '')}")

    print('\n-- 4. Anúncios: aprovação, review, ad strength --')
    for r in busca(surl, h, f"""
        SELECT ad_group.name, ad_group_ad.policy_summary.approval_status,
               ad_group_ad.policy_summary.review_status, ad_group_ad.ad_strength,
               ad_group_ad.primary_status, ad_group_ad.primary_status_reasons
        FROM ad_group_ad WHERE campaign.id = {CAMP} ORDER BY ad_group.name"""):
        a = r['adGroupAd']
        print(f"  {r['adGroup']['name']}: aprov={a['policySummary'].get('approvalStatus')} "
              f"review={a['policySummary'].get('reviewStatus')} "
              f"strength={a.get('adStrength')} primario={a.get('primaryStatus')} "
              f"{a.get('primaryStatusReasons', '')}")

    print('\n-- 5. Keywords com status primário != ELIGIBLE (motivos) --')
    problemas = {}
    total = 0
    for r in busca(surl, h, f"""
        SELECT ad_group.name, ad_group_criterion.keyword.text,
               ad_group_criterion.primary_status, ad_group_criterion.primary_status_reasons
        FROM ad_group_criterion
        WHERE campaign.id = {CAMP} AND ad_group_criterion.type = 'KEYWORD'
          AND ad_group_criterion.negative = FALSE"""):
        total += 1
        ps = r['adGroupCriterion'].get('primaryStatus')
        if ps != 'ELIGIBLE':
            motivo = ','.join(r['adGroupCriterion'].get('primaryStatusReasons', []) or ['?'])
            chave = f'{ps} [{motivo}]'
            problemas.setdefault(chave, []).append(
                f"{r['adGroup']['name'].split(']-')[-1]}: {r['adGroupCriterion']['keyword']['text']}")
    print(f'  total de KWs ativas: {total}')
    for chave, kws in sorted(problemas.items(), key=lambda x: -len(x[1])):
        print(f'  {chave}: {len(kws)} kws')
        for k in kws[:12]:
            print(f'    - {k}')
        if len(kws) > 12:
            print(f'    ... +{len(kws)-12}')

    print('\n-- 6. Top 15 KWs por impressões (7d) --')
    for r in busca(surl, h, f"""
        SELECT ad_group.name, ad_group_criterion.keyword.text, metrics.impressions,
               metrics.clicks, metrics.cost_micros
        FROM keyword_view WHERE campaign.id = {CAMP}
          AND segments.date DURING LAST_7_DAYS AND metrics.impressions > 0
        ORDER BY metrics.impressions DESC LIMIT 15"""):
        m = r['metrics']
        print(f"  {r['adGroupCriterion']['keyword']['text']}: imp={m['impressions']} "
              f"cliques={m.get('clicks', 0)} custo=R${int(m.get('costMicros', 0))/1e6:.2f}")

    print('\n-- 7. Critérios de campanha: geo + negativas --')
    geos, negs = [], 0
    for r in busca(surl, h, f"""
        SELECT campaign_criterion.type, campaign_criterion.negative,
               campaign_criterion.keyword.text, campaign_criterion.location.geo_target_constant
        FROM campaign_criterion WHERE campaign.id = {CAMP}"""):
        cc = r['campaignCriterion']
        if cc['type'] == 'LOCATION':
            geos.append((cc['location']['geoTargetConstant'], cc.get('negative', False)))
        elif cc['type'] == 'KEYWORD' and cc.get('negative'):
            negs += 1
    print(f'  geos: {geos} | negativas de campanha: {negs}')

    print('\n-- 8. Listas de negativas compartilhadas aplicadas à campanha --')
    r8 = busca(surl, h, f"""
        SELECT shared_set.name, shared_set.type, shared_set.status
        FROM campaign_shared_set WHERE campaign.id = {CAMP}""")
    if not r8:
        print('  nenhuma')
    for r in r8:
        s = r['sharedSet']
        print(f"  {s['name']} ({s['type']}, {s['status']})")
        # conteúdo da lista
        sid = r['campaignSharedSet']['sharedSet'].split('/')[-1] if 'sharedSet' in r.get('campaignSharedSet', {}) else None

    print('\n-- 8b. Todas as listas compartilhadas da conta (com contagem) --')
    for r in busca(surl, h, """
        SELECT shared_set.id, shared_set.name, shared_set.type, shared_set.status,
               shared_set.member_count
        FROM shared_set WHERE shared_set.status = 'ENABLED'"""):
        s = r['sharedSet']
        print(f"  [{s['id']}] {s['name']} ({s['type']}): {s.get('memberCount', 0)} membros")

    print('\n-- 9. Negativas de CONTA (customer_negative_criterion) --')
    r9 = busca(surl, h, """
        SELECT customer_negative_criterion.type, customer_negative_criterion.keyword.text,
               customer_negative_criterion.keyword.match_type
        FROM customer_negative_criterion""")
    if not r9:
        print('  nenhuma')
    for r in r9:
        cn = r['customerNegativeCriterion']
        if cn['type'] == 'KEYWORD':
            print(f"  {cn['keyword']['matchType']}: {cn['keyword']['text']}")
        else:
            print(f"  {cn['type']}")

    print('\n-- 10. Conta: status, moeda, conversões --')
    for r in busca(surl, h, "SELECT customer.status, customer.currency_code, customer.auto_tagging_enabled FROM customer"):
        print(f"  customer: {json.dumps(r['customer'], ensure_ascii=False)}")
    for r in busca(surl, h, """
        SELECT conversion_action.name, conversion_action.type, conversion_action.status,
               conversion_action.category, conversion_action.primary_for_goal
        FROM conversion_action WHERE conversion_action.status = 'ENABLED'"""):
        ca = r['conversionAction']
        print(f"  conv: {ca['name']} | {ca.get('category')} | primary={ca.get('primaryForGoal')}")

    print('\n-- 11. Comparativo: todas as campanhas (7d) --')
    for r in busca(surl, h, """
        SELECT campaign.name, campaign.status, metrics.impressions, metrics.clicks,
               metrics.cost_micros
        FROM campaign WHERE segments.date DURING LAST_7_DAYS ORDER BY metrics.cost_micros DESC"""):
        m = r['metrics']
        print(f"  {r['campaign']['name']:<32} {r['campaign']['status']:<8} "
              f"imp={m.get('impressions', 0):>7} cliques={m.get('clicks', 0):>5} "
              f"custo=R${int(m.get('costMicros', 0))/1e6:>8.2f}")


if __name__ == '__main__':
    main()
