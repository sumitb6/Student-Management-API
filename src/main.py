from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

api = FastAPI()

class Student(BaseModel):
    id: int
    name: str
    department: str
    semester: int
    cgpa: float

students: List[Student] = []

@api.get("/")
def index():
    return {"Message" : "Hello World"}

@api.get("/student")
def get_students():
    return students

@api.post("/student")
def add_student(student: Student):
    students.append(student)
    return students

@api.put("/student/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student.id == student_id:
            students[index] = updated_student
            return students
    return {"error": "Student Not Found"}

@api.delete("/student/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student.id == student_id:
            deleted = students.pop(index)
            return deleted
    
    return {"error": "Deletion error"}