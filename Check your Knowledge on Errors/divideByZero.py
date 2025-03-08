try:
    number = float(input("Enter a number: "))
    
    # Trying to divide 100 by the number
    result = 100 / number
    print(f"100 divided by {number} is {result}")

except ZeroDivisionError:
    # Handling division by zero exception
    print("Oops! You cannot divide by zero.")
    
except ValueError:
    # Handling the invalid input (non-numeric input)
    print("Invalid input! Please enter a valid number.")
