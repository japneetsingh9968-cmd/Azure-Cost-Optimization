
#### 3. `docs/MONITORING_AND_INTEGRITY.md`
```markdown
# Built-in Monitoring and Integrity Checks

## Monitoring Dashboard
```plantuml
@startuml
dashboard "Monitoring Overview" {
  chart "Latency (ms)" as latency {
    Hot Reads: 120
    Cold Reads: 850
    P95: 2100
  }
  
  chart "Error Rates" as errors {
    "4xx": 0.2
    "5xx": 0.05
    Archival Failures: 0.1
  }
  
  chart "Data Consistency" as data {
    Total Records: 2.1M
    Hot: 150K
    Cold: 1.95M
  }
}
@enduml