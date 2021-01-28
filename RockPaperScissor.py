import random
import sys


# computer generates a random move
def generate_move():
    move_array = ["rock", "paper", "scissor"]
    return move_array[random.randint(0, 2)]


# verifies that the user entered a valid move
def verify_move(this):
    if this == "rock" or this == "paper" or this == "scissor":
        return this
    else:
        sys.exit("Invalid input. Try again")


# takes both moves and determines the winner
def calculate_winner(player_move, opponent_move):
    if (player_move == "rock" and opponent_move == "scissor") or \
            (player_move == "scissor" and opponent_move == "paper") or \
            (player_move == "paper" and opponent_move == "rock"):
        return print("The winner is player 1!")
    elif player_move == opponent_move:
        return print("It's a tie!")
    else:
        return print("The winner is player 2!")


# runs the game
print("Rock, Paper, Scissor... Go!")
player_move = verify_move(input("Enter your move: ").lower())
opponent_move = generate_move()
print("\nPlayer 1: " + player_move)
print("Player 2: " + opponent_move)
calculate_winner(player_move, opponent_move)
