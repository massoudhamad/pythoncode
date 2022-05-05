a = int(input("Please enter your first number: "))
b = int(input("Please enter your second number: "))
c = int(input("Please enter your third number: "))
if(a>b):
    if(a>c):
        print(a," is a maximum number")
    else:
        print(c," is a maximum number")
else:
    if(b>c):
        print(b," is a maximum number")
    else:
        print(c," is maximum number")
