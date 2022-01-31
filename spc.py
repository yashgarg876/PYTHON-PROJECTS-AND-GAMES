import random


comp_win = 0
player_wins = 0



def Choose_option():
    user_choice = input("Choose Rock, Paper or Scissors: ")
    if user_choice in ["rock", "Rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["paper", "Paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["scissors", "Scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("try again")
        Choose_option()
    return user_choice


def Computer_option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    elif comp_choice == 3:
        comp_choice = "s"
    return comp_choice


while True:
    print("")
    user_choice = Choose_option()
    comp_choice = Computer_option()
    print("")

    if user_choice == "r":
        if comp_choice == "r":
            print("Computer chose: r. You Tied.")
        elif comp_choice == "p":
            print("Computer chose: p. You lose")
            comp_win += 1
        elif comp_choice == "s":
            print("Computer chose: s. You win")
            player_wins += 1

    elif user_choice == "p":
        if comp_choice == "p":
            print("Computer chose: p. You Tied.")
        elif comp_choice == "s":
            print("Computer chose: s. You lose")
            comp_win += 1
        elif comp_choice == "r":
            print("Computer chose: r. You win")
            player_wins += 1

    elif user_choice == "s":
        if comp_choice == "s":
            print("Computer chose: s. You Tied.")
        elif comp_choice == "r":
            print("Computer chose: r. You lose")
            comp_win += 1
        elif comp_choice == "p":
            print("Computer chose: p. You win")
            player_wins += 1

    print("")
    print("Player wins:"+str(player_wins))
    print("Computer wins:"+str(comp_win))
    print("")

    user_choice = input("Wanna play again? (y/n)")
    if user_choice in ["y"]:
        pass
    elif user_choice in ["n"]:
        break
    else:
        break
