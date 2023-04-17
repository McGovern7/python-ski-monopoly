import sys
import pygame
import socket
import pickle

import player
import random
from button import Button
from Bank_Account import Bank_Account
from die import Die
from Property import Property
from card import Card
from player import Player
from Railroad import Railroad
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
small_cs_font_1 = pygame.font.SysFont('comicsansms', 14)
small_cs_font_3 = pygame.font.SysFont('comicsansms', 11)
small_cs_font_4 = pygame.font.SysFont('comicsansms', 10)
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
    '''
    Function to draw a house icon on a property
    :param screen: game screen
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :return: nothing
    '''
    house = pygame.image.load('images/home.png')
    screen.blit(house, (x, y))


# hotel graphic
def create_hotel(screen, x, y):
    '''
    Function to draw a hotel icon on a property
    :param screen: game screen
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :return: nothing
    '''
    hotel = pygame.image.load('images/hotel.png')
    screen.blit(hotel, (x, y))


def create_card(screen, x, y, property):
    '''
    Function to create a card graphic for the card screen
    :param screen: game screen
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :param property: property that the card represent
    :return: nothing
    '''
    # draw text on every property card
    pygame.draw.rect(screen, white, (x, y, 150, 200))
    pygame.draw.rect(screen, property.region, (x + 5, y + 5, 140, 50))
    draw_text(screen, 'TITLE DEED', small_font_4, black, x + 40, y + 10)
    draw_text(screen, property.property_name, small_font_2, black, x + 20, y + 30)
    draw_text(screen, 'Rent: $', small_font_3, black, x + 40, y + 65)
    draw_text(screen, property.rent, small_font_3, black, x + 75, y + 65)
    draw_text(screen, 'With 1 House $', small_font_3, black, x + 10, y + 85)
    draw_text(screen, property.rent_1house, small_font_3, black, x + 85, y + 85)
    draw_text(screen, 'With 2 Houses $', small_font_3, black, x + 10, y + 100)
    draw_text(screen, property.rent_2house, small_font_3, black, x + 90, y + 100)
    draw_text(screen, 'With 3 Houses $', small_font_3, black, x + 10, y + 115)
    draw_text(screen, property.rent_3house, small_font_3, black, x + 89, y + 115)
    draw_text(screen, 'With 4 Houses $', small_font_3, black, x + 10, y + 130)
    draw_text(screen, property.rent_4house, small_font_3, black, x + 90, y + 130)
    draw_text(screen, 'With Hotel $', small_font_3, black, x + 10, y + 145)
    draw_text(screen, property.rent_hotel, small_font_3, black, x + 71, y + 145)
    draw_text(screen, 'Houses cost $', small_font_3, black, x + 10, y + 168)
    draw_text(screen, property.house_price, small_font_3, black, x + 78, y + 168)
    draw_text(screen, 'Hotel costs $', small_font_3, black, x + 10, y + 180)
    draw_text(screen, property.hotel_price, small_font_3, black, x + 73, y + 180)


# Function draws text with desired font, color, and location on page
def draw_text(screen, text, font, text_col, x, y):
    '''
    Function to draww text on the game screen
    :param screen: game screen
    :param text: text that will be displayed on-screen
    :param font: font that will be used
    :param text_col: the color of the text
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :return: nothing
    '''
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


def load_properties():
    '''
    Function to load in property information and create objects of Property class
    :return: list of property objects
    '''
    # initialize list to put properties in
    properties = []
    file = open('text/property_cards.txt', 'r')
    lines = file.readlines()
    count = 0
    # Strips the newline character
    for line in lines:
        count += 1
        # DEBUGGING
        # print('Line{}: {}'.format(count, line.strip()))
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
    for line in lines:
        count += 1
        # DEBUGGING
        # print('Line{}: {}'.format(count, line.strip()))
        # split the line by commas
        card_features = line.strip().split(',')
        # create a property object
        new_card = Card(card_features[0], card_features[1], card_features[2], card_features[3])
        cards.append(new_card)

    file.close()
    return cards


def load_players(total_players, player1, player2, player3, player4, unset_players):
    unset_players.append(player1)
    unset_players.append(player2)
    if total_players >= 3:
        unset_players.append(player3)
        if total_players == 4:
            unset_players.append(player4)
    return unset_players


def get_icon_positions():
    # trying to find the middle of each space's coordinate spot
    # and put each coordinate into list  clockwise starting at bottom left 'GO'
    # first position (start)
    icon_positions = [(35, 765)]
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


def buy_pop_up(screen, active_player, message, properties, option):
    # buttons
    roll_img = pygame.image.load('images/roll.png').convert_alpha()
    yes_button = Button(roll_img, 950, 400, 'yes', black, 1)
    no_button = Button(roll_img, 1050, 400, 'no', black, 1)
    # draws pop up message
    pygame.draw.rect(screen, red, (850, 310, 300, 150))
    pygame.draw.rect(screen, white, (860, 320, 280, 130))
    draw_text(screen, message, small_cs_font_1, black, 870, 330)
    yes_button.draw(screen)
    no_button.draw(screen)
    # if 'yes' button is clicked, user buys the property/railroad
    if yes_button.check_click():
        # determine what property player is on
        for property in properties:
            if int(active_player.location) == int(property.location):
                # option 2 is buying a railroad
                if option == 2:
                    active_player.buy_railroad(property)
                    return ''
                    # option 1 is buying a property
                elif option == 1:
                    active_player.buy_property(property)
                    return ''

    # if no button is clicked, user does not buy the property
    if no_button.check_click():
        return ''
    else:
        # if railroad, return railroad opportunity
        if option == 2:
            return 'railroad opportunity'
        # otherwise it's a normal property
        else:
            return 'landlord opportunity'


def card_pop_up(screen, message):
    # buttons
    roll_img = pygame.image.load('images/roll.png').convert_alpha()
    okay_button = Button(roll_img, 950, 400, 'ok', black, 1)
    # draws pop up message
    pygame.draw.rect(screen, red, (850, 310, 300, 150))
    pygame.draw.rect(screen, white, (860, 320, 280, 130))
    # remove 'message' part before printing
    message_edit = message[8:]
    # see if we need to split the string
    if message.find('//') != -1:
        messages = message_edit.split('//')
        draw_text(screen, messages[0], small_cs_font_1, black, 870, 330)
        draw_text(screen, messages[1], small_cs_font_1, black, 870, 350)
    else:
        draw_text(screen, message_edit, small_cs_font_1, black, 870, 330)
    okay_button.draw(screen)
    # if ok button is clicked, player can move on

    if okay_button.check_click():
        return ''
    else:
        return message


def interact(active_player, players, properties, railroads, cards):
    # shuffle the cards!
    random.shuffle(cards)

    # interaction for properties
    for property in properties:
        if int(active_player.location) == int(property.location):
            # check if property is owned by anyone
            if property.owner == 'NONE':
                # send message to call pop-up back to main
                return 'landlord opportunity'
            #if the property is owned by someone, active player must pay owner rent
            else:
                #DEBUGGING
                #print("real landlord: " + property.owner)
                #see who the landlord is
                for landlord in players:
                    if property.owner == landlord.name:
                        #DEBUG
                        #print("landlord chosen: " + landlord.name)
                        active_player.pay_rent(landlord, property.rent)
                        #DEBUG MONEY
                        #bank_l = landlord.bank
                        #print("landlord money now: ", bank_l.total)
                        message = "You paid $" + str(property.rent) + " in rent!"
                        return message


    # interaction for railroads
    for railroad in railroads:
        if int(active_player.location) == int(railroad.location):
            # check if property is owned by anyone
            if railroad.owner == 'NONE':
                # send message to call pop-up back to main
                return 'railroad opportunity'

    # interaction for go to jail spot (send player to jail)
    if int(active_player.location) == 30:
        active_player.go_to_jail()
        return ''
    # interaction for community chest
    if int(active_player.location) == 2 or int(active_player.location) == 17 or int(active_player.location) == 33:
        for card in cards:
            if card.kind == 'Community Chest':
                chosen_card = card
                chosen_card.play(active_player)
                return chosen_card.message

    # interaction for chance
    if int(active_player.location) == 7 or int(active_player.location) == 22 or int(active_player.location) == 36:
        for card in cards:
            if card.kind == 'Chance':
                chosen_card = card
                message = chosen_card.play(active_player)
                return message

    # interaction for tax
    if int(active_player.location) == 4 or int(active_player.location) == 38:
        active_player.pay_taxes()


def change_turn(players, active_player, turn):
    # change the turn
    if turn == 'Player 1':
        # change the turn to the name of the next player in the players list
        for i in range(0, len(players)):
            if players[i].name == 'Player 1' and i < len(players) - 1:
                turn = str(players[i + 1].name)
                new_active_player = players[i + 1]
            elif players[i].name == 'Player 1' and i == len(players) - 1:
                turn = str(players[0].name)
                new_active_player = players[0]
    elif turn == 'Player 2':
        for i in range(0, len(players)):
            if players[i].name == 'Player 2' and i < len(players) - 1:
                turn = str(players[i + 1].name)
                new_active_player = players[i + 1]
            elif players[i].name == 'Player 2' and i == len(players) - 1:
                turn = str(players[0].name)
                new_active_player = players[0]
    elif turn == 'Player 3':
        for i in range(0, len(players)):
            if players[i].name == 'Player 3' and i < len(players) - 1:
                turn = str(players[i + 1].name)
                new_active_player = players[i + 1]
            elif players[i].name == 'Player 3' and i == len(players) - 1:
                turn = str(players[0].name)
                new_active_player = players[0]
    elif turn == 'Player 4':
        for i in range(0, len(players)):
            if players[i].name == 'Player 4' and i < len(players) - 1:
                turn = str(players[i + 1].name)
                new_active_player = players[i + 1]
            elif players[i].name == 'Player 4' and i == len(players) - 1:
                turn = str(players[0].name)
                new_active_player = players[0]

    return turn, new_active_player


# SCREENS
# turn deciding screen
def turn_screen(screen, total_players):
    '''
    Function displaying the screen which decides the turn order of the game
    :param screen: game screen
    :param total_players: the number of active players
    :return: nothing
    '''
    medium_font = pygame.font.SysFont('Verdana', 20)
    screen.fill(lightblue)  # Fill screen background
    pygame.draw.rect(screen, (41, 50, 65), (200, 100, 800, 300))
    pygame.draw.rect(screen, black, (200, 100, 800, 300), 4)
    draw_text(screen, "Roll To Determine Player Order", medium_font, white, 440, 115)
    draw_text(screen, "Higher Rolls Go First", medium_font, white, 500, 140)
    if total_players == 2:
        pygame.draw.rect(screen, white, (480, 175, 80, 80))
        pygame.draw.rect(screen, black, (480, 175, 80, 80), 3)
        pygame.draw.rect(screen, white, (640, 175, 80, 80))
        pygame.draw.rect(screen, black, (640, 175, 80, 80), 3)
    elif total_players == 3:
        pygame.draw.rect(screen, white, (400, 175, 80, 80))
        pygame.draw.rect(screen, black, (400, 175, 80, 80), 3)
        pygame.draw.rect(screen, white, (560, 175, 80, 80))
        pygame.draw.rect(screen, black, (560, 175, 80, 80), 3)
        pygame.draw.rect(screen, white, (720, 175, 80, 80))
        pygame.draw.rect(screen, black, (720, 175, 80, 80), 3)
    elif total_players == 4:
        pygame.draw.rect(screen, white, (320, 175, 80, 80))
        pygame.draw.rect(screen, black, (320, 175, 80, 80), 3)
        pygame.draw.rect(screen, white, (480, 175, 80, 80))
        pygame.draw.rect(screen, black, (480, 175, 80, 80), 3)
        pygame.draw.rect(screen, white, (640, 175, 80, 80))
        pygame.draw.rect(screen, black, (640, 175, 80, 80), 3)
        pygame.draw.rect(screen, white, (800, 175, 80, 80))
        pygame.draw.rect(screen, black, (800, 175, 80, 80), 3)


# board screen
def board_screen(screen, icon_positions, properties, railroads):
    '''
    Function to display the screen with the monopoly board
    :param screen: game screen
    :param icon_positions:
    :param properties:
    :return: nothing
    '''
    large_font = pygame.font.SysFont('Verdana', 25)

    # Fill screen background
    screen.fill((127, 127, 127))
    # draw board
    # full board (outer square)
    pygame.draw.rect(screen, board_color, (0, 0, 795, 795))
    # center square
    center_dimension = 575  # Used for the height and width of the center space
    center_x = 110
    center_y = 110
    pygame.draw.rect(screen, green, (center_x, center_y, center_dimension, center_dimension))
    # center picture
    logo = pygame.image.load('images/ski-resort.png')
    screen.blit(logo, (center_x + 20, center_y + 20))

    house = pygame.image.load("images/home.png")

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
            # name of property
            draw_text(screen, property.property_name, small_cs_font_3, black, x_coord - 34, y_coord - 30)
            # draw the cost to buy property
            draw_text(screen, '$' + str(property.price), small_cs_font_4, black, x_coord, y_coord - 10)

            # logic to print houses down the left side
            houseY = y_coord - 32 + (64 / (property.num_houses + 1)) - 4
            for house in range(property.num_houses):
                pygame.draw.rect(screen, black, (96, houseY, 8, 8))
                houseY += (64 / (property.num_houses + 1))

        # across the top
        if y_coord == 35:
            # color square for region
            pygame.draw.rect(screen, property.region, (x_coord - 32, 90, 63.9, 20))

            # logic to print houses along the top row
            houseX = x_coord - 32 + (64 / (property.num_houses + 1)) - 4
            for house in range(property.num_houses):
                pygame.draw.rect(screen, black, (houseX, 100, 8, 8))
                houseX += (64 / (property.num_houses + 1))

            # if property name has more than two words, display it differently
            if property.property_name.find(' ') > -1:
                name = property.property_name.split(' ')
                draw_text(screen, name[0], small_cs_font_3, black, x_coord - 25, y_coord)
                draw_text(screen, name[1], small_cs_font_3, black, x_coord - 22, y_coord + 15)
                # draw the cost to buy property
                draw_text(screen, '$' + str(property.price), small_cs_font_4, black, x_coord - 20, y_coord + 35)
            else:
                draw_text(screen, property.property_name, small_cs_font_3, black, x_coord - 30, y_coord + 15)
                # draw the cost to buy property
                draw_text(screen, '$' + str(property.price), small_cs_font_4, black, x_coord - 20, y_coord + 35)

        # down the right side
        if x_coord == 765:
            pygame.draw.rect(screen, property.region, (685, y_coord - 32, 20, 64))
            draw_text(screen, property.property_name, small_cs_font_3, black, x_coord - 58, y_coord - 30)
            # draw the cost to buy property
            draw_text(screen, '$' + str(property.price), small_cs_font_4, black, x_coord - 34, y_coord - 10)

            # logic to print houses down the right side
            houseY = y_coord - 32 + (64 / (property.num_houses + 1)) - 4
            for house in range(property.num_houses):
                pygame.draw.rect(screen, black, (688, houseY, 8, 8))
                houseY += (64 / (property.num_houses + 1))

        # across the bottom
        if y_coord == 765:
            pygame.draw.rect(screen, property.region, (x_coord - 33, 685, 63.9, 20))
            draw_text(screen, property.property_name, small_cs_font_3, black, x_coord - 32, y_coord - 55)
            # draw the cost to buy property
            draw_text(screen, '$' + str(property.price), small_cs_font_4, black, x_coord - 24, y_coord - 35)

            # logic to print houses along the bottom row
            houseX = x_coord - 32 + (64 / (property.num_houses + 1)) - 4
            for house in range(property.num_houses):
                pygame.draw.rect(screen, black, (houseX, 688, 8, 8))
                houseX += (64 / (property.num_houses + 1))

    #print railroads
    tbar = pygame.image.load("images/tbar.png")
    quad = pygame.image.load("images/quad.png")
    tram = pygame.image.load("images/tram.png")
    gondola = pygame.image.load("images/gondola.png")
    for railroad in railroads:
        coordinates = str(icon_positions[int(railroad.location)])
        coordinates_list = coordinates[1:len(coordinates) - 1].split(',')
        x_coord = float(coordinates_list[0])
        y_coord = float(coordinates_list[1])
        # up the left side
        if x_coord == 35:
            screen.blit(tbar, (x_coord, y_coord-25))
            draw_text(screen, railroad.name, small_cs_font_3, black, x_coord - 32, y_coord-30)
        # across the top
        elif y_coord == 35:
            screen.blit(quad, (x_coord-25, y_coord+5))
            # if railroad name has more than two words, display it differently
            if railroad.name.find(' ') > -1:
                name = railroad.name.split(' ')
                draw_text(screen, name[0], small_cs_font_3, black, x_coord - 30, y_coord - 30)
                draw_text(screen, name[1], small_cs_font_3, black, x_coord - 22, y_coord - 15)
            else:
                draw_text(screen, railroad.name, small_cs_font_3, black, x_coord - 32, y_coord - 30)
        # down the right side
        elif x_coord == 765:
            screen.blit(tram, (x_coord - 45, y_coord - 25))
            draw_text(screen, railroad.name, small_cs_font_3, black, x_coord - 70, y_coord - 30)
        #across the bottom
        else:
            screen.blit(gondola, (x_coord - 25, y_coord - 45))
            draw_text(screen, railroad.name, small_cs_font_3, black, x_coord - 32, y_coord - 70)

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

    # tax squares
    draw_text(screen, 'TAX', small_cs_font_4, black, 75, 463)
    draw_text(screen, 'TAX', small_cs_font_4, black, 208, 725)

    # chance
    chance_logo = pygame.image.load("images/chance.png")
    chance_logo2 = pygame.image.load("images/chance2.png")
    chance_logo3 = pygame.image.load("images/chance3.png")
    screen.blit(chance_logo, (694, 158))
    screen.blit(chance_logo2, (7, 223))
    screen.blit(chance_logo3, (287, 694))

    # community chest

    # free parking
    draw_text(screen, 'Free', small_cs_font_4, black, 705, 10)
    parking = pygame.image.load("images/freeParking.png")
    draw_text(screen, 'Parking', small_cs_font_4, black, 705, 80)
    screen.blit(parking, (705, 25))


# card screen
def card_screen(screen, font, property_list):
    '''
    Function to display a screen that shows you cards and gives more details about your properties
    :param screen: game screen
    :param font: font of the text
    :return: nothing
    '''
    pygame.display.set_caption('Your cards')
    screen.fill(green)
    draw_text(screen, 'Properties: ', font, white, 50, 20)

    x = 50
    y = 150
    i = 0

    if len(property_list) > 7:
        for i in range(0, 7):
            # create card
            create_card(screen, x, y, property_list[i])
            x += 160

        x = 50
        y = 360
        for i in range(6, len(property_list)):
            create_card(screen, x, y, property_list[i])
            x += 160
    else:
        for property in property_list:
            create_card(screen, x, y, property)
            x += 160

    # create_house(screen, 100, 500)


def main():
    '''
    Main function to run the game
    :return: nothing
    '''

    # Constants
    DICE_DIMS = (40, 40)
    TEST_DICE = True

    # Initializations
    # Title and Icon
    pygame.display.set_caption('Monopoly | Ski Resort Edition')
    icon = pygame.image.load('images/ski-resort.png')
    pygame.display.set_icon(icon)
    # make screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screens = {
        'START': 1,
        'DECIDE_TURN': 2,
        'BOARD': 3,
        'PROPS': 4
    }
    current_screen = screens.get('START')

    is_rolling = False
    has_rolled = False
    counter = 0
    die1_value = -1
    die2_value = -1
    players_loaded = False

    # game type variables
    game_singleplayer = False
    game_multiplayer = False
    num_players = 0
    num_computers = 0
    total_players = 0

    # Multiplayer initializations
    ip_address = ''
    input_rect = pygame.Rect(SCREEN_WIDTH / 2 - 100, 300, 200, 32)
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
    singleplayer_img = pygame.image.load('images/singleplayer.png').convert_alpha()
    multiplayer_img = pygame.image.load('images/multiplayer.png').convert_alpha()
    startgame_img = pygame.image.load('images/startgame.png').convert_alpha()
    number_img = pygame.image.load('images/numplayer.png').convert_alpha()
    properties_img = pygame.image.load('images/properties.png').convert_alpha()
    board_return_img = pygame.image.load('images/board-return.png').convert_alpha()
    roll_img = pygame.image.load('images/roll.png').convert_alpha()
    icon1_img = pygame.image.load('images/icon1.png').convert_alpha()
    icon2_img = pygame.image.load('images/icon2.png').convert_alpha()
    icon3_img = pygame.image.load('images/icon3.png').convert_alpha()
    icon4_img = pygame.image.load('images/icon4.png').convert_alpha()

    # draw buttons
    singleplayer_button = Button(singleplayer_img, 500, 210, 'Single-Player', white, 1)
    multiplayer_button = Button(multiplayer_img, 700, 210, 'Multi-Player', white, 1)
    startgame_button = Button(startgame_img, 600, 500, 'Start Game', white, 1)
    num_computers1_button = Button(number_img, 525, 310, '1', white, 1.5)
    num_computers2_button = Button(number_img, 600, 310, '2', white, 1.5)
    num_computers3_button = Button(number_img, 675, 310, '3', white, 1.5)
    properties_button = Button(properties_img, 1000, 50, 'Inspect Properties', white, 1.5)
    board_return_button = Button(board_return_img, 1000, 50, 'Return to Board', white, 1.5)
    roll_button = Button(roll_img, 935, 757, 'ROLL', black, 2)
    turn_roll_button = Button(roll_img, 600, 370, 'ROLL', black, 2)
    end_button = Button(singleplayer_img, 970, 680, 'END TURN', black, .75)
    icon1_button = Button(icon1_img, 450, 420, 'Icon 1', white, 1)
    icon2_button = Button(icon2_img, 550, 420, 'Icon 2', white, 1)
    icon3_button = Button(icon3_img, 650, 420, 'Icon 3', white, 1)
    icon4_button = Button(icon4_img, 750, 420, 'Icon 4', white, 1)

    # load board positions
    icon_positions = get_icon_positions()

    # Bank accounts
    bank1 = Bank_Account('Player 1')
    bank2 = Bank_Account('Player 2')
    bank3 = Bank_Account('Player 3')
    bank4 = Bank_Account('Player 4')
    # create player objects
    player1 = Player(icon1_img, 'Player 1', bank1, .6, icon_positions)
    player2 = Player(icon2_img, 'Player 2', bank2, .6, icon_positions)
    player3 = Player(icon3_img, 'Player 3', bank3, .6, icon_positions)
    player4 = Player(icon4_img, 'Player 4', bank4, .6, icon_positions)

    # turn screen variables
    square_distance = 160
    unset_players = []  # array of players created in load_players
    players = []  # array of players w/ decided order
    turn_index = 0
    turn_rolls = []  # the holding the roll number of each unset_player
    turn = 'Player 1'

    result = '' #start with there being no results from an interaction (no pop-ups)
    # load community chest and chance cards
    cards = load_cards()
    # load property cards
    properties = load_properties()
    # create railroad cards
    railroads = [Railroad('Locke Mountain T-bar', 5),
                 Railroad('Bonaventure Quad', 15),
                 Railroad('Aerial Tramway', 25),
                 Railroad('Gondola One', 35)]

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

        if current_screen == screens.get('START'):
            # game_singleplayer, game_multiplayer = start_screen(screen, game_singleplayer, game_multiplayer)
            # Fill screen background
            screen.fill((135, 206, 235))

            draw_text(screen, 'Welcome to CS205 Project: Ski Resort Monopoly!', large_font, black, 290, 50)
            draw_text(screen, 'Press \'esc\' to close the program', small_font, black, 25, 750)
            draw_text(screen, 'Game Setup', medium_font, black, 540, 150)

            singleplayer_button.draw(screen)
            multiplayer_button.draw(screen)

            if singleplayer_button.check_new_press():
                if singleplayer_button.check_click():
                    game_singleplayer = True
            if multiplayer_button.check_new_press():
                if multiplayer_button.check_click():
                    game_multiplayer = True

            if game_singleplayer:
                game_multiplayer = False
                num_players = 1
                draw_text(screen, 'Number of Computers', medium_font, black, 490, 250)
                num_computers1_button.draw(screen)
                num_computers2_button.draw(screen)
                num_computers3_button.draw(screen)

                # set number of computers
                if num_computers1_button.check_new_press():
                    if num_computers1_button.check_click():
                        num_computers = 1
                if num_computers2_button.check_new_press():
                    if num_computers2_button.check_click():
                        num_computers = 2
                if num_computers3_button.check_new_press():
                    if num_computers3_button.check_click():
                        num_computers = 3

                total_players = num_players + num_computers

                if num_computers > 0:
                    draw_text(screen, 'Choose your Piece', medium_font, black, 510, 350)
                    icon1_button.draw(screen)
                    icon2_button.draw(screen)
                    icon3_button.draw(screen)
                    icon4_button.draw(screen)
                    if icon1_button.check_new_press():  # check if buttons clicked & ensure players don't share icons
                        if icon1_button.check_click():
                            player1.player_icon = icon1_img
                    if icon2_button.check_new_press():
                        if icon2_button.check_click():
                            player1.player_icon = icon2_img
                            player2.player_icon = icon1_img
                    if icon3_button.check_new_press():
                        if icon3_button.check_click():
                            player1.player_icon = icon3_img
                            player3.player_icon = icon1_img
                    if icon4_button.check_new_press():
                        if icon4_button.check_click():
                            player1.player_icon = icon4_img
                            player4.player_icon = icon1_img

                    startgame_button.draw(screen)

                    # if startgame button clicked and game setup, move to game screen
                    if startgame_button.check_new_press():
                        if startgame_button.check_click():
                            current_screen = screens.get('DECIDE_TURN')

            elif game_multiplayer:
                game_singleplayer = False

                draw_text(screen, 'Enter server ip:', medium_font, black, 320, 260)

                if active:
                    box_color = color_active
                else:
                    box_color = color_passive

                pygame.draw.rect(screen, box_color, input_rect)
                pygame.draw.rect(screen, pygame.Color('black'), input_rect, 3, 1)
                draw_text(screen, ip_address, medium_font, black, input_rect.x + 5, input_rect.y + 4)

                message = ''
                if not active and not connecting:
                    # Attempt connection to server
                    connecting = True
                    draw_text(screen,
                              'Loading...',
                              medium_font,
                              black,
                              285, 375)
                    # Bad style
                    pygame.display.update()
                    n = Network(ip_address)
                    if n.get_games() is None:
                        message = 'Error connecting to server. Please re-type IP.'
                        error = True
                        ip_address = ''
                        active = True
                        connecting = False
                    elif n.get_games() == 'full':
                        message = 'Server is full. Please wait for a spot.'
                        error = True
                        ip_address = ''
                        active = True
                        connecting = False
                    else:
                        error = False
                        connected = True

                if error:
                    draw_text(screen, message, medium_font, black, 285, 375)

                if connected:
                    games = n.get_games()

                    # for i in range(0, len(games)):
                    #     server_box = pygame.Rect(300, 360 + (32 * i), 200, 32)
                    #     server_box_color = pygame.Color('gray')
                    #     if i % 2 == 0:
                    #         server_box_color = pygame.Color('white')
                    #     pygame.draw.rect(screen, server_box_color, server_box)
                    #     draw_text(screen,
                    #               'Game #' + str(games[i].get_id() + 1),
                    #               medium_font,
                    #               black,
                    #               server_box.x + 5,
                    #               server_box.y + 5)

                    draw_text(screen, 'Choose your Piece', medium_font, black, 305, 350)
                    icon1_button.draw(screen)  # instead of player1_button renamed to icon1_button
                    icon2_button.draw(screen)
                    icon3_button.draw(screen)
                    icon4_button.draw(screen)
                    startgame_button.draw(screen)

        elif current_screen == screens.get('DECIDE_TURN'):
            turn_screen(screen, total_players)
            # (Created once) loads the number of players into each list based on the amount chosen in first screen
            if not players_loaded:
                unset_players = load_players(total_players, player1, player2, player3, player4, unset_players)
                players_loaded = True
            i = 0
            for p in unset_players:  # draw the icons into the squares
                if total_players == 2:
                    screen.blit(p.player_icon, (500 + i, 190))
                    i += square_distance
                elif total_players == 3:
                    screen.blit(p.player_icon, (420 + i, 190))
                    i += square_distance
                elif total_players == 4:
                    screen.blit(p.player_icon, (340 + i, 190))
                    i += square_distance
            for active_player in unset_players:  # determine the order by having each player roll
                for num in range(0, len(turn_rolls)):  # - prints rolled number under icon
                    if total_players == 2:
                        draw_text(screen, str(turn_rolls[num]), medium_font, white, 510 + num * square_distance, 268)
                    if total_players == 3:
                        draw_text(screen, str(turn_rolls[num]), medium_font, white, 435 + num * square_distance, 268)
                    if total_players == 4:
                        draw_text(screen, str(turn_rolls[num]), medium_font, white, 350 + num * square_distance, 268)
                if turn == active_player.name:
                    if not is_rolling:
                        if not has_rolled:
                            if total_players == 2:
                                draw_text(screen, str(active_player.name) + '\'s Turn', medium_font, white, 450 + turn_index, 268)
                            if total_players == 3:
                                draw_text(screen, str(active_player.name) + '\'s Turn', medium_font, white, 370 + turn_index, 268)
                            if total_players == 4:
                                draw_text(screen, str(active_player.name) + '\'s Turn', medium_font, white, 290 + turn_index, 268)
                            turn_roll_button.draw(screen)
                            if keys[pygame.K_SPACE]:  # rolls on a space key or button click
                                counter = 0
                                is_rolling = True
                            if turn_roll_button.check_new_press():
                                if turn_roll_button.check_click():
                                    counter = 0
                                    is_rolling = True
                        else:
                            turn_index += square_distance
                            if turn_index == square_distance * len(unset_players):  # returns player text to beginning
                                turn_index = 0
                            turn, active_player = change_turn(unset_players, active_player, turn)
                            has_rolled = False
                            if len(turn_rolls) == len(unset_players):
                                # reassign player list to the new order
                                for j in range(0, len(unset_players)):
                                    largest = turn_rolls.index(max(turn_rolls))
                                    players.append(unset_players[largest])  # appends correct player to empty list
                                    turn_rolls[largest] = -1  # get rid of the largest element in list
                                turn = players[0].name
                                active_player = players[0]
                                current_screen = screens.get('BOARD')
                    else:
                        if die1_value == -1:
                            die1_value = die1.roll(counter)
                        if die2_value == -1:
                            die2_value = die2.roll(counter)
                        if die1_value != -1 and die2_value != -1:
                            # Both dice are done rolling
                            has_rolled = True
                            # Return the dice to the start
                            if not die1.at_start:
                                die1.reset()
                            if not die2.at_start:
                                die2.reset()
                            if die1.at_start and die2.at_start:
                                # Both dice are at the start. Reset values
                                is_rolling = False
                                turn_roll = die1_value + die2_value
                                turn_rolls.append(turn_roll)

                                die1_value = -1
                                die2_value = -1
                        counter += 1
                    die1.draw(screen)
                    die2.draw(screen)

        elif current_screen == screens.get('BOARD'):
            board_screen(screen, icon_positions, properties, railroads)
            properties_button.draw(screen)

            # display bank account money
            draw_text(screen, 'Money: $', medium_font, black, 900, 90)
            if turn == 'Player 1':
                bank_account = player1.bank
            elif turn == 'Player 2':
                bank_account = player2.bank
            elif turn == 'Player 3':
                bank_account = player3.bank
            else:
                bank_account = player4.bank
            draw_text(screen, str(bank_account.total), medium_font, black, 995, 90)

            for p in players:
                p.draw(screen)
            #DEBUGGING
            # draw_text(screen, 'player ' + str(active_player.name), medium_font, black, 900, 300)
            # draw_text(screen, 'bank ' + str(bank_account.total), medium_font, black, 900, 400)
            # draw_text(screen, 'location ' + str(active_player.location), medium_font, black, 900, 500)
            # draw_text(screen, 'properties ' + str(active_player.property_list), medium_font, black, 900, 600)

            # print pop-ups if needed
            if result == 'landlord opportunity':
                result = buy_pop_up(screen, active_player, 'Would you like to buy this property?', properties, 1)
            elif result == 'railroad opportunity':
                result = buy_pop_up(screen, active_player, 'Would you like to buy this railroad?', railroads, 2)
            elif str(result)[:8] == 'message:':
                result = card_pop_up(screen, result)
            elif str(result)[:3] == 'You':
                draw_text(screen, result, medium_font, black, 900, 300)

            #dice and turn
            if turn == active_player.name:
                if not is_rolling:
                    draw_text(screen, str(active_player.name) + '\'s turn', medium_font, black, 900, 700)
                    if not has_rolled:
                        roll_button.draw(screen)
                        if keys[pygame.K_SPACE]:  # rolls on a space key or button click
                            counter = 0
                            is_rolling = True
                        if roll_button.check_new_press():
                            if roll_button.check_click():
                                counter = 0
                                is_rolling = True
                    else:
                        end_button.draw(screen)
                        if end_button.check_new_press():
                            if end_button.check_click():  # rolls on a space key or button click
                                #change the turn once player hit the end button
                                turn, active_player = change_turn(players, active_player, turn)
                                has_rolled = False
                else:
                    # A die_value of -1 indicates the die is not done rolling.
                    # Otherwise, roll() returns a random value from 1 to 6.
                    if die1_value == -1:
                        die1_value = die1.roll(counter)
                    if die2_value == -1:
                        die2_value = die2.roll(counter)
                    if die1_value != -1 and die2_value != -1:
                        # Both dice are done rolling
                        has_rolled = True

                        # Return the dice to the start
                        if not die1.at_start:
                            die1.reset()
                        if not die2.at_start:
                            die2.reset()
                        if die1.at_start and die2.at_start:
                            # Both dice are at the start. Reset values
                            is_rolling = False
                            print('You rolled a', die1_value + die2_value)
                            roll = die1_value + die2_value
                            # TODO -- test spaces here by changing the roll value
                            roll = 11
                            # player icon moves number of spaces rolled
                            active_player.movement(roll)
                            # interact with that spot on the board
                            result = interact(active_player, players, properties, railroads, cards)

                            die1_value = -1
                            die2_value = -1

                    counter += 1
                die1.draw(screen)
                die2.draw(screen)

            if keys[pygame.K_c]:  # press c to go to property screen
                current_screen = screens.get('PROPS')
            if properties_button.check_new_press():
                if properties_button.check_click():  # click to move to property screen
                    current_screen = screens.get('PROPS')

        elif current_screen == screens.get('PROPS'):
            # Player 1
            if turn == 'Player 1':
                card_screen(screen, font, player1.property_list)
            elif turn == 'Player 2':
                card_screen(screen, font, player2.property_list)
            elif turn == 'Player 3':
                card_screen(screen, font, player3.property_list)
            else:
                card_screen(screen, font, player4.property_list)
            board_return_button.draw(screen)
            if keys[pygame.K_g]:  # press g to return to game
                current_screen = screens.get('BOARD')
            if board_return_button.check_new_press():
                if board_return_button.check_click():  # click to move to board screen
                    current_screen = screens.get('BOARD')

        # Required to update screen
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
