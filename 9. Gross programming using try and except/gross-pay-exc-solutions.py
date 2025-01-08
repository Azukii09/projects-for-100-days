try:
    try:
        hours = float(input("Enter Hours: "))
    except ValueError:
        print("Error, please enter numeric input for Hours")
        quit()
    rate = float(input("Enter Rate ($): "))
except ValueError:
    print("Error, please enter numeric input for Rate")
    quit()
else:
    paid = 0
    if hours >= 40:
        paid = round(((hours-40) *1.5 )+ (rate*hours),2)
    else:
        paid = round(hours*rate,2)
    print(f"You must be paid the following amount: $ {paid}")