# Taking the user test mark and store it in the list using list comprehension.
marks = [int(input(f"Please enter your test{i+1} marks: ")) for i in range(3)]

# Calculating the average directly from the list
average = sum(marks) / 3

if average >= 80:
    print("A\nExcellent")
elif average >= 70:
    print("B+\nVery Good")
elif average >= 60:
    print("B\nGood")
elif average >= 50:
    print("C\nPass")
elif average >= 40:
    print("D\nPoor")
else:
    print("F\nFail\nLazy\nYou are not part of us")
