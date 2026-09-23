from pathlib import Path

# Gets the directory where main.py lives
current_dir = Path(__file__).parent
file_path = current_dir / "students.txt"


with open(file_path, "r") as file:
    # content = file.read()
    lines = file.readlines()
    
    for line in lines:
        # print(line.strip().split(","))
        name, score = line.strip().split(",")
        score = int(score)
        print(f"{name} scored: {score}")
        
        if score >= 80:
            print(f"{name} scored more than 80: {score}")
        
        # Alternative way to do it without unpacking
        # name = line.strip().split(",")[0]
        # score = int(line.strip().split(",")[1])
        # print(f"{name} scored: {score}")