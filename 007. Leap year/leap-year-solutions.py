# make variable input to input year
year = int(input("Please input year: "))

# check the year inputted is leap year or not using if else statement
# The year must be evenly divisible by 4;
if year % 4 == 0:
    # If the year can also be evenly divided by 100, it is not a leap year;
    if year % 100 == 0:
        # unless the year is also evenly divisible by 400
        if year % 400 == 0:
            print("Leap Year.")
        else:
            print("Not Leap Year.")
    else:
        print("Leap Year.")
else:
    print("Not Leap Year.")