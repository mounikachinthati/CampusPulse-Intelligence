import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# Load datasets
attendance = pd.read_csv(DATA_DIR / "attendance_kpi.csv")
students = pd.read_csv(DATA_DIR / "students_clean.csv")

# Convert date
attendance["date"] = pd.to_datetime(attendance["date"])

# Merge attendance with student details
attendance = attendance.merge(
    students,
    on="student_id",
    how="left"
)

# --------------------------------------------------
# 1. Overall Attendance
# --------------------------------------------------

overall_attendance = attendance["present_flag"].mean() * 100

print("\n==========================================")
print("STUDENT ATTENDANCE ANALYSIS")
print("==========================================")

print(f"\nOverall Attendance: {overall_attendance:.2f}%")

# --------------------------------------------------
# 2. Department-wise Attendance
# --------------------------------------------------

department_attendance = (
    attendance
    .groupby("department")
    .agg(
        total_records=("present_flag", "count"),
        attendance_percentage=("present_flag", "mean")
    )
    .reset_index()
)

department_attendance["attendance_percentage"] *= 100

department_attendance.to_csv(
    DATA_DIR / "department_attendance_analysis.csv",
    index=False
)

# --------------------------------------------------
# 3. Year-wise Attendance
# --------------------------------------------------

year_attendance = (
    attendance
    .groupby("year")
    .agg(
        total_records=("present_flag", "count"),
        attendance_percentage=("present_flag", "mean")
    )
    .reset_index()
)

year_attendance["attendance_percentage"] *= 100

year_attendance.to_csv(
    DATA_DIR / "year_attendance_analysis.csv",
    index=False
)

# --------------------------------------------------
# 4. Subject-wise Attendance
# --------------------------------------------------

subject_attendance = (
    attendance
    .groupby("subject")
    .agg(
        total_records=("present_flag", "count"),
        attendance_percentage=("present_flag", "mean")
    )
    .reset_index()
)

subject_attendance["attendance_percentage"] *= 100

subject_attendance.to_csv(
    DATA_DIR / "subject_attendance_analysis.csv",
    index=False
)

# --------------------------------------------------
# 5. Monthly Attendance
# --------------------------------------------------

attendance["month"] = attendance["date"].dt.to_period("M").astype(str)

monthly_attendance = (
    attendance
    .groupby("month")
    .agg(
        total_records=("present_flag", "count"),
        attendance_percentage=("present_flag", "mean")
    )
    .reset_index()
)

monthly_attendance["attendance_percentage"] *= 100

monthly_attendance.to_csv(
    DATA_DIR / "monthly_attendance_analysis.csv",
    index=False
)

# --------------------------------------------------
# 6. Individual Student Attendance
# --------------------------------------------------

student_attendance = (
    attendance
    .groupby("student_id")
    .agg(
        total_classes=("present_flag", "count"),
        attendance_percentage=("present_flag", "mean")
    )
    .reset_index()
)

student_attendance["attendance_percentage"] *= 100

# Add student details
student_attendance = student_attendance.merge(
    students[
        [
            "student_id",
            "student_name",
            "department",
            "year",
            "section",
            "hostel_status"
        ]
    ],
    on="student_id",
    how="left"
)

# Attendance status
student_attendance["attendance_status"] = student_attendance[
    "attendance_percentage"
].apply(
    lambda x: "Below 75%" if x < 75 else "75% and Above"
)

student_attendance.to_csv(
    DATA_DIR / "student_attendance_analysis.csv",
    index=False
)

# --------------------------------------------------
# 7. Students Below 75%
# --------------------------------------------------

below_75 = student_attendance[
    student_attendance["attendance_percentage"] < 75
]

print(f"Students Below 75% Attendance: {len(below_75)}")

# --------------------------------------------------
# Completion
# --------------------------------------------------

print("\n==========================================")
print("ATTENDANCE ANALYSIS COMPLETE")
print("==========================================")

print("\nFiles created:")
print("1. department_attendance_analysis.csv")
print("2. year_attendance_analysis.csv")
print("3. subject_attendance_analysis.csv")
print("4. monthly_attendance_analysis.csv")
print("5. student_attendance_analysis.csv")