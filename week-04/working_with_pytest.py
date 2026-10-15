from student_utils import filter_students

students = [
    {"name": "Tobi", "score": 90},
    {"name": "David", "score": 85},
    {"name": "Sarah", "score": 78},
    {"name": "John", "score": 92},
]

def filter_students(students, minimum_score=80):
    filtered_students = []
    for student in students:
        if student["score"] >= minimum_score:
            filtered_students.append(student)
    return filtered_students
result = filter_students(students)

def test_filter_students():
    result = filter_students(students, 80)
    
    assert len(result) == 3

test_filter_students()