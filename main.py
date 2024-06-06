# Write a game
# The game is called Rock, Paper Scissors
# The game will be played between the user and the computer
# The computer will randomly select one of the three options
# The user will be prompted to select one of the three options
# The winner will be determined based on the following rules:
# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock
# Print out in ascii art the winner of the game
# q to quit

import random
import pyfiglet

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
    while user_choice not in ['rock', 'paper', 'scissors', 'q']:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
    return user_choice

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "user"
    else:
        return "computer"

def fprint(message):
    print(pyfiglet.figlet_format(message))

def print_winner(winner):
    if winner == "user":
        fprint("You Win!")
    elif winner == "computer":
        fprint("You Lose!")
    else:
        fprint("It's a Tie!")

def play_game():
    while True:
        user_choice = get_user_choice()
        if user_choice == 'q':
            fprint("Thanks for playing!")
            break
        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        winner = determine_winner(user_choice, computer_choice)
        print_winner(winner)

if __name__ == "__main__":
    play_game()
