
import random


def get_guess():
    """Get a valid integer guess from the player."""
    while True:
        try:
            guess = int(input("Guess a number (1-50): "))
            if 1 <= guess <= 50:
                return guess
            print("Enter a number between 1 and 50.")
        except ValueError:
            print("Invalid input! Enter a number, not letters.")


def check_guess(guess, secret_number):
    """Compare the guess with the secret number."""
    if guess < secret_number:
        return "too low"
    elif guess > secret_number:
        return "too high"
    else:
        return "correct"


def play_round(secret_number):
    """Run one round and allow up to 7 valid guesses."""
    attempts = 0
    max_attempts = 7

    while attempts < max_attempts:
        guess = get_guess()
        attempts += 1

        result = check_guess(guess, secret_number)

        if result == "correct":
            print(f"Correct! You won in {attempts} attempts.")
            return

        print(f"Too {result}! Attempts left: {max_attempts - attempts}")

    print(f"You lost! The number was {secret_number}.")


def main():
    """Start the game with a randomly generated number."""
    secret_number = random.randint(1, 50)
    play_round(secret_number)


if __name__ == "__main__":
    main()
