import pandas as pd
import sqlite3
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "01_Data"
SQL_DIR = BASE_DIR / "03_SQL"

# Create SQL folder if it doesn't exist
SQL_DIR.mkdir(exist_ok=True)

# Database path
DB_PATH = SQL_DIR / "campuspulse.db"

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)

# Load cleaned datasets
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

# Write tables to database
students.to_sql(
    "students",
    conn,
    if_exists="replace",
    index=False
)

attendance.to_sql(
    "attendance",
    conn,
    if_exists="replace",
    index=False
)

electricity.to_sql(
    "electricity",
    conn,
    if_exists="replace",
    index=False
)

canteen.to_sql(
    "canteen",
    conn,
    if_exists="replace",
    index=False
)

operating_costs.to_sql(
    "operating_costs",
    conn,
    if_exists="replace",
    index=False
)

# Check tables
tables = pd.read_sql_query(
    """
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    ORDER BY name;
    """,
    conn
)

print("\n==========================================")
print("CAMPUSPULSE SQL DATABASE CREATED")
print("==========================================")

print("\nTables created:")

for table in tables["name"]:
    print("-", table)

conn.close()

print("\nDatabase location:")
print(DB_PATH)