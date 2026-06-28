from db import load_encounters
from transforms import add_wait_time, add_is_admitted, admission_rate_by_complaint


def explore():
    data_frame = load_encounters()
    data_frame = add_wait_time(data_frame)
    data_frame = add_is_admitted(data_frame)

    print("\n📋 Null counts per column:")
    print(data_frame.isnull().sum())

    print("\n📋 Admission breakdown:")
    print(data_frame["is_admitted"].value_counts())

    print("\n📋 Admission rate by complaint (pandas groupby):")
    summary = admission_rate_by_complaint(data_frame)
    print(summary.sort_values("admission_rate_pct", ascending=False))

    print(data_frame[["ed_csn", "ed_chief_complaint", "wait_time_minutes"]].head(10))

    print("\n📋 Wait time summary statistics:")
    print(data_frame["wait_time_minutes"].describe())

    print("\n📋 Visit counts by complaint:")
    print(data_frame["ed_chief_complaint"].value_counts())