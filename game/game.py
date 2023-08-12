#!/usr/bin/env python3

# used for finding modules
import sys
sys.path.insert(0,"..")
from config import Config
from enum import IntEnum
#from board.placed_tile import PlacedTile

cfg = Config()

class Feature(IntEnum):
    LEFT = 0
    TOP = 1
    RIGHT = 2
    BOT = 3

class Game():
    def __init__(self, board_side_length):
        self.board_side_length = board_side_length
        self.board = []
        self.init_board()

    def init_board(self):
        for row in range(0, self.board_side_length):
            row_array = []
            for col in range(0, self.board_side_length):
                row_array.append(0)
            self.board.append(row_array)
    
    def display_board(self):
        print(self.board)

    def add_game_tile(self, col, row, game_tile):
        self.board[row][col] = (game_tile.orientation)

    def get_game_tile(self, col, row):
        print (f"returning {self.board[row][col]}")
        return self.board[row][col]
    
    def tile_left_compatible(self, tile_coord, preview_tile):
        if (tile_coord[0] > 0):
            right_tile = self.board[tile_coord[1]][tile_coord[0]-1]
            if (right_tile == 0):
                return True
            else: 
                print(f"Right:{right_tile[2]} = {preview_tile[0][0]}]")
                return right_tile[Feature.RIGHT] == preview_tile[0][Feature.LEFT] 
        else: 
            return True
        
    def tile_right_compatible(self, tile_coord, preview_tile):
        if (tile_coord[0] < cfg.COL - 1):
            left_tile = self.board[tile_coord[1]][tile_coord[0]+1]
            if (left_tile == 0):
                return True
            else: 
                print(f"left {left_tile[0]} = {preview_tile[0][2]}")
                return left_tile[Feature.LEFT] == preview_tile[0][Feature.RIGHT]
        else: 
            return True
        
    def tile_above_compatible(self, tile_coord, preview_tile):
        if (tile_coord[1] > 0):
            above_tile = self.board[tile_coord[1]+1][tile_coord[0]]
            if (above_tile == 0):
                return True
            else: 
                print(f"above: {above_tile[1]} == {preview_tile[0][3]}")
                return above_tile[Feature.TOP] == preview_tile[0][Feature.BOT] 
        else: 
            return True
        
    def tile_below_compatible(self, tile_coord, preview_tile):
        if (tile_coord[1] < cfg.ROW - 1):
            below_tile = self.board[tile_coord[1]-1][tile_coord[0]]
            if (below_tile == 0):
                return True
            else: 
                print(f"below: {below_tile[3]} == {preview_tile[0][1]}")
                return below_tile[Feature.BOT] == preview_tile[0][Feature.TOP]
        else: 
            return True

    # tile is playable if tile does not already exist at target location
    # and adjacent tiles have matching tile edge
    def playable(self, tile_coord, preview_tile):
        open_board_space = (self.board[tile_coord[1]][tile_coord[0]] == 0)
        return open_board_space \
            and self.tile_left_compatible(tile_coord, preview_tile) \
            and self.tile_right_compatible(tile_coord, preview_tile) \
            and self.tile_above_compatible(tile_coord, preview_tile) \
            and self.tile_below_compatible(tile_coord, preview_tile) 

