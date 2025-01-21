# for name in ['fathiya','asya','hudhaima','fathiya']:
#     print(name)
    
# for x in [1,2,3,4,5]:
#     print("The value of x: ",x);

# for x in range(1,100):
#     if(x%2==0):
#         print(x,end=" ")

#this program uses a loop to dispaly a tbale of number and their squares

#get the starting values
'''print('This program displays a list of number')
print('and their squares. ')

start = int(input('enter the starting number'))
end = int(input('how high shoud I go'))
print()
print("Number\tSquare")
print("-----------")
for number in range(start,end+1):
    square = number**2;
    print(number,"\t",square)
    '''
# for num in range(10,0,-1):
#     print(num,end=" ")

''' Conditional Loop'''

''' print the numbers from 1 to 10 using while loop'''
# number=1
# sum=0
# while(number<=1000):
#     #print(number)
#     sum=sum+number
#     #print(number,"\t",sum)
#     number=number+1
# print("The summation of numbers from 1-10 is: ",sum)

# print("Temp(C)\tFahrenheit")
# temp=0
# while(temp<=20):
#     f=(5/9)*temp+32
#     print(temp,"\t",f)
#     temp=temp+1


# n=1
# product=1
# while(n<=10):
#     product=product*n
#     n=n+1
# print("The product of number between 1-10 is",product)

day=1
totalbugs=0
while(day<=7):
    nbugs=int(input("Enter your bugs for day "+str(day)+":"))
    totalbugs=totalbugs+nbugs
    day=day+1
print("The total number of bugs collected are: ",totalbugs)

