import random 
#from board.placed_tile import PlacedTile

class NextTile():
    def __init__(self, tiles):
        self.tiles = tiles

    def next(self):
        next_random = random.randint(1,len(self.tiles.get_tiles())-1) 
        next_preview = self.tiles.preview_tile(next_random)
        next_tile = self.tiles.use_tile(next_random)
        return (next_preview, next_tile)

# TODO rotate tile