'''
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if(a>b):
    if(a>c):
        print(f"{a} is the largest number")
    else:
        print(f"{c} is the largest number")
else:
    if(b>c):
        print(f"{b} is the largest number")
    else:
        print(f"{c} is the largest number")
'''
grade=int(input("Enter your grade: "))
if(grade>100 or grade<0):
    print("Invalid grade")
else:
    if(grade>=80):
        print("A")
    elif(grade>=60):
        print("B")
    elif(grade>=50):
        print("C")
    elif(grade>=40):
        print("D")
    else:
        print("F")