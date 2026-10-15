from typing import TypedDict


class Student(TypedDict):
    name: str
    score: int

def filter_students(students, minimum_score=80):
    filtered_students = []

    for student in students:
        if student["score"] >= minimum_score:
            filtered_students.append(student)

    return filtered_students

def get_student_count(students: list[Student]) -> int:
    return len(students)