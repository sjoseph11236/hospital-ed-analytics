# docs/week2-analysis.md

# Week 2 Analysis — ED Throughput & Admission Patterns

## Questions Asked

1. How long do patients wait between arrival and being roomed?
2. What's the volume of visits by chief complaint?
3. Which complaints most often result in admission?

## Methodology

Queries run against synthetic `ed_encounter` data (100 rows) using BigQuery.
Door-to-room time calculated via `TIMESTAMP_DIFF`. Admission status inferred
from whether `ed_admission_order_dttm` is NULL.

## Findings

### Door-to-Room Time

- Longest wait times topped out around 30-35 minutes
- Chest pain and fall injury appeared most frequently in the slowest cases

### Visit Volume by Complaint

| Complaint           | Visits |
| ------------------- | ------ |
| chest_pain          | 22     |
| weakness_fatigue    | 15     |
| abdominal_pain      | 15     |
| dizziness           | 14     |
| fall_injury         | 14     |
| shortness_of_breath | 10     |
| cough_congestion    | 10     |

### Admission Rate by Complaint

| Complaint           | Admission Rate |
| ------------------- | -------------- |
| chest_pain          | 77.3%          |
| weakness_fatigue    | 40.0%          |
| shortness_of_breath | 30.0%          |
| abdominal_pain      | 0.0%           |
| dizziness           | 0.0%           |
| fall_injury         | 0.0%           |
| cough_congestion    | 0.0%           |

## Takeaways

- Chest pain dominates both visit volume and admission rate — consistent
  with how EDs prioritize cardiac risk.
- Several complaints show 0% admission in this dataset. This is a property
  of the synthetic data generation, not a real clinical pattern — flagged
  here for transparency.

## Data Note

All data is synthetic, generated to mirror the schema of a real ED
encounter table. No real patient data (PHI) is used anywhere in this project.
