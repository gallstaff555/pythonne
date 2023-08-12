import random 
from collections import deque
#from board.placed_tile import PlacedTile

class NextTile():
    def __init__(self, tiles):
        self.tiles = tiles

    def next(self):
        next_random = random.randint(1,len(self.tiles.get_tiles())-1) 
        next_preview = self.tiles.preview_tile(next_random)
        next_tile = self.tiles.use_tile(next_random)
        return (next_preview, next_tile)
    
    def get_tile_info(self, tile):
        print(f"{tile[0]}\n{tile[1]}\npos:{tile[2]}\nmax_pos:{tile[3]}\n")

    def rotate_tile_left(self, tile):
        self.get_tile_info(tile)
        init_position = tile[2]
        # shift array to the left 
        queue = deque(tile[0])
        queue.rotate(-1)
        tile[0] = list(queue)
        # decrement current position using modular subtraction
        tile[2] = (tile[2] - 1) % (tile[3] + 1)
        # decrement image by replacing int value in string with new position int
        tile[1] = tile[1].replace(f'{init_position}', str(tile[2]))
        print("Tile rotated left!")
        self.get_tile_info(tile)
        return tile

# TODO rotate tile