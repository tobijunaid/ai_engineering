from pathlib import Path
import json
import csv

current_dir = Path(__file__).parent

def read_student():
    csv_path = current_dir / "students.csv"
    students = []  # This is our list
    
    with open(csv_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        
        for row in reader:# Changed 'students' to 'row' here
            if int(row["score"]) >= 80:
                student = {
                    "name": row["name"],
                    "score": int(row["score"]),
                    "department": row["department"]
                }
                students.append(student)  # Now it successfully appends to the list
            
    return students  # Returns the full list of students

def save_student():
    student_list = read_student()
    json_path = current_dir / "new_student.json"
    
    with open(json_path, "w", encoding="utf-8") as file:
        json.dump(student_list, file, indent=4)
        
    print(f"Student saved to {json_path}")

save_student()