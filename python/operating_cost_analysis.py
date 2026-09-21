import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# Load cleaned operating cost data
cost = pd.read_csv(
    DATA_DIR / "operating_costs_clean.csv"
)

# Convert date
cost["date"] = pd.to_datetime(cost["date"])

print("\n==========================================")
print("OPERATING COST ANALYSIS")
print("==========================================")

# --------------------------------------------------
# 1. Overall Operating Cost
# --------------------------------------------------

total_cost = cost["amount"].sum()

print(f"\nTotal Operating Cost: ₹{total_cost:,.2f}")

# --------------------------------------------------
# 2. Department-wise Cost
# --------------------------------------------------

department_cost = (
    cost
    .groupby("department")
    .agg(
        total_cost=("amount", "sum"),
        average_cost=("amount", "mean")
    )
    .reset_index()
)

department_cost.to_csv(
    DATA_DIR / "department_cost_analysis.csv",
    index=False
)

# --------------------------------------------------
# 3. Expense Category-wise Cost
# --------------------------------------------------

category_cost = (
    cost
    .groupby("expense_category")
    .agg(
        total_cost=("amount", "sum"),
        average_cost=("amount", "mean")
    )
    .reset_index()
)

category_cost.to_csv(
    DATA_DIR / "category_cost_analysis.csv",
    index=False
)

# --------------------------------------------------
# 4. Monthly Operating Cost
# --------------------------------------------------

cost["month"] = cost["date"].dt.to_period("M").astype(str)

monthly_cost = (
    cost
    .groupby("month")
    .agg(
        total_cost=("amount", "sum"),
        average_cost=("amount", "mean")
    )
    .reset_index()
)

monthly_cost.to_csv(
    DATA_DIR / "monthly_cost_analysis.csv",
    index=False
)

# --------------------------------------------------
# 5. Department + Category Analysis
# --------------------------------------------------

department_category_cost = (
    cost
    .groupby(["department", "expense_category"])
    .agg(
        total_cost=("amount", "sum")
    )
    .reset_index()
)

department_category_cost.to_csv(
    DATA_DIR / "department_category_cost_analysis.csv",
    index=False
)

# --------------------------------------------------
# Completion
# --------------------------------------------------

print("\n==========================================")
print("OPERATING COST ANALYSIS COMPLETE")
print("==========================================")

print("\nFiles created:")
print("1. department_cost_analysis.csv")
print("2. category_cost_analysis.csv")
print("3. monthly_cost_analysis.csv")
print("4. department_category_cost_analysis.csv")