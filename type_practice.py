
def get_student_count(students: list[dict]) -> int:
    return len(students)

count = get_student_count([{"name": "Tobi", "score": 90}])
# count = get_student_count("four")
#This was used to test mypy being able to detect the mismatch in required type

