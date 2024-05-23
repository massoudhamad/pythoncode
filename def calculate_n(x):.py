def calculate_n(x):
    if x == 0:
        return None  # Stop the algorithm if x = 0
    
    try:
        n = (x * x) / (1 - x)  # Calculate n
        return n
    except ZeroDivisionError:
        return None  # Handle the error condition if 1 - x = 0


def main():
    while True:
        x = float(input("Enter a value for x: "))
        
        n = calculate_n(x)
        if n is None:
            break  # Stop the algorithm if x = 0 or error condition
        
        print(f"n = {n}")
        print(f"x = {x}")
        print()
        

if __name__ == "__main__":
    main()