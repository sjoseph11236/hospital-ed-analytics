# Week 3 Analysis — Pandas Exploration & Validation

## Goal

Move beyond SQL-only analysis and use Pandas to explore the `ed_encounter`
dataset directly in Python — calculating fields, summarizing distributions,
and validating that SQL and Pandas produce identical results for the same
question.

## Methodology

The full `ed_encounter` table (100 rows) was loaded into a Pandas DataFrame
via `load_encounters()`. From there:

- `wait_time_minutes` was calculated as a new column using datetime
  subtraction (`.dt.total_seconds() / 60`), replicating the SQL
  `TIMESTAMP_DIFF` logic from Week 2 — but computed locally in Python
  instead of inside BigQuery.
- `is_admitted` was derived as a boolean column from
  `ed_admission_order_dttm.notnull()`, replacing repeated NULL checks
  with a single readable flag.
- `.isnull().sum()` was run across all columns to confirm null counts
  matched expectations before trusting any downstream analysis.
- `.groupby()` + `.agg()` was used to recompute admission rate by chief
  complaint — the Pandas equivalent of the Week 2 SQL `GROUP BY` query.

## Findings

### Wait Time Distribution

| Stat    | Value (minutes) |
| ------- | --------------- |
| Mean    | 24.8            |
| Std Dev | 3.6             |
| Min     | 15.0            |
| Max     | 35.0            |

Wait times are tightly clustered with no long tail — a property of how
the synthetic dataset was generated, not a realistic clinical pattern.
Real ED wait time distributions typically show significant right-skew
(most patients wait a short time, a smaller number wait much longer).

### Null Validation

| Column                    | Nulls |
| ------------------------- | ----- |
| `ed_admission_order_dttm` | 74    |
| All other columns         | 0     |

74 nulls in `ed_admission_order_dttm` exactly matches the 74 patients
who were not admitted, confirmed by the `is_admitted` boolean breakdown
(74 False / 26 True). No unexpected nulls were found elsewhere in the
dataset.

### Cross-Validation: SQL vs. Pandas

The admission rate by chief complaint, calculated independently in SQL
(Week 2) and Pandas (Week 3), produced identical results:

| Complaint           | Total Visits | Admissions | Admission Rate % |
| ------------------- | ------------ | ---------- | ---------------- |
| chest_pain          | 22           | 17         | 77.3             |
| weakness_fatigue    | 15           | 6          | 40.0             |
| shortness_of_breath | 10           | 3          | 30.0             |
| abdominal_pain      | 15           | 0          | 0.0              |
| cough_congestion    | 10           | 0          | 0.0              |
| dizziness           | 14           | 0          | 0.0              |
| fall_injury         | 14           | 0          | 0.0              |

## Takeaways

- Getting matching results from two independent calculation paths (SQL
  aggregation vs. Pandas `groupby`) is a meaningful data integrity check —
  it confirms the underlying logic is correct, not just that one tool
  "looks right."
- Deriving a clean boolean flag (`is_admitted`) instead of repeatedly
  checking for NULL/NaT is both more readable and less error-prone as
  analysis grows in complexity.
- The narrow wait time distribution and the complaints with 0% admission
  rate are both artifacts of the synthetic data generation process and
  should not be read as real clinical findings.

## Data Note

All data is synthetic, generated to mirror the schema of a real ED
encounter table. No real patient data (PHI) is used anywhere in this
project.
