import sys
import pygame
import socket
import pickle

import player
import button
import random
from Bank_Account import Bank_Account
from Die import Die
from Property import Property
from card import Card
from player import Player
from network import Network

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
board_color = (191, 219, 174)
# property region colors
brown = (165, 42, 42)
lightblue = (173, 216, 230)
pink = (255, 192, 203)
orange = (255, 165, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 100, 0)
blue = (30, 144, 225)


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


def create_card(screen, x, y, property):
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
    pygame.draw.rect(screen, property.region, (x + 5, y + 5, 140, 50))
    draw_text(screen, "TITLE DEED", small_font_4, black, x + 40, y + 10)
    draw_text(screen, property.property_name, small_font_2, black, x+20, y+30)
    draw_text(screen, "Rent: $", small_font_3, black, x+40, y+65)
    draw_text(screen, property.rent, small_font_3, black, x+75, y+65)
    draw_text(screen, "With 1 House $", small_font_3, black, x+10, y+85)
    draw_text(screen, property.rent_1house, small_font_3, black, x+85, y+85)
    draw_text(screen, "With 2 Houses $", small_font_3, black, x+10, y+100)
    draw_text(screen, property.rent_2house, small_font_3, black, x+90, y+100)
    draw_text(screen, "With 3 Houses $", small_font_3, black, x+10, y+115)
    draw_text(screen, property.rent_3house, small_font_3, black, x+89, y+115)
    draw_text(screen, "With 4 Houses $", small_font_3, black, x+10, y+130)
    draw_text(screen, property.rent_4house, small_font_3, black, x+90, y+130)
    draw_text(screen, "With Hotel $", small_font_3, black, x+10, y+145)
    draw_text(screen, property.rent_hotel, small_font_3, black, x+71, y+145)
    draw_text(screen, "Houses cost $", small_font_3, black, x+10, y+168)
    draw_text(screen, property.house_price, small_font_3, black, x+78, y+168)
    draw_text(screen, "Hotel costs $", small_font_3, black, x+10, y+180)
    draw_text(screen, property.hotel_price, small_font_3, black, x+73, y+180)


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
    Function to load in property information and create objects of Property class
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


def load_players(screen, total_players, player1, player2, player3, player4, players, new_players):
    player1.draw(screen)
    player2.draw(screen)
    if total_players >= 3:
        players.append(player3)
        new_players.append(player3)
        if total_players == 4:
            players.append(player4)
            new_players.append(player4)

    return players, new_players


def get_icon_positions():
    # trying to find the middle of each space's coordinate spot
    # and put each coordinate into list  clockwise starting at bottom left "GO"
    # first position (start)
    icon_positions = [(35, 765)]
    y_coord = 745
    for i in range(9):
        icon_positions.append((35, 655 - (575 / 9) * i))  # left row of vertical coords
    icon_positions.append((35, 35))  # top left
    for i in range(9):
        icon_positions.append((142 + (575 / 9) * i, 35))  # top row of horizontal coords
    icon_positions.append((765, 35))  # top right
    for i in range(9):
        icon_positions.append((765, 142 + (575 / 9) * i))  # right row of vertical coords
    icon_positions.append((765, 765))  # bottom right
    for i in range(9):
        icon_positions.append((655 - (575 / 9) * i, 765))  # bottom row of horizontal coords
    return icon_positions


# SCREENS
# board screen
def board_screen(screen, icon_positions, properties):
    """
    Function to display the screen with the monopoly board
    :param screen: game screen
    :param icon_positions:
    :param properties:
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
    # center picture
    logo = pygame.image.load("images/ski-resort.png")
    screen.blit(logo, (center_x + 20, center_y + 20))

    # draw the name of each property on the square and district colors
    for property in properties:
        coordinates = str(icon_positions[int(property.location)])
        coordinates_list = coordinates[1:len(coordinates) - 1].split(',')
        x_coord = float(coordinates_list[0])
        y_coord = float(coordinates_list[1])

        # draw in a different spot of the square depend on section of the board
        # up the left side
        if x_coord == 35:
            pygame.draw.rect(screen, property.region, (90, y_coord - 33, 20, 64))
            draw_text(screen, property.property_name, small_font_3, black, x_coord - 34, y_coord)
        # across the top
        if y_coord == 35:
            pygame.draw.rect(screen, property.region, (x_coord - 32, 90, 63.9, 20))
            draw_text(screen, property.property_name, small_font_3, black, x_coord - 25, y_coord + 30)
        # down the right side
        if x_coord == 765:
            pygame.draw.rect(screen, property.region, (685, y_coord - 32, 20, 64))
            draw_text(screen, property.property_name, small_font_3, black, x_coord - 50, y_coord)
        # across the bottom
        if y_coord == 765:
            pygame.draw.rect(screen, property.region, (x_coord - 33, 685, 63.9, 20))
            draw_text(screen, property.property_name, small_font_3, black, x_coord - 25, y_coord - 50)

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


# card screen
def card_screen(screen, font, property_list):
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
    #TODO -- figure out which x and y values we should use based on len(property_list)

    x = 50
    y = 150
    i = 0

    for i in range(0,7):
        # create card
        create_card(screen, x, y, property_list[i])
        x += 160
    x = 50
    y = 360
    for i in range(6,len(property_list)):
        create_card(screen, x, y, property_list[i])
        x += 160


    #create_house(screen, 100, 500)


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
    screens = {
        "START": 1,
        "BOARD": 2,
        "PROPS": 3
    }
    current_screen = screens.get("START")

    is_rolling = False
    counter = 0
    die1_value = -1
    die2_value = -1
    turn = "Player 1"
    players_loaded = False

    # game type variables
    game_singleplayer = False
    game_multiplayer = False
    num_players = 0
    num_computers = 0
    total_players = 0

    # Multiplayer initializations
    ip_address = ""
    input_rect = pygame.Rect(300, 320, 200, 32)
    color_active = pygame.Color('white')
    color_passive = pygame.Color('gray')
    box_color = color_passive
    active = True
    connecting = False
    connected = False
    error = False

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
    bank1 = Bank_Account("Player 1")
    bank2 = Bank_Account("Player 2")
    bank3 = Bank_Account("Player 3")
    bank4 = Bank_Account("Player 4")
    # create player objects
    player1 = Player(player1_img, "Player 1", bank1, .6, icon_positions)
    player2 = Player(player2_img, "Player 2", bank2, .6, icon_positions)
    player3 = Player(player3_img, "Player 3", bank3, .6, icon_positions)
    player4 = Player(player4_img, "Player 4", bank4, .6, icon_positions)
    players = [player1, player2]
    new_players = [player1, player2]

    # initial roll to see who goes first
    first_rolls = []
    first_roll = True

    # load community chest and chance cards
    cards = load_cards()
    # load property cards
    properties = load_properties()

    # TESTING ----
    player1.add_property(properties[0])
    player1.add_property(properties[7])
    player1.add_property(properties[3])
    player1.add_property(properties[4])
    player1.add_property(properties[10])
    player1.add_property(properties[14])
    player1.add_property(properties[9])
    player1.add_property(properties[20])
    player1.add_property(properties[18])




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
            elif event.type == pygame.KEYDOWN and active and game_multiplayer:
                if event.key == pygame.K_BACKSPACE:
                    ip_address = ip_address[:-1]
                elif event.key == pygame.K_RETURN:
                    active = False
                else:
                    ip_address += event.unicode

        # Vector of all keys on keyboard.
        # keys[pygame.K_SPACE] will return True if the space-bar is pressed; False if otherwise
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if current_screen == screens.get("START"):
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
                    num_computers = 1
                if num_computers2_button.check_click():
                    num_computers = 2
                if num_computers3_button.check_click():
                    num_computers = 3

                total_players = num_players + num_computers

                if num_computers > 0:
                    draw_text(screen, "Choose your Piece", medium_font, black, 305, 350)
                    player1_button.draw(screen)
                    player2_button.draw(screen)
                    player3_button.draw(screen)
                    player4_button.draw(screen)
                    startgame_button.draw(screen)

                    # if startgame button clicked and game setup, move to game screen
                    if startgame_button.check_click():
                        current_screen = screens.get("BOARD")

            elif game_multiplayer:
                game_singleplayer = False

                draw_text(screen, "Enter server ip:", medium_font, black, 320, 285)

                if active:
                    box_color = color_active
                else:
                    box_color = color_passive

                pygame.draw.rect(screen, box_color, input_rect)
                draw_text(screen, ip_address, medium_font, black, input_rect.x + 5, input_rect.y + 5)

                if not active and not connecting:
                    # Attempt connection to server
                    connecting = True
                    n = Network(ip_address)
                    if n.get_games() is not None:
                        error = False
                        connected = True
                    else:
                        error = True
                        ip_address = ""
                        active = True
                        connecting = False

                if error:
                    draw_text(screen,
                              "Error connecting to server. Please re-type IP.",
                              medium_font,
                              black,
                              285, 375)

                if connected:
                    games = n.get_games()

                    for i in range(0, len(games)):
                        server_box = pygame.Rect(300, 330 + (32 * i), 200, 32)
                        server_box_color = pygame.Color("gray")
                        if i % 2 == 0:
                            server_box_color = pygame.Color("white")
                        pygame.draw.rect(screen, server_box_color, server_box)
                        draw_text(screen,
                                  "Game #" + str(games[i + 1].get_id()),
                                  medium_font,
                                  black,
                                  server_box.x + 5,
                                  server_box.y + 5)

                    # draw_text(screen,
                    #           "Connected to game #" + str(n.get_game_id() + 1),
                    #           medium_font,
                    #           black,
                    #           285, 375)
                    # draw_text(screen,
                    #           "You are player " + str(n..get_p() + 1),
                    #           medium_font,
                    #           black,
                    #           285, 400)

                    # draw_text(screen, "Number of Computers", medium_font, black, 285, 375)

        elif current_screen == screens.get("BOARD"):
            board_screen(screen, icon_positions, properties)
            # load roll dice image (eventually only loads during player's turn
            roll_button.draw(screen)
            properties_button.draw(screen)
            #display bank account money
            draw_text(screen, "Money: $", medium_font, black, 900, 90)
            if turn == 'Player 1':
                bank_account = player1.bank
            elif turn == 'Player 2':
                bank_account = player2.bank
            elif turn == 'Player 3':
                bank_account = player3.bank
            else:
                bank_account = player4.bank
            draw_text(screen, str(bank_account.total), medium_font, black, 995, 90)

            # (Created once) loads the number of players into each list based on the amount chosen in first screen
            if not players_loaded:
                players, new_players = load_players(screen, total_players, player1, player2, player3, player4,
                                                    players, new_players)
                players_loaded = True
            # draws all active players
            for p in players:
                p.draw(screen)

            # For loop iterates over all the players and checks if it is their turn
            for active_player in players:
                # display instructions if its the first roll
                if first_roll:
                    draw_text(screen, "Determine player order by", medium_font, black, 890, 300)
                    draw_text(screen, "each person rolling the dice once", medium_font, black,
                              850, 330)
                active_player.turn = True
                if turn == active_player.name and active_player.turn:
                    active_player.turn = True
                    if not is_rolling:
                        active_player.turn = True
                        draw_text(screen, str(active_player.name) + "'s turn", medium_font, black, 900, 700)
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
                                roll = die1_value + die2_value
                                # if it's not the first roll, player icon should move number of spaces rolled
                                if not first_roll:
                                    active_player.movement(roll)

                                # FIRST ROLL-----
                                # Have everyone roll once to find out the order of when each person players
                                if first_roll:
                                    first_rolls.append(roll)
                                    # stop when everyone has rolled once
                                    if len(first_rolls) >= 4:
                                        first_roll = False
                                        # find player with largest roll and assign them to have a turn first, continue
                                        for i in range(0, len(players)):
                                            largest = first_rolls.index(max(first_rolls))
                                            new_players[i] = players[largest]
                                            # get rid of the largest element in list
                                            first_rolls[largest] = -1
                                        # reassign player list to the new order
                                        count = 0
                                        for player in new_players:
                                            players[count] = player
                                            count += 1
                                        # DEBUGGING - print new player order
                                        # for player in players:
                                        # print(player.name)

                                die1_value = -1
                                die2_value = -1
                                # change the turn
                                if turn == "Player 1":
                                    # change the turn to the name of the next player in the players list
                                    for i in range(0, len(players)):
                                        if players[i].name == "Player 1" and i < 3:
                                            turn = str(players[i + 1].name)
                                        elif players[i].name == "Player 1" and i == 3:
                                            turn = str(players[0].name)
                                elif turn == "Player 2":
                                    for i in range(0, len(players)):
                                        if players[i].name == "Player 2" and i < 3:
                                            turn = str(players[i + 1].name)
                                        elif players[i].name == "Player 2" and i == 3:
                                            turn = str(players[0].name)
                                elif turn == "Player 3":
                                    for i in range(0, len(players)):
                                        if players[i].name == "Player 3" and i < 3:
                                            turn = str(players[i + 1].name)
                                        elif players[i].name == "Player 3" and i == 3:
                                            turn = str(players[0].name)
                                elif turn == "Player 4":
                                    for i in range(0, len(players)):
                                        if players[i].name == "Player 4" and i < 3:
                                            turn = str(players[i + 1].name)
                                        elif players[i].name == "Player 4" and i == 3:
                                            turn = str(players[0].name)
                                active_player.turn = False

                        counter += 1
                    die1.draw(screen)
                    die2.draw(screen)

            if keys[pygame.K_c] or properties_button.check_click():  # check if property button screen has been clicked
                current_screen = screens.get("PROPS")

        elif current_screen == screens.get("PROPS"):
            #Player 1
            if turn == 'Player 1':
                card_screen(screen, font, player1.property_list)
            elif turn == 'Player 2':
                card_screen(screen, font, player2.property_list)
            elif turn == 'Player 3':
                card_screen(screen, font, player3.property_list)
            else:
                card_screen(screen, font, player4.property_list)


            if keys[pygame.K_g]:  # press g to return to game
                current_screen = screens.get("BOARD")

        # Required to update screen
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
