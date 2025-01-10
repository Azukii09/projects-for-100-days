def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap Year."
            else:
                return "Not Leap Year."
        else:
            return "Leap Year."
    else:
        return "Not Leap Year."

year_input = int(input("Please input year: "))

print(is_leap_year(year_input))