from turtle import width


class Rectangle:
    len=None #int(input("Enter the length of rectangle: "))
    height=None #int(input("Enter the width of rectangle: "))
    def __init__(self,length,h):
        self.len=length
        self.height=h
        area = length*h
        print("Area of rectangle are: ",area)

obj=Rectangle(6,9)



        