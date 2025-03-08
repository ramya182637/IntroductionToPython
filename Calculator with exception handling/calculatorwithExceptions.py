import logging

# Seting up logging to log errors to 'error_log.txt'
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    while True:
        print("\nWelcome to the Error-Free Calculator!")
        print("Choose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        
        try:
            choice = int(input("> "))
            
            if choice == 5:
                print("Goodbye!")
                break
            
            if choice not in [1, 2, 3, 4]:
                print("Invalid choice! Please select a valid option.")
                continue

            # Getting the numbers for the selected operation
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            # Performing the selected operation
            if choice == 1:
                result = add(num1, num2)
                print(f"The result of {num1} + {num2} is {result}.")
            elif choice == 2:
                result = subtract(num1, num2)
                print(f"The result of {num1} - {num2} is {result}.")
            elif choice == 3:
                result = multiply(num1, num2)
                print(f"The result of {num1} * {num2} is {result}.")
            elif choice == 4:
                try:
                    result = divide(num1, num2)
                    print(f"The result of {num1} / {num2} is {result}.")
                except ZeroDivisionError as e:
                    print("Oops! Division by zero is not allowed.")
                    logging.error(f"ZeroDivisionError occurred: {e}")
                except Exception as e:
                    print("An unexpected error occurred.")
                    logging.error(f"Unexpected error occurred: {e}")

        except Exception as e:
            print("An error occurred with your selection. Please try again.")
            logging.error(f"Error: {e}")
        
        finally:
            print("Thank you for using the calculator!")

if __name__ == "__main__":
    main()
