# Rock, Paper, Scissors Game

Rock paper scissors is an intransitive hand game, usually played between two people, in which each player simultaneously forms one of three shapes with an outstretched hand. 

These shapes are "rock" (a closed fist), "paper" (a flat hand), and "scissors" (a fist with the index finger and middle finger extended, forming a V). 

A simultaneous, zero-sum game, it has three possible outcomes: a draw, a win or a loss. A player who decides to play rock will beat another player who has chosen scissors ("rock crushes scissors" or "breaks scissors" or sometimes "blunts scissors"), but will lose to one who has played paper ("paper covers rock"); a play of paper will lose to a play of scissors ("scissors cuts paper"). If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie.

The code below how you can use python to play the rock, paper, scissor game.

```
import random

def play_game():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("Enter your choice (rock/paper/scissors): ")
    print("You chose:", player_choice)
    print("Computer chose:", computer_choice)
    if player_choice == computer_choice:
        print("It's a tie!")
    elif player_choice == "rock" and computer_choice == "scissors":
        print("You win!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("You win!")
    elif player_choice == "scissors" and computer_choice == "paper":
        print("You win!")
    else:
        print("Computer wins!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break

```

This code uses the random module to randomly choose the computer's choice from a list of choices (rock, paper, scissors), and prompts the player to enter their choice. It then compares the two choices to determine the winner, and prompts the player if they want to play again.