import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# CAMPUSPULSE - ENERGY VISUALIZATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

building_energy = pd.read_csv(
    DATA_DIR / "building_energy_analysis.csv"
)

monthly_energy = pd.read_csv(
    DATA_DIR / "monthly_energy_analysis.csv"
)

# ------------------------------------------------------------
# 1. BUILDING-WISE ENERGY CONSUMPTION
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    building_energy["building"],
    building_energy["total_kwh"]
)

plt.title("Energy Consumption by Building")
plt.xlabel("Building")
plt.ylabel("Energy Consumption (kWh)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    DATA_DIR / "energy_by_building.png"
)

plt.show()

# ------------------------------------------------------------
# 2. MONTHLY ENERGY TREND
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_energy["month"],
    monthly_energy["total_kwh"],
    marker="o"
)

plt.title("Monthly Campus Energy Consumption")
plt.xlabel("Month")
plt.ylabel("Energy Consumption (kWh)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    DATA_DIR / "monthly_energy_trend.png"
)

plt.show()

# ------------------------------------------------------------
# 3. MONTHLY ELECTRICITY COST
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_energy["month"],
    monthly_energy["electricity_cost"],
    marker="o"
)

plt.title("Monthly Electricity Cost")
plt.xlabel("Month")
plt.ylabel("Electricity Cost (₹)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    DATA_DIR / "monthly_electricity_cost.png"
)

plt.show()

print("\n==========================================")
print("ENERGY VISUALIZATION COMPLETE")
print("==========================================")

print("\nCharts saved in:")
print(DATA_DIR)