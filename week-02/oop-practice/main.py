class Student: #Class
    #Constructor method to initialize the attributes of the Student class
    def __init__(self, name, age, department, score): #Constructor
        self.name = name
        self.age = age
        self.department = department
        self.score = score

    #Method to return a string representation of the Student object
    def __str__(self):
        return f"{self.name}, {self.age}, {self.department}, {self.score}"

    #Method to introduce the student and print their details
    def introduce(self): 
        print(f"Hi, my name is {self.name}. I am {self.age} years old and I study {self.department}. My score is {self.score}.")

    def check_result(self):
        if self.score >= 70:
            print(f"{self.name} has passed with a score of {self.score}.")
        else:
            print(f"{self.name} has failed with a score of {self.score}.")
    
    def get_grade(self):
        if self.score >=70:
            return "A"
        elif self.score >= 60 and self.score < 70:
            return "B"
        elif self.score >= 50 and self.score < 60:
            return "C"
        elif self.score >= 45 and self.score < 50:
            return "D" 
        else:
            return "F"
    
    def is_distinction(self):
        if self.score >=80:
            return True
        else:
            return False
    
student1 = Student("Tobi", 23, "Computer Engineering", 90) #Object
student2 = Student("David", 24, "Computer Science", 85)
student3 = Student("Sarah", 22, "Electrical Engineering", 68)
student4 = Student("John", 25, "Mechanical Engineering", 40)

students = [student1, student2, student3, student4]

for student in students:
    student.introduce()
    student.check_result()
    print(f"Grade: {student.get_grade()}")
    print("---")

    if student.is_distinction():
        print(f"{student.name} achieved distinction!\n") 




# student1.introduce()  # Output: Hi, my name is Tobi. I am 23 years old and I study Computer Engineering. My score is 90.
# student2.introduce()  # Output: Hi, my name is David. I am 24 years old and I study Computer Science. My score is 85.
# student3.introduce()  # Output: Hi, my name is Sarah. I am 22 years old and I study Electrical Engineering. My score is 68.
# student4.introduce()  # Output: Hi, my name is John. I am 25 years old and I study Mechanical Engineering. My score is 40.
# student1.check_result()  # Output: Tobi has passed with a score of 90.
# student2.check_result()  # Output: David has passed with a score of 85.
# student3.check_result()  # Output: Sarah has failed with a score of 57.
# student4.check_result()  # Output: John has failed with a score of 45.
# print(f"{student1.name}'s grade is {student1.get_grade()}.")  # Output: Tobi's grade is A.
# print(f"{student2.name}'s grade is {student2.get_grade()}.")  # Output: David's grade is A.
# print(f"{student3.name}'s grade is {student3.get_grade()}.")  # Output: Sarah's grade is C.
# print(f"{student4.name}'s grade is {student4.get_grade()}.")  # Output: John's grade is F.