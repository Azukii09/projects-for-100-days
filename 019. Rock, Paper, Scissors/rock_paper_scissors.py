from random import choice

def win_condition(option, player):
    if option[0] == option[1]:
        print("")
        print(f"You chose {option[1]}, computer chose {option[0]}.")
        return f"You both chose the same thing! The result is a tie"
    elif "rock" in option and "scissors" in option:
        l_index = option.index("rock")
        print(f"You chose {option[1]}, computer chose {option[0]}.")
        return f"Rock beats scissors! The result is a {player[l_index]} win"
    elif "rock" in option and "paper" in option:
        l_index = option.index("paper")
        print(f"You chose {option[1]}, computer chose {option[0]}.")
        return f"Paper beats rock! The result is a {player[l_index]} win"
    elif "paper" in option and "scissors" in option:
        l_index = option.index("scissors")
        print(f"You chose {option[1]}, computer chose {option[0]}.")
        return f"Scissors beats paper! The result is a {player[l_index]} win"
    else:
        return f"Please input according to the available options (rock, paper, scissors)!"

options = ['rock', 'paper', 'scissors']
while True:
    computer_choose = choice(options)
    user_input = input("Enter a choice (rock, paper, scissors): ")
    print("")
    print(win_condition([computer_choose,user_input],["Computer","You"]))
    print("")

    check = input("Play again (Y/N)? ")
    if check.lower() == 'y':
        continue
    else:
        print("")
        print("Thank you for playing!")
        break


