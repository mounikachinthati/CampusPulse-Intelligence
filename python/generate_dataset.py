import pandas as pd
import numpy as np
from pathlib import Path

# ============================================================
# CAMPUSPULSE INTELLIGENCE - DATASET GENERATION
# ============================================================

np.random.seed(42)

# Project folders
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"
DATA_DIR.mkdir(exist_ok=True)

# ------------------------------------------------------------
# 1. STUDENTS DATA
# ------------------------------------------------------------

num_students = 2000

departments = ["CSE", "AIML", "ECE", "EEE", "MECH", "CIVIL", "IT"]
years = [1, 2, 3, 4]
sections = ["A", "B", "C", "D"]
genders = ["Male", "Female"]
hostel_statuses = ["Hostel", "Day Scholar"]

students = pd.DataFrame({
    "student_id": [f"STU{i:04d}" for i in range(1, num_students + 1)],
    "student_name": [f"Student_{i:04d}" for i in range(1, num_students + 1)],
    "department": np.random.choice(departments, num_students),
    "year": np.random.choice(years, num_students),
    "section": np.random.choice(sections, num_students),
    "gender": np.random.choice(genders, num_students),
    "hostel_status": np.random.choice(hostel_statuses, num_students)
})

students.to_csv(DATA_DIR / "students.csv", index=False)

# ------------------------------------------------------------
# 2. ATTENDANCE DATA
# ------------------------------------------------------------

dates = pd.date_range("2026-01-01", "2026-08-31", freq="D")

subjects = {
    "CSE": ["DBMS", "Python", "OS", "DSA"],
    "AIML": ["Python", "Machine Learning", "Statistics", "DBMS"],
    "ECE": ["Digital Electronics", "Signals", "Networks", "Microprocessors"],
    "EEE": ["Power Systems", "Circuits", "Machines", "Control Systems"],
    "MECH": ["Thermodynamics", "CAD", "Mechanics", "Manufacturing"],
    "CIVIL": ["Structures", "Surveying", "Concrete", "Geotechnical"],
    "IT": ["DBMS", "Web Development", "Python", "Networks"]
}

attendance_records = []

# Approximately 50 attendance records per student
for student in students.itertuples(index=False):

    student_dates = np.random.choice(
        dates,
        size=50,
        replace=False
    )

    student_subjects = subjects[student.department]

    for date in student_dates:

        subject = np.random.choice(student_subjects)

        status = np.random.choice(
            ["Present", "Absent"],
            p=[0.82, 0.18]
        )

        attendance_records.append([
            f"ATT{len(attendance_records) + 1:06d}",
            student.student_id,
            date,
            subject,
            status
        ])

attendance = pd.DataFrame(
    attendance_records,
    columns=[
        "attendance_id",
        "student_id",
        "date",
        "subject",
        "status"
    ]
)

attendance.to_csv(DATA_DIR / "attendance.csv", index=False)

# ------------------------------------------------------------
# 3. ELECTRICITY DATA
# ------------------------------------------------------------

energy_dates = pd.date_range(
    "2026-01-01",
    "2026-08-31",
    freq="D"
)

buildings = [
    "Academic Block",
    "Hostel A",
    "Hostel B",
    "Library",
    "Canteen",
    "Computer Lab",
    "Admin Block"
]

energy_records = []

for date in energy_dates:

    for building in buildings:

        base_consumption = {
            "Academic Block": 950,
            "Hostel A": 1100,
            "Hostel B": 1050,
            "Library": 650,
            "Canteen": 450,
            "Computer Lab": 1250,
            "Admin Block": 400
        }[building]

        consumption = max(
            100,
            np.random.normal(base_consumption, base_consumption * 0.12)
        )

        peak_units = consumption * np.random.uniform(0.35, 0.55)

        electricity_rate = np.random.uniform(7, 9)

        electricity_cost = consumption * electricity_rate

        energy_records.append([
            f"ENG{len(energy_records) + 1:06d}",
            date,
            building,
            f"MTR-{buildings.index(building) + 1:02d}",
            round(consumption, 2),
            round(electricity_cost, 2),
            round(peak_units, 2)
        ])

electricity = pd.DataFrame(
    energy_records,
    columns=[
        "energy_id",
        "date",
        "building",
        "meter_id",
        "units_consumed_kwh",
        "electricity_cost",
        "peak_hour_units"
    ]
)

electricity.to_csv(DATA_DIR / "electricity.csv", index=False)

# ------------------------------------------------------------
# 4. CANTEEN DATA
# ------------------------------------------------------------

canteen_dates = pd.date_range(
    "2026-01-01",
    "2026-08-31",
    freq="D"
)

meal_types = ["Breakfast", "Lunch", "Snacks", "Dinner"]

food_items = [
    "Rice",
    "Dal",
    "Vegetable Curry",
    "Chicken Curry",
    "Chapati",
    "Idli",
    "Dosa",
    "Sambar",
    "Fried Rice",
    "Noodles",
    "Biryani",
    "Curd Rice"
]

canteen_records = []

for date in canteen_dates:

    for meal in meal_types:

        # Generate several food items per meal
        selected_items = np.random.choice(
            food_items,
            size=4,
            replace=False
        )

        for food_item in selected_items:

            quantity_prepared = np.random.randint(50, 250)

            waste_percentage = np.random.uniform(0.04, 0.20)

            quantity_wasted = int(
                quantity_prepared * waste_percentage
            )

            quantity_sold = (
                quantity_prepared -
                quantity_wasted -
                np.random.randint(0, 8)
            )

            quantity_sold = max(
                0,
                quantity_sold
            )

            cost_per_unit = np.random.uniform(15, 80)

            total_cost = (
                quantity_prepared *
                cost_per_unit
            )

            canteen_records.append([
                f"FOOD{len(canteen_records) + 1:06d}",
                date,
                meal,
                food_item,
                quantity_prepared,
                quantity_sold,
                quantity_wasted,
                round(cost_per_unit, 2),
                round(total_cost, 2)
            ])

canteen = pd.DataFrame(
    canteen_records,
    columns=[
        "food_id",
        "date",
        "meal_type",
        "food_item",
        "quantity_prepared",
        "quantity_sold",
        "quantity_wasted",
        "cost_per_unit",
        "total_cost"
    ]
)

canteen.to_csv(DATA_DIR / "canteen.csv", index=False)

# ------------------------------------------------------------
# 5. OPERATING COST DATA
# ------------------------------------------------------------

cost_dates = pd.date_range(
    "2026-01-01",
    "2026-08-31",
    freq="D"
)

cost_departments = [
    "Administration",
    "Hostel",
    "Canteen",
    "Academic",
    "Maintenance",
    "Transport"
]

expense_categories = [
    "Electricity",
    "Food",
    "Maintenance",
    "Water",
    "Transport",
    "Cleaning",
    "Internet",
    "Other"
]

cost_records = []

for date in cost_dates:

    for department in cost_departments:

        # Randomly select a few expenses per department
        selected_categories = np.random.choice(
            expense_categories,
            size=2,
            replace=False
        )

        for category in selected_categories:

            base_cost = {
                "Electricity": 15000,
                "Food": 12000,
                "Maintenance": 8000,
                "Water": 5000,
                "Transport": 7000,
                "Cleaning": 4000,
                "Internet": 2500,
                "Other": 3000
            }[category]

            amount = np.random.normal(
                base_cost,
                base_cost * 0.20
            )

            amount = max(
                500,
                amount
            )

            cost_records.append([
                f"COST{len(cost_records) + 1:06d}",
                date,
                department,
                category,
                round(amount, 2)
            ])

operating_costs = pd.DataFrame(
    cost_records,
    columns=[
        "cost_id",
        "date",
        "department",
        "expense_category",
        "amount"
    ]
)

operating_costs.to_csv(
    DATA_DIR / "operating_costs.csv",
    index=False
)

# ------------------------------------------------------------
# FINAL SUMMARY
# ------------------------------------------------------------

print("\n==========================================")
print("CAMPUSPULSE DATASET GENERATION COMPLETE")
print("==========================================")

print(f"\nStudents:          {len(students):,}")
print(f"Attendance:        {len(attendance):,}")
print(f"Electricity:       {len(electricity):,}")
print(f"Canteen:           {len(canteen):,}")
print(f"Operating Costs:   {len(operating_costs):,}")

print("\nFiles saved to:")
print(DATA_DIR)

print("\nDataset files:")
for file in DATA_DIR.glob("*.csv"):
    print(" -", file.name)

print("\n==========================================")
# ============================================================
# DATA QUALITY CHECK
# ============================================================

print("\n==========================================")
print("DATA QUALITY CHECK")
print("==========================================")

files = {
    "Students": DATA_DIR / "students.csv",
    "Attendance": DATA_DIR / "attendance.csv",
    "Electricity": DATA_DIR / "electricity.csv",
    "Canteen": DATA_DIR / "canteen.csv",
    "Operating Costs": DATA_DIR / "operating_costs.csv"
}

for name, file_path in files.items():

    df = pd.read_csv(file_path)

    print(f"\n--- {name} ---")

    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("\nMissing values:")
    print(df.isnull().sum())

    print("\nDuplicate rows:", df.duplicated().sum())

    print("\nData types:")
    print(df.dtypes)