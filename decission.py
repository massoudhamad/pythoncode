"""x=1
if(x>=4):
    print(x)
    print(2)
else:
    print(x)
    print("this is SUZA under else condition")
print(3)"""
#Question2
"""
l1=int(input("Enter length of R1: "))
w1=int(input("Enter width of R1: "))
l2=int(input("Enter length of R2: "))
w2=int(input("Enter width of R2: "))

rect1=l1*w1
rect2=l2*w2
print("Rect 1 area is ",rect1)
print("Rect 2 area is ",rect2)
if(rect1>=rect2):
    print("Rectangle 1 is greater than Rectangle 2")
else:
    print("Rectangle 2 is greater than Rectangle 1")
    """
marks= int(input("Enter your marks: "))
if(marks>100 or marks<0):
    print("marks is out of range")
else: 
    if(marks>=80):
        print("A\t\tExcellent")
    elif(marks>=70):
       print("B+\t\tVery Good")
    elif(marks>=60):
        print("B\t\tGood")
    elif(marks>=50):
        print("C\t\tPoor")
    else:
        print("F\t\tFail\t\tLazy")

#nested condition
"""a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))
c=int(input("Enter value of c: "))
if(a>b):
    if(a>c):
        print(a," is a maximum number")
    else: 
        print(c," is a muximum number")
else:
    if(b>c):
        print(b," is a maximum number")
    else:
        print(c," is a maximum number")
        """
    