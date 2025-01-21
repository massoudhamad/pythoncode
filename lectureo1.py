#marks=30
marks=int(input("Enter the marks:"))
if(marks>100 or marks<0):
    print("Invalid marks")
else:
    if(marks>=80):
        print("A")
    elif(marks>=60):
        print("B")  
    elif(marks>=50):
        print("C")
    elif(marks>=40):
        print("D")
    else:
        print("F")


# if(marks>=40):
#     print("pass")
#     print("good")
# else:
#     print("fail")
#     print("bad")
# print("This is testing")


