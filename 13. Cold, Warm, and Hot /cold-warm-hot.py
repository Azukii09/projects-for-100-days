def cold_warm_hot(n):
    if n > 28:
        return "Hot"
    elif 18 <= n <= 28:
        return "Warm"
    else:
        return "Cold"

temp = int(input("Enter Temperature: "))
print(cold_warm_hot(temp))