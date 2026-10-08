from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir / "names.txt"

with open(file_path, "r") as file:
    lines = file.readlines()
    

def display_names():
    for line in lines:
        name = line.strip()
        print (f"Hello {name}")

display_names()