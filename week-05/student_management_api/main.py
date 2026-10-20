from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Student(BaseModel): #BaseModel provides data validation.
    name: str = Field(min_length=2) #name: str means the student's name should be a string.
    age: int = Field(..., ge=1, description="Age must be greater than zero") #age: int means the age should be an integer.

@app.post("/students") #Registers a route that responds to HTTP POST requests at /students.
def create_student(student: Student): #Defines the function FastAPI calls for that route. The student parameter is of type Student, which means FastAPI will automatically validate the incoming request data against the Student model.
    return {"message": "Student registered successfully",
            "name": student.name,
            "age": student.age} # Returns a message confirming the creation of the student.