import pygame

#Initialize PyGame
pygame.init()

#make screen
screen = pygame.display.set_mode((1200,800))

#game title and icon
pygame.display.set_caption("Ski Monopoly!")
icon = pygame.image.load("deposit.png")
pygame.display.set_icon(icon)

#Players
#P1
player1_icon = pygame.image.load("skiing.png")
player1_x = 300
player1_y = 600
# #P2
# player2_icon = pygame.image.load("deposit.png")
# player2_x= 500
# player2_y= 600
# #P3
# player3_icon = pygame.image.load("deposit.png")
# player3_x = 300
# player3_y = 300
# #P4
# player4_icon = pygame.image.load("deposit.png")
# player4_x = 300
# player4_y = 300

def player1():
    screen.blit(player1_icon, (player1_x, player1_y))

#loop that runs the game
running = True
while running:
    # screen color
    screen.fill((0, 128, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player1()
    pygame.display.update()