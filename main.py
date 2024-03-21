import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Galaxus-z8Mow.ttf', 32)
        self.running = True

        #init sprite sheets
        self.character_spritesheet = Spritesheet('img/character.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')
        self.enemy_spritesheet = Spritesheet('img/enemy.png')
        self.intro_background = pygame.image.load('./img/introbackground.png')

    def createTileMap(self):
        for i, row in enumerate(tilemap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "W":
                    Block(self, j, i)
                if column == "E":
                    Enemy(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):
        #new game
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates() #take all sprites and bunch them together, allowing ability to update them all at once
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTileMap()

    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #when we press the X button on our window
                self.playing = False
                self.running = False

    def update(self):
        #game loop updates
        self.all_sprites.update() #goes into our all_sprites group and run each of their update()


    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen) #goes to every srpite, finds the image, rectangle, post, and draw it to our window
        self.clock.tick(FPS) #update the screen based on FPS
        pygame.display.update()

    def main(self):
        #game loop
        while self.playing:
            self.events() #contain key press events
            self.update()#update game
            self.draw()#display all sprites
        self.running = False
    
    def game_over(self):
        pass

    def intro_screen(self):
        intro = True

        title = self.font.render('DEMO GAME', True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 50, 100, 50, WHITE, BLACK, 'PLAY', 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed() #0 left click, 1 right click, 2 middle click

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)

            pygame.display.update()

g = Game()
g.intro_screen() 
g.new() #create a new game everytime we run
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()