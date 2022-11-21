def multiplication():
    num = int(input("Display multiplication table of? "))
    for i in range(1, 13):
        print(num, 'x', i, '=', num*i)

def fibonacci():
    nterms = int(input("How many terms? "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print("Fibonacci sequence upto",nterms,":")
        print(n1)

    else:
        print("Fibonacci sequence:")
    while count < nterms:
       print(n1)
       nth = n1 + n2
      
       n1 = n2
       n2 = nth
       count += 1        

def armstrong():
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
        if num == sum:
            print(num,"is an Armstrong number")
        else:
            print(num,"is not an Armstrong number")

def ainterval():
    lower = 100
    upper = 2000
    for num in range(lower, upper + 1):
        order = len(str(num))
        sum = 0
        temp = num
        while temp > 0:
            digit = temp % 10
            sum += digit ** order
            temp //= 10
            if num == sum:
                print(num)

def addition():
    print("Enter number")
    num=int(input())
    if num < 0:
        print("Enter a positive number")
    else:
        sum = 0
        while(num > 0):
            sum += num
            num -= 1
            print("The sum is", sum)
                
            
