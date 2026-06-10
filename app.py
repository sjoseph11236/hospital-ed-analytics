import os
from dotenv import load_dotenv
from google.cloud import bigquery
 
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
 
client = bigquery.Client(project=PROJECT_ID)

def run():
    query = """
    SELECT 
        *
    FROM `elvtr-advanced-analytics.ed_analytics.ed_visits` ed;
    """

    results = client.query(query).to_dataframe()
    print("\n📋 ED Visits:")
    print(results)

if __name__  == "__main__":
    run()