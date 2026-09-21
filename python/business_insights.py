import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

print("\n==========================================")
print("CAMPUSPULSE BUSINESS INSIGHTS")
print("==========================================")

# --------------------------------------------------
# 1. Attendance
# --------------------------------------------------

attendance = pd.read_csv(
    DATA_DIR / "department_attendance_analysis.csv"
)

attendance_overall = pd.read_csv(
    DATA_DIR / "attendance_kpi.csv"
)

overall_attendance = attendance_overall["present_flag"].mean() * 100

# --------------------------------------------------
# 2. Energy
# --------------------------------------------------

energy = pd.read_csv(
    DATA_DIR / "electricity_kpi.csv"
)

total_energy = energy["units_consumed_kwh"].sum()
total_energy_cost = energy["electricity_cost"].sum()

# --------------------------------------------------
# 3. Food Waste
# --------------------------------------------------

canteen = pd.read_csv(
    DATA_DIR / "canteen_kpi.csv"
)

total_food_prepared = canteen["quantity_prepared"].sum()
total_food_waste = canteen["quantity_wasted"].sum()

food_waste_percentage = (
    total_food_waste / total_food_prepared
) * 100

food_waste_cost = canteen["waste_cost"].sum()

# --------------------------------------------------
# 4. Operating Cost
# --------------------------------------------------

operating = pd.read_csv(
    DATA_DIR / "operating_costs_kpi.csv"
)

total_operating_cost = operating["amount"].sum()

# --------------------------------------------------
# 5. Create Summary
# --------------------------------------------------

summary = pd.DataFrame({
    "KPI": [
        "Total Students",
        "Overall Attendance (%)",
        "Total Energy Consumption (kWh)",
        "Total Electricity Cost (₹)",
        "Total Food Prepared",
        "Total Food Waste",
        "Food Waste Percentage (%)",
        "Food Waste Cost (₹)",
        "Total Operating Cost (₹)"
    ],
    "Value": [
        2000,
        round(overall_attendance, 2),
        round(total_energy, 2),
        round(total_energy_cost, 2),
        total_food_prepared,
        total_food_waste,
        round(food_waste_percentage, 2),
        round(food_waste_cost, 2),
        round(total_operating_cost, 2)
    ]
})

summary.to_csv(
    DATA_DIR / "campuspulse_business_summary.csv",
    index=False
)

# --------------------------------------------------
# 6. Print Summary
# --------------------------------------------------

print("\nKEY CAMPUS KPIs")
print("------------------------------------------")

for _, row in summary.iterrows():
    print(f"{row['KPI']}: {row['Value']}")

print("\n==========================================")
print("BUSINESS INSIGHTS COMPLETE")
print("==========================================")

print("\nCreated:")
print("campuspulse_business_summary.csv")