from calendar import c
from unicodedata import name

#CLASS DEFINITION SIMPLE EXAMPLE

class First:
    name=str(input("Enter your name:"))
    age=int(input("Enter the age:"))

a=First()
print("My name is:",a.name,"My age are:",a.age) 

class Number:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter the second number:"))

    sum=num1+num2
obj=Number()
print("The sum of two numbers are:",obj.sum)  

#IMPORTANCE OF INIT FUNCTION

class person:
    firstname=None
    lastname=None
    age=0
    def __init__(self,fname,lname,age):
        self.firstname=fname
        self.lastname=lname
        self.age=age

obj=person("shema","cedrick",10)
fullname=obj.firstname + obj.lastname
print(fullname)    

#IMPORTANCE OF STR FUNCTION

class Second:
    def __str__(self):
        return "hello"

a=Second()
print(a)


class Third():
    pass
b=Third()
print(b)
  