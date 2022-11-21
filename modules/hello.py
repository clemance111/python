import calendar

def hello():
    print("hello python")

def miles():
    kilometers = float(input("Enter value in kilometers: "))
    conv_fac = 0.621371
    miles = kilometers * conv_fac
    print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))
    
def celsius():
    celsius = 37.5
    fahrenheit = (celsius * 1.8) + 32
    print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

def calend():
    yy = int(input("Enter a year:"))
    mm = int(input("Enter a month:"))
    print(calendar.month(yy,mm))    

def check():
    print("Enter number to check:")
    number=int(input())
    if number>0:
        print("Number is positive")
    elif number<0:
        print("Number is negative") 
    elif number==0:
        print("Number is zero")
               
    