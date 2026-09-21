import pandas as pd
from pathlib import Path

# ============================================================
# CAMPUSPULSE - DATA CLEANING & VALIDATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

students = pd.read_csv(DATA_DIR / "students.csv")
attendance = pd.read_csv(DATA_DIR / "attendance.csv")
electricity = pd.read_csv(DATA_DIR / "electricity.csv")
canteen = pd.read_csv(DATA_DIR / "canteen.csv")
operating_costs = pd.read_csv(DATA_DIR / "operating_costs.csv")

# ------------------------------------------------------------
# 2. CONVERT DATE COLUMNS
# ------------------------------------------------------------

attendance["date"] = pd.to_datetime(attendance["date"])
electricity["date"] = pd.to_datetime(electricity["date"])
canteen["date"] = pd.to_datetime(canteen["date"])
operating_costs["date"] = pd.to_datetime(operating_costs["date"])

# ------------------------------------------------------------
# 3. REMOVE DUPLICATES
# ------------------------------------------------------------

students = students.drop_duplicates()
attendance = attendance.drop_duplicates()
electricity = electricity.drop_duplicates()
canteen = canteen.drop_duplicates()
operating_costs = operating_costs.drop_duplicates()

# ------------------------------------------------------------
# 4. VALIDATE ATTENDANCE
# ------------------------------------------------------------

valid_status = ["Present", "Absent"]

invalid_attendance = attendance[
    ~attendance["status"].isin(valid_status)
]

print("\nInvalid attendance records:", len(invalid_attendance))

# ------------------------------------------------------------
# 5. VALIDATE ELECTRICITY
# ------------------------------------------------------------

invalid_electricity = electricity[
    (electricity["units_consumed_kwh"] < 0) |
    (electricity["electricity_cost"] < 0) |
    (electricity["peak_hour_units"] < 0)
]

print("Invalid electricity records:", len(invalid_electricity))

# ------------------------------------------------------------
# 6. VALIDATE CANTEEN DATA
# ------------------------------------------------------------

invalid_canteen = canteen[
    (canteen["quantity_prepared"] < 0) |
    (canteen["quantity_sold"] < 0) |
    (canteen["quantity_wasted"] < 0) |
    (canteen["cost_per_unit"] < 0) |
    (canteen["total_cost"] < 0)
]

print("Invalid canteen records:", len(invalid_canteen))

# Check that sold + wasted does not exceed prepared
invalid_food_quantity = canteen[
    canteen["quantity_sold"] + canteen["quantity_wasted"]
    > canteen["quantity_prepared"]
]

print(
    "Invalid food quantity records:",
    len(invalid_food_quantity)
)

# ------------------------------------------------------------
# 7. VALIDATE OPERATING COSTS
# ------------------------------------------------------------

invalid_costs = operating_costs[
    operating_costs["amount"] < 0
]

print("Invalid operating cost records:", len(invalid_costs))

# ------------------------------------------------------------
# 8. CHECK STUDENT IDs IN ATTENDANCE
# ------------------------------------------------------------

invalid_student_ids = attendance[
    ~attendance["student_id"].isin(students["student_id"])
]

print(
    "Attendance records with invalid student IDs:",
    len(invalid_student_ids)
)

# ------------------------------------------------------------
# 9. SAVE CLEAN DATA
# ------------------------------------------------------------

students.to_csv(DATA_DIR / "students_clean.csv", index=False)
attendance.to_csv(DATA_DIR / "attendance_clean.csv", index=False)
electricity.to_csv(DATA_DIR / "electricity_clean.csv", index=False)
canteen.to_csv(DATA_DIR / "canteen_clean.csv", index=False)
operating_costs.to_csv(
    DATA_DIR / "operating_costs_clean.csv",
    index=False
)

# ------------------------------------------------------------
# FINAL MESSAGE
# ------------------------------------------------------------

print("\n==========================================")
print("DATA CLEANING & VALIDATION COMPLETE")
print("==========================================")

print("\nClean files created successfully.")