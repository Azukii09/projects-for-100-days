# make variable input and convert string input to int format
celsius = int(input("Enter Temperature in Celsius: "))

# make calculations to convert Celsius to Fahrenheit
# after that round the results using the built-in function round().
fahrenheit = round((celsius * 9 / 5) + 32)

# Print output to the standard output device. This is using string formating.
print(f"{celsius} Celsius = {fahrenheit} Fahrenheit")

# note: you can check python built-in function in https://docs.python.org/3/library/functions.html