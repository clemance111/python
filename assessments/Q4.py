from cmath import sqrt


print("Enter three elements:")
a=int(input())
b=int(input())
c=int(input())
delta=b*b-4*a*c
print("Delta=",delta)
x1=-b+sqrt(delta)/2*a
x2=-b-sqrt(delta)/2*a
if delta>0:
    print("Value of x are:",x1,x2)
elif delta<0:
        print("Null")
elif delta==0:
           print("Value of x1 and x2 are:",-b/2*a)        
