# def generate_numbers():
#     yield 1
#     yield 2
#     yield 3

# numbers = generate_numbers()

# print(next(numbers))
# print(next(numbers))
# print(next(numbers))

# def generate_even_number(n):
#     even_numbers = [number for number in range(2,n+1) if number % 2 == 0]
#     yield even_numbers

#for number in generate_even_numbers(10):
# print(number)

def generate_even_numbers(n):
    for number in range(2,n+1) :
        if number % 2 == 0:
            yield number

print(list(generate_even_numbers(10)))

students = [
    {"name": "Tobi", "score": 90},
    {"name": "David", "score": 65},
    {"name": "Sarah", "score": 85},
    {"name": "John", "score": 72}
]

def generate_high_scores(students):
    for student in students:
        if student["score"] >= 80:
            yield student

for student in generate_high_scores(students):
    print(student)

#In List Comprehension but prints as list
high_scores = [
    student
    for student in students
    if student["score"] >= 80
]

print(high_scores)