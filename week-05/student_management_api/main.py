from os import name

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field

students = []
app = FastAPI()

# You've now covered:
# - HTTP GET and POST routes.
# - Path and query parameters.
# - Pydantic request models.
# - Required fields and type validation.
# - Numeric constraints with ge.
# - String constraints with min_length.
# - Testing valid and invalid requests using Swagger UI.
class Student(BaseModel): #BaseModel provides data validation.
    name: str = Field(..., min_length=2, description="Name must have 2 or more characters") #name: str means the student's name should be a string.
    age: int = Field(..., ge=1, description="Age must be greater than zero") #age: int means the age should be an integer.

class StudentResponse(BaseModel):
    message: str
    name: str
    age: int



def get_app_name():
    return "Student Management API"

def get_api_version():
    return "1.0.0"

# @app.post("/students") #Registers a route that responds to HTTP POST requests at /students.
# # @app.post("/students", status_code=201)
# def create_student(student: Student): #Defines the function FastAPI calls for that route. The student parameter is of type Student, which means FastAPI will automatically validate the incoming request data against the Student model.
#     return {"message": "Student registered successfully",
#             "name": student.name,
#             "age": student.age} # Returns a message confirming the creation of the student.

@app.post("/students", status_code=201, response_model=StudentResponse)
def student_response(student: Student):
    students.append(student)
    return {
        "message": "Student record", 
            "name": student.name,
            "age": student.age
            }


@app.get("/students", response_model=list[StudentResponse])
def get_student():
    return [
        {
            "message": "Student record",
            "name": student.name,
            "age": student.age
        }
        for student in students
    ]
    
@app.get("/students/{name}", response_model=StudentResponse)
def get_student_by_name(name: str):
    for student in students:
        if student.name == name:
            return {
                "message": "Student record",
                "name": student.name,
                "age": student.age
            }
    raise HTTPException(status_code=404, detail="Student 'Unknown' not found")


class StudentRequest(BaseModel):
    age: int = Field(..., ge=1, description="Age must be greater than zero")
    

@app.put("/students/{name}", response_model=StudentResponse)
def update_student(name: str, updated_student: StudentRequest):
    for student in students:
        if student.name == name:
            student.age = updated_student.age
            return {
                "message": "Student record updated",
                "name": student.name,
                "age": student.age
            }
    raise HTTPException(
        status_code=404,
        detail=f"Student '{name}' not found"
    )

# A useful lesson for your backend journey
# This is exactly why response models matter. 
# They help your API enforce a consistent output structure,
# but you must ensure that the data your function returns actually matches that structure.
# Make that one change and let me know what you get!

@app.get("/info")
def get_info(app_name: str = Depends(get_app_name), 
            version: str = Depends(get_api_version)):
    return {"app_name": app_name,
            "version": version}

@app.get("/status")
def get_status(version: str = Depends(get_api_version)):
    return {"status": "API is running", "version": version}

@app.get("/version")
def get_version(app_version: str = Depends(get_api_version)):
    return {"version": app_version}