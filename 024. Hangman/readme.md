# Hangman

## 📄 Step 1 - Picking a secret word and asking for player input

### 📝 To do list
>1. TODO 1 - Choose a random word from a given list which is word_list and assign it to variable called secret_word
>2. TODO 2 - Generate/show blanks which equals to number of characters in secret word
>3. TODO 3 - Ask a player to guess letter and assign it to a variable called guess and make it upper case

## 📄 Step 2 - Picking a secret word and asking for player input

### 📝 To do list
>1. TODO 1 - Check if guessed letter is already guessed or not. Create guessed_letters list and add guessed letters to the list and in every step check that if letter exists or not
>2. TODO 2 - Check if the letter that player guessed is one of the letter in the secret word
>3. TODO 3 - If letter is in the secret word, loop through each position in secret word the update blanks list with macthed letter in its position in secret word. Eg: if the secret word is PYTHON and user chose T, the blanks list will be like this, ['_','_','T','_','_','_']

## 📄 Step 3 - Loop until Player Wins

### 📝 To do list
>1. TODO 1 - By using a while loop let the player to guess again if the current guess is previously guessed.
>2. TODO 2 - In the same while loop implement a logic to guess again until they have guessed all letters and there is not blank ("_") left in blanks list and print you win

## 📄 Step 4 - Track Lives

### 📝 To do list
>1. TODO 1 - Create lives variable and set it to 6. Check if the letter that player guessed is not one of the letter in the secret word then decrease lives by 1 for each wrong guess
>2. TODO 2 - When the lives reaches 0, implement a logic to stop game and print You Lose.
>3. TODO 3 - Instead of printing blanks list, convert it to string and print

## 📄 Step 5 - ASCI Art

### 📝 To do list
>1. TODO 1 - Add condition which asks whether players want to play again
>2. TODO 2 - Print ASCI Art from hangman_stages list

Happy Coding! 🚀✨
