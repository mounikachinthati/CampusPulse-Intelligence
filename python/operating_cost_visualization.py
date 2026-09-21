import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"

# Load analysis files
department = pd.read_csv(
    DATA_DIR / "department_cost_analysis.csv"
)

category = pd.read_csv(
    DATA_DIR / "category_cost_analysis.csv"
)

monthly = pd.read_csv(
    DATA_DIR / "monthly_cost_analysis.csv"
)

department_category = pd.read_csv(
    DATA_DIR / "department_category_cost_analysis.csv"
)

# --------------------------------------------------
# 1. Operating Cost by Department
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    department["department"],
    department["total_cost"]
)

plt.title("Operating Cost by Department")
plt.xlabel("Department")
plt.ylabel("Total Cost (₹)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    DATA_DIR / "operating_cost_by_department.png"
)

plt.show()


# --------------------------------------------------
# 2. Operating Cost by Expense Category
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.bar(
    category["expense_category"],
    category["total_cost"]
)

plt.title("Operating Cost by Expense Category")
plt.xlabel("Expense Category")
plt.ylabel("Total Cost (₹)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    DATA_DIR / "operating_cost_by_category.png"
)

plt.show()


# --------------------------------------------------
# 3. Monthly Operating Cost Trend
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.plot(
    monthly["month"],
    monthly["total_cost"],
    marker="o"
)

plt.title("Monthly Operating Cost Trend")
plt.xlabel("Month")
plt.ylabel("Total Cost (₹)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    DATA_DIR / "monthly_operating_cost.png"
)

plt.show()


# --------------------------------------------------
# 4. Department + Category Cost
# --------------------------------------------------

pivot_data = department_category.pivot(
    index="department",
    columns="expense_category",
    values="total_cost"
)

pivot_data.plot(
    kind="bar",
    figsize=(12, 6)
)

plt.title("Operating Cost by Department and Category")
plt.xlabel("Department")
plt.ylabel("Total Cost (₹)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    DATA_DIR / "department_category_cost.png"
)

plt.show()


# --------------------------------------------------
# Completion
# --------------------------------------------------

print("\n==========================================")
print("OPERATING COST VISUALIZATION COMPLETE")
print("==========================================")

print("\nCharts saved successfully:")
print("1. operating_cost_by_department.png")
print("2. operating_cost_by_category.png")
print("3. monthly_operating_cost.png")
print("4. department_category_cost.png")