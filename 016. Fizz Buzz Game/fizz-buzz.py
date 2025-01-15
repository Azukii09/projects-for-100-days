for i in range(1,101):
    if i % 7 == 0 and i % 5 == 0 and i % 10 == 0:
        print("FizzBuzz")
        continue
    elif i % 7 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
        continue
    elif i % 5 == 0 and i % 10 == 0:
        print("Fizz")
        continue
    elif i % 5 == 0:
        print("Fizz", end=" ")
        continue
    elif i % 7 == 0:
        print("Buzz", end=" ")
        continue
    else:
        print(i, end=" ")
        continue