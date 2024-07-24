import google_ads_client
import logging
import zipfile
import os
import base64
from google.ads.google_ads.v17.services.asset_service import AssetServiceClient
from google.ads.google_ads.v17.resources.asset import Asset
from google.ads.google_ads.v17.enums.asset_type_enum import AssetTypeEnum
from google.ads.google_ads.v17.services.media_file_service import MediaFileServiceClient
from google.ads.google_ads.v17.resources.media_file import MediaFile
from google.ads.google_ads.v17.enums.media_file_type_enum import MediaFileTypeEnum

def upload_html5_ads_to_banana_campaigns(client, customer_id, html5_ads_directory):
  """Uploads all HTML5 ads containing "Jeep" to ad groups in campaigns containing "bananas"."""

  google_ads_service = client.get_service('GoogleAdsService')
  asset_service = AssetServiceClient(client)
  media_file_service = MediaFileServiceClient(client)

  # ... (rest of your function)

  def create_media_file_and_ad_image_asset(client, customer_id, html5_ad_path):
    # Create media file
    media_file = MediaFile(
        type_=MediaFileTypeEnum.MEDIA_BUNDLE,
        name='my_html5_ad.zip',
    )

    with open(html5_ad_path, 'rb') as f:
      media_file.data = base64.b64encode(f.read()).decode('utf-8')

    media_file_response = media_file_service.create_media_file(
        customer_id=customer_id, media_file=media_file
    )
    media_file_resource_name = media_file_response.resource_name

    # Create ad image asset
    image_asset = Asset(
        type_=AssetTypeEnum.IMAGE,
        media_file=media_file_resource_name,
        name='My HTML5 Ad'
    )

    asset_operation = client.get_type('AssetOperation')
    asset_operation.create = image_asset

    response = asset_service.mutate_assets(
      customer_id=customer_id,
      operations=[asset_operation],
      partial_failure=True
    )

    ad_image_asset_resource_name = response.results[0].resource_name

    return media_file_resource_name, ad_image_asset_resource_name

  # ... (rest of the function)
