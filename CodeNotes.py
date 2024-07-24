def upload_html5_ad(client, customer_id, ad_group_id, html5_zip_path):
    """Uploads an HTML5 ad and creates a Display Upload Ad associated with an ad group.

    Args:
        client: An initialized GoogleAdsClient instance.
        customer_id: The Google Ads customer ID.
        ad_group_id: The ID of the ad group to associate the ad with.
        html5_zip_path: The local path to the HTML5 zip file.
    """

    # 1. Read the HTML5 zip file
    with open(html5_zip_path, "rb") as zip_file:
        zip_data = zip_file.read()

    # 2. Create a Media Bundle Asset
    asset_service = client.get_service("AssetService")
    media_bundle_operation = client.get_type("AssetOperation")
    media_bundle = media_bundle_operation.create
    media_bundle.type_ = client.get_type("AssetTypeEnum").AssetType.MEDIA_BUNDLE
    media_bundle.media_bundle_asset.data = zip_data

    # 3. Upload the Media Bundle Asset
    mutate_asset_response = asset_service.mutate_assets(
        customer_id=customer_id, operations=[media_bundle_operation]
    )
    media_bundle_resource_name = mutate_asset_response.results[0].resource_name

    # 4. Create Display Upload Ad
    ad_group_ad_service = client.get_service("AdGroupAdService")
    ad_group_ad_operation = client.get_type("AdGroupAdOperation")
    ad_group_ad = ad_group_ad_operation.create
    ad_group_ad.ad_group = client.get_service(
        "AdGroupService"
    ).ad_group_path(customer_id, ad_group_id)

    display_upload_ad = ad_group_ad.ad.display_upload_ad
    display_upload_ad.display_upload_product_type = (
        client.get_type("DisplayUploadProductTypeEnum")
        .DisplayUploadProductType.HTML5_UPLOAD_AD
    )
    display_upload_ad.media_bundle.asset = media_bundle_resource_name

    # 5. Add the Display Upload Ad to the Ad Group
    ad_group_ad_response = ad_group_ad_service.mutate_ad_group_ads(
        customer_id=customer_id, operations=[ad_group_ad_operation]
    )
    print(
        f"Created Display Upload Ad with resource name: {ad_group_ad_response.results[0].resource_name}"
    )