#import random package from build-in function python
import random
#set check condition for while loop
check_var = True
#while loop block code
while check_var:
    #set random number int from 1 to 6
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    #print out put
    print(f"Dice1: {dice1}")
    print(f"Dice2: {dice2}")
    #ask user want to end program or not
    try_again=input("Roll the dice again? (Y/N)")
    #check if user say N change check condition to false for end program
    if try_again.upper()=="N":
        check_var=False