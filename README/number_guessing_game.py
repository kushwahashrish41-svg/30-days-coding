##Build a number-guessing game where the computer picks a number from 1 to 50 and the player has 7 tries, 
##with 'too high' or 'too low' hints. Use a while loop and a counter. 
##Test edge cases such as typing letters

import random

number = random.randint(1, 50)
attempts = 0
max_tries = 7

print("=== Number Guessing Game ===")
print("Guess a number between 1 and 50.")
print("You have 7 tries!")

while attempts < max_tries:
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if guess < 1 or guess > 50:
        print("Enter a number between 1 and 50.")
        continue

    attempts += 1

    if guess == number:
        print("Congratulations! You guessed it!")
        print("Attempts used:", attempts)
        break
    elif guess < number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")

    print("Tries left:", max_tries - attempts)

if attempts == max_tries and guess != number:
    print("Game over! The number was:", number)
