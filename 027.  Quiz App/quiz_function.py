logo = """ 
 ██████  ██    ██ ██ ███████      █████  ██████  ██████  
██    ██ ██    ██ ██    ███      ██   ██ ██   ██ ██   ██ 
██    ██ ██    ██ ██   ███       ███████ ██████  ██████  
██ ▄▄ ██ ██    ██ ██  ███        ██   ██ ██      ██      
 ██████   ██████  ██ ███████     ██   ██ ██      ██      
    ▀▀                                                  """

# Player definition
# This function defines each player's attributes based on user input.
def player_definition(user_player):
    # Splitting the player names using commas, resulting in a list of strings.
    player_list = user_player.split(', ')
    # Creating a dictionary with each player's name as the key
    # and the value as another dictionary containing 'score'.
    return {name: {"score": 0} for name in player_list}

# Check answer
# This function checks if the user's answer is correct.
def check_answer(question_answer, answer):
    # Comparing answers in a case-insensitive way and stripping any extra spaces.
    return question_answer.strip().lower() == answer.strip().lower()

# Player turn
# This function handles each player's turn to answer a question.
def player_turn(question, question_index, user_attribute):
    attempts = 2  # Reset attempts for each question.
    # Looping through the number of available attempts.
    for _ in range(attempts):
        # Asking the user for an answer.
        answer = input(f"{question_index}. {question['question']}? ")
        # Checking if the answer is correct using the `check_answer` function.
        if check_answer(question["answer"], answer):
            # If correct, increment the player's score.
            user_attribute['score'] += 1
            print("Correct answer!")  # Providing positive feedback.
            break  # Exit the loop if the answer is correct.
        else:
            # If incorrect, reduce the remaining attempts.
            attempts -= 1
            print(f"Incorrect. You have {attempts} attempts left.")
    print("\033[2J")  # Clearing the screen after the turn.
    return user_attribute

# Winner checker
# This function determines the winner based on the highest score.
def winner_check(user_attribute):
    # Sorting the players by score in descending order.
    sorted_players = sorted(user_attribute.items(), key=lambda x: x[1]['score'], reverse=True)

    # If there are fewer than 2 players, handle the result appropriately.
    if len(sorted_players) == 0:
        return "No players participated."  # Handle case with no players.
    elif len(sorted_players) == 1:
        return f"{sorted_players[0][0]} is the only player and the winner!"  # Handle case with one player.

    # Compare scores of the top two players to determine the winner.
    if sorted_players[0][1]['score'] > sorted_players[1][1]['score']:
        return f"{sorted_players[0][0]} is the winner!"  # Returning the winner's name.
    elif sorted_players[0][1]['score'] < sorted_players[1][1]['score']:
        return f"{sorted_players[1][0]} is the winner!"  # Returning the second player's name.
    return "It's a tie!"  # If scores are equal, it's a tie.

