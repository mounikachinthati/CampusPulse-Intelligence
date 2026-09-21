import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "03_SQL" / "campuspulse.db"

conn = sqlite3.connect(DB_PATH)

query = """
SELECT student_id, student_name, department, year
FROM students
ORDER BY student_name ASC
LIMIT 10;
"""

result = conn.execute(query).fetchall()

for row in result:
    print(row)

conn.close()