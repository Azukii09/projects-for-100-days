#import package
from random import choice, shuffle
#set up character variable
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

#function for random choice character base on user input
def for_loop_password(loops_numb, chose_letters):
    return [choice(chose_letters) for _ in range(loops_numb)]

#function for shuffling chosen character
def shuffle_password(p_list):
    shuffle(p_list)
    return "".join(p_list)

#input password criteria
password=[]
p_letter = int(input("How many letters do you want in your password? "))
p_numbs=int(input("How many numbers do you want in your password? "))
p_symbols=int(input("How many symbols do you want in your password? "))

#generate password base on user criteria
password.extend(for_loop_password(p_letter, letters))
password.extend(for_loop_password(p_numbs, nums))
password.extend(for_loop_password(p_symbols, symbols))

#print final output from password that shuffled
print(shuffle_password(password))

