#define nested dictionary for item data
item = {
    "1":["computer",{ "price": 500, "quantity" : 10}],
    "2":["monitor",{"price": 200, "quantity": 8}],
    "3":["keyboard",{ "price": 500, "quantity" : 5}],
    "4":["mouse",{ "price": 10, "quantity" : 0}],
    "5":["hdmi cable",{ "price": 20, "quantity" : 7}],
    "6":["dvd drive",{ "price": 50, "quantity" : 5}],
}
#define temp var for count total price
count_total = 0
#program logic
while True:
    #print out the item list
    for index, chose_item in enumerate(item.values()):
        #check quantity
        if chose_item[1]["quantity"] > 0:
            print(f"{index+1}. {chose_item[0]}")
        else:
            print(f"{index+1}. {chose_item[0]} (out of stock)")
    print("0. Finish")

    #user input
    user_choice = int(input("Enter your choice: "))
    #logic for user current item choice
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