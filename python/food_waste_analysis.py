import pandas as pd
from pathlib import Path

# ============================================================
# CAMPUSPULSE - FOOD WASTE ANALYSIS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

canteen = pd.read_csv(
    DATA_DIR / "canteen_kpi.csv"
)

canteen["date"] = pd.to_datetime(
    canteen["date"]
)

# ------------------------------------------------------------
# 1. OVERALL FOOD WASTE
# ------------------------------------------------------------

total_prepared = canteen["quantity_prepared"].sum()
total_sold = canteen["quantity_sold"].sum()
total_waste = canteen["quantity_wasted"].sum()
total_waste_cost = canteen["waste_cost"].sum()

waste_percentage = (
    total_waste / total_prepared
) * 100

print("\n==========================================")
print("OVERALL FOOD WASTE")
print("==========================================")

print(f"Food Prepared: {total_prepared:,}")
print(f"Food Sold: {total_sold:,}")
print(f"Food Waste: {total_waste:,}")
print(f"Food Waste %: {waste_percentage:.2f}%")
print(f"Waste Cost: ₹{total_waste_cost:,.2f}")

# ------------------------------------------------------------
# 2. WASTE BY FOOD ITEM
# ------------------------------------------------------------

food_item_waste = (
    canteen
    .groupby("food_item")
    .agg(
        food_prepared=("quantity_prepared", "sum"),
        food_sold=("quantity_sold", "sum"),
        food_waste=("quantity_wasted", "sum"),
        waste_cost=("waste_cost", "sum")
    )
    .reset_index()
)

food_item_waste["waste_percentage"] = (
    food_item_waste["food_waste"]
    / food_item_waste["food_prepared"]
) * 100

food_item_waste = food_item_waste.sort_values(
    "food_waste",
    ascending=False
)

print("\n==========================================")
print("FOOD WASTE BY ITEM")
print("==========================================")

print(
    food_item_waste.to_string(index=False)
)

# ------------------------------------------------------------
# 3. WASTE BY MEAL
# ------------------------------------------------------------

meal_waste = (
    canteen
    .groupby("meal_type")
    .agg(
        food_prepared=("quantity_prepared", "sum"),
        food_waste=("quantity_wasted", "sum"),
        waste_cost=("waste_cost", "sum")
    )
    .reset_index()
)

meal_waste["waste_percentage"] = (
    meal_waste["food_waste"]
    / meal_waste["food_prepared"]
) * 100

meal_waste = meal_waste.sort_values(
    "food_waste",
    ascending=False
)

print("\n==========================================")
print("FOOD WASTE BY MEAL")
print("==========================================")

print(
    meal_waste.to_string(index=False)
)

# ------------------------------------------------------------
# 4. MONTHLY FOOD WASTE
# ------------------------------------------------------------

canteen["month"] = (
    canteen["date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_waste = (
    canteen
    .groupby("month")
    .agg(
        food_prepared=("quantity_prepared", "sum"),
        food_sold=("quantity_sold", "sum"),
        food_waste=("quantity_wasted", "sum"),
        waste_cost=("waste_cost", "sum")
    )
    .reset_index()
)

monthly_waste["waste_percentage"] = (
    monthly_waste["food_waste"]
    / monthly_waste["food_prepared"]
) * 100

print("\n==========================================")
print("MONTHLY FOOD WASTE")
print("==========================================")

print(
    monthly_waste.to_string(index=False)
)

# ------------------------------------------------------------
# 5. SAVE RESULTS
# ------------------------------------------------------------

food_item_waste.to_csv(
    DATA_DIR / "food_item_waste_analysis.csv",
    index=False
)

meal_waste.to_csv(
    DATA_DIR / "meal_waste_analysis.csv",
    index=False
)

monthly_waste.to_csv(
    DATA_DIR / "monthly_food_waste_analysis.csv",
    index=False
)

print("\n==========================================")
print("FOOD WASTE ANALYSIS COMPLETE")
print("==========================================")

print("\nAnalysis files saved successfully.")