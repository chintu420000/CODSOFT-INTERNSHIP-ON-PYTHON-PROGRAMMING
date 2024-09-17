import random as rd


def print_choice(choice):
    if choice == 0:
        return "Rock"
    elif choice == 1:
        return "Paper"
    elif choice == 2:
        return "Scissor"
    return "Unknown"


def determine_winner(user_choice, computer_choice):
    global user_score, computer_score
    if user_choice == computer_choice:
        print(f"Match is a draw. Both chose {print_choice(user_choice)}.")
    elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
        print(f"User wins! User chose {print_choice(user_choice)} and Computer chose {print_choice(computer_choice)}.")
        user_score += 1
    else:
        print(
            f"Computer wins! User chose {print_choice(user_choice)} and Computer chose {print_choice(computer_choice)}.")
        computer_score += 1


def play_game():
    global user_score, computer_score

    Rock = '''✋'''
    Paper = '''✌️'''
    Scissor = '''✊'''

    game = [Rock, Paper, Scissor]

    while True:
        try:
            user_choice = int(input("Please select your choice [0.Rock, 1.Paper, 2.Scissor, 3.Exit]: "))
            if user_choice == 3:
                print("Exiting game...")
                break
            if user_choice < 0 or user_choice > 2:
                print("Invalid choice entered.")
                continue
            computer_choice = rd.randint(0, 2)
            print(f"You chose: {game[user_choice]}")
            print(f"Computer chose: {game[computer_choice]}")
            determine_winner(user_choice, computer_choice)
            print(f"Current Score -> User: {user_score}, Computer: {computer_score}\n")

        except ValueError:
            print("Invalid input. Please enter a number.")


user_score = 0
computer_score = 0
play_game()
