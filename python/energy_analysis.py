import pandas as pd
from pathlib import Path

# ============================================================
# CAMPUSPULSE - ENERGY ANALYSIS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# Load electricity KPI data
electricity = pd.read_csv(
    DATA_DIR / "electricity_kpi.csv"
)

electricity["date"] = pd.to_datetime(
    electricity["date"]
)

# ------------------------------------------------------------
# 1. TOTAL ENERGY BY BUILDING
# ------------------------------------------------------------

building_energy = (
    electricity
    .groupby("building")
    .agg(
        total_kwh=("units_consumed_kwh", "sum"),
        electricity_cost=("electricity_cost", "sum")
    )
    .reset_index()
    .sort_values(
        "total_kwh",
        ascending=False
    )
)

print("\n==========================================")
print("ENERGY CONSUMPTION BY BUILDING")
print("==========================================")

print(building_energy.to_string(index=False))

# ------------------------------------------------------------
# 2. MONTHLY ENERGY CONSUMPTION
# ------------------------------------------------------------

electricity["month"] = (
    electricity["date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_energy = (
    electricity
    .groupby("month")
    .agg(
        total_kwh=("units_consumed_kwh", "sum"),
        electricity_cost=("electricity_cost", "sum")
    )
    .reset_index()
)

print("\n==========================================")
print("MONTHLY ENERGY CONSUMPTION")
print("==========================================")

print(monthly_energy.to_string(index=False))

# ------------------------------------------------------------
# 3. PEAK HOUR CONSUMPTION
# ------------------------------------------------------------

peak_by_building = (
    electricity
    .groupby("building")
    .agg(
        peak_hour_kwh=("peak_hour_units", "sum")
    )
    .reset_index()
    .sort_values(
        "peak_hour_kwh",
        ascending=False
    )
)

print("\n==========================================")
print("PEAK HOUR CONSUMPTION")
print("==========================================")

print(peak_by_building.to_string(index=False))

# ------------------------------------------------------------
# 4. AVERAGE DAILY CONSUMPTION
# ------------------------------------------------------------

daily_energy = (
    electricity
    .groupby("date")["units_consumed_kwh"]
    .sum()
)

average_daily_energy = daily_energy.mean()

print("\n==========================================")
print("AVERAGE DAILY ENERGY")
print("==========================================")

print(
    f"Average Daily Consumption: "
    f"{average_daily_energy:,.2f} kWh"
)

# ------------------------------------------------------------
# 5. SAVE ANALYSIS RESULTS
# ------------------------------------------------------------

building_energy.to_csv(
    DATA_DIR / "building_energy_analysis.csv",
    index=False
)

monthly_energy.to_csv(
    DATA_DIR / "monthly_energy_analysis.csv",
    index=False
)

peak_by_building.to_csv(
    DATA_DIR / "peak_energy_analysis.csv",
    index=False
)

print("\nAnalysis files saved successfully.")