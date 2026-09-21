import pandas as pd
from pathlib import Path

# ============================================================
# CAMPUSPULSE - KPI CALCULATIONS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# ------------------------------------------------------------
# LOAD CLEAN DATA
# ------------------------------------------------------------

students = pd.read_csv(
    DATA_DIR / "students_clean.csv"
)

attendance = pd.read_csv(
    DATA_DIR / "attendance_clean.csv"
)

electricity = pd.read_csv(
    DATA_DIR / "electricity_clean.csv"
)

canteen = pd.read_csv(
    DATA_DIR / "canteen_clean.csv"
)

operating_costs = pd.read_csv(
    DATA_DIR / "operating_costs_clean.csv"
)

# ------------------------------------------------------------
# 1. ATTENDANCE KPI
# ------------------------------------------------------------

attendance["present_flag"] = (
    attendance["status"] == "Present"
).astype(int)

# ------------------------------------------------------------
# 2. ELECTRICITY KPI
# ------------------------------------------------------------

electricity["cost_per_kwh"] = (
    electricity["electricity_cost"]
    / electricity["units_consumed_kwh"]
)

# ------------------------------------------------------------
# 3. CANTEEN KPIs
# ------------------------------------------------------------

canteen["food_waste_percentage"] = (
    canteen["quantity_wasted"]
    / canteen["quantity_prepared"]
) * 100

canteen["sold_percentage"] = (
    canteen["quantity_sold"]
    / canteen["quantity_prepared"]
) * 100

canteen["waste_cost"] = (
    canteen["quantity_wasted"]
    * canteen["cost_per_unit"]
)

# ------------------------------------------------------------
# 4. OPERATING COST KPI
# ------------------------------------------------------------

operating_costs["cost_month"] = pd.to_datetime(
    operating_costs["date"]
).dt.to_period("M").astype(str)

# ------------------------------------------------------------
# 5. SAVE KPI DATA
# ------------------------------------------------------------

attendance.to_csv(
    DATA_DIR / "attendance_kpi.csv",
    index=False
)

electricity.to_csv(
    DATA_DIR / "electricity_kpi.csv",
    index=False
)

canteen.to_csv(
    DATA_DIR / "canteen_kpi.csv",
    index=False
)

operating_costs.to_csv(
    DATA_DIR / "operating_costs_kpi.csv",
    index=False
)

# ------------------------------------------------------------
# 6. DISPLAY IMPORTANT KPI RESULTS
# ------------------------------------------------------------

total_students = students["student_id"].nunique()

attendance_rate = (
    attendance["present_flag"].mean() * 100
)

total_energy = (
    electricity["units_consumed_kwh"].sum()
)

total_electricity_cost = (
    electricity["electricity_cost"].sum()
)

total_food_prepared = (
    canteen["quantity_prepared"].sum()
)

total_food_waste = (
    canteen["quantity_wasted"].sum()
)

food_waste_percentage = (
    total_food_waste /
    total_food_prepared
) * 100

total_waste_cost = (
    canteen["waste_cost"].sum()
)

total_operating_cost = (
    operating_costs["amount"].sum()
)

# ------------------------------------------------------------
# FINAL KPI SUMMARY
# ------------------------------------------------------------

print("\n==========================================")
print("CAMPUSPULSE KPI SUMMARY")
print("==========================================")

print(f"Total Students: {total_students:,}")

print(
    f"Overall Attendance: "
    f"{attendance_rate:.2f}%"
)

print(
    f"Total Energy Consumption: "
    f"{total_energy:,.2f} kWh"
)

print(
    f"Total Electricity Cost: "
    f"₹{total_electricity_cost:,.2f}"
)

print(
    f"Total Food Prepared: "
    f"{total_food_prepared:,}"
)

print(
    f"Total Food Waste: "
    f"{total_food_waste:,}"
)

print(
    f"Food Waste Percentage: "
    f"{food_waste_percentage:.2f}%"
)

print(
    f"Food Waste Cost: "
    f"₹{total_waste_cost:,.2f}"
)

print(
    f"Total Operating Cost: "
    f"₹{total_operating_cost:,.2f}"
)

print("\n==========================================")