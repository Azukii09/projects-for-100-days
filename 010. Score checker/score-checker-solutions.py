#The try block lets you test a block of code for user input for score.
try:
    # This is for user input and convert it to float for score
    score = float(input("Enter score: "))
    #First check is whether the score is in the limit
    if score > 1:
        #Print error message
        print("Error, Bad Score. Please enter score in range 0 - 1.0.")
        #The quit() function is used to exit a python program.
        quit()
# The except block lets you handle the error for user input.
except ValueError:
    #Print error message and exit a python program
    print("Error, Bad Score. Please enter numeric input.")
# The else block lets you execute code when there is no error.
else:
    #The logic for determine the final score
    if score < 0.6:
        print(f"Score : E")
    elif 0.6 <= score < 0.7:
        print(f"Score : D")
    elif 0.7 <= score < 0.8:
        print(f"Score : C")
    elif 0.8 <= score < 0.9:
        print(f"Score : B")
    elif 0.9 <= score:
        print(f"Score : A")