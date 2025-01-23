#set up initial game
from secret_word import choosing_word
from logo_hangman import logo, hangman_stages
missing_word = choosing_word()
guesses = list()

#setup blanked list for guessing the word
for letter in missing_word:
    guesses.append("_")
live = 6
print(logo)

#game logic
while True:
    print(hangman_stages[live])
    #checking for live
    if live>0:
        print(missing_word)
        print(" ".join(guesses))
        print("You have {} guesses remaining.".format(live))
        user_guess = input("Guess a letter: ").upper()
        print("\033[2J")

        #guessing logic
        if user_guess not in guesses:
            for index, letter in enumerate(missing_word):
                if user_guess == letter:
                    guesses[index] = letter
        else:
            print("Already guessed!")
            continue
        if "_" not in guesses:
            print("You guessed the word!")
            break
        elif user_guess in guesses:
            continue
        else:
            live = live-1
    else:
        print("You lose!")
        break
