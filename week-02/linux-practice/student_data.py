students = [
    {"name": "Tobi", "score": 90},
    {"name": "David", "score": 85},
    {"name": "Sarah", "score": 78},
    {"name": "John", "score": 92},
]

def print_student_score():
    for student in students:
        print(f"{student['name']} scored: {student['score']}")

def score_more_than_80():
    for student in students:
        if student["score"] >= 80:
            print(f"{student['name']} scored more than 80: {student['score']}")

def calculate_average_score():
    total_score = sum(student["score"] for student in students)
    average_score = total_score / len(students)
    return average_score

print_student_score()
score_more_than_80()
print(f"Average score: {calculate_average_score()}")