#make loop until 100
for i in range(1,101):
    #check number divisible by 5, 7, and 10 for next line
    if i % 7 == 0 and i % 5 == 0 and i % 10 == 0:
        print("FizzBuzz")
        continue
    #check number divisible by 5 and 7 for FizzBuzz
    elif i % 7 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
        continue
    #check number divisible by 5 and 10 for Fizz and next line
    elif i % 5 == 0 and i % 10 == 0:
        print("Fizz")
        continue
    #check number divisible by 5 for Fizz
    elif i % 5 == 0:
        print("Fizz", end=" ")
        continue
    #check number divisible by 7 for Buzz
    elif i % 7 == 0:
        print("Buzz", end=" ")
        continue
    #print number
    else:
        print(i, end=" ")
        continue