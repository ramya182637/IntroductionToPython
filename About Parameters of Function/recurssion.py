# Recursive function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive function to calculate nth Fibonacci number
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Enter the number to find factorial:")
num = int(input())  # Read number for factorial
print("Enter the number to find the fibonacci:")
fib_num = int(input())  # Read number for fibonacci
factorial_result = factorial(num)
fibonacci_result = fibonacci(fib_num)

print(f"Factorial of {num} is {factorial_result}. The {fib_num}th Fibonacci number is {fibonacci_result}.")
