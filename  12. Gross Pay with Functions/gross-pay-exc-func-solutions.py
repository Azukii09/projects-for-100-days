def gross_pay(h,r):
    paid = 0
    if h >= 40:
        paid = round(((h-40) *1.5 )+ (r*h),2)
    else:
        paid = round(h*r,2)
    return f"You must be paid the following amount: $ {paid}"

def check_float(input_value, var):
        try:
            val= float(input_value)
            return val
        except ValueError:
            print("Error, please enter numeric input for {}".format(var))
            quit()

hours = check_float(input("Enter Hours: "),"hours")
rate = check_float(input("Enter Rate ($): "),"rate")

print(gross_pay(hours,rate))

