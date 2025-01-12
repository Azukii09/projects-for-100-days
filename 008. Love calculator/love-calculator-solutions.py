# input variable name 1 and name 2
name1 = input("name1: ")
name2 = input("name2: ")
name = name1 + name2

#count the number of times the letters in the word TRUE occurs.
T = name.upper().count("T")
R = name.upper().count("R")
U = name.upper().count("U")
E = name.upper().count("E")
#count total from TRUE occurs letter
TotalFirst = T + R + U + E

#count the number of times the letters in the word LOVE occurs.
L = name.upper().count("L")
O = name.upper().count("O")
V = name.upper().count("V")
E = name.upper().count("E")
#count total from LOVE occurs letter
TotalSecond = L + O + V + E

#combine TRUE and LOVE total numbers to make a 2-digit number.
FinalScore = str(TotalFirst)+str(TotalSecond)
#check the result
if int(FinalScore)<10 or int(FinalScore)>85:
    print(f"Your score is {FinalScore}, you go together like coke and mentos.")
elif 40 <= int(FinalScore) <= 70:
    print(f"Your score is {FinalScore}, you are alright together.")
else:
    print(f"Your score is {FinalScore}.")

# The .upper() function is a function to change a word to all capital letters# note: you can check python built-in function in https://docs.python.org/3/library/functions.html