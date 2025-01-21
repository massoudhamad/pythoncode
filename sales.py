# python program which enter sales per day for a week and display total sales for the week
'''sales = []
for day in range(1,8):
    dailysales=float(input("Enter sales for day {}: ".format(day)))
    sales.append(dailysales)
print(sales)

total=0
for sale in sales:
    total+=sale
print("Total sales for the week is: ", total)'''

def dailySales(dailysales):
    sales = []
    for day in range(1,8):
        sales.append(dailysales)
    return sales

def totalSales(sales):
    total = 0
    for sale in sales:
        total += sale
    return total

def main():
    sales = dailySales(100)
    print(sales)
    total = totalSales(sales)
    print("Total sales for the week is: ", total)

main()

    


    
