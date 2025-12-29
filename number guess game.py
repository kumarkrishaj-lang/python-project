import random

print("Welcome to Number Guessing Game!")
number = random.randint(1, 50)
attempts = 0

while True:
    try:
        guess = int(input("Guess a number between 1 and 50: "))
        attempts += 1

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
