import pygame
from config import *
import math
import random

class Spritesheet:
    def __init__(self, file):
        #load our sprite sheet
        self.sheet = pygame.image.load(file).convert()

    #cut out the sprite we want (used for animations)
    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        #blit() is the function used to draw an image onto a surface
        sprite.blit(self.sheet, (0,0), (x, y, width, height))#creates the cut out that grabs the image we want from the sprite sheet
        #set_colorkey() sets the dg color of a sprite transparent
        sprite.set_colorkey(BLACK)
        return sprite
 

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups) #add player to all sprites group

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        #temporary value at init
        self.x_change = 0
        self.y_change = 0

        self.facing = 'down' #default facing
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x_change -= PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_RIGHT]:
            self.x_change += PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_UP]:
            self.y_change -= PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_DOWN]:
            self.y_change += PLAYER_SPEED
            self.facing = 'down'

    def collide_blocks(self, direction):
        if direction == "x":
            #hits returns a boolean if sprite collides with block -> returns the position of the block as well
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits: #we need to check what direction the collision is from
                if self.x_change > 0: #colliding from left
                    #we set the position of the player at 0,0 (top left) of the block and subtract the width of the player
                    # that way we are ensuring the the player is exactly touching the block at the very last pixel
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0: #collide below
                    self.rect.y = hits[0].rect.top - self.rect.height #same logic as direction x
                if self.y_change < 0: #collide above
                    self.rect.y = hits[0].rect.bottom

    def animate(self):
        down_animations = [self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 2, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 2, self.width, self.height)]

        up_animations = [self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(35, 34, self.width, self.height),
                         self.game.character_spritesheet.get_sprite(68, 34, self.width, self.height)]

        left_animations = [self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(35, 98, self.width, self.height),
                           self.game.character_spritesheet.get_sprite(68, 98, self.width, self.height)]

        right_animations = [self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(35, 66, self.width, self.height),
                            self.game.character_spritesheet.get_sprite(68, 66, self.width, self.height)]

        if self.facing == "down":
            if self.y_change == 0: #standing still
                self.image = self.game.character_spritesheet.get_sprite(3, 2, self.width, self.height)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1 #we are reaching 1, 2, 3 in our array every 0.1->10 frames
                if self.animation_loop >= 3: #reset back to 1 -> looping the animation
                    self.animation_loop = 1

        if self.facing == "up":
            if self.y_change == 0: #standing still
                self.image = self.game.character_spritesheet.get_sprite(3, 34, self.width, self.height)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1 #we are reaching 1, 2, 3 in our array every 0.1->10 frames
                if self.animation_loop >= 3: #reset back to 1 -> looping the animation
                    self.animation_loop = 1

        if self.facing == "left":
            if self.x_change == 0: #standing still
                self.image = self.game.character_spritesheet.get_sprite(3, 98, self.width, self.height)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1 #we are reaching 1, 2, 3 in our array every 0.1->10 frames
                if self.animation_loop >= 3: #reset back to 1 -> looping the animation
                    self.animation_loop = 1

        if self.facing == "right":
            if self.x_change == 0: #standing still
                self.image = self.game.character_spritesheet.get_sprite(3, 66, self.width, self.height)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1 #we are reaching 1, 2, 3 in our array every 0.1->10 frames
                if self.animation_loop >= 3: #reset back to 1 -> looping the animation
                    self.animation_loop = 1
        
class Block(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(960, 448, self.width, self.height)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)
        
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y