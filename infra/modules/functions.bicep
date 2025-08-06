resource functionApp 'Microsoft.Web/sites@2022-09-01' = {
  name: 'archivefunc${uniqueString(resourceGroup().id)}'
  location: resourceGroup().location
  kind: 'functionapp'
  properties: {
    serverFarmId: '<app_service_plan_id>'
    siteConfig: {
      appSettings: [
        {
          name: 'AzureWebJobsStorage'
          value: '<storage_connection_string>'
        }
        // ...other settings...
      ]
    }
  }
}
