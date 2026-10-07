numbers1 = [1, 2, 3, 4, 5]
squares = []
for number in numbers1:
    squares.append(number ** 2)
print(squares)


squares = [number ** 2 for number in numbers1]
print(squares)

numbers2 = [2, 4, 6, 8, 10]

doubled = []
for number in numbers2:
    doubled.append(number * 2)
print(doubled)

doubled = [number * 2 for number in numbers2]
print(doubled)

numbers3 = [1, 2, 3, 4, 5, 6]

squares = [number ** 2 for number in numbers3]
print(squares)

numbers = [3, 8, 11, 14, 17, 20, 25, 30]

even_numbers = [number for number in numbers if number % 2 == 0]
odd_numbers = [number for number in numbers if number % 2 != 0]
print(even_numbers)
print(odd_numbers)

students = [
    {"name": "Tobi", "score": 90},
    {"name": "David", "score": 85},
    {"name": "Sarah", "score": 78},
    {"name": "John", "score": 92},
    {"name": "Mike", "score": 65}
]

scores = {}

for student in students:
    scores[student["name"]] = student["score"]
print(scores)

scores = {
    student["name"]: student["score"]
    for student in students
}
print(scores)

top_students = {
    student["name"]: student["score"]
    for student in students
    if student["score"] >= 80
}
print(top_students)

passed_students = {
    student["name"]: student["score"]
    for student in students
    if student["score"] >= 70
}
print(passed_students)

def get_high_scores(students):
    high_score = {
        student["name"] : student["score"]
        for student in students
        if student["score"] >= 80
    }
    return high_score

print(get_high_scores(students))