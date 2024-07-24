import google_ads_client
import logging
import zipfile
import os

def upload_html5_ads_to_banana_campaigns(client, customer_id, html5_ads_directory):
  """Uploads all HTML5 ads containing "Jeep" to ad groups in campaigns containing "bananas"."""

  google_ads_service = client.get_service('GoogleAdsService')
  search_query_service = client.get_service('SearchQueryService')
  ad_service = client.get_service('AdService')

  def get_ad_group_id_from_ad(client, ad_id):
    ad_query = f'SELECT ad_group.id FROM ad WHERE ad.id = "{ad_id}"'
    ad_selector = search_query_service.search_stream(query=ad_query, customer_id=customer_id)

    try:
      for batch in ad_selector:
        for row in batch:
          return row['ad_group']['id']
    except Exception as e:
      logging.error(f"Error getting ad group ID for ad {ad_id}: {e}")
      return None

  def get_final_url_from_rda_ads(rda_ads):
    if rda_ads:
      return rda_ads[0][1]  # Assuming the first RDA ad has the desired final URL
    else:
      logging.warning("No RDA ads found for ad group")
      return None



  def create_media_file_and_ad_image_asset(client, customer_id, html5_ad_path):
    media_file = client.get_type('MediaFile')
    media_file.type_ = client.enums.MediaTypeEnum.MEDIA_BUNDLE
    media_file.name = 'my_html5_ad.zip'

    with open(html5_ad_path, 'rb') as f:
      media_file.data = base64.b64encode(f.read()).decode('utf-8')

    ad_image_asset = client.get_type('AdImageAsset')
    ad_image_asset.media_file = media_file

    response = google_ads_service.mutate(
      customer_id=customer_id,
      media_file_operations=[media_file],
      ad_image_asset_operations=[ad_image_asset],
      partial_failure=True
    )

    media_file_resource_name = response.results[0].resource_name
    ad_image_asset_resource_name = response.results[1].resource_name

    return media_file_resource_name, ad_image_asset_resource_name

  # Get campaigns containing "bananas"
  query = f'SELECT campaign.id, campaign.name FROM campaign WHERE campaign.name CONTAINS "bananas"'
  campaign_selector = search_query_service.search_stream(query=query, customer_id=customer_id)

  for batch in campaign_selector:
    for row in batch:
      campaign_id = row['campaign']['id']
      campaign_name = row['campaign']['name']

      # Get ad groups for the campaign
      query = f'SELECT ad_group.id FROM ad_group WHERE ad_group.campaign = "{campaign_id}"'
      ad_group_selector = search_query_service.search_stream(query=query, customer_id=customer_id)

      # Get RDA ads for the campaign
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
              media_file_resource_name, ad_image_asset_resource_name = create_media_file_and_ad_image_asset(client, customer_id, html5_ad_path)

              # Create the ad
              ad = ad_service.ad()
              ad.ad_group = ad_group_id
              ad.final_url = get_final_url_from_rda_ads(rda_ads_by_ad_group.get(ad_group_id, []))
              # ... (other ad fields)
              ad.html5_media_bundle = ad_image_asset_resource_name
              ad_response = ad_service.create_ad(ad)

              # ... (error handling and logging)

def main():
  # Replace with your actual authentication and account information
  client = google_ads_client.GoogleAdsClient.load_from_storage('path/to/your/key.json')
  customer_id = 'your_customer_id'
  html5_ads_directory = '/path/to/your/html5/ads'

  upload_html5_ads_to_banana_campaigns(client, customer_id, html5_ads_directory)

if __name__ == '__main__':
  main()
