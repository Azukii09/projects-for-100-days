# make variable input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate ($): "))

# make calculations to calculate gross pay by multiplying the rate by the hours worked
# after that round the results using the built-in function round() with a exactly two digits after the decimal place.
# but in this case we will consider the overtime using if else statement
paid = 0
if hours >= 40:
    paid = round(((hours-40) *1.5 )+ (rate*hours),2)
else:
    paid = round(hours*rate,2)

# Print output to the standard output device. This is using string formating.
print(f"You must be paid the following amount: $ {paid}")

# note: you can check python built-in function in https://docs.python.org/3/library/functions.html