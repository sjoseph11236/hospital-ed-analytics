# Hospital Ed Analytics

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BigQuery](https://img.shields.io/badge/BigQuery-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white)

A healthcare analytics project analyzing Emergency Department performance data using Google BigQuery.

Built as the final project for ELVTR's Advanced Healthcare Analytics course (instructor: Jesse Andrist, Mayo Clinic Rochester).

---

## Status

🔄 Week 1 — BigQuery connection established, setting up own dataset

---

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/your-username/hospital-ed-analytics.git
cd hospital-ed-analytics
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip3 install -r requirements.txt
```

### 4. Install and configure Google Cloud CLI

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

### 5. Run

```bash
python3 app.py
```

Expected output:

```
✅ Connected to BigQuery
   Project: your-project-id
   Dataset: your-dataset-id
```

---

## Project Structure

```
hospital-ed-analytics/
├── app.py            # BigQuery connection and queries
├── requirements.txt  # Python dependencies
├── .gitignore        # Excludes credentials, venv, data files
└── README.md
```

---

## Stack

- Python 3
- Google BigQuery
- Google Cloud CLI (gcloud)
- Pandas _(coming soon)_
- Matplotlib _(coming soon)_
- Streamlit _(coming Week 5)_

---

## Roadmap

| Week | Goal                                    | Status         |
| ---- | --------------------------------------- | -------------- |
| 1    | BigQuery connection + own dataset setup | 🔄 In Progress |
| 2    | First SQL queries on ED data            | ⏳ Upcoming    |
| 3    | Pandas analysis + data cleaning         | ⏳ Upcoming    |
| 4    | Visualizations + trend analysis         | ⏳ Upcoming    |
| 5    | Streamlit dashboard v1                  | ⏳ Upcoming    |
| 6    | Deeper insights + predictive analytics  | ⏳ Upcoming    |
| 7    | Final polish + deployment               | ⏳ Upcoming    |
