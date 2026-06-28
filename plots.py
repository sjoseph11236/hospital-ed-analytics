import matplotlib.pyplot as plt
from db import load_encounters
from transforms import add_wait_time, add_is_admitted, admission_rate_by_complaint


def plot_visits_by_complaint():
    data_frame = load_encounters()
    counts = data_frame["ed_chief_complaint"].value_counts().sort_values(ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(counts.index, counts.values, color="#1a6b4a")
    ax.set_xlabel("Number of Visits")
    ax.set_title("ED Visits by Chief Complaint")
    plt.tight_layout()
    plt.savefig("assets/visits_by_complaint.png", dpi=150)
    print("✅ Chart saved to assets/visits_by_complaint.png")


def plot_admission_rate():
    data_frame = load_encounters()
    data_frame = add_is_admitted(data_frame)
    summary = admission_rate_by_complaint(data_frame)
    summary = summary.sort_values("admission_rate_pct", ascending=True)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.barh(summary.index, summary["admission_rate_pct"], color="#b3261e")
    ax.set_xlabel("Admission Rate (%)")
    ax.set_title("ED Admission Rate by Chief Complaint")
    plt.tight_layout()
    plt.savefig("assets/admission_rate_by_complaint.png", dpi=150)
    print("✅ Chart saved to assets/admission_rate_by_complaint.png")


def plot_wait_time_distribution():
    data_frame = load_encounters()
    data_frame = add_wait_time(data_frame)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(data_frame["wait_time_minutes"], bins=10, color="#1a6b4a", edgecolor="white")
    ax.set_xlabel("Wait Time (minutes)")
    ax.set_ylabel("Number of Patients")
    ax.set_title("Distribution of Door-to-Room Wait Times")
    plt.tight_layout()
    plt.savefig("assets/wait_time_distribution.png", dpi=150)
    print("✅ Chart saved to assets/wait_time_distribution.png")