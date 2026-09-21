# ============================================================
# IMPORTS & PROJECT PATHS
# ============================================================

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project/Lab directory
BASE_DIR = Path(__file__).resolve().parent

# Local database path
DB_PATH = BASE_DIR / "socioeconomic.db"

# Local CSV dataset path
CSV_PATH = BASE_DIR / "data" / "chicago_socioeconomic_data.csv"

# ============================================================
# STEP 1 — ENVIRONMENT CHECK
# ============================================================

print("Pandas version:", pd.__version__)
print("SQLite module: OK")
print("IBM Lab 03 environment: READY")

# ============================================================
# STEP 2 — CONNECT TO SQLITE DATABASE
# ============================================================

con = sqlite3.connect(DB_PATH)
cur = con.cursor()

print("Database connection: SUCCESS")
print("Cursor creation: SUCCESS")
print("Database:", DB_PATH)

# ============================================================
# STEP 3 — LOAD DATASET
# ============================================================

df = pd.read_csv(CSV_PATH)

print("\nDataset loaded successfully")
print("Dataset path:", CSV_PATH)
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Rows:")
print(df.head())

# ============================================================
# STEP 4 — STORE DATASET IN SQLITE TABLE
# ============================================================

table_name = "chicago_socioeconomic_data"

df.to_sql(table_name, con, if_exists="replace", index=False)

print("Dataset stored successfully in SQLite")
print("Table:", table_name)
# Verify table exists
tables = cur.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()

print("\nSQLite Tables:")
print(tables)
# ============================================================
# STEP 5 — VERIFY SQLITE TABLE DATA
# ============================================================

row_count = cur.execute("SELECT COUNT(*) FROM chicago_socioeconomic_data;").fetchone()[
    0
]

print("\nSQLite Row Count:", row_count)

print("\nFirst 5 SQLite Records:")

rows = cur.execute("""
    SELECT
        ca,
        community_area_name,
        per_capita_income_,
        hardship_index
    FROM chicago_socioeconomic_data
    LIMIT 5;
""").fetchall()

for row in rows:
    print(row)

# ============================================================
# PROBLEM 1 — COUNT NUMBER OF ROWS
# ============================================================

result = cur.execute("""
    SELECT COUNT(*)
    FROM chicago_socioeconomic_data;
""").fetchone()[0]

print("\nProblem 1 — Number of Rows:", result)

# ============================================================
# PROBLEM 2 — COMMUNITY AREAS WITH HARDSHIP INDEX > 50
# ============================================================

result = cur.execute("""
    SELECT COUNT(*)
    FROM chicago_socioeconomic_data
    WHERE hardship_index > 50;
""").fetchone()[0]

print("\nProblem 2 — Community Areas with Hardship Index > 50:", result)

# ============================================================
# PROBLEM 3 — MAXIMUM HARDSHIP INDEX
# ============================================================

result = cur.execute("""
    SELECT MAX(hardship_index)
    FROM chicago_socioeconomic_data;
""").fetchone()[0]

print("\nProblem 3 — Maximum Hardship Index:", result)

# ============================================================
# PROBLEM 4 — COMMUNITY AREA WITH HIGHEST HARDSHIP INDEX
# ============================================================

result = cur.execute("""
    SELECT community_area_name, hardship_index
    FROM chicago_socioeconomic_data
    WHERE hardship_index = (
        SELECT MAX(hardship_index)
        FROM chicago_socioeconomic_data
    );
""").fetchone()

print("\nProblem 4 — Community Area with Highest Hardship Index:")
print("Community Area:", result[0])
print("Hardship Index:", result[1])

# ============================================================
# PROBLEM 5 — COMMUNITY AREAS WITH PER CAPITA INCOME > 60000
# ============================================================

results = cur.execute("""
    SELECT community_area_name, per_capita_income_
    FROM chicago_socioeconomic_data
    WHERE per_capita_income_ > 60000;
""").fetchall()

print("\nProblem 5 — Community Areas with Per Capita Income > $60,000:")

for row in results:
    print(row)

# ============================================================
# PROBLEM 6 — PER CAPITA INCOME VS HARDSHIP INDEX
# ============================================================

import matplotlib.pyplot as plt

rows = cur.execute("""
    SELECT
        per_capita_income_,
        hardship_index
    FROM chicago_socioeconomic_data
    WHERE per_capita_income_ IS NOT NULL
      AND hardship_index IS NOT NULL;
""").fetchall()

plot_df = pd.DataFrame(rows, columns=["per_capita_income", "hardship_index"])

print("\nProblem 6 — Data prepared for scatter plot")
print("Rows:", len(plot_df))
print(plot_df.head())

# ============================================================
# PROBLEM 6 — SCATTER PLOT
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(plot_df["per_capita_income"], plot_df["hardship_index"])

plt.xlabel("Per Capita Income")
plt.ylabel("Hardship Index")
plt.title("Per Capita Income vs Hardship Index")

plt.grid(True)
plt.tight_layout()
plt.show()

# ============================================================
# PROBLEM 6 — PEARSON CORRELATION
# ============================================================

correlation = plot_df["per_capita_income"].corr(plot_df["hardship_index"])

print("\nProblem 6 — Pearson Correlation Coefficient:", correlation)
