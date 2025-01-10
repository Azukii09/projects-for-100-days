#Define the leap year checker function
def is_leap_year(year):
    # check the year inputted is leap year or not using if else statement
    # The year must be evenly divisible by 4;
    if year % 4 == 0:
        # If the year can also be evenly divided by 100, it is not a leap year;
        if year % 100 == 0:
            # unless the year is also evenly divisible by 400
            if year % 400 == 0:
                return "Leap Year."
            else:
                return "Not Leap Year."
        else:
            return "Leap Year."
    else:
        return "Not Leap Year."
# make variable input to input year
year_input = int(input("Please input year: "))
#Print out the result with calling the is_leap_year() function
print(is_leap_year(year_input))



