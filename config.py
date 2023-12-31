class Config:
    ZOOM_FACTOR = 1
    TILE_WIDTH = 32
    TILE_HEIGHT = TILE_WIDTH / 2
    ROW = 20 
    COL = ROW
    FULL_WIDTH = TILE_WIDTH * ROW
    FULL_HEIGHT = TILE_HEIGHT * COL
    HALF_WIDTH = FULL_WIDTH / 2
    HALF_HEIGHT = FULL_HEIGHT / 2
    TILE_COUNT = ROW * COL 
    X_OFFSET = (TILE_WIDTH * ROW / 2)
    Y_OFFSET = -1 * TILE_HEIGHT
    ADJ_Y_OFFSET = 22
