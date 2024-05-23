"""for i in range(1,1001,1):
    print(i)"""
"""mysales = [3,5,1,4,1,5,1,3,4,2]
for i in mysales:
    print(i)"""

""" sum=0
for i in range(1,10):
    if i%2 == 0:
        print(i)
        sum = sum+i
print("Total Sum is ",sum) """

""" my_data=[3,6,7,19]
for i in my_data:
    print(i) """
    
#while loop
""" 1-100 """
"""i=1
while(i>=1):
    print(i)
    i=i+2
    """
""" def convert(celcius):
    return 1.8*celcius+32

def main():
    print("Celcius\t\t\tFahrenheit")
    for i in range(0,21):
        print(i,"\t\t\t",convert(i))
main() """

"""def summation(number):
    sum=0
    for i in range(1,number+1):
        sum+=i #sum=sum+i
    print("Summation of the number is: ",sum)

def main():
    number=int(input("Enter your number: "))
    summation(number)
main()"""

#sentinel value
"""def grade(score):
    if(score<0 or score >100):
        return "Invalid Marks"
    else:
        if(score>70):
            return "A"
        elif(score>60):
            return "B+"
        elif(score>50):
            return "B"
        elif(score>40):
            return "C"
        else:
            return "F"
    
def calculateGrade(marks):
    while marks != -1 :
        print(grade(marks))
        marks=int(input("Enter your marks: "))

def main():
    score=int(input("Enter your marks: "))
    calculateGrade(score)

main()"""

#break and continue
"""for i in range(1,10):
    if i==5:
        break
    print(i)
"""
"""for i in range(1,10):
    if i==5:
        continue
    print(i)"""

"""i=1
while(i<=10):
    if i==5:
        continue
    print(i)
    i=i+1"""
    
#nested loop
""" for h in range(0,24):
    for m in range(0,60):
        for s in range(0,60):
            print(h,":",m,":",s)  """

def calculate_grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

def main():
    # Get the number of students
    while True:
        try:
            num_students = int(input("Enter the number of students in the class: "))
            if num_students > 0:
                break
            else:
                print("Please enter a positive number of students.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    total_class_score = 0

    # Loop through each student
    for student in range(1, num_students + 1):
        while True:
            try:
                # Get the test score for each student
                score = float(input(f"Enter the test score for student {student}: "))
                if score >= 0:
                    break
                else:
                    print("Please enter a positive test score.")
            except ValueError:
                print("Invalid input. Please enter a valid test score.")

        # Calculate and display the grade for each student
        grade = calculate_grade(score)
        print(f"Grade for student {student}: {grade}")

        # Accumulate the score for class average
        total_class_score += score

    # Calculate and display the overall class average
    class_average = total_class_score / num_students
    print(f"\nOverall class average: {class_average:.2f}")

if __name__ == "__main__":
    main()  
        


    
        


    