# a,b,c=eval(input("Enter three numbers:"))
# if(a>b):
#     if(a>c):
#         print(a)
#     else:
#         print(c)
# else:
#     if(b>c):
#         print(b)
#     else:
#         print(c)

day=int(input("Enter the day number:"))
match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day number")