import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "students.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                age INTEGER NOT NULL CHECK (age >= 1)
            )
        """)

def add_student(name, age):
    with get_connection() as connection:
        connection.execute(
            "INSERT INTO students (name, age) VALUES (?, ?)",
            (name, age)
        )

def get_all_students():
    with get_connection() as connection:
        return connection.execute(
            "SELECT id, name, age FROM students"
        ).fetchall()


def get_student_by_name(name):
    with get_connection() as connection:
        return connection.execute(
            "SELECT id, name, age FROM students WHERE name = ?",
            (name,)
        ).fetchone()


def update_student_age(name, age):
    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE students SET age = ? WHERE name = ?",
            (age, name)
        )
        return cursor.rowcount > 0


def delete_student(name):
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM students WHERE name = ?",
            (name,)
        )
        return cursor.rowcount > 0


if __name__ == "__main__":
    create_table()

    for student in get_all_students():
        print(dict(student))



# What you just built
# - sqlite3.connect() opens a connection to the database.
# - students.db stores your data on disk.
# - CREATE TABLE IF NOT EXISTS creates the table without recreating it every time.
# - PRIMARY KEY AUTOINCREMENT gives each student a unique ID.
# - UNIQUE prevents duplicate student names at the database level.
# - CHECK (age >= 1) prevents invalid ages from being stored.