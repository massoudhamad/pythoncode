test1 = int(input("Please enter your test1 marks: "))
test2 = int(input("Please enter your test2 marks: "))
test3 = int(input("Please enter your test3 marks: "))
average=(test1+test2+test3)/3
if(average >= 80):
    print("A\nExcellent")
elif(average >= 70):
    print("B+\nVery Good")
elif(average >= 60):
    print("B\nGood")
elif(average >= 50):
    print("C\nPass")
elif(average >= 40):
    print("D\nPoor")
else:
    print("F\nFail\nLazy\nYou are not part of us")