class Student:
    def __init__(self,student_id,student_name,student_class):
        self.student_id=student_id
        self.student_name=student_name
        self.student_class=student_class

obj=Student(19,"Cedrick","p5")
print(obj.__dict__)        

