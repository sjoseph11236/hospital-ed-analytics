import os
from dotenv import load_dotenv
from google.cloud import bigquery
 
load_dotenv()

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
 
client = bigquery.Client(project=PROJECT_ID)


def door_to_room_time():
    # Door-to-room time — how long between arrival and being roomed? (calculated from ed_arrival_dttm and ed_roomed_dttm)
    query = """
    SELECT 
        ed.ed_csn,
        ed.ed_chief_complaint,
        TIMESTAMP_DIFF(ed.ed_roomed_dttm, ed.ed_arrival_dttm, MINUTE) as wait_time
    FROM `elvtr-advanced-analytics.ed_analytics.ed_encounter` ed  
    ORDER BY wait_time DESC 
    LIMIT 5; 
    """
    return query

def total_visits_by_chief_complaint():
    query = """
    SELECT
        ed.ed_chief_complaint,
        COUNT(*) AS total_visits
    FROM`elvtr-advanced-analytics.ed_analytics.ed_encounter` ed  
    GROUP BY ed.ed_chief_complaint
    ORDER BY total_visits DESC
    LIMIT 5; 
    """
    return query


def admission_rate_by_complaint():
    query = """
        SELECT 
            ed.ed_chief_complaint,
            COUNT(*) AS total_visits,
            COUNTIF(ed.ed_admission_order_dttm IS NOT NULL) AS admissions,
            ROUND(COUNTIF(ed.ed_admission_order_dttm IS NOT NULL) / COUNT(*) * 100 , 1) AS admission_rate_pct
        FROM `elvtr-advanced-analytics.ed_analytics.ed_encounter` ed  
        GROUP BY ed.ed_chief_complaint
        ORDER BY admission_rate_pct DESC;
    """
    
    
    return query
    
def run(query_name="total_visits"):
    queries = {
        "door_to_room": door_to_room_time,
        "total_visits": total_visits_by_chief_complaint,
        "admission_rate": admission_rate_by_complaint,
        "explore": explore,
    }

    query_func = queries.get(query_name)
    if not query_func:
        print(f"⚠️  Unknown query: {query_name}")
        print(f"   Available options: {list(queries.keys())}")
        return
    
    if query_name == "explore": 
        query_func()
        return 

    results = client.query(query_func()).to_dataframe()
    print(f"\n📋 Results for: {query_name}")
    print(results)


def load_encounters():
    """Pull the full ed_encounter table into a DataFrame for analysis"""
    query = """
        SELECT * 
        FROM `elvtr-advanced-analytics.ed_analytics.ed_encounter`;
    """
    
    return client.query(query).to_dataframe()

def explore():
    data_frame = load_encounters()
    
    data_frame["wait_time_minutes"] = (
        data_frame["ed_roomed_dttm"] - data_frame["ed_arrival_dttm"]
    ).dt.total_seconds() / 60
    
    data_frame["is_admitted"] = data_frame["ed_admission_order_dttm"].notnull()
    
    print("\n📋 Null counts per column:")
    print(data_frame.isnull().sum())
    
    print("\n📋 Admission breakdown:")
    print(data_frame["is_admitted"].value_counts())
    
    print("\n📋 Admission rate by complaint (pandas groupby):")
    admission_summary = data_frame.groupby("ed_chief_complaint")["is_admitted"].agg(
        total_visits="count",
        admissions="sum",
    )
    
    admission_summary["admission_rate_pct"] = (
        admission_summary["admissions"] / admission_summary["total_visits"] * 100
    ).round(1)
    
    print(admission_summary.sort_values("admission_rate_pct", ascending=False))
    
    print(data_frame[["ed_csn", "ed_chief_complaint", "wait_time_minutes"]].head(10))
    
    print("\n📋 Wait time summary statistics:")
    print(data_frame["wait_time_minutes"].describe())
    
    print("\n📋 Visit counts by complaint:")
    print(data_frame["ed_chief_complaint"].value_counts())


if __name__ == "__main__":
    run("explore")