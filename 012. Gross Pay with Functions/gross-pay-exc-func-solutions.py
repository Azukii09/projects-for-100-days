#define function that have same logic with day 6 project
def gross_pay(h,r):
    paid = 0
    if h >= 40:
        paid = round(((h-40) *1.5 )+ (r*h),2)
    else:
        paid = round(h*r,2)
    return f"You must be paid the following amount: $ {paid}"

#define function to check user input.
def check_float(input_value, var):
        try:
            val= float(input_value)
            return val
        except ValueError:
            print("Error, please enter numeric input for {}".format(var))
            quit()

# make user input
hours = check_float(input("Enter Hours: "),"hours")
rate = check_float(input("Enter Rate ($): "),"rate")
# Print output to the standard output device.
print(gross_pay(hours,rate))

