class Config:
    TILE_WIDTH = 32
    TILE_HEIGHT = 16
    ROW = 10
    COL = 10
    FULL_WIDTH = TILE_WIDTH * ROW
    FULL_HEIGHT = TILE_HEIGHT * COL
    HALF_WIDTH = FULL_WIDTH / 2
    HALF_HEIGHT = FULL_HEIGHT / 2
    TILE_COUNT = 100
    X_OFFSET = (TILE_WIDTH * ROW / 2)
    Y_OFFSET = -1 * TILE_HEIGHT
    ADJ_Y_OFFSET = 22
