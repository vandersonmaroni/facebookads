from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.ad import Ad
from facebookads.adobjects.campaign import Campaign
from facebookads.adobjects.adsinsights import AdsInsights
from facebookads.exceptions import FacebookRequestError
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.user import User
import csv
import json
import datetime


my_app_id = '<my_app_id>'
my_app_secret = '<my_app_secret>'
my_access_token = '<my_access_token>'
account_id = "<account_id>"
account_id_request = 'act_' + account_id
proxies = ''
now = datetime.datetime.now()
yesterday = datetime.date.today() - datetime.timedelta(1)

print("===========================================")
print("Iniciando conexão com o Facebook Ads API...")
print("===========================================")

FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, proxies)


ad_account = AdAccount(account_id_request)

fields = [
    Ad.Field.id,
    Ad.Field.name,
    Ad.Field.configured_status,
    Ad.Field.campaign,
]

insights_fields = [AdsInsights.Field.ad_id,
                   AdsInsights.Field.ad_name,
                   AdsInsights.Field.adset_id,
                   AdsInsights.Field.adset_name,
                   AdsInsights.Field.campaign_id,
                   AdsInsights.Field.campaign_name,
                   AdsInsights.Field.reach,
                   AdsInsights.Field.frequency,
                   AdsInsights.Field.impressions,
                   AdsInsights.Field.unique_clicks,
                   AdsInsights.Field.spend,
                   AdsInsights.Field.cpc,
                   AdsInsights.Field.cpm,
                   AdsInsights.Field.cpp,
                   AdsInsights.Field.ctr,
                   AdsInsights.Field.video_10_sec_watched_actions,
                   AdsInsights.Field.video_30_sec_watched_actions,
                   AdsInsights.Field.video_avg_percent_watched_actions,
                   AdsInsights.Field.video_avg_time_watched_actions,
                   AdsInsights.Field.video_p100_watched_actions,
                   AdsInsights.Field.video_p25_watched_actions,
                   AdsInsights.Field.video_p50_watched_actions,
                   AdsInsights.Field.video_p75_watched_actions,
                   AdsInsights.Field.video_p95_watched_actions,
                   AdsInsights.Field.video_p95_watched_actions,
                   AdsInsights.Field.social_clicks,
                   AdsInsights.Field.clicks,
                   AdsInsights.Field.inline_post_engagement,
                   ]

params = {
}

params_insights = {
    'level': AdsInsights.Level.ad,
    # 'time_range': {'since':yesterday.strftime("%Y-%m-%d"),'until':now.strftime("%Y-%m-%d")}, 
    'date_preset': AdsInsights.DatePreset.yesterday,
    'breakdowns':['device_platform', 'publisher_platform'],
    # Quebra por tipo de dispositivo
    # 'breakdowns':['impression_device'],
}

print("===========================================")
print("Buscando Ads...")
print("===========================================")

ad_iter = ad_account.get_ads(fields=fields, params=params)
ads = []
for ad in ad_iter:
    insights = ad.get_insights(fields=insights_fields, params=params_insights)
    # print(insights)
    # break
    if ad.get("configured_status") == "PAUSED":
        ads.append({
            "date_stop": None,
            "id": ad.get("id"),
            "name": ad.get("name"),
            "configured_status": ad.get("configured_status"),
            "adset_id": None,
            "adset_name": None,
            "campaign_id": None,
            "campaign_name": None,
            "device_platform": None,
            "reach": None,
            "frequency": None,
            "impressions": None,
            "unique_clicks": None,
            "spend": None,
            "cpc": None,
            "cpm": None,
            "cpp": None,
            "ctr": None,
            "clicks": None,
            "social_clicks": None,
            "inline_post_engagement": None,
            "video_10_sec_watched_actions": None,
            "video_30_sec_watched_actions": None,
            "video_avg_percent_watched_actions": None,
            "video_avg_time_watched_actions": None,
            "video_p100_watched_actions": None,
            "video_p25_watched_actions": None,
            "video_p50_watched_actions": None,
            "video_p75_watched_actions": None,
            "video_p95_watched_actions": None,
        })
    else:
        for insight in insights:
            ads.append({
                "date_stop": insight.get("date_stop"),
                "id": ad.get("id"),
                "name": ad.get("name"),
                "configured_status": ad.get("configured_status"),
                "adset_id": insight.get("adset_id"),
                "adset_name": insight.get("adset_name"),
                "campaign_id": insight.get("campaign_id"),
                "campaign_name": insight.get("campaign_name"),
                "device_platform": insight.get("device_platform"),
                "reach": insight.get("reach"),
                "frequency": insight.get("frequency"),
                "impressions": insight.get("impressions"),
                "unique_clicks": insight.get("unique_clicks"),
                "spend": insight.get("spend"),
                "cpc": insight.get("cpc"),
                "cpm": insight.get("cpm"),
                "cpp": insight.get("cpp"),
                "ctr": insight.get("ctr"),
                "clicks": insight.get("clicks"),
                "social_clicks": insight.get("social_clicks"),
                "inline_post_engagement": insight.get("inline_post_engagement") if insight.get("inline_post_engagement") else None,
                "video_10_sec_watched_actions": insight.get("video_10_sec_watched_actions") if insight.get("video_10_sec_watched_actions") else None,
                "video_30_sec_watched_actions": insight.get("video_30_sec_watched_actions") if insight.get("video_30_sec_watched_actions") else None,
                "video_avg_percent_watched_actions": insight.get("video_avg_percent_watched_actions") if insight.get("video_avg_percent_watched_actions") else None,
                "video_avg_time_watched_actions": insight.get("video_avg_time_watched_actions") if insight.get("video_avg_time_watched_actions") else None,
                "video_p100_watched_actions": insight.get("video_p100_watched_actions") if insight.get("video_p100_watched_actions") else None,
                "video_p25_watched_actions": insight.get("video_p25_watched_actions") if insight.get("video_p25_watched_actions") else None,
                "video_p50_watched_actions": insight.get("video_p50_watched_actions") if insight.get("video_p50_watched_actions") else None,
                "video_p75_watched_actions": insight.get("video_p75_watched_actions") if insight.get("video_p75_watched_actions") else None,
                "video_p95_watched_actions": insight.get("video_p95_watched_actions") if insight.get("video_p95_watched_actions") else None,
            })



# print(ads)

header = ["date_stop",
          "campaign_id",
          "campaign_name",
          "adset_id",
          "adset_name",
          "ad_id", 
          "ad_name", 
          "device_platform",
          "configured_status", 
          "reach",
          "frequency",
          "impressions",
          "unique_clicks",
          "spend",
          "cpc",
          "cpm",
          "cpp",
          "ctr",
          "clicks",
          "social_clicks",
          "inline_post_engagement",
          "video_10_sec_watched_actions",
          "video_30_sec_watched_actions",
          "video_avg_percent_watched_actions",
          "video_avg_time_watched_actions",
          "video_p100_watched_actions",
          "video_p25_watched_actions",
          "video_p50_watched_actions",
          "video_p75_watched_actions",
          "video_p95_watched_actions",
          "video_p95_watched_actions",
          "data_source",
          "extraction_date"
          ]

print("===========================================")
print("Gerando relatório...")
print("===========================================")

with open('example.csv', 'w', newline='', encoding="utf-8") as csvfile:
    spamwriter = csv.writer(csvfile)
    spamwriter.writerow(header)
    for ad in ads:
        spamwriter.writerow([ad['date_stop'],
                            ad['campaign_id'],
                            ad['campaign_name'],
                            ad['adset_id'],
                            ad['adset_name'],
                            ad['id'],
                            ad['name'],
                            ad['device_platform'],
                            ad['configured_status'],
                            ad['reach'],
                            ad['frequency'],
                            ad['impressions'],
                            ad['unique_clicks'],
                            ad['spend'],
                            ad['cpc'],
                            ad['cpm'],
                            ad['cpp'],
                            ad['ctr'],
                            ad['clicks'],
                            ad['social_clicks'],
                            ad['inline_post_engagement'],
                            ad['video_10_sec_watched_actions'],
                            ad['video_30_sec_watched_actions'],
                            ad['video_avg_percent_watched_actions'],
                            ad['video_avg_time_watched_actions'],
                            ad['video_p100_watched_actions'],
                            ad['video_p25_watched_actions'],
                            ad['video_p50_watched_actions'],
                            ad['video_p75_watched_actions'],
                            ad['video_p95_watched_actions'],
                            ad['video_p95_watched_actions'],
                            'Facebook Ads',
                            now.strftime("%Y-%m-%d %H:%M"),
                            ])

print("===========================================")
print("Relatório gerado com sucesso!!!")
print("===========================================")
# teste