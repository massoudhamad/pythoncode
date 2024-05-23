def max_of_three(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

result = max_of_three(5, 10, 3)
print(result)

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

year = 2019
result = is_leap_year(year)
print(result)


x = 1
while x <= 20:
    print(x, end='\t' if x % 5 != 0 else '\n')
    x += 1
    

    sum_even = 0
    for num in range(1, 101):
        if num % 2 == 0:
            sum_even += num
    print(sum_even)