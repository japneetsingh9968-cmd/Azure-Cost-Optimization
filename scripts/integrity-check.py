# Data validation script

def verify_record_counts():
    cosmos_count = get_cosmos_count()
    blob_count = get_blob_count()
    expected_total = get_expected_total()
    assert cosmos_count + blob_count == expected_total

# ...implement get_cosmos_count, get_blob_count, get_expected_total...
