import random
check_var = True
while check_var:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print(f"Dice1: {dice1}")
    print(f"Dice2: {dice2}")
    try_again=input("Roll the dice again? (Y/N)")
    if try_again.upper()=="N":
        check_var=False