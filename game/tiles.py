import random

class Tiles():
    def __init__(self):
        # array of features, image file, current_orientation, total orientations (for rotation) - 1
        self.tiles = []
        self.init_tiles()

    # tile to array conversion
    # 0 / \ 1
    # 3 \ / 2

    def init_tiles(self):
        self.tiles.append([['r','r','r','r'], 'four_way_road.png', 0, 0])
        for i in range(0,4):
            self.tiles.append([['r','r','g','r'], 'three_way_road_0.png', 0, 3])
        for i in range(0,8):
            self.tiles.append([['r','g','g','r'], 'L_road_0.png', 0, 3])
        for i in range(0,9):
            self.tiles.append([['g','r','g','r'], 'straight_road_0.png', 0, 1])

    def get_tiles(self):
        return self.tiles
    
    def get_tile_count(self):
        return len(self.tiles)
    
    def use_tile(self, index):
        print(f"{len(self.tiles) - 2} remain")
        return self.tiles.pop(index)
    
    def preview_tile(self, index):
        return self.tiles[index]
    
    # def get_tile_info(self, tile):
    #     print(f"{tile[0]}\n{tile[1]}\npos:{tile[2]}\nmax_pos:{tile[3]}\n")
    
    # def rotate_tile_left(self, tile):
    #     self.get_tile_info(tile)
    #     init_position = tile[2]
    #     # shift array to the left 
    #     tile[0] = tile[0].rotate(-1)
    #     # decrement current position using modular subtraction
    #     tile[2] = (tile[2] - 1) % (tile[3] + 1)
    #     # decrement image by replacing int value in string with new position int
    #     tile[1] = tile[1].replace(f'{init_position}', tile[2])
    #     print("Tile rotated left!")
    #     self.get_tile_info()
    #     return tile




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