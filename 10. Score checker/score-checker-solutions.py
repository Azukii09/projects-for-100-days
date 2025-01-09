try:
    score = float(input("Enter score: "))
    if score > 1:
        print("Error, Bad Score. Please enter score in range 0 - 1.0.")
        quit()
except ValueError:
    print("Error, Bad Score. Please enter numeric input.")
else:
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