"""
def miles(km):
    return km * 0.6214


def main():
    km = int(input("Enter your km: "))
    print(miles(km))


main()
"""


def estimator(feet, price):
    number_of_gallons = feet / 115
    hours_required = (feet * 8) / 115
    cost = number_of_gallons * price
    labor_charges = hours_required * 20

    print("number_of_gallons=", number_of_gallons)
    print("hours_required=", (feet * 8) / 115)
    print("cost=", number_of_gallons * price)
    print("labor_charges=", hours_required * 20)
    print("total_cost= ", cost + labor_charges)


def main():
    feet = int(input("Enter your feet: "))
    price = float(input("Enter your price: "))
    estimator(feet, price)


main()
