def check1():
    print("Enter number to check:")
    number=int(input())
    if number%2==0:
        print("Number is even")
    else:
        print("Number is odd")

def leap():
    year = int(input("Enter a year: "))
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))

    elif (year % 4 ==0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))

    else:
        print("{0} is not a leap year".format(year))

def prime():
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
            else:
                print(num,"is a prime number")
        else:
            print(num,"is not a prime number") 

def pinterval():
    lower = int(input("Enter lower range:"))
    upper = int(input("Enter higher range:"))
    print("Prime numbers between", lower, "and", upper, "are:")
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
                else:
                    print(num)  

def factorial():
    num = int(input("Enter a number: "))
    factorial = 1
    if num < 0:
        print("factorial of negative number does not exist")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1,num + 1):
            factorial = factorial*i
            print("The factorial of",num,"is",factorial)
                                     