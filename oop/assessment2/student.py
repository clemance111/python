from tokenize import Name
from unicodedata import name


class Student:
    student_name=None
    marks=None
    def __init__(self,name,mark):
        self.student_name=name
        self.marks=mark
        print("Student name is:",name,"And marks are:",mark)

obj=Student("Cedrick",80)


