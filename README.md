# Hospital Ed Analytics

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

A healthcare analytics project analyzing Emergency Department performance data using Google BigQuery.

Built as the final project for ELVTR's Advanced Healthcare Analytics course (instructor: Jesse Andrist, Mayo Clinic Rochester).

---

## Status

✅ Week 1 — BigQuery connection established, own dataset created and queried
✅ Week 2 — Writing analytical SQL queries (door-to-room time, visit volume, admission rates)
✅ Week 3 — Pandas exploration, null validation, SQL/Pandas cross-check complete
✅ Week 4 — Matplotlib visualizations complete (visit volume, admission rate, wait time distribution)

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/hospital-ed-analytics.git
cd hospital-ed-analytics
```

### 2. Create and activate a virtual environment

```bash
python3.11 -m venv venv
source venv/bin/activate
```

### 3. Configure environment variables

Create a `.env` file in the project root:

**Setup:**

### 4. Install dependencies

```bash
git clone https://github.com/yourusername/lhs-gmail-poller.git
cd lhs-gmail-poller

python3 -m venv venv
source venv/bin/activate

cp .env.example .env
# Fill in your values in .env

make install
```

### 5. Install and configure Google Cloud CLI

This project uses Google Application Default Credentials (ADC) — no credentials JSON file needed locally.

```bash
# Install gcloud CLI (Mac)
brew install --cask google-cloud-sdk
```

Restart your terminal after installation, then:

```bash
# Connect gcloud to your Google account and select your GCP project
gcloud init

# Set up Application Default Credentials — this is what lets Python authenticate
gcloud auth application-default login
```

> **Why two commands?** `gcloud init` connects the CLI to your Google account and project. `gcloud auth application-default login` is what actually lets your Python code authenticate with Google APIs — they serve different purposes.

### 6. Run

```bash
make dev
```

---

## Current Analysis

This project currently answers three operational questions using BigQuery — door-to-room time, visit volume by chief complaint, and admission rate by chief complaint. Week 3 added Pandas-based exploration and validated the SQL results independently. Week 4 turned these findings into visualizations.

![ED Admission Rate by Chief Complaint](assets/admission_rate_by_complaint.png)

📄 Week 2 write-up: [docs/week2-analysis.md](docs/week2-analysis.md)
📄 Week 3 write-up: [docs/week3-analysis.md](docs/week3-analysis.md)
📄 Week 4 write-up: [docs/week4-analysis.md](docs/week4-analysis.md)

> **Note:** Data is synthetic, generated to mirror the schema of a real Emergency Department encounter table (`ed_encounter`). No real patient data is used.

---

## Stack

- Python 3
- Google BigQuery
- Google Cloud CLI (gcloud)
- Pandas
- Matplotlib _(coming soon)_
- Streamlit _(coming Week 5)_

---

## Roadmap

| Week | Goal                                    | Status      |
| ---- | --------------------------------------- | ----------- |
| 1    | BigQuery connection + own dataset setup | ✅ Complete |
| 2    | First SQL queries on ED data            | ✅ Complete |
| 3    | Pandas analysis + data cleaning         | ✅ Complete |
| 4    | Visualizations + trend analysis         | ✅ Complete |
| 5    | Streamlit dashboard v1                  | ⏳ Upcoming |
| 6    | Deeper insights + predictive analytics  | ⏳ Upcoming |
| 7    | Final polish + deployment               | ⏳ Upcoming |
