from cmath import sqrt
import random

def arthmetic():
    print("Enter two elements")
    num1=int(input())
    num2=int(input())
    sum=num1+num2
    print("Sum are:",sum)
    product=num1*num2
    print("Product are:",product)
    division=num1/num2
    print("Division are:",division)
    substraction=num1-num2
    print("Substraction are:",substraction)


def triangle():
    print("Question 3")
    print("Enter base of triangle")
    base=int(input())
    print("Enter the height")
    height=int(input())
    area=base*height/2
    print("Area of triangle are:",area)

def quadratic():
    print("Enter three elements:")
    a=int(input())
    b=int(input())
    c=int(input())
    delta=int(b**2-4*a*c)
    print("Delta=",delta)
    x1=-b+sqrt(delta)/2*a
    x2=-b-sqrt(delta)/2*a
    if delta>0:
        print("Value of x are:",x1,x2)
    elif delta<0:
        print("Null")
    elif delta==0:
        print("Value of x1 and x2 are:",-b/2*a) 

def swapping():
    print("Enter numbers before swap:")
    a=int(input())
    b=int(input())
    print("Numbers before swap:",a,b)
    a=a+b
    b=a-b
    a=a-b
    print("The numbers after swap are:",a,b)

def random():
    print(random.randint(0,100))
    
               



    
