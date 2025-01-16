import math
import random

def finish_wrong(number_chance):
    return f"""
The number is {number_chance}!
    Better Luck Next time!    
    """

lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))
number = random.randint(lower, upper)
chance = round(math.log(upper-lower,2))
print(f"     You've only  {chance}  chances to guess the integer!")

for i in range(1,chance+1):
    guess_number = int(input("Guess a number: "))
    if guess_number < number:
        print("You guessed too small!")
        if i == chance:
            print(finish_wrong(chance))
        continue
    elif guess_number > number:
        print("You Guessed too high!")
        if i == chance:
            print(finish_wrong(chance))
        continue
    elif guess_number == number:
        print(f"Congratulations you did it in  {chance}  try")
        break