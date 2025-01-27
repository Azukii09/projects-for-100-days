from pig_latin_function import logo,word_change

print(word_change("alive"))
while True:
    print(logo)
    word = input("Type a word to convert: ")
    print(f"New word : {word_change(word)}")
    play_var = input("wanna convert some text again (Y/N)? ")
    if play_var.lower() == "n":
        break

