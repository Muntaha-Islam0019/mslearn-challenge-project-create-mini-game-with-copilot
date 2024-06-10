# Create a Rock, Paper, Scissors game where the user plays against the computer.
# Rock beats scissors.
# Scissors beat paper.
# Paper beats rock.
# The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
# At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
# The computer can randomly choose one of the elements (rock, paper, or scissors) for each move, just like the user.
# By the end of each round, the player can choose whether to play again.
# Display the player's score at the end of the game.
# The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random


def get_user_choice():
    print("\nPlease choose one of the following options: rock, paper, or scissors.")
    user_choice = input().lower()
    while user_choice not in ["rock", "paper", "scissors"]:
        print(
            "Invalid option. Please choose one of the following options: rock, paper, or scissors."
        )
        user_choice = input().lower()
    return user_choice


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"


def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose {user_choice}, computer chose {computer_choice}.")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "user":
            print("You win this round!")
            user_score += 1
        elif winner == "computer":
            print("Computer wins this round!")
            computer_score += 1
        else:
            print("It's a tie!")
        print(f"Score: You - {user_score}, Computer - {computer_score}")
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        while play_again not in ["yes", "no"]:
            print("Invalid option. Please choose yes or no.")
            play_again = input().lower()
        if play_again != "yes":
            break


play_game()
