import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I picked a number between 1 and 100.")

    while True:
        guess = input("Enter your guess: ").strip()

        if not guess.isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            break

def main():
    while True:
        play_game()
        again = input("Play again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Thanks for playing.")
            break

if __name__ == "__main__":
    main()