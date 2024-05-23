l=[3,5,8,"Omar"]
""" print(l[0]) #3
print(l[3]) #Omar
print(len(l)) """

""" for x in l:
    print(x) """

""" l.append(6)

for x in range(len(l)):
    print(x,"\t",l[x]) """
    
    
""" s= "I <3 cs"
print(list(s))
re="BITA/7/23/001/TZ"
list(re)
print(re.split("/"))
print(''.join(re)) """

months=["Jan","Feb","Mar","Dec"]
rainfall = []
for m in range(len(months)):
    rain=input("Enter your rainfall for the month "+months[m]+": ")
    rainfall.extend(int(rain))
max=rainfall[0]
min=rainfall[0]
for x in rainfall:
    print(x)
    

