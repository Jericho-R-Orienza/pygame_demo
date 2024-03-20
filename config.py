WIN_WIDTH = 640
WIN_HEIGHT = 480
TILESIZE = 32
FPS = 60

PLAYER_LAYER = 2 #when we layer our game, we want our player to be in its own layer - i.e. bg layer would be 0
BLOCK_LAYER = 1

PLAYER_SPEED = 3

RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

#20 by 15 i.e. divide our window width and height by tilezie (32)
#each W represents a wall while each . represents an open space
#P represents the player
tilemap = [
    'WWWWWWWWWWWWWWWWWWWW',
    'W..................W',
    'W....WW............W',
    'W..................W',
    'W......WWW.........W',
    'W....WWW...........W',
    'W..................W',
    'W........P.....W...W',
    'W..............W...W',
    'W...........WWWW...W',
    'W..................W',
    'W...WW.............W',
    'W..................W',
    'W..................W',
    'WWWWWWWWWWWWWWWWWWWW',
]