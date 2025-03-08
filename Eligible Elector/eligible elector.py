while True:
    try:
        age = int(input("How old are you? "))  # Try converting the input to an integer
        if age < 0:
            print("Please enter a positive number for age.")
        else:
            break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")

# Now, age is guaranteed to be a non-negative integer
if age > 18:
    print("Congratulations! You are eligible to vote. Go make a difference!")
else:
    X = 18 - age
    print(f"Oops! You’re not eligible yet. But hey, only {X} more years to go!")
