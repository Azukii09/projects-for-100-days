#import package
from random import choice

#define function for determine winner
def win_condition(option, player):
    #if result tie
    if option[0] == option[1]:
        print("")
        print(f"You chose {option[1]}, computer chose {option[0]}.")
        return f"You both chose the same thing! The result is a tie"
    #if rock and scissors in option, rock win
    elif "rock" in option and "scissors" in option:
        l_index = option.index("rock")
        print(f"You chose {option[1]}, computer chose {option[0]}.")
        return f"Rock beats scissors! The result is a {player[l_index]} win"
    #if rock and paper in option, paper win
    elif "rock" in option and "paper" in option:
        l_index = option.index("paper")
        print(f"You chose {option[1]}, computer chose {option[0]}.")
        return f"Paper beats rock! The result is a {player[l_index]} win"
    #if paper and scissors in option, scissors win
    elif "paper" in option and "scissors" in option:
        l_index = option.index("scissors")
        print(f"You chose {option[1]}, computer chose {option[0]}.")
        return f"Scissors beats paper! The result is a {player[l_index]} win"
    #if user input not in option
    else:
        return f"Please input according to the available options (rock, paper, scissors)!"

#variable for computer input
options = ['rock', 'paper', 'scissors']
#Program still run when condition is true
while True:
    #computer random choose
    computer_choose = choice(options)
    #user input
    user_input = input("Enter a choice (rock, paper, scissors): ")
    print("")
    #print result
    print(win_condition([computer_choose,user_input],["Computer","You"]))
    print("")

    #check player want to play again or not
    check = input("Play again (Y/N)? ")
    if check.lower() == 'y':
        continue
    else:
        print("")
        print("Thank you for playing!")
        break


