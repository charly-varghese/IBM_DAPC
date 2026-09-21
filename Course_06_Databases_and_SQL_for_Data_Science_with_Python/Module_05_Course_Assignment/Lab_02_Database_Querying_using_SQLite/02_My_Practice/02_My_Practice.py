from pathlib import Path
import sqlite3
import pandas as pd

# ============================================================
# LAB 02 — DATABASE QUERYING USING SQLITE
# IBM DAPC — COURSE 06 / MODULE 05
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

SCHOOLS_CSV = BASE_DIR / "CHICAGO_PUBLIC_SCHOOLS.csv"
CENSUS_CSV = BASE_DIR / "CENSUS_DATA.csv"
CRIME_CSV = BASE_DIR / "CHICAGO_CRIME_DATA.csv"

DB_FILE = BASE_DIR / "FinalDB.db"


# ============================================================
# HELPER FUNCTIONS
# ============================================================


def section(title):
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def run_query(conn, title, query):
    section(title)

    try:
        df = pd.read_sql_query(query, conn)

        if df.empty:
            print("No records returned.")
        else:
            print(df.to_string(index=False))

        return df

    except Exception as e:
        print(f"ERROR: {e}")
        return pd.DataFrame()


# ============================================================
# STEP 1 — LOAD DATASETS
# ============================================================

section("STEP 1 — LOAD CHICAGO PUBLIC SCHOOLS DATA")

schools_df = pd.read_csv(SCHOOLS_CSV)

print("Chicago Public Schools dataset loaded successfully.")
print(f"Rows    : {len(schools_df)}")
print(f"Columns : {len(schools_df.columns)}")


section("STEP 2 — LOAD SOCIOECONOMIC DATA")

census_df = pd.read_csv(CENSUS_CSV)

print("Socioeconomic Indicators dataset loaded successfully.")
print(f"Rows    : {len(census_df)}")
print(f"Columns : {len(census_df.columns)}")


section("STEP 3 — LOAD CHICAGO CRIME DATA")

crime_df = pd.read_csv(CRIME_CSV)

print("Chicago Crime dataset loaded successfully.")
print(f"Rows    : {len(crime_df)}")
print(f"Columns : {len(crime_df.columns)}")


# ============================================================
# STEP 4 — CONNECT TO SQLITE
# ============================================================

section("STEP 4 — CREATE / CONNECT TO SQLITE DATABASE")

print(f"Database: {DB_FILE}")

conn = sqlite3.connect(DB_FILE)


# ============================================================
# STEP 5 — CREATE THREE REQUIRED TABLES
# ============================================================

section("STEP 5 — STORE DATASETS IN SQLITE")

schools_df.to_sql("CHICAGO_PUBLIC_SCHOOLS", conn, if_exists="replace", index=False)

print("[✓] CHICAGO_PUBLIC_SCHOOLS table created")


census_df.to_sql("CENSUS_DATA", conn, if_exists="replace", index=False)

print("[✓] CENSUS_DATA table created")


crime_df.to_sql("CHICAGO_CRIME_DATA", conn, if_exists="replace", index=False)

print("[✓] CHICAGO_CRIME_DATA table created")


# ============================================================
# STEP 6 — VERIFY TABLES
# ============================================================

run_query(
    conn,
    "STEP 6 — AVAILABLE TABLES",
    """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
    """,
)


# ============================================================
# STEP 7 — VERIFY ROW COUNTS
# ============================================================

run_query(
    conn,
    "STEP 7 — TABLE ROW COUNTS",
    """
    SELECT
        'CHICAGO_PUBLIC_SCHOOLS' AS TABLE_NAME,
        COUNT(*) AS ROW_COUNT
    FROM CHICAGO_PUBLIC_SCHOOLS

    UNION ALL

    SELECT
        'CENSUS_DATA',
        COUNT(*)
    FROM CENSUS_DATA

    UNION ALL

    SELECT
        'CHICAGO_CRIME_DATA',
        COUNT(*)
    FROM CHICAGO_CRIME_DATA;
    """,
)


# ============================================================
# PROBLEM 1
# Find the total number of crimes recorded in the CRIME table.
# ============================================================

run_query(
    conn,
    "PROBLEM 1 — TOTAL NUMBER OF CRIMES",
    """
    SELECT COUNT(*) AS TOTAL_CRIMES
    FROM CHICAGO_CRIME_DATA;
    """,
)


# ============================================================
# PROBLEM 2
# List community area names and numbers with per capita income
# less than 11000.
# ============================================================

run_query(
    conn,
    "PROBLEM 2 — COMMUNITY AREAS WITH PER CAPITA INCOME < 11000",
    """
    SELECT
        "COMMUNITY AREA NAME",
        "Community Area Number",
        "PER CAPITA INCOME "
    FROM CENSUS_DATA
    WHERE CAST("PER CAPITA INCOME " AS REAL) < 11000
    ORDER BY "Community Area Number";
    """,
)


# ============================================================
# PROBLEM 3
# List all case numbers for crimes involving minors.
# ============================================================

run_query(
    conn,
    "PROBLEM 3 — CRIMES INVOLVING MINORS",
    """
    SELECT CASE_NUMBER
    FROM CHICAGO_CRIME_DATA
    WHERE DESCRIPTION LIKE '%MINOR%';
    """,
)


# ============================================================
# PROBLEM 4
# List all kidnapping crimes involving a child.
# ============================================================

run_query(
    conn,
    "PROBLEM 4 — KIDNAPPING CRIMES INVOLVING A CHILD",
    """
    SELECT CASE_NUMBER
    FROM CHICAGO_CRIME_DATA
    WHERE PRIMARY_TYPE = 'KIDNAPPING'
      AND DESCRIPTION LIKE '%CHILD%';
    """,
)


# ============================================================
# PROBLEM 5
# List the kinds of crimes recorded at schools.
# No repetitions.
# ============================================================

run_query(
    conn,
    "PROBLEM 5 — CRIME TYPES RECORDED AT SCHOOLS",
    """
    SELECT DISTINCT PRIMARY_TYPE
    FROM CHICAGO_CRIME_DATA
    WHERE LOCATION_DESCRIPTION LIKE '%SCHOOL%'
    ORDER BY PRIMARY_TYPE;
    """,
)


# ============================================================
# PROBLEM 6
# List school types with average safety score.
# ============================================================

run_query(
    conn,
    "PROBLEM 6 — AVERAGE SAFETY SCORE BY SCHOOL TYPE",
    """
    SELECT
        "Elementary, Middle, or High School" AS SCHOOL_TYPE,
        AVG("Safety Score") AS AVERAGE_SAFETY_SCORE
    FROM CHICAGO_PUBLIC_SCHOOLS
    GROUP BY "Elementary, Middle, or High School"
    ORDER BY SCHOOL_TYPE;
    """,
)


# ============================================================
# PROBLEM 7
# List 5 community areas with highest percentage of households
# below poverty line.
# ============================================================

run_query(
    conn,
    "PROBLEM 7 — TOP 5 COMMUNITY AREAS BY POVERTY",
    """
    SELECT
        "COMMUNITY AREA NAME",
        "Community Area Number",
        "PERCENT HOUSEHOLDS BELOW POVERTY"
    FROM CENSUS_DATA
    ORDER BY "PERCENT HOUSEHOLDS BELOW POVERTY" DESC
    LIMIT 5;
    """,
)


# ============================================================
# PROBLEM 8
# Which community area is most crime prone?
# Display community area number only.
# ============================================================

run_query(
    conn,
    "PROBLEM 8 — MOST CRIME-PRONE COMMUNITY AREA",
    """
    SELECT COMMUNITY_AREA_NUMBER
    FROM CHICAGO_CRIME_DATA
    GROUP BY COMMUNITY_AREA_NUMBER
    ORDER BY COUNT(*) DESC
    LIMIT 1;
    """,
)


# ============================================================
# PROBLEM 9
# Use a sub-query to find the name of the community area
# with highest hardship index.
# ============================================================

run_query(
    conn,
    "PROBLEM 9 — COMMUNITY AREA WITH HIGHEST HARDSHIP INDEX",
    """
    SELECT "COMMUNITY AREA NAME"
    FROM CENSUS_DATA
    WHERE "HARDSHIP INDEX" = (
        SELECT MAX("HARDSHIP INDEX")
        FROM CENSUS_DATA
    );
    """,
)


# ============================================================
# PROBLEM 10
# Use a sub-query to determine the Community Area Name
# with the most number of crimes.
# ============================================================

run_query(
    conn,
    "PROBLEM 10 — COMMUNITY AREA WITH MOST CRIMES",
    """
    SELECT "COMMUNITY AREA NAME"
    FROM CENSUS_DATA
    WHERE "Community Area Number" = (
        SELECT COMMUNITY_AREA_NUMBER
        FROM CHICAGO_CRIME_DATA
        GROUP BY COMMUNITY_AREA_NUMBER
        ORDER BY COUNT(*) DESC
        LIMIT 1
    );
    """,
)


# ============================================================
# FINAL VALIDATION
# ============================================================

section("FINAL LAB 02 VALIDATION")

tables = pd.read_sql_query(
    """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name;
    """,
    conn,
)

print("Tables:")
print(tables.to_string(index=False))


schools_count = pd.read_sql_query(
    "SELECT COUNT(*) AS count FROM CHICAGO_PUBLIC_SCHOOLS;", conn
).iloc[0, 0]


census_count = pd.read_sql_query(
    "SELECT COUNT(*) AS count FROM CENSUS_DATA;", conn
).iloc[0, 0]


crime_count = pd.read_sql_query(
    "SELECT COUNT(*) AS count FROM CHICAGO_CRIME_DATA;", conn
).iloc[0, 0]


print(f"\nCHICAGO_PUBLIC_SCHOOLS rows : {schools_count}")
print(f"CENSUS_DATA rows            : {census_count}")
print(f"CHICAGO_CRIME_DATA rows     : {crime_count}")


if schools_count == 566 and census_count == 78 and crime_count == 533:
    print("\n[✓] Dataset row-count validation PASSED")
else:
    print("\n[!] Dataset row-count validation requires review")


conn.close()


print("\n" + "=" * 80)
print("LAB 02 SINGLE-SHOT EXECUTION FINISHED")
print("=" * 80)
