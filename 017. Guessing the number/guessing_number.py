#import package
import math
import random

#def function for wrong number
def finish_wrong(number_chance):
    return f"""
The number is {number_chance}!
    Better Luck Next time!    
    """

#user input
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

#generate random number base on user bound input
number = random.randint(lower, upper)
#create chance for guessing
chance = round(math.log(upper-lower,2))
print(f"     You've only  {chance}  chances to guess the integer!")

#program logic using for loop for user guessing
for i in range(1,chance+1):
    guess_number = int(input("Guess a number: "))
    if guess_number == number:
        print(f"Congratulations you did it in  {chance}  try")
        break
    elif guess_number < number:
        print("You guessed too small!")
        if i == chance:
            print(finish_wrong(chance))
        continue
    elif guess_number > number:
        print("You Guessed too high!")
        if i == chance:
            print(finish_wrong(chance))
        continue
