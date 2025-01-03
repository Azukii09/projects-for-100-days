hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate ($): "))

paid = round(hours * rate,2)
print(f"You must be paid the following amount: $ {paid}")