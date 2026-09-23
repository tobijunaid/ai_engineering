from pathlib import Path

current_dir = Path(__file__).parent
file_path = current_dir / "students.txt"
result_path = current_dir / "results.txt"

def save_results(name, score):
    if score >= 80:
        print(f"{name} scored more than 80: {score}")
        with open(result_path, "a") as file :
                file.write(f"{name},{score}\n")

        # Alternative way to do it without unpacking
        # name = line.strip().split(",")[0]
        # score = int(line.strip().split(",")[1])
        # print(f"{name} scored: {score}")
        
def read_students():
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    for line in lines:
        name, score = line.strip().split(",")
        score = int(score)
        print(f"{name} scored: {score}")
        save_results(name, score)

def main():
    with open(result_path, "w") as file:
        pass  # Clear the results file before writing new results
    read_students()
    
if __name__ == "__main__":
    main()