from pathlib import Path
import csv
import json

current_dir = Path(__file__).parent
file_path1 = current_dir / "names.txt"
file_path2 = current_dir / "students.csv"
file_path3 = current_dir / "students.json"
file_path4 = current_dir / "new_student.json"

with open(file_path1, "r") as file:
    lines = file.readlines()

def check_file_exists():
    if file_path1.exists():
        print(f"File exists.")
    else:
        print(f"File does not exist.")

def display_names():
    for line in lines:
        name = line.strip()
        print (f"Hello {name}")

def display_students():
    with open(file_path2, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for student in reader:
            print(
                f"Name: {student['name']}, "
                f"Score: {student['score']}, "
                f"Department: {student['department']}"
            )

def display_student_json():
    with open(file_path3, "r", encoding="utf-8") as file:
        students = json.load(file)
        
        for student in students:
            print(
                f"Name: {student['name']}\n"
                # f"Age: {student['age']}\n"
                f"Department: {student['department']}"
            )
            print()
student = {
    "name": "Tobi",
    "age": 23,
    "department": "Computer Engineering"
}

def save_student():
    with open (file_path4, "w", encoding = "utf-8") as file:
        json.dump(student, file, indent=4)
        
        print(f"Student saved to {file_path4}")
    

check_file_exists()
display_names()
display_students()
display_student_json()
save_student()