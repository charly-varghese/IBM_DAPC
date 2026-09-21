from pathlib import Path
import sqlite3
import pandas as pd

# =============================================================================
# COURSE 06 — MODULE 05 — LAB 01
# WORKING WITH A REAL-WORLD DATA SET
# SINGLE-SHOT PRACTICE
# =============================================================================


# =============================================================================
# PATH CONFIGURATION
# =============================================================================

BASE_DIR = Path(__file__).resolve().parent

CPS_CSV = BASE_DIR / (
    "Chicago_Public_Schools_-_Progress_Report_Cards_(2011-2012)_20260914.csv"
)

CENSUS_CSV = BASE_DIR / "Chicago_Census_Data.csv"

DB_FILE = BASE_DIR / "RealWorldData.db"


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================


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


# =============================================================================
# STEP 1 — LOAD CPS SCHOOL DATA
# =============================================================================

section("STEP 1 — LOAD CPS SCHOOL DATA")

schools_df = pd.read_csv(CPS_CSV)

print("CPS dataset loaded successfully.")
print(f"Rows    : {len(schools_df)}")
print(f"Columns : {len(schools_df.columns)}")


# =============================================================================
# STEP 2 — LOAD CHICAGO SOCIOECONOMIC DATA
# =============================================================================

section("STEP 2 — LOAD CHICAGO SOCIOECONOMIC DATA")

census_df = pd.read_csv(CENSUS_CSV)

print("Chicago socioeconomic dataset loaded successfully.")
print(f"Rows    : {len(census_df)}")
print(f"Columns : {len(census_df.columns)}")

print("\nColumns:")
for column in census_df.columns:
    print(f" - {column}")


# =============================================================================
# STEP 3 — CONNECT TO SQLITE
# =============================================================================

section("STEP 3 — CREATE / CONNECT TO SQLITE DATABASE")

print(f"Database: {DB_FILE}")

conn = sqlite3.connect(DB_FILE)


# =============================================================================
# STEP 4 — CREATE SCHOOLS TABLE
# =============================================================================

section("STEP 4 — STORE CPS DATA IN SCHOOLS TABLE")

schools_df.to_sql("SCHOOLS", conn, if_exists="replace", index=False)

print("SCHOOLS table created successfully.")


# =============================================================================
# STEP 5 — CREATE CHICAGO_SOCIOECONOMIC_DATA TABLE
# =============================================================================

section("STEP 5 — STORE SOCIOECONOMIC DATA")

census_df.to_sql("CHICAGO_SOCIOECONOMIC_DATA", conn, if_exists="replace", index=False)

print("CHICAGO_SOCIOECONOMIC_DATA table created successfully.")


# =============================================================================
# STEP 6 — DATABASE TABLE CHECK
# =============================================================================

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


# =============================================================================
# STEP 7 — ROW COUNT VALIDATION
# =============================================================================

run_query(
    conn,
    "STEP 7 — TABLE ROW COUNTS",
    """
    SELECT 'SCHOOLS' AS TABLE_NAME,
           COUNT(*) AS ROW_COUNT
    FROM SCHOOLS

    UNION ALL

    SELECT 'CHICAGO_SOCIOECONOMIC_DATA',
           COUNT(*)
    FROM CHICAGO_SOCIOECONOMIC_DATA;
    """,
)


# =============================================================================
# STEP 8 — SOCIOECONOMIC DATA VALIDATION
# =============================================================================

run_query(
    conn,
    "STEP 8 — SOCIOECONOMIC DATA CHECK",
    """
    SELECT
        COMMUNITY_AREA_NUMBER,
        COMMUNITY_AREA_NAME,
        PER_CAPITA_INCOME,
        HARDSHIP_INDEX
    FROM CHICAGO_SOCIOECONOMIC_DATA
    WHERE COMMUNITY_AREA_NUMBER = 5;
    """,
)


# =============================================================================
# IBM PROBLEM 1
# =============================================================================

run_query(
    conn,
    "PROBLEM 1 — NUMBER OF ELEMENTARY SCHOOLS",
    """
    SELECT COUNT(*) AS Elementary_Schools
    FROM SCHOOLS
    WHERE "Elementary, Middle, or High School" = 'ES';
    """,
)


# =============================================================================
# IBM PROBLEM 2
# =============================================================================

run_query(
    conn,
    "PROBLEM 2 — HIGHEST SAFETY SCORE",
    """
    SELECT MAX("Safety Score") AS Highest_Safety_Score
    FROM SCHOOLS;
    """,
)


# =============================================================================
# IBM PROBLEM 3
# =============================================================================

run_query(
    conn,
    "PROBLEM 3 — SCHOOLS WITH HIGHEST SAFETY SCORE",
    """
    SELECT
        "Name of School",
        "Safety Score"
    FROM SCHOOLS
    WHERE "Safety Score" = (
        SELECT MAX("Safety Score")
        FROM SCHOOLS
    )
    ORDER BY "Name of School";
    """,
)


# =============================================================================
# IBM PROBLEM 4
# =============================================================================

run_query(
    conn,
    "PROBLEM 4 — TOP 10 SCHOOLS BY AVERAGE STUDENT ATTENDANCE",
    """
    SELECT
        "Name of School",
        "Average Student Attendance"
    FROM SCHOOLS
    WHERE "Average Student Attendance" IS NOT NULL
    ORDER BY
        CAST(
            REPLACE("Average Student Attendance", '%', '')
            AS REAL
        ) DESC
    LIMIT 10;
    """,
)


# =============================================================================
# IBM PROBLEM 5
# =============================================================================

run_query(
    conn,
    "PROBLEM 5 — 5 SCHOOLS WITH LOWEST ATTENDANCE",
    """
    SELECT
        "Name of School",
        "Average Student Attendance"
    FROM SCHOOLS
    WHERE "Average Student Attendance" IS NOT NULL
    ORDER BY
        CAST(
            REPLACE("Average Student Attendance", '%', '')
            AS REAL
        ) ASC
    LIMIT 5;
    """,
)


# =============================================================================
# IBM PROBLEM 6
# =============================================================================

run_query(
    conn,
    "PROBLEM 6 — REMOVE % SIGN",
    """
    SELECT
        "Name of School",
        CAST(
            REPLACE("Average Student Attendance", '%', '')
            AS REAL
        ) AS Attendance
    FROM SCHOOLS
    WHERE "Average Student Attendance" IS NOT NULL
    ORDER BY Attendance ASC
    LIMIT 5;
    """,
)


# =============================================================================
# IBM PROBLEM 7
# =============================================================================

run_query(
    conn,
    "PROBLEM 7 — SCHOOLS WITH ATTENDANCE BELOW 70%",
    """
    SELECT
        "Name of School",
        "Average Student Attendance"
    FROM SCHOOLS
    WHERE
        CAST(
            REPLACE("Average Student Attendance", '%', '')
            AS REAL
        ) < 70
    ORDER BY
        CAST(
            REPLACE("Average Student Attendance", '%', '')
            AS REAL
        ) ASC;
    """,
)


# =============================================================================
# IBM PROBLEM 8
# =============================================================================

run_query(
    conn,
    "PROBLEM 8 — TOTAL COLLEGE ENROLLMENT BY COMMUNITY AREA",
    """
    SELECT
        "Community Area Name",
        SUM(
            CAST(
                REPLACE(
                    "College Enrollment (number of students) ",
                    ',',
                    ''
                )
                AS INTEGER
            )
        ) AS Total_College_Enrollment
    FROM SCHOOLS
    WHERE "Community Area Name" IS NOT NULL
    GROUP BY "Community Area Name"
    ORDER BY "Community Area Name";
    """,
)


# =============================================================================
# IBM PROBLEM 9
# =============================================================================

run_query(
    conn,
    "PROBLEM 9 — 5 COMMUNITY AREAS WITH LOWEST ENROLLMENT",
    """
    SELECT
        "Community Area Name",
        SUM(
            CAST(
                REPLACE(
                    "College Enrollment (number of students) ",
                    ',',
                    ''
                )
                AS INTEGER
            )
        ) AS Total_College_Enrollment
    FROM SCHOOLS
    WHERE "Community Area Name" IS NOT NULL
    GROUP BY "Community Area Name"
    ORDER BY Total_College_Enrollment ASC
    LIMIT 5;
    """,
)


# =============================================================================
# IBM PROBLEM 10
# =============================================================================

run_query(
    conn,
    "PROBLEM 10 — 5 SCHOOLS WITH LOWEST SAFETY SCORE",
    """
    SELECT
        "Name of School",
        "Safety Score"
    FROM SCHOOLS
    WHERE "Safety Score" IS NOT NULL
    ORDER BY "Safety Score" ASC
    LIMIT 5;
    """,
)


# =============================================================================
# IBM PROBLEM 11
# =============================================================================

run_query(
    conn,
    "PROBLEM 11 — HARDSHIP INDEX FOR COLLEGE ENROLLMENT = 4368",
    """
    SELECT
        CD.COMMUNITY_AREA_NAME,
        CD.HARDSHIP_INDEX
    FROM CHICAGO_SOCIOECONOMIC_DATA AS CD
    JOIN SCHOOLS AS CPS
        ON CD.COMMUNITY_AREA_NUMBER =
           CPS."Community Area Number"
    WHERE CAST(
        REPLACE(
            CPS."College Enrollment (number of students) ",
            ',',
            ''
        ) AS INTEGER
    ) = 4368;
    """,
)


# =============================================================================
# IBM PROBLEM 12
# =============================================================================

run_query(
    conn,
    "PROBLEM 12 — HARDSHIP INDEX FOR SCHOOL WITH HIGHEST COLLEGE ENROLLMENT",
    """
    SELECT
        CD.COMMUNITY_AREA_NUMBER,
        CD.COMMUNITY_AREA_NAME,
        CD.HARDSHIP_INDEX
    FROM CHICAGO_SOCIOECONOMIC_DATA AS CD
    WHERE CD.COMMUNITY_AREA_NUMBER IN
    (
        SELECT "Community Area Number"
        FROM SCHOOLS
        ORDER BY
            CAST(
                REPLACE(
                    "College Enrollment (number of students) ",
                    ',',
                    ''
                ) AS INTEGER
            ) DESC
        LIMIT 1
    );
    """,
)


# =============================================================================
# FINAL VALIDATION
# =============================================================================

section("FINAL LAB 01 VALIDATION")

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

school_count = pd.read_sql_query("SELECT COUNT(*) AS count FROM SCHOOLS;", conn).iloc[
    0, 0
]

census_count = pd.read_sql_query(
    "SELECT COUNT(*) AS count FROM CHICAGO_SOCIOECONOMIC_DATA;", conn
).iloc[0, 0]

print(f"\nSCHOOLS rows                    : {school_count}")
print(f"CHICAGO_SOCIOECONOMIC_DATA rows: {census_count}")

if school_count == 566 and census_count == 78:
    print("\n[✓] Dataset row-count validation PASSED")
else:
    print("\n[!] Dataset row-count validation requires review")


# =============================================================================
# CLOSE DATABASE
# =============================================================================

conn.close()

print("\n" + "=" * 80)
print("LAB 01 SINGLE-SHOT EXECUTION FINISHED")
print("=" * 80)
