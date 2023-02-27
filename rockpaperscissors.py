import random

game = ['rock', 'paper', 'scissors']
user_choice = int(
    input("What is your choice? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game[user_choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose: {computer_choice}")
    print(game[computer_choice])

    if user_choice >= 3 or user_choice < 0:
        print("Invalid number, you lose!")
    elif user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
    while True:
            play_again = input('Would you like to quit?: (y) ')
            if play_again.lower() == 'y':
              print('Thank you for playing!')
            break