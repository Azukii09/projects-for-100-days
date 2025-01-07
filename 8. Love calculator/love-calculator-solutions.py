from itertools import count

name1 = input("name1: ")
name2 = input("name2: ")
name = name1 + name2

T = name.upper().count("T")
R = name.upper().count("R")
U = name.upper().count("U")
E = name.upper().count("E")

TotalFirst = T + R + U + E
L = name.upper().count("L")
O = name.upper().count("O")
V = name.upper().count("V")
E = name.upper().count("E")
TotalSecond = L + O + V + E

FinalScore = str(TotalFirst)+str(TotalSecond)

if int(FinalScore)<10 or int(FinalScore)>85:
    print(f"Your score is {FinalScore}, you go together like coke and mentos.")
elif 40 <= int(FinalScore) <= 70:
    print(f"Your score is {FinalScore}, you are alright together.")
else:
    print(f"Your score is {FinalScore}.")