import random
import sys

from game_setting import (
    tile_types,
    up_down,
    down_left,
    up_left,
    left_right,
    up_right,
    down_right,
    board_width,
    board_height,
    no_color,colors_map
)


def get_new_board():
    board = {}
    # Create random color numbers for the board
    for x in range(board_width):
        for y in range(board_height):
            board[(x,y)] = random.choice(tile_types)
    for i in range(board_width * board_height):
        x = random.randint(0, board_width - 2)
        y = random.randint(0, board_height - 1)
        board[(x+1,y)] = board[(x,y)]
    return board

def display_board(board):
    print(down_right + (left_right * board_width) + down_left)
    for y in range(board_height):
        if y == 0:
            print('>', end = "")
        else:
            print(up_down, end="")
        # Display each tile in this row
        for x in range(board_width):
            print(colors_map[board[(x,y)]],end="")
        print(no_color+up_down)
    print(up_right + (left_right * board_width)+up_left)

def ask_for_player_move():
    """Let the player select a color to paint upper left tile"""
    while True:
        print("Choose one of ", end="")
        print("\033[31m (R)ed "+no_color, end="")
        print("\033[32m (G)reen "+no_color, end="")
        print("\033[34m (B)lue "+no_color, end="")
        print("\033[33m (Y)ellow "+no_color, end="")
        print("\033[36m (C)yan "+no_color, end="")
        print("\033[35m (P)purple "+no_color, end="")
        print("or QUIT:")
        response = input("> ").upper()
        if response == "QUIT":
            print("Thanks for playing!")
            sys.exit()
        result = {'R':0, 'G': 1, 'B':2, 'Y':3, 'C':4, 'P':5}
        return result[response]

def change_tile(tile_color, board, x,y, color_to_change=None):
    """Change the color of tile using recursive call"""
    if x == 0 and y == 0:
        color_to_change = board[(x,y)]
        if tile_color == color_to_change:
            return
    board[(x,y)] = tile_color

    if x > 0 and board[(x-1,y)] == color_to_change:
        # change left tile's color
        change_tile(tile_color,board, x-1, y, color_to_change)
    if y > 0 and board[(x, y-1)] == color_to_change:
        # change bottom tile's color
        change_tile(tile_color,board, x, y-1, color_to_change)
    if x < board_width - 1 and board[(x+1, y)] == color_to_change:
        # change right tile's color
        change_tile(tile_color,board, x+1, y, color_to_change)
    if y < board_height - 1 and board[(x, y+1)] == color_to_change:
        # change top tile's color
        change_tile(tile_color,board, x, y+1, color_to_change)


def has_won(board):
    """Return true if entire board is one color"""
    tile = board[(0,0)]
    for x in range(board_width):
        for y in range(board_height):
            if board[(x,y)] != tile:
                return False
    return True

