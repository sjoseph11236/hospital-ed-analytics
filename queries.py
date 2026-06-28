def door_to_room_time():
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
    FROM `elvtr-advanced-analytics.ed_analytics.ed_encounter` ed  
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