import random
import word_list

#chosing random word from list of word
def choosing_word():
    word = random.choice(word_list.word_list)
    return list(word)