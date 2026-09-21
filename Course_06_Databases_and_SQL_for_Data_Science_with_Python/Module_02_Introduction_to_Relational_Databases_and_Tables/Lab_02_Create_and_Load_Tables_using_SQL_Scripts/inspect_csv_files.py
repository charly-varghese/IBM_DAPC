from pathlib import Path
import csv

DATA_FOLDER = Path("data")

csv_files = [
    "PATIENTS.csv",
    "MEDICAL_HISTORY.csv",
    "MEDICAL_PROCEDURES.csv",
    "MEDICAL_DEPARTMENTS.csv",
    "MEDICAL_LOCATIONS.csv",
]


for filename in csv_files:

    file_path = DATA_FOLDER / filename

    print("\n" + "=" * 70)
    print(f"FILE: {filename}")
    print("=" * 70)

    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)

        rows = list(reader)

        print(f"Total rows: {len(rows)}")

        if rows:
            print(f"Columns in first row: {len(rows[0])}")

            print("\nFirst row:")
            print(rows[0])

            print("\nSecond row:")
            if len(rows) > 1:
                print(rows[1])
