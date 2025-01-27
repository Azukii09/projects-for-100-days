logo = """
░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░       ░▒▓█▓▒░       ░▒▓██████▓▒░▒▓████████▓▒░▒▓█▓▒░▒▓███████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓███████▓▒░░▒▓█▓▒░▒▓█▓▒▒▓███▓▒░      ░▒▓█▓▒░      ░▒▓████████▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░      ░▒▓█▓▒░░▒▓██████▓▒░       ░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░ ░▒▓█▓▒░   ░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
"""

#Function for converting english word to pig latin version
def word_change(word):
    vocal = ['a','e','i','o','u']
    word = word.lower()
    list_of_words = word.split(" ")
    new_word = list()
    for separate_word in list_of_words:
        temp_word = list(separate_word)
        if temp_word[0] not in vocal:
            swap_word = temp_word.pop(temp_word.index(temp_word[0]))
            temp_word.append(swap_word)
            temp_word.append("ay")
            new_word.append("".join(temp_word).capitalize())
        else:
            temp_word.append("yay")
            new_word.append("".join(temp_word).capitalize())
    return " ".join(new_word)