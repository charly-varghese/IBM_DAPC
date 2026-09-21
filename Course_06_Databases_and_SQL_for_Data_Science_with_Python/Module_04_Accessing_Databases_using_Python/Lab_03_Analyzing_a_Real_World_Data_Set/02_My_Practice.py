# ============================================================
# CHICAGO COMMUNITY SOCIOECONOMIC ANALYSIS
# 02_My_Practice.py
# ============================================================

import sqlite3
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "socioeconomic.db"


# ============================================================
# DATABASE CONNECTION
# ============================================================

con = sqlite3.connect(DB_PATH)
cur = con.cursor()

print("Database connection: SUCCESS")
print("Database:", DB_PATH)
# ============================================================
# PRACTICE 1 — DISPLAY COMMUNITY AREAS
# ============================================================

rows = cur.execute("""
    SELECT
        ca,
        community_area_name
    FROM chicago_socioeconomic_data
    ORDER BY ca;
""").fetchall()

print("\nPractice 1 — Community Areas:")

for row in rows:
    print(row)

# ============================================================
# PRACTICE 1 — DISPLAY COMMUNITY AREAS
# ============================================================

rows = cur.execute("""
    SELECT
        ca,
        community_area_name
    FROM chicago_socioeconomic_data
    ORDER BY ca;
""").fetchall()

print("\nPractice 1 — Community Areas:")

for row in rows:
    print(row)
    # ============================================================
# PRACTICE 3 — BOTTOM 10 COMMUNITIES BY INCOME
# ============================================================

rows = cur.execute("""
    SELECT
        community_area_name,
        per_capita_income_
    FROM chicago_socioeconomic_data
    WHERE per_capita_income_ IS NOT NULL
    ORDER BY per_capita_income_ ASC
    LIMIT 10;
""").fetchall()

print("\nPractice 3 — Bottom 10 Communities by Per Capita Income:")

for row in rows:
    print(row)
    # ============================================================
# PRACTICE 4 — AVERAGE PER CAPITA INCOME
# ============================================================

result = cur.execute("""
    SELECT
        AVG(per_capita_income_)
    FROM chicago_socioeconomic_data;
""").fetchone()[0]

print("\nPractice 4 — Average Per Capita Income:", round(result, 2))
# ============================================================
# PRACTICE 5 — AVERAGE HARDSHIP INDEX
# ============================================================

result = cur.execute("""
    SELECT
        AVG(hardship_index)
    FROM chicago_socioeconomic_data;
""").fetchone()[0]

print("\nPractice 5 — Average Hardship Index:", round(result, 2))
# ============================================================
# PRACTICE 6 — HIGH INCOME + LOW HARDSHIP
# ============================================================

rows = cur.execute("""
    SELECT
        community_area_name,
        per_capita_income_,
        hardship_index
    FROM chicago_socioeconomic_data
    WHERE per_capita_income_ > 50000
      AND hardship_index < 30
    ORDER BY per_capita_income_ DESC;
""").fetchall()

print("\nPractice 6 — High Income + Low Hardship:")

for row in rows:
    print(row)
    # ============================================================
# PRACTICE 7 — HIGH HARDSHIP + LOW INCOME
# ============================================================

rows = cur.execute("""
    SELECT
        community_area_name,
        per_capita_income_,
        hardship_index
    FROM chicago_socioeconomic_data
    WHERE hardship_index > 70
      AND per_capita_income_ < 30000
    ORDER BY hardship_index DESC;
""").fetchall()

print("\nPractice 7 — High Hardship + Low Income:")

for row in rows:
    print(row)

    # ============================================================
# PRACTICE 8 — TOP 10 HARDSHIP COMMUNITIES
# ============================================================

rows = cur.execute("""
    SELECT
        community_area_name,
        hardship_index
    FROM chicago_socioeconomic_data
    WHERE hardship_index IS NOT NULL
    ORDER BY hardship_index DESC
    LIMIT 10;
""").fetchall()

print("\nPractice 8 — Top 10 Communities by Hardship Index:")

for row in rows:
    print(row)
    # ============================================================
# PRACTICE 9 — INCOME STATISTICS
# ============================================================

result = cur.execute("""
    SELECT
        MIN(per_capita_income_),
        MAX(per_capita_income_),
        AVG(per_capita_income_)
    FROM chicago_socioeconomic_data;
""").fetchone()

print("\nPractice 9 — Income Statistics:")
print("Minimum Income:", result[0])
print("Maximum Income:", result[1])
print("Average Income:", round(result[2], 2))
# ============================================================
# PRACTICE 10 — HARDSHIP STATISTICS
# ============================================================

result = cur.execute("""
    SELECT
        MIN(hardship_index),
        MAX(hardship_index),
        AVG(hardship_index)
    FROM chicago_socioeconomic_data;
""").fetchone()

print("\nPractice 10 — Hardship Statistics:")
print("Minimum Hardship:", result[0])
print("Maximum Hardship:", result[1])
print("Average Hardship:", round(result[2], 2))
# ============================================================
# PRACTICE 11 — SOCIOECONOMIC PRIORITY RANKING
# ============================================================

rows = cur.execute("""
    SELECT
        community_area_name,
        per_capita_income_,
        hardship_index,
        (hardship_index * 100000.0 / per_capita_income_) AS priority_score
    FROM chicago_socioeconomic_data
    WHERE per_capita_income_ IS NOT NULL
      AND hardship_index IS NOT NULL
      AND per_capita_income_ > 0
    ORDER BY priority_score DESC
    LIMIT 10;
""").fetchall()

print("\nPractice 11 — Top 10 Socioeconomic Priority Communities:")

for row in rows:
    print(row)
# ============================================================
# PRACTICE 12 — SQL RESULT INTO PANDAS
# ============================================================

query = """
SELECT
    community_area_name,
    per_capita_income_,
    hardship_index
FROM chicago_socioeconomic_data
WHERE per_capita_income_ IS NOT NULL
  AND hardship_index IS NOT NULL
ORDER BY per_capita_income_ DESC;
"""

analysis_df = pd.read_sql_query(query, con)

print("\nPractice 12 — SQL Result → Pandas:")
print(analysis_df.head(10))

print("\nDataFrame Shape:", analysis_df.shape)
# ============================================================
# PRACTICE VISUALIZATION — INCOME VS HARDSHIP
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(analysis_df["per_capita_income_"], analysis_df["hardship_index"])

plt.xlabel("Per Capita Income")
plt.ylabel("Hardship Index")
plt.title("Per Capita Income vs Hardship Index")

plt.grid(True)
plt.tight_layout()
plt.show()
# ============================================================
# PRACTICE ANALYTICS — CORRELATION
# ============================================================

correlation = analysis_df[["per_capita_income_", "hardship_index"]].corr().iloc[0, 1]

print("\nPractice Analytics — Pearson Correlation:", correlation)
# ============================================================
# PRACTICE VISUALIZATION — TOP 10 HARDSHIP
# ============================================================

top_hardship_df = pd.read_sql_query(
    """
    SELECT
        community_area_name,
        hardship_index
    FROM chicago_socioeconomic_data
    WHERE hardship_index IS NOT NULL
    ORDER BY hardship_index DESC
    LIMIT 10;
""",
    con,
)

plt.figure(figsize=(10, 6))

plt.bar(top_hardship_df["community_area_name"], top_hardship_df["hardship_index"])

plt.xlabel("Community Area")
plt.ylabel("Hardship Index")
plt.title("Top 10 Community Areas by Hardship Index")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
# ============================================================
# CLOSE DATABASE CONNECTION
# ============================================================

con.close()

print("\nDatabase connection: CLOSED")
print("02_My_Practice.py — COMPLETE")
