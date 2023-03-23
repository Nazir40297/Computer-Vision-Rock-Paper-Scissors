import random

def get_computer_choice():
    rps = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(rps)
    return computer_choice

def get_user_choice():
    rps = ['rock', 'paper', 'scissors']
    user_choice = input("Pick an option between rock, paper or scissors...\n")
    user_choice.lower()
    if user_choice in rps:
        return user_choice
    else:
        print("Not an available option. Please try again")

def get_winner(computer_choice, user_choice):
    if user_choice == 'rock' and computer_choice == 'rock':
        print("It is a tie!")
    elif user_choice == 'rock' and computer_choice == 'paper':
        print("You lost!")
    elif user_choice == 'rock' and computer_choice == 'scissors':
        print("You won!")
    elif user_choice == 'scissors' and computer_choice == 'rock':
        print("You lost!")
    elif user_choice == 'scissors' and computer_choice == 'paper':
        print("You won!")
    elif user_choice == 'scissors' and computer_choice == 'scissors':
        print("It is a tie!")
    elif user_choice == 'paper' and computer_choice == 'rock':
        print("You won!")
    elif user_choice == 'paper' and computer_choice == 'paper':
        print("It is a tie!")
    elif user_choice == 'paper' and computer_choice == 'scissors':
        print("You lost!")

def play():
    computer_choice = get_computer_choice()
    user_choice = get_user_choice()
    get_winner(computer_choice, user_choice)

play()
    