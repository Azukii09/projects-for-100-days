import random

name = input("Who are the names that will pay? ")
name = name.split(", ")
print(f"{random.choice(name)} is going to pay for the meal today!")