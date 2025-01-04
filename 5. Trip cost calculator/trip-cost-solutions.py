print("Welcome to the Trip Cost Calculator!")
days = float(input("How many days will you stay?"))
hotel =float(input("How much does hotel cost per night? $"))
flight = float(input("How much does flight cost? $"))
rental = float(input("If you need rental car please enter the price otherwise enter zero. $"))
other = float(input("Enter other possible expenses $"))

cost = round(((days-1) * hotel)+(2*flight)+rental+other,2)
print(f"> The total cost you have to pay is: $ {cost}")

