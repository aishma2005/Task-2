import random
import time

def welcome():
    print("Welcome to the number guessing game!")
    time.sleep(0.5)

def get_player_name():
    print("May I have your name?")
    return input().strip()

def game():
    number_to_guess = random.randint(1, 200)
    attempts = 0
    
    while attempts < 6:
        try:
            guess = int(input("Guess the number between 1 and 200: "))
            attempts += 1

            if guess < 1 or guess > 200:
                print("Please enter a number between 1 and 200.")
                continue
            
            if guess < number_to_guess:
                print("Too low!")
            elif guess > number_to_guess:
                print("Too high!")
            else:
                break
            
            if attempts < 6:
                time.sleep(0.5)
                print("Try again!")

        except ValueError:
            print("That's not a valid number. Please try again.")
    
    if guess == number_to_guess:
        print(f"Congratulations, {player_name}! You guessed the number {number_to_guess} in {attempts} attempts.")
    else:
        print(f"Sorry, {player_name}. The number I was thinking of was {number_to_guess}.")

def play_again():
    while True:
        response = input("Do you want to play again? (yes/no): ").strip().lower()
        if response in {'yes', 'y'}:
            return True
        elif response in {'no', 'n'}:
            return False
        else:
            print("Please enter 'yes' or 'no'.")

welcome()
player_name = get_player_name()

while True:
    game()
    if not play_again():
        break

print("Thank you for playing!")
