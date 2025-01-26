from question import quiz
from quiz_function import logo, winner_check, check_answer, player_turn, player_definition

# Display the application logo at the start of the program.
print(logo)

# Prompt the user to input player names, separated by commas.
player_input = input("Who wants to play? (Separate names with a comma): ")

# Define each player's attributes based on the input.
player = player_definition(player_input)

# Main game loop.
while True:
    # Iterate through all questions in the quiz.
    for question_index, question in quiz.items():
        # Give each player a turn to answer the question.
        for person in player.keys():
            print(logo)  # Display the logo for aesthetics.
            # Announce the current player's turn.
            print(f"Now it's {person}'s turn to answer")
            # Display the current score.
            print(f"Current score: {player[person]['score']}")
            print("-" * 40)  # Add a visual separator.
            # Handle the player's turn using the `player_turn` function.
            player[person] = player_turn(question, question_index, player[person])

    # Display the final scores after all questions are answered.
    print("=" * 40)
    print("Final Scores")  # Title for the final scores.
    for person, stats in player.items():
        # Display each player's score.
        print(f"{person}: {stats['score']} points")
    print("=" * 40)

    # Display the game result using the `winner_check` function.
    print(f"Result: {winner_check(player)}")

    # Ask if the user wants to play again.
    other_game = input("Do you want to play again? (Y/N): ").strip().upper()
    print("\033[2J")  # Clear the screen for the next game.
    if other_game == "Y":
        # If yes, prompt for player names and reinitialize attributes.
        player_input = input("Who wants to play? (Separate names with a comma): ")
        player = player_definition(player_input)
    else:
        # If no, exit the loop and end the program.
        break
