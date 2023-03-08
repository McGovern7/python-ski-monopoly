import pygame
import button

# Initialize PyGame
pygame.init()

# Create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Title and Icon
pygame.display.set_caption("Monopoly | Ski Resort Edition")
icon = pygame.image.load("images/ski-resort.png")
pygame.display.set_icon(icon)

# define colors
TEXT_COL = (0, 0, 0)


# Function draws text with desired font, color, and location on page
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


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
    singleplayer_img = pygame.image.load("images/button_singleplayer.png").convert_alpha()
    singleplayer_pressed_img = pygame.image.load("images/button_singleplayer_pressed.png").convert_alpha()
    multiplayer_img = pygame.image.load("images/button_multiplayer.png").convert_alpha()
    multiplayer_pressed_img = pygame.image.load("images/button_multiplayer_pressed.png").convert_alpha()
    startgame_img = pygame.image.load("images/button_startgame.png").convert_alpha()

    zero_img = pygame.image.load("images/button_zero.png").convert_alpha()
    zero_pressed_img = pygame.image.load("images/button_zero_pressed.png").convert_alpha()

    one_img = pygame.image.load("images/button_one.png").convert_alpha()
    one_pressed_img = pygame.image.load("images/button_one_pressed.png").convert_alpha()

    two_img = pygame.image.load("images/button_two.png").convert_alpha()
    two_pressed_img = pygame.image.load("images/button_two_pressed.png").convert_alpha()

    three_img = pygame.image.load("images/button_three.png").convert_alpha()
    three_pressed_img = pygame.image.load("images/button_three_pressed.png").convert_alpha()

    four_img = pygame.image.load("images/button_four.png").convert_alpha()
    four_pressed_img = pygame.image.load("images/button_four_pressed.png").convert_alpha()

    # create button instances
    singleplayer_button = button.Button(260, 200, singleplayer_img, 1)
    multiplayer_button = button.Button(400, 200, multiplayer_img, 1)
    startgame_button = button.Button(330, 450, startgame_img, 1)

    zero_button = button.Button(220, 285, zero_img, 1)
    one_button = button.Button(280, 285, one_img, 1)
    two_button = button.Button(340, 285, two_img, 1)
    three_button = button.Button(400, 285, three_img, 1)
    four_button = button.Button(460, 285, four_img, 1)

    while True:
        # Fill screen background
        screen.fill((135, 206, 235))

        draw_text("Welcome to CS205 Project: Ski Resort Monopoly!", large_font, TEXT_COL, 70, 50)
        draw_text("Press 'esc' to close the program", small_font, TEXT_COL, 25, 550)
        draw_text('Game Setup', medium_font, TEXT_COL, 325, 150)

        if singleplayer_button.draw(screen):
            game_singleplayer = True

        if multiplayer_button.draw(screen):
            game_multiplayer = True

        if game_singleplayer:
            num_players = 1
            singleplayer_button = button.Button(260, 200, singleplayer_pressed_img, 1)
            draw_text("Number of Computers", medium_font, TEXT_COL, 285, 250)
            if one_button.draw(screen):
                one_button = button.Button(280, 285, one_pressed_img, 1)
                num_computers = 1
            if two_button.draw(screen):
                two_button = button.Button(340, 285, two_pressed_img, 1)
                num_computers = 2
            if three_button.draw(screen):
                three_button = button.Button(400, 285, three_pressed_img, 1)
                num_computers = 3
            if four_button.draw(screen):
                four_button = button.Button(460, 285, four_pressed_img, 1)
                num_computers = 4
            draw_text("Choose your Piece", medium_font, TEXT_COL, 295, 340)
            if startgame_button.draw(screen):
                # move to game start page
                game()

        # elif game_multiplayer:
            # draw_text("Number of Players", medium_font, TEXT_COL, 300, 285)
            # draw_text("Number of Computers", medium_font, TEXT_COL, 285, 375)

        # Loop through all events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()

        # Required to update screen
        pygame.display.update()


def game():
    while True:
        large_font = pygame.font.SysFont('Verdana', 25)

        # Fill screen background
        screen.fill((255, 255, 255))

        draw_text('Game Menu', large_font, TEXT_COL, 300, 100)

        # Loop through all events
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.QUIT:
                pygame.quit()


        # Required to update screen
        pygame.display.update()

menu()
