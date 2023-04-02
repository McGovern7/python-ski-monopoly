import sys
import pygame

import player
import button
import random
from Bank_Account import Bank_Account
from Die import Die
from Property import Property
from card import Card
from player import Player

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
green = (0, 100, 0)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (30, 144, 225)
red = (255, 0, 0)
board_color = (191, 219, 174)


# house graphic
def create_house(screen, x, y):
    """
    Function to draw a house icon on a property
    :param screen: game screen
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :return: nothing
    """
    house = pygame.image.load("images/home.png")
    screen.blit(house, (x, y))


# hotel graphic
def create_hotel(screen, x, y):
    """
    Function to draw a hotel icon on a property
    :param screen: game screen
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :return: nothing
    """
    hotel = pygame.image.load("images/hotel.png")
    screen.blit(hotel, (x, y))


def create_card(screen, x, y, region_color):
    """
    Function to create a card graphic for the card screen
    :param screen: game screen
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :param region_color: the color of the district the property is in
    :return: nothing
    """
    # draw text on every property card
    pygame.draw.rect(screen, white, (x, y, 150, 200))
    pygame.draw.rect(screen, region_color, (x + 5, y + 5, 140, 50))
    draw_text(screen, "TITLE DEED", small_font_4, black, 90, 160)
    draw_text(screen, "Property Name", small_font_2, black, 70, 180)
    draw_text(screen, "Rent: $", small_font_3, black, 90, 215)
    draw_text(screen, "With 1 House", small_font_3, black, 60, 235)
    draw_text(screen, "With 2 Houses", small_font_3, black, 60, 250)
    draw_text(screen, "With 3 Houses", small_font_3, black, 60, 265)
    draw_text(screen, "With 4 Houses", small_font_3, black, 60, 280)
    draw_text(screen, "With Hotel", small_font_3, black, 60, 295)
    draw_text(screen, "Houses cost $", small_font_3, black, 60, 320)
    draw_text(screen, "Hotel costs $", small_font_3, black, 60, 330)


# Function draws text with desired font, color, and location on page
def draw_text(screen, text, font, text_col, x, y):
    """
    Function to draww text on the game screen
    :param screen: game screen
    :param text: text that will be displayed on-screen
    :param font: font that will be used
    :param text_col: the color of the text
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :return: nothing
    """
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def load_properties():
    """
    Function to load in property information and create objects of Propery class
    :return: list of property objects
    """
    # initialize list to put properties in
    properties = []
    file = open('text/property_cards.txt', 'r')
    lines = file.readlines()
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        # DEBUGGING
        # print("Line{}: {}".format(count, line.strip()))
        # split the line by commas
        property_features = line.split(',')
        # create a property object
        new_prop = Property(property_features[0], property_features[1], property_features[2], property_features[3],
                            property_features[4], property_features[5], property_features[6], property_features[7],
                            property_features[8], property_features[9], property_features[10], property_features[11])
        properties.append(new_prop)

    file.close()
    return properties


def load_cards():
    cards = []
    file = open('text/cards.txt', 'r')
    lines = file.readlines()
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        # DEBUGGING
        # print("Line{}: {}".format(count, line.strip()))
        # split the line by commas
        card_features = line.split(',')
        # create a property object
        new_card = Card(card_features[0], card_features[1], card_features[2], card_features[3])
        cards.append(new_card)

    file.close()
    return cards


def get_icon_positions():
    # trying to find the middle of each space's coordinate spot
    # and put each coordinate into list  clockwise starting at bottom left "GO"
    icon_positions = []
    # first position (start)
    icon_positions.append((75, 725))  # bottom left
    y_coord = 745
    for i in range(9):
        icon_positions.append((75, 655 - (575 / 9) * i))  # left row of vertical coords
    icon_positions.append((75, 75))  # top left
    for i in range(9):
        icon_positions.append((142 + (575 / 9) * i, 75))  # top row of horizontal coords
    icon_positions.append((725, 75))  # top right
    for i in range(9):
        icon_positions.append((725, 142 + (575 / 9) * i))  # right row of vertical coords
    icon_positions.append((745, 725))  # bottom right
    for i in range(9):
        icon_positions.append((655 - (575 / 9) * i, 725))  # bottom row of horizontal coords
    return icon_positions


# SCREENS
# board screen
def board_screen(screen, icon_positions, properties):
    """
    Function to display the screen with the monopoly board
    :param screen: game screen
    :return: nothing
    """
    large_font = pygame.font.SysFont('Verdana', 25)

    # Fill screen background
    screen.fill((127, 127, 127))
    # draw board
    # full board (outer square)
    pygame.draw.rect(screen, board_color, (0, 0, 800, 800))
    # center square
    center_dimension = 575  # Used for the height and width of the center space
    center_x = 110
    center_y = 110
    pygame.draw.rect(screen, green, (center_x, center_y, center_dimension, center_dimension))

    # tile lines
    y = center_y
    for i in range(10):
        # lines going down the left side of the board
        pygame.draw.rect(screen, black, (0, y, center_y, 1))
        # lines going down the right side of the board
        pygame.draw.rect(screen, black, (center_x + center_dimension, y, center_y, 1))
        y += center_dimension / 9  # Spaces all the squares evenly

    x = center_x
    for i in range(10):
        # going across top of board
        pygame.draw.rect(screen, black, (x, 0, 1, center_x))
        # lines going across bottom of board
        pygame.draw.rect(screen, black, (x, center_y + center_dimension, 1, center_x))
        x += center_dimension / 9  # Spaces all the squares evenly

    # draw the name of each property on the square
    for property in properties:
        coordinates = str(icon_positions[int(property.location)])
        coordinates_list = coordinates[1:len(coordinates) - 1].split(',')
        # print(coordinates_list)
        draw_text(screen, property.property_name, small_font_3, black, float(coordinates_list[0]),
                  float(coordinates_list[1]))


# card screen
def card_screen(screen, font):
    """
    Function to display a screen that shows you cards and gives more details about your properties
    :param screen: game screen
    :param font: font of the text
    :return: nothing
    """
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
    Main function to run the game
    :return: nothing
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
    turn = "Player1"

    # game type variables
    game_singleplayer = False
    game_multiplayer = False
    num_players = 1
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
    properties_img = pygame.image.load("images/properties.png").convert_alpha()
    roll_img = pygame.image.load("images/roll.png").convert_alpha()
    player1_img = pygame.image.load("images/icon1.png").convert_alpha()
    player2_img = pygame.image.load("images/icon2.png").convert_alpha()
    player3_img = pygame.image.load("images/icon3.png").convert_alpha()
    player4_img = pygame.image.load("images/icon4.png").convert_alpha()

    # draw buttons
    singleplayer_button = button.Button(singleplayer_img, 280, 210, "Single-Player", white, 1)
    multiplayer_button = button.Button(multiplayer_img, 520, 210, "Multi-Player", white, 1)
    startgame_button = button.Button(startgame_img, 400, 500, "Start Game", white, 1)
    num_computers1_button = button.Button(number_img, 300, 310, "1", white, 1.5)
    num_computers2_button = button.Button(number_img, 400, 310, "2", white, 1.5)
    num_computers3_button = button.Button(number_img, 500, 310, "3", white, 1.5)
    properties_button = button.Button(properties_img, 1000, 50, "Inspect Properties", white, 1.5)
    roll_button = button.Button(roll_img, 935, 757, "ROLL", black, 2)
    player1_button = button.Button(player1_img, 250, 420, "Icon 1", white, 1)
    player2_button = button.Button(player2_img, 350, 420, "Icon 2", white, 1)
    player3_button = button.Button(player3_img, 450, 420, "Icon 3", white, 1)
    player4_button = button.Button(player4_img, 550, 420, "Icon 4", white, 1)

    # load board positions
    icon_positions = get_icon_positions()

    # Bank accounts
    bank1 = Bank_Account("player1")
    bank2 = Bank_Account("player2")
    bank3 = Bank_Account("player3")
    bank4 = Bank_Account("player4")
    # create player objects
    player1 = player.Player(player1_img, "Player1", bank1, .6, icon_positions)
    player2 = player.Player(player2_img, "Player2", bank2, .6, icon_positions)
    player3 = player.Player(player3_img, "Player3", bank3, .6, icon_positions)
    player4 = player.Player(player4_img, "Player4", bank4, .6, icon_positions)
    players = [player1, player2, player3, player4]
    # load community chest and chance cards
    cards = load_cards()
    # load property cards
    properties = load_properties()

    # created die
    die1 = Die(screen,
               screen.get_width() - screen.get_width() * 0.1 - DICE_DIMS[0] * 1.5,
               screen.get_height() - DICE_DIMS[0] * 1.5,
               DICE_DIMS)
    die2 = Die(screen,
               screen.get_width() - screen.get_width() * 0.1,
               screen.get_height() - DICE_DIMS[0] * 1.5,
               DICE_DIMS)

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

            draw_text(screen, "Welcome to CS205 Project: Ski Resort Monopoly!", large_font, black, 80, 50)
            draw_text(screen, "Press 'esc' to close the program", small_font, black, 25, 750)
            draw_text(screen, 'Game Setup', medium_font, black, 335, 150)

            singleplayer_button.draw(screen)
            multiplayer_button.draw(screen)

            if singleplayer_button.check_click():
                game_singleplayer = True
            if multiplayer_button.check_click():
                game_multiplayer = True

            if game_singleplayer:
                game_multiplayer = False
                num_players = 1
                draw_text(screen, "Number of Computers", medium_font, black, 285, 250)
                num_computers1_button.draw(screen)
                num_computers2_button.draw(screen)
                num_computers3_button.draw(screen)

                # set number of computers
                if num_computers1_button.check_click():
                    num_computers = 3
                if num_computers2_button.check_click():
                    num_computers = 3
                if num_computers3_button.check_click():
                    num_computers = 3

                if num_computers > 0:
                    draw_text(screen, "Choose your Piece", medium_font, black, 305, 350)
                    player1_button.draw(screen)
                    player2_button.draw(screen)
                    player3_button.draw(screen)
                    player4_button.draw(screen)
                    startgame_button.draw(screen)

                    # if startgame button clicked and game setup, move to game screen
                    if startgame_button.check_click():
                        current_screen = 1

            # elif game_multiplayer:
            # game_singleplayer = False
            # draw_text("Number of Players", medium_font, black, 300, 285)
            # draw_text("Number of Computers", medium_font, black, 285, 375)
        elif current_screen == 1:
            board_screen(screen, icon_positions, properties)
            # load roll dice image (eventually only loads during player's turn
            roll_button.draw(screen)
            properties_button.draw(screen)

            player1.draw(screen)
            player2.draw(screen)
            player3.draw(screen)
            player4.draw(screen)

            # For loop iterates over all the players and checks if it is their turn
            for active_player in players:
                active_player.turn = True
                if turn == active_player.name and active_player.turn:
                    # TEST MOVE
                    player1.movement(1)  # moves player1 forward 1 space
                    active_player.turn = True
                    if not is_rolling:
                        active_player.turn = True
                        draw_text(screen, active_player.name, medium_font, black, 900, 700)
                        if keys[pygame.K_SPACE] or roll_button.check_click():  # rolls on a space key or button click
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
                                if turn == "Player1":
                                    turn = "Player2"
                                elif turn == "Player2":
                                    turn = "Player3"
                                elif turn == "Player3":
                                    turn = "Player4"
                                elif turn == "Player4":
                                    turn = "Player1"
                                active_player.turn = False

                        counter += 1
                    die1.draw(screen)
                    die2.draw(screen)

            if keys[pygame.K_c] or properties_button.check_click():  # check if property button screen has been clicked
                current_screen = 2

        elif current_screen == 2:
            card_screen(screen, font)

            if keys[pygame.K_g]:  # press g to return to game
                current_screen = 1

        # Required to update screen
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
