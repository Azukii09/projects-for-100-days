#defines a function to determine cold, warm and hot criteria
def cold_warm_hot(n):
    if n > 28:
        return "Hot"
    elif 18 <= n <= 28:
        return "Warm"
    else:
        return "Cold"

#user input
temp = int(input("Enter Temperature: "))
# Print output to the standard output device.
#with calling the function
print(cold_warm_hot(temp))