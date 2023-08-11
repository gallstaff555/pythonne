#!/usr/bin/env python3

# used for finding modules
import sys
sys.path.insert(0,"..")

from board.game_tile import GameTile

class Game():
    def __init__(self, board_side_length):
        self.board_side_length = board_side_length
        self.board = []

    def init_board(self):
        for row in range(0, self.board_side_length):
            row_array = []
            for col in range(0, self.board_side_length):
                row_array.append(0)
            self.board.append(row_array)
    
    def display_board(self):
        print(self.board)

    def add_game_tile(self, col, row, game_tile):
        self.board[row][col] = (game_tile)

    def get_game_tile(self, col, row):
        print (f"returning {self.board[row][col]}")
        return self.board[row][col]


# new_tile = GameTile((x,y), pygame.image.load(f'./assets/sprites/roads/road_{random_tile}.png').convert_alpha(), \
#                            placed_game_tiles)
