import pygame
from buttons import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Galaxus-z8Mow.ttf', 32)
        self.running = True
    
    def new(self):
        #new game
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates() #take all sprites and bunch them together, allowing ability to update them all at once
        self.blocks = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.player = Player(self, 1, 2) #one on the x axis and 2 on the y axis (time tilezie)

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
        pass

g = Game()
g.intro_screen() 
g.new() #create a new game everytime we run
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()