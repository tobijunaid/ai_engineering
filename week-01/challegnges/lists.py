numbers = [10, 4, 7, 2, 15, 8]

def analyze_numbers(numbers):
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return {"largest": largest,
            "smallest": smallest, 
            "total_sum": total_sum, 
            "average": average}

results = analyze_numbers(numbers)
print(results["largest"])
print(results["smallest"])
print(results["total_sum"])
print(results["average"])


students = {
    "name": "Tobi Junaid",
    "department": "Computer Engineering",
    "level": 500,
    "skills": ["Python", "Git", "UI/UX"]
}
print(students)
print(students["skills"])

#Loop + Condition Challenge
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")