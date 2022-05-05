import math
a = int(input("Please enter your first number: "))
b = int(input("Please enter your second number: "))
c = int(input("Please enter your third number: "))
#ax2+bx+c=0
if(a==0):
    x=-c/b
    print("The value of x: ",x)
elif(((b**2)-(4*a*c))==0):
    x=-b/(2*a)
    print("The value of x is: ",x)
elif(((b**2)-(4*a*c))>0):
    x1=(-b+math.sqrt((b**2)-(4*a*c)))/(2*a)
    x2=(-b-math.sqrt((b**2)-(4*a*c)))/(2*a)
    print("The value of x1: ",x1," and the value of x2 is: ",x2)
else:
    print("Imaginary Root")