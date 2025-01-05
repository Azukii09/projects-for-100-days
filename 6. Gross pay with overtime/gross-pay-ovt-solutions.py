hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate ($): "))

paid = 0
if hours >= 40:
    paid = round(((hours-40) *1.5 )+ (rate*hours),2)
else:
    paid = round(hours*rate,2)
print(f"You must be paid the following amount: $ {paid}")