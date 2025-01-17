from random import choice, shuffle

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
nums = "1234567890"
symbols = "-+=!@#$%^&*"

def for_loop_password(loops_numb, chose_letters):
    return [choice(chose_letters) for _ in range(loops_numb)]


def shuffle_password(p_list):
    shuffle(p_list)
    return "".join(p_list)

password=[]
p_letter = int(input("How many letters do you want in your password? "))
p_numbs=int(input("How many numbers do you want in your password? "))
p_symbols=int(input("How many symbols do you want in your password? "))

password.extend(for_loop_password(p_letter, letters))
password.extend(for_loop_password(p_numbs, nums))
password.extend(for_loop_password(p_symbols, symbols))

print(shuffle_password(password))

