# 1. Create a greeting for your program.
print("Welcome to the Trip Cost Calculator!")

# 2. Ask the user for number of days.
days = float(input("How many days will you stay?"))

# 3. Ask the user for hotel price.
hotel =float(input("How much does hotel cost per night? $"))

# 4. Ask the user for flight price.
flight = float(input("How much does flight cost? $"))

# 5. Ask the user for rental car price.
rental = float(input("If you need rental car please enter the price otherwise enter zero. $"))

# 6. Ask for other expenses.
other = float(input("Enter other possible expenses $"))

# 7. Combine all expenses together and print with 2 digits after decimal places.
cost = round(((days-1) * hotel)+(2*flight)+rental+other,2)

# Print output to the standard output device. This is using string formating.
print(f"> The total cost you have to pay is: $ {cost}")

