import random
def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

def set_star(p_map):
    star = [random.randint(0,2), random.randint(0,2)]
    # star = [0, 1]
    if star[1] > 0:
        p_map[star[0]][star[1]] = " ⭐️"
    else:
        p_map[star[0]][star[1]] = "⭐️"
    return p_map

def find_gold(p_map,user_input):
    check_answer = []
    user_input = list(user_input)
    user_input = [int(user_input[0])-1,int(user_input[1])-1]
    for i, row in enumerate(p_map):
        for index, item in enumerate(row):
            if item == "⭐️":
                check_answer.extend([i,index])
            elif item == " ⭐️":
                check_answer.extend([i,index])

    if user_input == check_answer:
        return ["Congratulations!!! You have found the Golden STAR!", p_map]
    else:
        if user_input[1] > 0:
            p_map[user_input[0]][user_input[1]] = " 🅇"
        else:
            p_map[user_input[0]][user_input[1]] = "🅇"
        return ["Unfortunately you could find it 🙁",p_map]


map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map1)
print_map("")

guest_input = input("What do you think: where is the Golden Star in the map? ")

output = find_gold(set_star(map1),guest_input)
print(output[0])
print_map(output[1])

