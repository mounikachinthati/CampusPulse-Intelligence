import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# Load analysis files
department = pd.read_csv(
    DATA_DIR / "department_attendance_analysis.csv"
)

year = pd.read_csv(
    DATA_DIR / "year_attendance_analysis.csv"
)

subject = pd.read_csv(
    DATA_DIR / "subject_attendance_analysis.csv"
)

monthly = pd.read_csv(
    DATA_DIR / "monthly_attendance_analysis.csv"
)

# --------------------------------------------------
# 1. Department-wise Attendance
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    department["department"],
    department["attendance_percentage"]
)

plt.title("Attendance by Department")
plt.xlabel("Department")
plt.ylabel("Attendance Percentage (%)")

plt.tight_layout()

plt.savefig(
    DATA_DIR / "attendance_by_department.png"
)

plt.show()


# --------------------------------------------------
# 2. Year-wise Attendance
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    year["year"].astype(str),
    year["attendance_percentage"]
)

plt.title("Attendance by Year")
plt.xlabel("Year")
plt.ylabel("Attendance Percentage (%)")

plt.tight_layout()

plt.savefig(
    DATA_DIR / "attendance_by_year.png"
)

plt.show()


# --------------------------------------------------
# 3. Subject-wise Attendance
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    subject["subject"],
    subject["attendance_percentage"]
)

plt.title("Attendance by Subject")
plt.xlabel("Subject")
plt.ylabel("Attendance Percentage (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    DATA_DIR / "attendance_by_subject.png"
)

plt.show()


# --------------------------------------------------
# 4. Monthly Attendance Trend
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly["month"],
    monthly["attendance_percentage"],
    marker="o"
)

plt.title("Monthly Attendance Trend")
plt.xlabel("Month")
plt.ylabel("Attendance Percentage (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    DATA_DIR / "monthly_attendance_trend.png"
)

plt.show()


# --------------------------------------------------
# Completion
# --------------------------------------------------

print("\n==========================================")
print("ATTENDANCE VISUALIZATION COMPLETE")
print("==========================================")

print("\nCharts saved successfully:")
print("1. attendance_by_department.png")
print("2. attendance_by_year.png")
print("3. attendance_by_subject.png")
print("4. monthly_attendance_trend.png")