import sys
import pygame

#Initialize PyGame
pygame.init()

#make screen
screen = pygame.display.set_mode((1200,800))

#constants
#TODO - which font should we use?
#print(pygame.font.get_fonts())
font = pygame.font.SysFont("times", 30)
green = (0, 100, 0)
white = (255,255,255)



#TODO - was just messing around with player icons (definitely feel free to change)
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

#SCREENS
#start screen
def start_screen():
    # game title and icon
    pygame.display.set_caption("Monopoly | Ski Resort Edition")
    icon = pygame.image.load("ski-resort.png")
    pygame.display.set_icon(icon)
    while True:
        return True
#board screen
def board_screen():
    while True:
        return True

#card screen
def card_screen():
    pygame.display.set_caption("Your cards")
    text = font.render("Properties: ", True, white)
    while True:
        screen.fill(green)
        screen.blit(text, (50, 50))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        return True


# Game loop
while True:
    #start_screen()
    card_screen()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
