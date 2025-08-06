# Production-grade Architecture with Failure Mitigation

## Core Architecture
```plantuml
@startuml
!theme azure
left to right direction

component "API Gateway" as gateway
component "Azure Functions" as func
database "Cosmos DB (Hot)" as cosmos
cloud "Blob Storage (Cold)" as blob
component "CDN" as cdn
component "Application Insights" as ai

gateway --> func : HTTP Requests
func --> cosmos : Hot Data Access
func --> blob : Cold Data Access
blob --> cdn : Caching
cosmos --> func : Change Feed
func --> ai : Telemetry

@enduml