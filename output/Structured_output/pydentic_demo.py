from pydantic import BaseModel
from typing import TypedDict

class Student(BaseModel):
    name :str
    age :int

new_student = {"name":"guru","age":"25"}

student = Student(**new_student)

print(student)