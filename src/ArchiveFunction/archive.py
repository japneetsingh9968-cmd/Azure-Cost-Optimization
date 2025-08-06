def archive_record(record):
    # Write to blob first
    blob_client = container.get_blob_client(f"{record['id']}.json")
    blob_client.upload_blob(json.dumps(record))
    
    # Verify upload
    if not blob_client.exists():
        raise Exception("Blob upload failed")
    
    # Delete from Cosmos
    cosmos_container.delete_item(record['id'], record['id'])
    
    # Return success
    return {
        "status": "archived",
        "record_id": record['id'],
        "timestamp": datetime.utcnow()
    }