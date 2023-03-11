import sys
import pygame
import button
import random
from Bank_Account import Bank_Account
from Die import Die

# Initialize PyGame
pygame.init()

# Constants
# which font should we use?
# print(pygame.font.get_fonts())
FONT_NAME = 'timesnewroman'
font = pygame.font.SysFont(FONT_NAME, 30)
small_font_1 = pygame.font.SysFont(FONT_NAME, 16)
small_font_2 = pygame.font.SysFont(FONT_NAME, 15)
small_font_3 = pygame.font.SysFont(FONT_NAME, 12)
small_font_4 = pygame.font.SysFont(FONT_NAME, 10)
# Create the screen
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

clock = pygame.time.Clock()

# define colors
TEXT_COL = (0, 0, 0)
green = (0, 100, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (30, 144, 225)


def player1(screen, player1_icon, player1_x, player1_y):
    screen.blit(player1_icon, (player1_x, player1_y))


# house graphic
def create_house(screen, x, y):
    house = pygame.image.load("images/home.png")
    screen.blit(house, (x, y))


# hotel graphic
def create_hotel(screen, x, y):
    hotel = pygame.image.load("images/hotel.png")
    screen.blit(hotel, (x, y))


def create_card(screen, x, y, region_color):
    # text on every property card
    deed_text = small_font_4.render("TITLE DEED", True, black)
    property_text = small_font_1.render("Property Name", True, black)
    rent_text = small_font_2.render("Rent: $", True, black)
    house_1_text = small_font_3.render("With 1 House", True, black)
    house_2_text = small_font_3.render("With 2 Houses", True, black)
    house_3_text = small_font_3.render("With 3 Houses", True, black)
    house_4_text = small_font_3.render("With 4 Houses", True, black)
    hotel_text = small_font_3.render("With Hotel", True, black)
    cost_text_1 = small_font_3.render("Houses cost $", True, black)
    cost_text_2 = small_font_3.render("Hotel costs $", True, black)
    # draw
    pygame.draw.rect(screen, white, (x, y, 150, 200))
    pygame.draw.rect(screen, region_color, (x + 5, y + 5, 140, 50))
    screen.blit(deed_text, (90, 160))
    screen.blit(property_text, (70, 180))
    screen.blit(rent_text, (90, 215))
    screen.blit(house_1_text, (60, 235))
    screen.blit(house_2_text, (60, 250))
    screen.blit(house_3_text, (60, 265))
    screen.blit(house_4_text, (60, 280))
    screen.blit(hotel_text, (60, 295))
    screen.blit(cost_text_1, (60, 320))
    screen.blit(cost_text_2, (60, 330))


# Function draws text with desired font, color, and location on page
def draw_text(screen, text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


# SCREENS
# start screen
def start_screen(screen, game_singleplayer, game_multiplayer):
    # game type variables
    # game_singleplayer = False
    # game_multiplayer = False
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

    # Fill screen background
    screen.fill((135, 206, 235))

    draw_text(screen, "Welcome to CS205 Project: Ski Resort Monopoly!", large_font, TEXT_COL, 80, 50)
    draw_text(screen, "Press 'esc' to close the program", small_font, TEXT_COL, 25, 550)
    draw_text(screen, 'Game Setup', medium_font, TEXT_COL, 335, 150)

    singleplayer_button.draw()
    multiplayer_button.draw()

    if singleplayer_button.check_click():
        game_singleplayer = True
    if multiplayer_button.check_click():
        game_multiplayer = True

    if game_singleplayer:
        game_multiplayer = False
        num_players = 1
        draw_text(screen, "Number of Computers", medium_font, TEXT_COL, 285, 250)
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
            draw_text(screen, "Choose your Piece", medium_font, TEXT_COL, 305, 350)
            startgame_button.draw()

            # if startgame button clicked and game setup, move to game screen
            if startgame_button.check_click():
                board_screen()

    # elif game_multiplayer:
    # game_singleplayer = False
    # draw_text("Number of Players", medium_font, TEXT_COL, 300, 285)
    # draw_text("Number of Computers", medium_font, TEXT_COL, 285, 375)
    return game_singleplayer, game_multiplayer


# board screen
def board_screen(screen):
    large_font = pygame.font.SysFont('Verdana', 25)

    # Fill screen background
    screen.fill((127, 127, 127))

    draw_text(screen, 'Board Screen Filler Window', large_font, white, 325, 100)


# card screen
def card_screen(screen, font):
    pygame.display.set_caption("Your cards")
    text1 = font.render("Available money: ", True, white)
    text2 = font.render("Properties: ", True, white)

    screen.fill(green)
    screen.blit(text1, (50, 50))
    screen.blit(text2, (50, 100))
    # create card
    create_card(screen, 50, 150, blue)
    create_house(screen, 100, 500)


def main():
    """
    Main function
    :return: void
    """
    # Constants
    DICE_DIMS = (40, 40)
    TEST_DICE = True

    # Initializations
    # Title and Icon
    pygame.display.set_caption("Monopoly | Ski Resort Edition")
    icon = pygame.image.load("images/ski-resort.png")
    pygame.display.set_icon(icon)
    # make screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    current_screen = 0

    is_rolling = False
    counter = 0
    die1_value = -1
    die2_value = -1

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

    die1 = Die(screen,
               screen.get_width() - screen.get_width() * 0.1 - DICE_DIMS[0] * 1.5,
               screen.get_height() - DICE_DIMS[0] * 1.5,
               DICE_DIMS)
    die2 = Die(screen,
               screen.get_width() - screen.get_width() * 0.1,
               screen.get_height() - DICE_DIMS[0] * 1.5,
               DICE_DIMS)

    # TODO - was just messing around with player icons (definitely feel free to change)
    # Players
    # P1
    player1_icon = pygame.image.load("images/skiing.png")
    player1_x = 300
    player1_y = 600
    # # P2
    # player2_icon = pygame.image.load("deposit.png")
    # player2_x= 500
    # player2_y= 600
    # # P3
    # player3_icon = pygame.image.load("deposit.png")
    # player3_x = 300
    # player3_y = 300
    # # P4
    # player4_icon = pygame.image.load("deposit.png")
    # player4_x = 300
    # player4_y = 300
    player1(screen, player1_icon, player1_x, player1_y)

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Vector of all keys on keyboard.
        # keys[pygame.K_SPACE] will return True if the space-bar is pressed; False if otherwise
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if current_screen == 0:
            # game_singleplayer, game_multiplayer = start_screen(screen, game_singleplayer, game_multiplayer)
            # Fill screen background
            screen.fill((135, 206, 235))

            draw_text(screen, "Welcome to CS205 Project: Ski Resort Monopoly!", large_font, TEXT_COL, 80, 50)
            draw_text(screen, "Press 'esc' to close the program", small_font, TEXT_COL, 25, 550)
            draw_text(screen, 'Game Setup', medium_font, TEXT_COL, 335, 150)

            singleplayer_button.draw()
            multiplayer_button.draw()

            if singleplayer_button.check_click():
                game_singleplayer = True
            if multiplayer_button.check_click():
                game_multiplayer = True

            if game_singleplayer:
                game_multiplayer = False
                num_players = 1
                draw_text(screen, "Number of Computers", medium_font, TEXT_COL, 285, 250)
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
                    draw_text(screen, "Choose your Piece", medium_font, TEXT_COL, 305, 350)
                    startgame_button.draw()

                    # if startgame button clicked and game setup, move to game screen
                    if startgame_button.check_click():
                        current_screen = 1

            # elif game_multiplayer:
            # game_singleplayer = False
            # draw_text("Number of Players", medium_font, TEXT_COL, 300, 285)
            # draw_text("Number of Computers", medium_font, TEXT_COL, 285, 375)
        elif current_screen == 1:
            board_screen(screen)

            if keys[pygame.K_c]:
                card_screen(screen, font)
            else:
                if not is_rolling:
                    if keys[pygame.K_SPACE]:
                        counter = 0
                        is_rolling = True
                else:
                    # A die_value of -1 indicates the die is not done rolling.
                    # Otherwise, roll() returns a random value from 1 to 6.
                    if die1_value == -1:
                        die1_value = die1.roll(counter)
                    if die2_value == -1:
                        die2_value = die2.roll(counter)
                    if die1_value != -1 and die2_value != -1:
                        # Both dice are done rolling

                        # Return the dice to the start
                        if not die1.at_start:
                            die1.reset()
                        if not die2.at_start:
                            die2.reset()
                        if die1.at_start and die2.at_start:
                            # Both dice are at the start. Reset values
                            is_rolling = False
                            print("You rolled a", die1_value + die2_value)
                            die1_value = -1
                            die2_value = -1

                    counter += 1
                die1.draw(screen)
                die2.draw(screen)

        # Required to update screen
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
