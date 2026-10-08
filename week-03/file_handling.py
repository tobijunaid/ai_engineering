from pathlib import Path
import csv

current_dir = Path(__file__).parent
file_path1 = current_dir / "names.txt"
file_path2 = current_dir / "students.csv"

with open(file_path1, "r") as file:
    lines = file.readlines()

def check_file_exists():
    if file_path1.exists():
        print(f"File exists.")
    else:
        print(f"File does not exist.")

with open(file_path2, "r") as file:
    reader = csv.DictReader(file)
    
def display_students():
    for student in reader:
        print(f"Name: {student['name']}, Score: {student['score']}, Department: {student['department']}")
        

def display_names():
    for line in lines:
        name = line.strip()
        print (f"Hello {name}")

check_file_exists()
display_names()
display_students