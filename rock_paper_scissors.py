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
