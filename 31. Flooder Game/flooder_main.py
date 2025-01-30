from flooder_function import (
    get_new_board,
    display_board,
    has_won,
    change_tile,
    ask_for_player_move
)
from game_setting import moves_per_game

print("Welcome to Flooder Game!")
moves_left = moves_per_game
new_board = get_new_board()

while True:
    display_board(new_board)
    print("Moves left:", moves_left)
    player_move = ask_for_player_move()
    change_tile(player_move, new_board, 0, 0)
    moves_left -= 1
    print("\033[2J")

    if has_won(new_board):
        display_board(new_board)
        print("You have won!")
        break
    elif moves_left == 0:
        display_board(new_board)
        print("You have run out of moves!")
        break


