resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: 'coldrecords${uniqueString(resourceGroup().id)}'
  location: resourceGroup().location
  sku: {
    name: 'Standard_GZRS'
  }
  kind: 'StorageV2'
  properties: {
    allowBlobPublicAccess: false
    minimumTlsVersion: 'TLS1_2'
    supportsHttpsTrafficOnly: true
    // ...other settings...
  }
}
