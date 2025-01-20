#import random package
import random
#print map as matrix
def print_map(p_map):
    print('\n'.join([' '.join(['{:2}'.format(item) for item in row]) for row in p_map]))

#set star to the map function
def set_star(p_map):
    #set coordinate for star
    star = [random.randint(0,2), random.randint(0,2)]
    # set star logic
    if star[1] > 0:
        p_map[star[0]][star[1]] = " ⭐️"
    else:
        p_map[star[0]][star[1]] = "⭐️"
    return p_map

#find star function
def find_gold(p_map,user_input):
    #set empty list for answer
    check_answer = []
    #change user input to list of coordinate
    user_input = list(user_input)
    #change user input to int and match the coordinates
    user_input = [int(user_input[0])-1,int(user_input[1])-1]
    #check and find star coordinate in map
    for i, row in enumerate(p_map):
        for index, item in enumerate(row):
            if item == "⭐️":
                check_answer.extend([i,index])
            elif item == " ⭐️":
                check_answer.extend([i,index])
    #check user and star coordinate
    #if coordinate same that's mean star is founded
    if user_input == check_answer:
        return ["Congratulations!!! You have found the Golden STAR!", p_map]
    #if coordinate not same that's mean star is not founded
    else:
        if user_input[1] > 0:
            p_map[user_input[0]][user_input[1]] = " 🅇"
        else:
            p_map[user_input[0]][user_input[1]] = "🅇"
        return ["Unfortunately you could find it 🙁",p_map]

#program initiate
map1 = [["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"],["⬜️","️⬜️","️⬜️"]]
print("This is our initial map...")
print_map(map1)
print_map("")

#user input
guest_input = input("What do you think: where is the Golden Star in the map? ")

#process the logic and print out the result
output = find_gold(set_star(map1),guest_input)
print(output[0])
print_map(output[1])

