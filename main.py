import pygame

#Initialize PyGame
pygame.init()

#make screen
screen = pygame.display.set_mode((1200,800))

#loop that runs the game
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False