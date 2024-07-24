import google_ads_client
import logging
import zipfile
import os

def upload_html5_ads_to_banana_campaigns(client, customer_id, html5_ads_directory):
  """Uploads all HTML5 ads containing "Jeep" to ad groups in campaigns containing "bananas"."""

  google_ads_service = client.get_service('GoogleAdsService')  # Use GoogleAdsService
  search_query_service = client.get_service('SearchQueryService')
  ad_service = client.get_service('AdService')                 # Keep AdService

  def create_html5_ad_asset(client, html5_ad_path):
    """ (Function body remains the same) """
    # ... (implement using GoogleAdsService.mutate for media file and ad image asset creation)

  # Get campaigns containing "bananas" (remains the same)
  query = f'SELECT campaign.id, campaign.name FROM campaign WHERE campaign.name CONTAINS "bananas"'
  campaign_selector = search_query_service.search_stream(query=query, customer_id=customer_id)

  for batch in campaign_selector:
    for row in batch:
      campaign_id = row['campaign']['id']
      campaign_name = row['campaign']['name']

      # Get ad groups for the campaign (remains the same)
      query = f'SELECT ad_group.id FROM ad_group WHERE ad_group.campaign = "{campaign_id}"'
      ad_group_selector = search_query_service.search_stream(query=query, customer_id=customer_id)

      # Get RDA ads for the campaign (remains the same)
      rda_ad_query = f'SELECT ad.id, ad.final_url FROM ad WHERE ad.type = "RESPONSIVE_DISPLAY_AD" AND ad.campaign = "{campaign_id}"'
      rda_ad_selector = search_query_service.search_stream(query=rda_ad_query, customer_id=customer_id)

      rda_ads_by_ad_group = {}
      for batch in rda_ad_selector:
        for row in batch:
          ad_id = row['ad']['id']
          final_url = row['ad']['final_url']
          ad_group_id = get_ad_group_id_from_ad(client, ad_id)
          rda_ads_by_ad_group.setdefault(ad_group_id, []).append((ad_id, final_url))

      for batch in ad_group_selector:
        for row in batch:
          ad_group_id = row['ad_group']['id']

          for html5_ad_file in os.listdir(html5_ads_directory):
            if "Jeep" in html5_ad_file:
              html5_ad_path = os.path.join(html5_ads_directory, html5_ad_file)
              ad_image_asset_id = create_html5_ad_asset(client, html5_ad_path)  # Call the fixed function

              # Create the ad (remains the same)
              ad = ad_service.ad()
              ad.ad_group = ad_group_id
              ad.final_url = get_final_url_from_rda_ads(rda_ads_by_ad_group.get(ad_group_id, []))
              # ... (other ad fields)
              ad.html5_media_bundle = ad_image_asset_id
              ad_response = ad_service.create_ad(ad)

              # ... (error handling and logging)

# ... (rest of the code including main function)
