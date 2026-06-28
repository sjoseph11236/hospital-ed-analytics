from db import client
from queries import (
    door_to_room_time,
    total_visits_by_chief_complaint,
    admission_rate_by_complaint,
)
from analysis import explore
from plots import (
    plot_visits_by_complaint,
    plot_admission_rate,
    plot_wait_time_distribution,
)

SQL_QUERIES = {"door_to_room", "total_visits", "admission_rate"}
PANDAS_FUNCS = {"explore", "plot_visits", "plot_admission", "plot_wait_time"}


def run(query_name="total_visits"):
    queries = {
        "door_to_room": door_to_room_time,
        "total_visits": total_visits_by_chief_complaint,
        "admission_rate": admission_rate_by_complaint,
        "explore": explore,
        "plot_visits": plot_visits_by_complaint,
        "plot_admission": plot_admission_rate,
        "plot_wait_time": plot_wait_time_distribution,
    }

    query_func = queries.get(query_name)
    if not query_func:
        print(f"⚠️  Unknown query: {query_name}")
        print(f"   Available options: {list(queries.keys())}")
        return

    if query_name in PANDAS_FUNCS:
        query_func()
        return

    results = client.query(query_func()).to_dataframe()
    print(f"\n📋 Results for: {query_name}")
    print(results)


if __name__ == "__main__":
    run("plot_wait_time")