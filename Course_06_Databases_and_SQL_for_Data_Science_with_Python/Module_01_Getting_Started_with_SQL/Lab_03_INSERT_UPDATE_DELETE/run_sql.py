import sqlite3

connection = sqlite3.connect("data/Instructor.db")

with open("03_Challenge.sql", encoding="utf-8") as file:
    sql = file.read()

cursor = connection.cursor()

statements = [statement.strip() for statement in sql.split(";") if statement.strip()]

for number, statement in enumerate(statements, start=1):

    print(f"\n--- Query {number} ---")
    print(statement)

    cursor.execute(statement)

    # Check if the executed statement returned columns
    if cursor.description is not None:

        rows = cursor.fetchall()

        for row in rows:
            print(row)

    else:

        connection.commit()
        print(f"Rows affected: {cursor.rowcount}")

connection.close()
