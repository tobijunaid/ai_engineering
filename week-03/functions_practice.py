def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

numbers = [10, 20, 30, 40, 50]

print(calculate_average(numbers))

def greet (name, message="Welcome to Python"):
    print(f"Hello {name}, {message}")

greet("Tobi", "Keep learning")

def analyze_numbers(numbers):
    largest_num = max(numbers)
    smallest_num = min(numbers)
    total = sum(numbers)
    average = total / len(numbers)
    
    return {
        "largest": largest_num,
        "smallest": smallest_num,
        "total": total,
        "average": average
    }

print(analyze_numbers(numbers))
