import random as rd
from time import sleep

def games(user_choice,computer_choice,user_score,computer_score):
    if user_choice == 0 and computer_choice == 0:
        print()
        print(f"Here the User_choice:{user_choice},Here the Computer_choice:{computer_choice}")
        print("\n\t\t\t\t\"Match is Draw..\"")
        print(f"\nHere the User_score{user_score}\t\tHere the Computer_score{computer_score}")
    elif user_choice == 0 and computer_choice == 2:
        print()
        print(f"Here the User_choice:{user_choice}\t\tHere the Computer_choice:{computer_choice}")
        user_score=user_score+1
        print("\n\t\t\t\t\"user is winner..\"")
        print(f"\nHere the User_score{user_score}\t\tHere theComputer_score{computer_score}")
    elif user_choice == 0 and computer_choice == 1:
        print()
        print(f"Here the User_choice:{user_choice}\t\tHere the Computer_choice:{computer_choice}")
        computer_score=computer_score+1
        print("\n\t\t\t\t\"computer is the winner..\" ")
        print(f"\nHere the User_score:{user_score}\t\tHere the Computer_score:{computer_score}")

    elif user_choice == 1 and computer_choice == 1:
        print()
        print(f"Here the User_choice:{user_choice}\t\tHere the Computer_choice:{computer_choice}")
        print("\n\t\t\t\t\"match is Draw \"")
        print(f"\nHere the User_score:{user_score}\t\tHere the Computer_score:{computer_score}")

    elif user_choice == 1 and computer_choice == 0:
        print()
        print(f"Here the User_choice:{user_choice}\t\tHere the Computer_choice:{computer_choice}")
        print("\n\t\t\t\t\"User is winner..\"")
        user_score=user_score+1
        print(f"\nHere the User_score:{user_score}\t\tHere the Computer_score:{computer_score}")

    elif user_choice == 1 and computer_choice == 2:
        print()
        print(f"Here the User_choice:{user_choice}\t\tHere the Computer_choice:{computer_choice}")
        print("\n\t\t\t\t\"Computer is winner..\" ")
        computer_score=computer_score+1
        print(f"\nHere the User_score:{user_score}\t\tHere the Computer_score:{computer_score}")

    elif user_choice == 2 and computer_choice == 0:
        print()
        print(f"Here the User_choice:{user_choice}\t\tHere the Computer_choice:{computer_choice}")
        print("\n\t\t\t\t\"Computer is winner..\"")
        computer_score=computer_score+1
        print(f"\nHere the User_score:{user_score}\t\tHere the Computer_score:{computer_score}")

    elif user_choice == 2 and computer_choice == 1:
        print()
        print(f"Here the User_choice:{user_choice}\t\tHere the Computer_choice:{computer_choice}")
        print("\n\t\t\t\t\"user is winner...\" ")
        user_score=user_score+1
        print(f"\nHere the User_score:{user_score}\t\tHere the Computer_score:{computer_score}")

    elif user_choice == 2 and computer_choice == 2:
        print()
        print(f"Here the User_choice:{user_choice}\t\tHere the Computer_choice:{computer_choice}")
        print("\n\t\t\t\t\"match is Draw \"")
        print(f"\nHere the User_score:{user_score}\t\tHere the Computer_score:{computer_score}")
    return computer_score,user_score

choice='y'
computer_score = 0
user_score=0
while choice=="y" or choice=="Y":
    user_choice=int(input("Plz select your choice [0.Rock,1.Paper,2.Scissor]:"))
    Rock='''✋'''
    paper='''✌'''
    scissor='''✊'''
    if user_choice>2 or user_choice<0:
        print("your are invalid enter")
    else:
        game = [Rock, paper, scissor]
        print(game[user_choice],end=" ")
        if user_choice == 0:
            print("Rock\n")
        elif user_choice == 1:
            print("paper\n")
        elif user_choice == 2:
            print("scissor\n")
        computer_choice = rd.randint(0, 2)
        list = ["rock", "paper", "scissor"]
        print(game[computer_choice],end=" ")
        print(list[computer_choice],end="\n")

        a,b=games(user_choice,computer_choice,user_score,computer_score)

        sleep(.5)
        computer_score=a
        user_score=b
        choice=input("\nDo you want to continue..(y/n):\n")
        print()
        sleep(.5)
else:
    print(f"Users choice:{b}\t\tComputers choice:{a}\n")
    if a>b:
        print("\t\tComputer won the Match")
    elif b>a:
        print("\t\tHurray!...\n\t\tYou have won the Match..")
    else:
        print("\t\tIts a Draw... better luck next time")
