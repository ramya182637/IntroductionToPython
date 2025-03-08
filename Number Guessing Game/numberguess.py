import random
number_to_guess = random.randint(1, 100)
attempts = 0
max_attempts = 10
while attempts < max_attempts:
    print("Enter the number you guessed (between 1 and 100): ", end="")
    n = int(input())
    attempts += 1

    if n > number_to_guess:
        print("Too high! Try again.")
    elif n < number_to_guess:
        print("Too low! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        break
else:
    print(f"Game over! Better luck next time! The number was {number_to_guess}.")
