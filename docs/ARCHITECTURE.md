# Architecture Design Decisions

## Data Consistency
- Lease locking with Table Storage
- Use of etag for concurrency
- Idempotent archival logic

## Latency Optimization
- CDN for cold data
- Premium Block Blobs
- Predictive pre-fetch

## Scalability
- Data Factory for bulk migration
- Auto-scale functions
- Partition key optimization

## Query Support
- Hybrid: Cosmos DB (hot), Cognitive Search (cold)

## DR & Data Protection
- Geo-ZRS, soft delete, immutability, backup
