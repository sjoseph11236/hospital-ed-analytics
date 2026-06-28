import os
from dotenv import load_dotenv
from google.cloud import bigquery

load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")

client = bigquery.Client(project=PROJECT_ID)


def load_encounters():
    """Pull the full ed_encounter table into a DataFrame for analysis"""
    query = """
        SELECT *
        FROM `elvtr-advanced-analytics.ed_analytics.ed_encounter`;
    """
    return client.query(query).to_dataframe()