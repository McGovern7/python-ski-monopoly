import pygame
import button
import sys

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

# Create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("Monopoly | Ski Resort Edition")
icon = pygame.image.load("images/ski-resort.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# define colors
TEXT_COL = (0, 0, 0)


# Function draws text with desired font, color, and location on page
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# menu screen
def menu():
    # game type variables
    game_singleplayer = False
    game_multiplayer = False
    num_players = 0
    num_computers = 0

    # define fonts
    large_font = pygame.font.SysFont('Verdana', 25)
    medium_font = pygame.font.SysFont('Verdana', 20)
    small_font = pygame.font.SysFont('Verdana', 15)

    # load button images
    singleplayer_img = pygame.image.load("images/singleplayer.png").convert_alpha()
    multiplayer_img = pygame.image.load("images/multiplayer.png").convert_alpha()
    startgame_img = pygame.image.load("images/startgame.png").convert_alpha()
    number_img = pygame.image.load("images/numplayer.png").convert_alpha()

    # draw buttons
    singleplayer_button = button.Button(singleplayer_img, 280, 210, "Single-Player", 1)
    multiplayer_button = button.Button(multiplayer_img, 520, 210, "Multi-Player", 1)
    startgame_button = button.Button(startgame_img, 400, 500, "Start Game", 1)
    num_computers1_button = button.Button(number_img, 300, 310, "1", 1.5)
    num_computers2_button = button.Button(number_img, 400, 310, "2", 1.5)
    num_computers3_button = button.Button(number_img, 500, 310, "3", 1.5)


    while True:
        # Fill screen background
        screen.fill((135, 206, 235))

        draw_text("Welcome to CS205 Project: Ski Resort Monopoly!", large_font, TEXT_COL, 80, 50)
        draw_text("Press 'esc' to close the program", small_font, TEXT_COL, 25, 550)
        draw_text('Game Setup', medium_font, TEXT_COL, 335, 150)

        singleplayer_button.draw()
        multiplayer_button.draw()

        if singleplayer_button.check_click():
            game_singleplayer = True
        if multiplayer_button.check_click():
            game_multiplayer = True

        if game_singleplayer:
            game_multiplayer = False
            num_players = 1
            draw_text("Number of Computers", medium_font, TEXT_COL, 285, 250)
            num_computers1_button.draw()
            num_computers2_button.draw()
            num_computers3_button.draw()

            # set number of computers
            if num_computers1_button.check_click():
                num_computers = 1
            if num_computers2_button.check_click():
                num_computers = 2
            if num_computers3_button.check_click():
                num_computers = 3

            if num_computers > 0:
                draw_text("Choose your Piece", medium_font, TEXT_COL, 305, 350)
                startgame_button.draw()

                # if startgame button clicked and game setup, move to game screen
                if startgame_button.check_click():
                    game()

        # elif game_multiplayer:
            # game_singleplayer = False
            # draw_text("Number of Players", medium_font, TEXT_COL, 300, 285)
            # draw_text("Number of Computers", medium_font, TEXT_COL, 285, 375)

        # Loop through all events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Required to update screen
        pygame.display.update()
        clock.tick(60)


# game screen
def game():
    while True:
        large_font = pygame.font.SysFont('Verdana', 25)

        # Fill screen background
        screen.fill((255, 255, 255))

        draw_text('Game Menu', large_font, TEXT_COL, 325, 100)

        # Loop through all events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Required to update screen
        pygame.display.update()
        clock.tick(60)


menu()
