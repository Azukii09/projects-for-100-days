#The first try block lets you test a block of code for user input for hours and rate.
try:
    #The second try block lets you test a block of code for user input for hours.
    try:
        # This is for user input and convert it to float for hours
        hours = float(input("Enter Hours: "))
    # The except block lets you handle the error for non-numeric user input in hours variable.
    except ValueError:
        #Print error message
        print("Error, please enter numeric input for Hours")
        #The quit() function is used to exit a python program.
        quit()
    # This is for user input and convert it to float for rate
    rate = float(input("Enter Rate ($): "))
# The except block lets you handle the error for non-numeric user input in rate variable.
except ValueError:
    #Print error message
    print("Error, please enter numeric input for Rate")
    #The quit() function is used to exit a python program.
    quit()
# The else block lets you execute code when there is no error.
else:
    # this is uses same logic as day 6 project
    paid = 0
    if hours >= 40:
        paid = round(((hours-40) *1.5 )+ (rate*hours),2)
    else:
        paid = round(hours*rate,2)
    print(f"You must be paid the following amount: $ {paid}")