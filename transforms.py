def add_wait_time(data_frame):
    """Add a wait_time_minutes column calculated from arrival and roomed timestamps."""
    data_frame["wait_time_minutes"] = (
        data_frame["ed_roomed_dttm"] - data_frame["ed_arrival_dttm"]
    ).dt.total_seconds() / 60
    return data_frame


def add_is_admitted(data_frame):
    """Add a boolean is_admitted column based on admission order timestamp."""
    data_frame["is_admitted"] = data_frame["ed_admission_order_dttm"].notnull()
    return data_frame


def admission_rate_by_complaint(data_frame):
    """Return a DataFrame summarizing admission rate by chief complaint."""
    summary = data_frame.groupby("ed_chief_complaint")["is_admitted"].agg(
        total_visits="count",
        admissions="sum",
    )
    summary["admission_rate_pct"] = (
        summary["admissions"] / summary["total_visits"] * 100
    ).round(1)
    return summary