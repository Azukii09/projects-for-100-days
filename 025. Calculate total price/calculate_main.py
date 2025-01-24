# computer - price: 500, quantity : 10
# monitor - price: 200, quantity : 8
# keyboard - price: 500, quantity : 5
# mouse - price: 10, quantity : 0
# hdmi cable - price: 20, quantity : 7
# dvd drive - price: 50, quantity : 5
from itertools import count

item = {
    "1":["computer",{ "price": 500, "quantity" : 10}],
    "2":["monitor",{"price": 200, "quantity": 8}],
    "3":["keyboard",{ "price": 500, "quantity" : 5}],
    "4":["mouse",{ "price": 10, "quantity" : 0}],
    "5":["hdmi cable",{ "price": 20, "quantity" : 7}],
    "6":["dvd drive",{ "price": 50, "quantity" : 5}],
}
count_total = 0
for index, chose_item in enumerate(item.values()):
    print(f"{index+1}. {chose_item[0]}")
print("0. Finish")
while True:
    user_choice = int(input("Enter your choice: "))
    if user_choice == 0:
        print(f"Total price: {count_total}")
        break
    else:
        if item[str(user_choice)][1]["quantity"] != 0:
            print(f"Adding {item[str(user_choice)][0]}")
            count_total += item[str(user_choice)][1]["price"]
            item[str(user_choice)][1]["quantity"] -= 1
        else:
            print(f"{item[str(user_choice)][0]} is out of stock")
        continue