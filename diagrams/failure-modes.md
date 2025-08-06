# Failure Scenarios Visuals

## Data Consistency Risks

```mermaid
sequenceDiagram
    participant C as Change Feed
    participant F as Azure Function
    participant B as Blob Storage
    participant D as Cosmos DB
    C->>F: Record update event
    F->>B: Write record (with lease ID)
    B-->>F: Write confirmation
    F->>D: Delete record (with etag)
    D-->>F: Delete confirmation
    F->>B: Remove lease ID
```

## Latency Spikes for Cold Data

```mermaid
graph LR
    A[Client] --> B[API Gateway]
    B --> C{Record Type?}
    C -->|Hot| D[Cosmos DB]
    C -->|Cold| E[CDN Edge Cache]
    E -->|Cache Miss| F[Blob Storage]
    F --> E
    E --> B
    subgraph Cold Data Flow
        F --> G[Blob Index Tags]
        F --> H[Premium Block Blobs]
    end
```

## Archival Backlog & Throughput

```mermaid
flowchart TB
    A[2M Records] --> B{Batch Size}
    B -->|100K records| C[Data Factory Pipeline]
    B -->|1K records| D[Change Feed Function]
    C --> E[Blob Storage]
    D --> E
    E --> F[Throughput Monitor]
    F -->|High Load| G[Scale Out Functions]
    F -->|Normal| H[Steady State]
    G --> I[Partition Key Optimization]
    I --> J[Increase RU/s Temporarily]
```

## Query Support Limitations

```mermaid
graph TD
    A[Query Request] --> B[API Gateway]
    B --> C{Time Range?}
    C -->|Last 3 months| D[Query Cosmos DB]
    C -->|Older| E[Azure Cognitive Search]
    D --> F[Combine Results]
    E --> F
    F --> B
    G[Change Feed] --> H[Update Search Index]
    I[Blob Storage] --> J[Indexer]
```

## Blob Storage Regional Outage

```mermaid
graph LR
    A[Primary Region] -->|Sync| B[Secondary Region]
    B -->|Async| C[Archive Tier]
    D[Data Access Layer] --> E{Read Request}
    E -->|Normal| A
    E -->|Primary Down| F[Failover to Secondary]
    F --> B
    G[Monitoring] --> H[Health Probe]
    H -->|Unhealthy| I[Auto-Failover]
    subgraph DR Strategy
        A --> J[Geo-ZRS Storage]
        B --> J
        C --> J
    end
```

## Accidental Data Deletion

```mermaid
graph TB
    A[Blob Storage] --> B[Soft Delete]
    A --> C[Immutable Policies]
    A --> D[Backup Vault]
    B -->|7-365 days| E[Undelete]
    C -->|WORM Compliance| F[Time-based Hold]
    D -->|Daily Snapshots| G[Recovery]
    H[Monitoring] --> I[Delete Alerts]
    I --> J[Azure Sentinel]
    J --> K[Auto-Remediate]
```
