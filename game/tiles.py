class Tiles():
    def __init__(self):
        self.tiles = []
        self.init_tiles()

    def init_tiles(self):
        self.tiles.append((['r','r','r','r'], 'road_1.png'))
        for i in range(0,4):
            self.tiles.append((['r','r','r','g'], 'road_4.png'))
        for i in range(0,8):
            self.tiles.append((['g','r','r','g'], 'road_2.png'))
        for i in range(0,9):
            self.tiles.append((['r','r','g','g'], 'road_8.png'))

    def get_tiles(self):
        return self.tiles
    
    def get_tile_count(self):
        return len(self.tiles)
    
    def use_tile(self, index):
        print(f"{len(self.tiles) - 2} remain")
        return self.tiles.pop(index)

# tile has four side and four corners
# # terrain types: road, grass (castle, water)

# 1 4 way 
# 4 3 way 
# 9 L 2 way 
# 8 straight 2 way tiles

# {'four-road': 'road_1.png'} x1
# {'three-road', 'road_4'} x4
# {'straight-road', 'road_2.png'} x8
# {'l-road', 'road_8.png'} x9