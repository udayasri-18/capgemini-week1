import random

def number_guessing_game():
    target = random.randint(1, 100)
    attempts = 0
    print("Guess the number (between 1 and 100):")

    while True:
        num = input("Enter your guess: ")
        if num.isdigit():
            num = int(num)
            attempts += 1
            if num < target:
                print("Too Low! Try again.")
            elif num > target:
                print("Too High! Try again.")
            else:
                print(f"Congratulations! You guessed it right in {attempts} attempts. The number was {target}.")
                break
        else:
            print("Invalid input! Please enter a number.")


number_guessing_game()
