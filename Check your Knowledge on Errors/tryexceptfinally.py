try:
    # Prompting user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Attempting to divide num1 by num2
    result = num1 / num2

except ZeroDivisionError:
    # Handling division by zero
    print("Oops! You cannot divide by zero.")

except ValueError:
    # Handling invalid input (non-numeric input)
    print("Invalid input! Please enter valid numbers.")

else:
    # This block executes if no exceptions occur
    print(f"The result is {result}.")

finally:
    # This block always executes, regardless of exceptions
    print("This block always executes.")
