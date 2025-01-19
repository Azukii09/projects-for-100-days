#import random package
import random

#user input
name = input("Who are the names that will pay? ")
#split input into list that separate bay ", "
name = name.split(", ")
#pick random list and print it
print(f"{random.choice(name)} is going to pay for the meal today!")