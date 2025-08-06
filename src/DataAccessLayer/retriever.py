def get_record(record_id):
    try:
        # Try hot storage
        item = cosmos_container.read_item(record_id, record_id)
        item['data_source'] = 'hot'
        return item
    except exceptions.CosmosResourceNotFoundError:
        # Fallback to cold storage
        blob_client = container.get_blob_client(f"{record_id}.json")
        data = blob_client.download_blob().readall()
        record = json.loads(data)
        record['data_source'] = 'cold'
        
        # Warm CDN cache
        warm_cdn_cache(record_id)
        return record