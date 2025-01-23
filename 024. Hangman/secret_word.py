import random
import word_list

def choosing_word():
    word = random.choice(word_list.word_list)
    return list(word)