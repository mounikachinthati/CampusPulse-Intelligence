import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# CAMPUSPULSE - FOOD WASTE VISUALIZATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

food_item_waste = pd.read_csv(
    DATA_DIR / "food_item_waste_analysis.csv"
)

meal_waste = pd.read_csv(
    DATA_DIR / "meal_waste_analysis.csv"
)

monthly_waste = pd.read_csv(
    DATA_DIR / "monthly_food_waste_analysis.csv"
)

# ------------------------------------------------------------
# 1. FOOD WASTE BY ITEM
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    food_item_waste["food_item"],
    food_item_waste["food_waste"]
)

plt.title("Food Waste by Food Item")
plt.xlabel("Food Item")
plt.ylabel("Food Waste")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    DATA_DIR / "food_waste_by_item.png"
)

plt.show()

# ------------------------------------------------------------
# 2. FOOD WASTE BY MEAL
# ------------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar(
    meal_waste["meal_type"],
    meal_waste["food_waste"]
)

plt.title("Food Waste by Meal")
plt.xlabel("Meal Type")
plt.ylabel("Food Waste")

plt.tight_layout()

plt.savefig(
    DATA_DIR / "food_waste_by_meal.png"
)

plt.show()

# ------------------------------------------------------------
# 3. MONTHLY FOOD WASTE TREND
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_waste["month"],
    monthly_waste["food_waste"],
    marker="o"
)

plt.title("Monthly Food Waste Trend")
plt.xlabel("Month")
plt.ylabel("Food Waste")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    DATA_DIR / "monthly_food_waste.png"
)

plt.show()

# ------------------------------------------------------------
# 4. FOOD WASTE PERCENTAGE TREND
# ------------------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly_waste["month"],
    monthly_waste["waste_percentage"],
    marker="o"
)

plt.title("Monthly Food Waste Percentage")
plt.xlabel("Month")
plt.ylabel("Waste Percentage (%)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    DATA_DIR / "food_waste_percentage_trend.png"
)

plt.show()

print("\n==========================================")
print("FOOD WASTE VISUALIZATION COMPLETE")
print("==========================================")

print("\nCharts saved successfully.")