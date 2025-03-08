import turtle

# Function to calculate the factorial of a number using recursion
def factorial(n):
    # Base case: factorial of 0 or 1 is 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial(n-1)
    return n * factorial(n - 1)

# Function to calculate the nth Fibonacci number using recursion
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: fibonacci(n-1) + fibonacci(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive function to draw a fractal tree using turtle
def draw_tree(t, length, angle, depth):
    if depth == 0:
        return
    # Draw the current branch
    t.forward(length)
    # Recursively draw the left subtree
    t.left(angle)
    draw_tree(t, length * 0.7, angle, depth - 1)
    # Go back to the previous branch position
    t.right(2 * angle)
    draw_tree(t, length * 0.7, angle, depth - 1)
    # Return to the original branch position
    t.left(angle)
    t.backward(length)

# Function to initialize and set up the turtle for drawing
def draw_fractal_tree():
    # Set up the screen and the turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)  # Set the turtle's speed to maximum
    t.left(90)  # Start facing upward

    # Set the starting position and draw the tree
    t.up()
    t.backward(100)
    t.down()
    draw_tree(t, 100, 30, 7)  # Start with branch length of 100, angle of 30 degrees, and depth of 7

    # Finish drawing
    turtle.done()

# Main function to display menu and handle user input
def main():
    while True:
        print("\nWelcome to the Recursive Artistry Program!")
        print("Choose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice, please enter a number between 1 and 4.")
            continue
        
        if choice == '1':
            # Factorial Function
            while True:
                try:
                    number = int(input("Enter a number to find its factorial: "))
                    if number < 0:
                        raise ValueError("Please enter a positive integer.")
                    print(f"The factorial of {number} is {factorial(number)}.")
                    break
                except ValueError as e:
                    print(f"Invalid input. {e}")
        
        elif choice == '2':
            # Fibonacci Function
            while True:
                try:
                    n = int(input("Enter the position of the Fibonacci number: "))
                    if n < 0:
                        raise ValueError("Please enter a non-negative integer.")
                    print(f"The {n}th Fibonacci number is {fibonacci(n)}.")
                    break
                except ValueError as e:
                    print(f"Invalid input. {e}")
        
        elif choice == '3':
            # Recursive Fractal Pattern (Tree)
            print("Drawing a simple fractal tree!")
            draw_fractal_tree()
        
        elif choice == '4':
            # Exit Program
            print("Goodbye! Thanks for using the Recursive Artistry Program.")
            break

# Run the main program
if __name__ == "__main__":
    main()
