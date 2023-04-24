import sys
import pygame
from button import Button
from button_group import ButtonGroup
from die import Die
from Property import Property
from card import Card
from player import Player
from Other_Cards import Railroad
from Other_Cards import Utility
from network import Network


# Initialize PyGame
pygame.init()

# Constants
FONT_NAME = 'timesnewroman'
font = pygame.font.SysFont(FONT_NAME, 30)
small_font_1 = pygame.font.SysFont(FONT_NAME, 16)
small_font_2 = pygame.font.SysFont(FONT_NAME, 15)
small_font_3 = pygame.font.SysFont(FONT_NAME, 12)
small_font_4 = pygame.font.SysFont(FONT_NAME, 10)
small_cs_font_1 = pygame.font.SysFont('comicsansms', 14)
small_cs_font_3 = pygame.font.SysFont('comicsansms', 11)
small_cs_font_4 = pygame.font.SysFont('comicsansms', 10)
corner_font = pygame.font.SysFont('comicsansms', 20)
small_v_font = pygame.font.SysFont('Verdana', 15)
medium_v_font = pygame.font.SysFont('Verdana', 20)
large_v_font = pygame.font.SysFont('Verdana', 25)
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
blue = (30, 144, 225)


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


def create_other_card(screen, x, y, object_name, type):
    '''
    Function to create a railroad/utiilies card
    :param screen: game screen
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :param object_name: name of railroad/ utility that the card will represent
    :param type: either railroad or utility
    :return: nothing
    '''
    # draw this on every card
    pygame.draw.rect(screen, white, (x, y, 150, 200))
    # name of object
    draw_text(screen, '____________________________', small_font_4, black, x + 5, y + 70)
    draw_text(screen, str(object_name).upper(), small_font_3, black, x + 2, y + 85)
    draw_text(screen, '____________________________', small_font_4, black, x + 5, y + 90)

    # specific things drawn for railroads only
    if type == 'railroad':
        # image on each card
        lift = pygame.image.load('images/ski-lift.png')
        screen.blit(lift, (x + 50, y + 10))
        # info on each card
        draw_text(screen, 'Rent                              $25', small_font_3, black, x + 5, y + 110)
        draw_text(screen, 'Rent if 2 lifts are owned $50', small_font_3, black, x + 5, y + 130)
        draw_text(screen, 'Rent      \"      \"      \"       $75', small_font_3, black, x + 5, y + 150)
        draw_text(screen, 'Rent      \"      \"      \"       $100', small_font_3, black, x + 5, y + 170)

    # specific things drawn for utilities only
    else:
        # image on each card
        lift = pygame.image.load('images/blower.png')
        screen.blit(lift, (x + 50, y + 15))
        # info on each card
        draw_text(screen, 'If one \"Utility\" owned rent', small_font_3, black, x + 5, y + 110)
        draw_text(screen, 'is 4 times amount on dice', small_font_3, black, x + 5, y + 130)
        draw_text(screen, 'If both \"Utilities\" owned rent', small_font_3, black, x + 5, y + 150)
        draw_text(screen, 'is 10 times amount on dice', small_font_3, black, x + 5, y + 170)


def create_jail_free_card(screen, x, y):
    '''
    Function to draw a get out of jail free card
    :param screen: screen
    :param x: x coordinate
    :param y: y coordinate
    :return:
    '''
    pygame.draw.rect(screen, white, (x, y, 200, 150))
    lift = pygame.image.load('images/escape.png')
    screen.blit(lift, (x + 120, y + 50))
    draw_text(screen, 'Chance', small_font_3, black, x + 25, y + 30)
    draw_text(screen, 'GET OUT OF JAIL', small_font_3, black, x + 15, y + 60)
    draw_text(screen, 'FREE', small_font_3, black, x + 25, y + 75)
    draw_text(screen, 'This card may be kept until needed', small_font_4, black, x + 25, y + 120)


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


def draw_text_center(screen, text, font, text_col, y):
    """
    Function to draw text centered horizontally on the game screen
    :param screen: game screen
    :param text: text that will be displayed on-screen
    :param font: font that will be used
    :param text_col: the color of the text
    :param x: x coordinate where icon will be drawn
    :param y: y coordinate where icon will be drawn
    :return: nothing
    """
    img = font.render(text, True, text_col)
    screen.blit(img, (screen.get_width() / 2 - img.get_width() / 2, y))


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
    '''
    Function to load all the community chest/chance cards
    :return:
    '''
    cards = []
    file = open('text/cards.txt', 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        count += 1
        # split the line by commas
        card_features = line.strip().split(',')
        # create a property object
        new_card = Card(card_features[0], card_features[1], card_features[2], card_features[3])
        cards.append(new_card)

    file.close()
    return cards


def load_players(total_players, player1, player2, player3, player4, unset_players):
    '''
    Function to load the players
    :param total_players:
    :param player1:
    :param player2:
    :param player3:
    :param player4:
    :param unset_players:
    :return:
    '''
    unset_players.append(player1)
    unset_players.append(player2)
    if total_players >= 3:
        unset_players.append(player3)
        if total_players == 4:
            unset_players.append(player4)
    return unset_players


def get_icon_positions():
    '''
    Function to set the coordinates for the middle of each spot on the board
    :return: the coordinates in a list
    '''
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

def mortgage_card(screen, card, active_player, mortgage_buttons, unmortgage_buttons, card_idx, start_x, start_y):
    '''
    :param screen:
    :param card:
    :param active_player:
    :param mortgage_buttons:
    :param unmortgage_buttons:
    :param card_idx:
    :param start_x:
    :param start_y:
    :return:
    '''
    button_x_offset = start_x + 75
    button_y_offset = start_y + 225
    mortgage_img = pygame.image.load('images/mortgage.png').convert_alpha()
    unmortgage_img = pygame.image.load('images/mortgage.png').convert_alpha()
    mortgage_buttons.append(Button(mortgage_img, button_x_offset, button_y_offset, 'Mortgage', white, 1))
    unmortgage_buttons.append(Button(unmortgage_img, button_x_offset, button_y_offset, 'Unmortgage', white, 1))
    if not card.mortgaged:
        mortgage_buttons[card_idx].draw(screen)
        if mortgage_buttons[card_idx].check_click():
            card.mortgage(active_player.bank)
    else:
        unmortgage_buttons[card_idx].draw(screen)
        if unmortgage_buttons[card_idx].check_click():
            card.remove_mortgage(active_player.bank)
    return mortgage_buttons, unmortgage_buttons


def buy_sell_house(screen, card, active_player, house_buttons, card_idx, start_x, start_y):
    '''
    Function to buy or sell a house
    :param screen: screen
    :param card: the property card you might buy a hotel on
    :param active_player: the player whose turn it is
    :param house_buttons: the button where you can select if you want to buy a house
    :param card_idx: the index of the card
    :param start_x: the x coordinate of the first card
    :param start_y: the y coordinate of the first card
    :return:
    '''
    button_x_offset = start_x + 36
    button_y_offset = start_y + 270
    house_button_img = pygame.image.load('images/house_button.png').convert_alpha()
    house_buttons.append(Button(house_button_img, button_x_offset, button_y_offset, 'House', white, 1))
    card.part_of_monopoly = True
    if not card.mortgaged and card.part_of_monopoly and card.num_houses < 4 and card.num_hotels == 0:
        house_buttons[card_idx].draw(screen)
        if house_buttons[card_idx].check_click():
            card.buy_house(active_player.bank)

    return house_buttons


def buy_sell_hotel(screen, card, active_player, hotel_buttons, card_idx, start_x, start_y):
    '''
    Function to buy or sell a hotel
    :param screen: screen
    :param card: the property card that you might buy a hotel on
    :param active_player: the player whose turn it is
    :param hotel_buttons: the button that says hotel
    :param card_idx: index of the card
    :param start_x: the x coordinate of the first card
    :param start_y: the y coordinate of the first card
    :return:
    '''
    button_x_offset = start_x + 114
    button_y_offset = start_y + 270
    hotel_button_img = pygame.image.load('images/hotel_button.png').convert_alpha()
    hotel_buttons.append(Button(hotel_button_img, button_x_offset, button_y_offset, 'Hotel', white, 1))
    if not card.mortgaged and card.part_of_monopoly and card.num_houses == 4 and card.num_hotels == 0:
        hotel_buttons[card_idx].draw(screen)
        if hotel_buttons[card_idx].clicked:
            hotel_buttons[card_idx].clicked = False
            card.buy_hotel(active_player.bank)

    return hotel_buttons

def buy_pop_up(screen, active_player, message, properties, option, yes_button, no_button):
    '''
    Function to create a pop-up when a player lands on a property to see if they want to buy is
    :param screen: screen
    :param active_player: player whose turn it is
    :param message: message to display
    :param properties: all the properties in the game
    :param option: option 1 is for properties, option 2 is for railroads, option 3 is for utilities
    :param yes_button: button to say yes to buying
    :param no_button: button to deny buying
    :return:
    '''
    # option 1 is for properties, option 2 is for railroads, option 3 is for utilities
    # draws pop up message (only if player is human)
    if not active_player.computer:
        pygame.draw.rect(screen, red, (850, 210, 300, 150))
        pygame.draw.rect(screen, white, (860, 220, 280, 130))
        draw_text(screen, message, small_cs_font_1, black, 875, 240)
        yes_button.show()
        yes_button.draw(screen)
        no_button.show()
        no_button.draw(screen)
        for property in properties:  # draws property landed on
            if int(active_player.location) == int(property.location):
                # if option 1, create card
                if option == 1:
                    create_card(screen, 900, 400, property)
                # if option 2, create other card (railroad)
                elif option == 3:
                    create_other_card(screen, 900, 400, property.name, 'railroad')
                # if option 3, create other card (utility)
                else:
                    create_other_card(screen, 900, 400, property.name, 'utility')
    # PLAYER CHOICE (click yes or no for buying)
    if active_player.computer:
        # computer always buys property -- (automatic yes)
        # determine what property player is on and delay a little so human can read what they buy
        for property in properties:
            if int(active_player.location) == int(property.location):
                # option 1 is buying a property
                if option == 1:
                    active_player.buy_property(property)
                    return ''
                # option 2 is buying a railroad
                elif option == 2:
                    active_player.buy_railroad(property)
                    return ''
                # option 3 is buying a utility
                else:
                    active_player.buy_utility(property)
                    return ''
    # player must interact with buttons to move on
    else:
        # if 'yes' button is clicked, user buys the property/railroad
        if yes_button.clicked:
            yes_button.clicked = False
            # determine what property player is on
            for property in properties:
                if int(active_player.location) == int(property.location):
                    # option 1 is buying a property
                    if option == 1:
                        active_player.buy_property(property)
                        return ''
                    # option 2 is buying a railroad
                    elif option == 2:
                        active_player.buy_railroad(property)
                        return ''
                    # option 3 is buying a utility
                    else:
                        active_player.buy_utility(property)
                        return ''

        # if no button is clicked, user does not buy the property
        if no_button.clicked:
            no_button.clicked = False
            return ''
        else:
            # if property, return landlord opportunity
            if option == 1:
                return 'landlord opportunity'
            # if railroad, return railroad opportunity
            elif option == 2:
                return 'railroad opportunity'
            # if utility, return utility opportunity
            else:
                return 'utility opportunity'

def card_pop_up(screen, active_player, message, okay_button):
    '''
    Function to create a pop-up for the player to interact with the card pulled
    :param screen: screen played on
    :param active_player: player whose turn it is
    :param message: message that the card holds
    :param okay_button: button to get rid of the pop-up
    :return: message to trigger pop-up
    '''
    #only show pop up if player is human
    if not active_player.computer:
        # draws pop up message
        pygame.draw.rect(screen, red, (850, 210, 300, 150))
        pygame.draw.rect(screen, white, (860, 220, 280, 130))
        # remove 'message' part before printing
        message_edit = message[8:]
        # see if we need to split the string
        if message.find('//') != -1:
            messages = message_edit.split('//')
            draw_text(screen, messages[0], small_cs_font_1, black, 875, 240)
            draw_text(screen, messages[1], small_cs_font_1, black, 875, 260)
        else:
            draw_text(screen, message_edit, small_cs_font_1, black, 875, 240)
        okay_button.show()
        okay_button.draw(screen)
    # PLAYER CHOICE (click okay button to move on)
    if active_player.computer:
        return ''
    # human must actually hit the okay button to move on
    else:
        # if ok button is clicked, player can move on
        if okay_button.clicked:
            okay_button.clicked = False
            return ''
        else:
            return message


def jail_pop_up(screen, active_player, yes_button, no_button):
    '''
    Function to create a pop-up for the player to interact with about being in jail
    :param screen: screen
    :param active_player: player whose turn it is
    :param yes_button: button to hit yes
    :param no_button: button to hit no
    :return: message to trigger pop-up
    '''
    #only show pop-up if player is human
    if not active_player.computer:
        # draws pop up message
        pygame.draw.rect(screen, red, (850, 210, 300, 150))
        pygame.draw.rect(screen, white, (860, 220, 280, 130))
        draw_text(screen, "Do you want to pay $50 to get out of jail?", small_cs_font_1, black, 865, 240)
        yes_button.show()
        yes_button.draw(screen)
        no_button.show()
        no_button.draw(screen)
    # PLAYER CHOICE (pay to get out of jail)
    if active_player.computer:
        # computer will automatically pay to get out of jail
        # wait a little so human can read
        # pygame.time.delay(60)
        bank = active_player.bank
        bank.withdraw(50)
        active_player.jail = False
        return ''
    # player must hit yes or no to move on
    else:
        # if 'yes' button is clicked, user pays 50 to get out of jail
        if yes_button.clicked:
            yes_button.clicked = False
            bank = active_player.bank
            bank.withdraw(50)
            active_player.jail = False
            return ''

        # if no button is clicked, user does not buy the property
        if no_button.clicked:
            no_button.clicked = False
            return ''
        else:
            return 'jail'


def interact(active_player, players, properties, railroads, utilities, dice_roll, cards):
    '''
    Function to make the icon interact with the square
    :param active_player: the player whose turn it is
    :param players: all the players in the game
    :param properties: all the properties a player owns
    :param railroads: the railroads a player owns
    :param utilities: the utilities a player owns
    :param dice_roll: the roll the player just had
    :param cards: the cards in the game
    :return: a message about which pop-up to show
    '''
    #shuffle the cards!
    #random.shuffle(cards)

    # interaction for properties
    for property in properties:
        if int(active_player.location) == int(property.location):
            # check if property is owned by anyone
            if property.owner == 'NONE':
                # send message to call pop-up back to main
                return 'landlord opportunity'
            # if the property is owned by someone, active player must pay owner rent
            else:
                # see who the landlord is
                for landlord in players:
                    # make sure it is not the active player
                    if property.owner == landlord.name:
                        active_player.pay_rent(landlord, property.rent)
                        # make sure it is not the active player
                        if property.owner != active_player.name:
                            message = "You paid $" + str(property.rent) + " in rent!"
                        else:
                            message = ''
                        return message

    # interaction for railroads
    for railroad in railroads:
        if int(active_player.location) == int(railroad.location):
            # check if property is owned by anyone
            if railroad.owner == 'NONE':
                # send message to call pop-up back to main
                return 'railroad opportunity'
            else:
                # see who the owns the railroad
                for landlord in players:
                    if railroad.owner == landlord.name:
                        active_player.pay_rent(landlord, railroad.rent)
                        # make sure it is not the active player
                        if railroad.owner != active_player.name:
                            message = "You paid $" + str(railroad.rent) + " in rent!"
                        else:
                            message = ''
                        return message

    # interation for utilities
    for utility in utilities:
        if int(active_player.location) == int(utility.location):
            # check if property is owned by anyone
            if utility.owner == 'NONE':
                # send message to call pop-up back to main
                return 'utility opportunity'
            else:
                # see who the owns the utility
                for landlord in players:
                    if utility.owner == landlord.name:
                        rent = utility.calculate_rent(landlord, dice_roll)
                        active_player.pay_rent(landlord, rent)
                        # make sure it is not the active player
                        if utility.owner != active_player.name:
                            message = "You paid $" + str(rent) + " in rent!"
                        else:
                            message = ''
                        return message

    # interaction for go to jail spot (send player to jail)
    if int(active_player.location) == 30:
        active_player.go_to_jail()
        return 'jail'
    # interaction for if you are in jail
    if int(active_player.location) == 10 and active_player.jail:
        # will return 'jail' unless it is the person's third time rolling
        result = active_player.go_to_jail()
        return result
    # interaction for community chest
    if int(active_player.location) == 2 or int(active_player.location) == 17 or int(active_player.location) == 33:
        for card in cards:
            if card.kind == 'Community Chest':
                chosen_card = card
                chosen_card.play(active_player)
                cards.remove(chosen_card)
                return chosen_card.message

    # interaction for chance
    if int(active_player.location) == 7 or int(active_player.location) == 22 or int(active_player.location) == 36:
        for card in cards:
            if card.kind == 'Chance':
                chosen_card = card
                chosen_card.play(active_player)
                cards.remove(chosen_card)
                return chosen_card.message

    # interaction for tax
    if int(active_player.location) == 4 or int(active_player.location) == 38:
        active_player.pay_taxes()
        return 'tax'


def change_turn(players, turn):
    '''
    Function to change the turn to the next player in the list
    :param players: players in the game
    :param turn: whose turn it is
    :return: the new active player and whose turn is it
    '''
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
    screen.fill(lightblue)  # Fill screen background
    pygame.draw.rect(screen, (41, 50, 65), (200, 100, 800, 300))
    pygame.draw.rect(screen, black, (200, 100, 800, 300), 4)
    draw_text(screen, "Roll To Determine Player Order", medium_v_font, white, 440, 115)
    draw_text(screen, "Higher Rolls Go First", medium_v_font, white, 500, 140)
    square_distance = 0
    start_x = 640 - 80 * total_players
    for i in range(0, total_players):
        pygame.draw.rect(screen, white, (start_x + square_distance, 175, 80, 80))
        pygame.draw.rect(screen, black, (start_x + square_distance, 175, 80, 80), 3)
        square_distance += 160


# board screen
def board_screen(screen, icon_positions, properties, railroads, utilities):
    '''
    Function to display the screen with the monopoly board
    :param screen: game screen
    :param icon_positions:
    :param properties:
    :return: nothing
    '''
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

    home = pygame.image.load("images/home.png")

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
            pygame.draw.rect(screen, black, (90, y_coord - 33, 20, 64), 1)  # black outline
            # name of property
            draw_text(screen, property.property_name, small_cs_font_4, black, x_coord - 34, y_coord - 30)
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
            pygame.draw.rect(screen, property.region, (x_coord - 31, 90, 63.9, 20))
            pygame.draw.rect(screen, black, (x_coord - 31, 90, 63.9, 20), 1)  # black outline

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
            pygame.draw.rect(screen, black, (685, y_coord - 32, 20, 64), 1)  # black outline
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
            pygame.draw.rect(screen, black, (x_coord - 33, 685, 63.9, 20), 1)  # black outline
            draw_text(screen, property.property_name, small_cs_font_3, black, x_coord - 30, y_coord - 55)
            # draw the cost to buy property
            draw_text(screen, '$' + str(property.price), small_cs_font_4, black, x_coord - 24, y_coord - 35)

            # logic to print houses along the bottom row
            houseX = x_coord - 32 + (64 / (property.num_houses + 1)) - 4
            for house in range(property.num_houses):
                screen.blit(home, (houseX, 688))
                # pygame.draw.rect(screen, black, (houseX, 688, 8, 8))
                houseX += (64 / (property.num_houses + 1))

    # print railroads
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
            screen.blit(tbar, (x_coord - 2, y_coord-13))
            draw_text(screen, railroad.name, small_cs_font_4, black, x_coord - 32, y_coord-32)
            draw_text(screen, '$' + str(railroad.price), small_cs_font_4, black, x_coord + 40, y_coord )
        # across the top
        elif y_coord == 35:
            screen.blit(quad, (x_coord-25, y_coord+12))
            # if railroad name has more than two words, display it differently
            if railroad.name.find(' ') > -1:
                name = railroad.name.split(' ')
                draw_text(screen, name[0], small_cs_font_4, black, x_coord - 28, y_coord - 36)
                draw_text(screen, name[1], small_cs_font_3, black, x_coord - 16, y_coord - 26)
                draw_text(screen, '$' + str(railroad.price), small_cs_font_3, black, x_coord - 14, y_coord - 10)
            else:
                draw_text(screen, railroad.name, small_cs_font_3, black, x_coord - 32, y_coord - 30)
                draw_text(screen, '$' + str(railroad.price), small_cs_font_3, black, x_coord - 4, y_coord - 10)
        # down the right side
        elif x_coord == 765:
            screen.blit(tram, (x_coord - 45, y_coord - 12))
            draw_text(screen, railroad.name, small_cs_font_3, black, x_coord - 70, y_coord - 30)
            draw_text(screen, '$' + str(railroad.price), small_cs_font_3, black, x_coord - 4, y_coord - 10)
        # across the bottom
        else:
            if railroad.name.find(' ') > -1:
                name = railroad.name.split(' ')
                draw_text(screen, name[0], small_cs_font_3, black, x_coord - 22, y_coord - 80)
                draw_text(screen, name[1], small_cs_font_3, black, x_coord - 14, y_coord - 65)
                draw_text(screen, '$' + str(railroad.price), small_cs_font_3, black, x_coord - 18, y_coord - 48)
            else:
                draw_text(screen, railroad.name, small_cs_font_3, black, x_coord - 32, y_coord - 30)
                draw_text(screen, '$' + str(railroad.price), small_cs_font_3, black, x_coord - 18, y_coord - 48)

            screen.blit(gondola, (x_coord - 25, y_coord - 30))

    # draw utilities
    for utility in utilities:
        coordinates = str(icon_positions[int(utility.location)])
        coordinates_list = coordinates[1:len(coordinates) - 1].split(',')
        x_coord = float(coordinates_list[0])
        y_coord = float(coordinates_list[1])
        # across the top
        if y_coord == 35:
            draw_text(screen, utility.name, small_cs_font_3, black, x_coord - 25, y_coord - 30)
            draw_text(screen, '$' + str(utility.price), small_cs_font_3, black, x_coord-16, y_coord-10)
        # down the right side
        elif x_coord == 765:
            draw_text(screen, utility.name, small_cs_font_3, black, x_coord - 70, y_coord - 30)
            draw_text(screen, '$' + str(utility.price), small_cs_font_3, black, x_coord - 10, y_coord - 5)

    # draw jail
    jail = pygame.image.load('images/jail.png')
    screen.blit(jail, (33, 33))
    # draw jail
    text = small_font_1.render('JUST', True, black)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [8, 45])
    text = small_font_1.render('VISITING', True, black)
    screen.blit(text, [25, 8])
    jail = pygame.image.load('images/jail.png')
    screen.blit(jail, (33, 33))
    # draw go to jail
    draw_text(screen, 'GO TO', small_font_1, black, 720, 690)
    draw_text(screen, 'JAIL', small_font_1, black, 725, 772)
    go_to_jail = pygame.image.load('images/handcuff.png')
    screen.blit(go_to_jail, (710, 710))

    # GO square
    go_icon = pygame.image.load('images/go.png')
    screen.blit(go_icon, (2, 692))
    text = small_font_1.render('COLLECT', True, black)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [70, 698])
    text = small_font_1.render('$200', True, black)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [90, 714])

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
    draw_text(screen, 'Ski', small_cs_font_3, black, 80, 445)
    draw_text(screen, 'Wax', small_cs_font_3, black, 78, 460)
    ski_wax = pygame.image.load("images/ski-wax.png")
    screen.blit(ski_wax, (10, 430))
    draw_text(screen, 'Gear', small_cs_font_3, black, 194, 695)
    draw_text(screen, 'Upgrade', small_cs_font_3, black, 184, 710)
    boot = pygame.image.load("images/ski-boot.png")
    screen.blit(boot, (182, 740))

    # chance
    chance_logo = pygame.image.load("images/chance.png")
    chance_logo2 = pygame.image.load("images/chance2.png")
    chance_logo3 = pygame.image.load("images/chance3.png")
    screen.blit(chance_logo, (694, 158))
    screen.blit(chance_logo2, (7, 223))
    screen.blit(chance_logo3, (287, 694))

    # community chest
    chest = pygame.image.load("images/chest.png")
    screen.blit(chest, (501, 10))
    draw_text(screen, 'Community', small_font_3, black, 498, 65)
    draw_text(screen, 'Chest', small_font_3, black, 512, 80)
    screen.blit(chest, (501, 740))
    draw_text(screen, 'Community', small_font_3, black, 498, 705)
    draw_text(screen, 'Chest', small_font_3, black, 512, 720)
    screen.blit(chest, (6, 572))
    draw_text(screen, 'Community', small_font_3, black, 49, 561)
    draw_text(screen, 'Chest', small_font_3, black, 67, 580)
    # free parking
    draw_text(screen, 'FREE', small_font_1, black, 720, 4)
    parking = pygame.image.load("images/freeParking.png")
    draw_text(screen, 'PARKING', small_font_1, black, 705, 90)
    screen.blit(parking, (705, 25))

    # Utilities
    snow_gun = pygame.image.load('images/snow-gun.png')
    screen.blit(snow_gun, (183, 48))
    snow_groomer = pygame.image.load('images/snowPlow.png')
    screen.blit(snow_groomer, (700, 578))


# card screen
def prop_card_screen(screen, font, active_player):
    '''
    Function to display a screen that shows you cards and gives more details about your properties
    :param screen: game screen
    :param font: font of the text
    :return: nothing
    '''
    pygame.display.set_caption('Your cards')
    screen.fill(green)

    # DRAW FIRST 14 PROPERTIES
    draw_text(screen, ' Your Properties: Add Houses & Hotels, Or Mortgage For Money', font, white, 50, 20)
    start_x = 50
    start_y = 70
    level = 1
    mortgage_buttons = []
    unmortgage_buttons = []
    house_buttons = []
    hotel_buttons = []

    for card_idx in range(0, len(active_player.property_list)):
        create_card(screen, start_x, start_y, active_player.property_list[card_idx])
        mortgage_buttons, unmortgage_buttons = mortgage_card(screen, active_player.property_list[card_idx], active_player,
                                                             mortgage_buttons, unmortgage_buttons, card_idx,
                                                             start_x, start_y)
        house_buttons = buy_sell_house(screen, active_player.property_list[card_idx], active_player, house_buttons, card_idx,
                                  start_x, start_y)
        hotel_buttons = buy_sell_hotel(screen, active_player.property_list[card_idx], active_player, hotel_buttons, card_idx,
                                  start_x, start_y)
        start_x += 160
        if level % 7 == 0:
            start_x = 50
            start_y += 300
        level += 1
        if card_idx >= 13:
            break


def prop_card_screen2(screen, font, active_player):
    '''
    Function to create the second screen of properties if a player a lot
    :param screen: screen were are drawing to
    :param font: font we are using
    :param active_player: the player whose turn it is
    :return: nothing
    '''
    pygame.display.set_caption('Your cards')
    screen.fill(green)

    # DRAW REMAINING PROPERTIES
    draw_text(screen, ' Your Properties: Add Houses & Hotels, Or Mortgage For Money', font, white, 50, 20)
    start_x = 50
    start_y = 70
    level = 1
    mortgage_buttons = []
    unmortgage_buttons = []
    house_buttons = []
    hotel_buttons = []
    offset = 14
    for i in range(0, offset):  # filler space in arrays
        mortgage_buttons.append(0)
        unmortgage_buttons.append(0)
        house_buttons.append(0)
        hotel_buttons.append(0)

    for card_idx in range(offset, len(active_player.property_list)):
        create_card(screen, start_x, start_y, active_player.property_list[card_idx])
        mortgage_buttons, unmortgage_buttons = mortgage_card(screen, active_player.property_list[card_idx],
                                                             active_player, mortgage_buttons, unmortgage_buttons,
                                                             card_idx, start_x, start_y)
        house_buttons = buy_sell_house(screen, active_player.property_list[card_idx], active_player, house_buttons, card_idx,
                                  start_x, start_y)
        hotel_buttons = buy_sell_hotel(screen, active_player.property_list[card_idx], active_player, hotel_buttons, card_idx,
                                  start_x, start_y)
        start_x += 160
        if level % 7 == 0:
            start_x = 50
            start_y += 300
        level += 1


# other card screen
def other_card_screen(screen, font, active_player):
    '''
    Function to display a screen that shows you the cards besides property cards
    :param screen: game screen
    :param font: font of the text
    :param active_player: the player whose turn it is
    :return: nothing
    '''
    pygame.display.set_caption('Your cards')
    screen.fill(green)

    # DRAW RAILROADS
    draw_text(screen, 'Railroads: ', font, white, 50, 100)
    start_x = 50
    start_y = 160
    mor_rail_buttons = []
    unmor_rail_buttons = []
    rail_idx = 0

    for railroad in active_player.railroad_list:
        create_other_card(screen, start_x, start_y, railroad.name, 'railroad')
        mor_rail_buttons, unmor_rail_buttons = mortgage_card(screen, railroad, active_player, mor_rail_buttons,
                                                             unmor_rail_buttons, rail_idx, start_x, start_y)
        rail_idx += 1
        start_x += 160

    # DRAW UTILITIES
    draw_text(screen, 'Utilities: ', font, white, 850, 100)
    start_x = 850
    start_y = 160
    mor_util_buttons = []
    unmor_util_buttons = []
    util_idx = 0
    for utility in active_player.utility_list:
        create_other_card(screen, start_x, start_y, utility.name, 'utilities')
        mor_util_buttons, unmor_util_buttons = mortgage_card(screen, utility, active_player, mor_util_buttons,
                                                             unmor_util_buttons, util_idx, start_x, start_y)
        util_idx += 1
        start_x += 160

    # DRAW GET OUT OF JAIL FREE
    draw_text(screen, 'Get out of jail free: ', font, white, 50, 550)
    start_x = 50
    start_y = 590
    for i in range(0,int(active_player.jail_free)):
        create_jail_free_card(screen, start_x, start_y)
        start_x += 210

def check_for_bankruptcy(active_player, bankruptcies):
    '''
    Function to check if the active player is bankrupt
    :param active_player: the player whose turn it is
    :param bankruptcies: the number of player show are bankrupt
    :return: the updated number of bankruptcies
    '''
    bank = active_player.bank
    if int(bank.total) <= 0:
        # if the bankrupt player is player1, human has lost
        if active_player.name == 'Player 1':
            active_player.bankrupt = True
            return bankruptcies
        else:
            #computer decision--
            # sell back all their properties, railroads, and utilities to get money back
            for utility in active_player.utility_list:
                 active_player.sell_utility(utility)
                 #if they are no longer bankrupt, return to game
                 if int(bank.total) > 0:
                     return bankruptcies
            for railroad in active_player.railroad_list:
                active_player.sell_railroad(railroad)
                if int(bank.total) > 0:
                    return bankruptcies
            for property in active_player.property_list:
                active_player.sell_property(property)
                if int(bank.total) > 0:
                    return bankruptcies
            # this player has now gone bankrupt and lost the game if they still have no money
            if int(bank.total) <= 0:
                active_player.bankrupt = True
                bankruptcies += 1
    return bankruptcies


def main():
    '''
    Main function to run the game
    :return: nothing
    '''


    # Constants
    DICE_DIMS = (40, 40)
    LEFT_CLICK = 1

    # Initializations
    # Title and Icon
    pygame.display.set_caption('Monopoly | Ski Resort Edition')
    icon = pygame.image.load('images/ski-resort.png')
    pygame.display.set_icon(icon)
    # make screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screens = {
        'START': 1,
        'TURNS': 2,
        'BOARD': 3,
        'PROPS': 4,
        'PROPS2': 5,
        'CARDS': 6,
        'LOSE': 7,
        'WIN': 8
    }
    current_screen = screens.get('START')

    is_rolling = False
    player_has_rolled = False
    roll_counter = 0
    die1_value = -1
    die2_value = -1
    doubles = 0

    # game type variables
    game_singleplayer = False
    game_multiplayer = False
    num_players = 0
    num_computers = 0
    total_players = 0

    # Multiplayer initializations
    ip_address = ''
    network = ''
    input_rect = pygame.Rect(SCREEN_WIDTH / 2 - 100, 280, 200, 32)
    color_active = pygame.Color('white')
    color_passive = pygame.Color('gray')
    box_color = color_passive
    active = True
    connecting = False
    connected = False
    error = False
    is_full = False
    has_started = False
    my_player = -1
    my_icon = ''
    player_selected = False

    # load button images
    singleplayer_img = pygame.image.load('images/singleplayer.png').convert_alpha()
    multiplayer_img = pygame.image.load('images/multiplayer.png').convert_alpha()
    startgame_img = pygame.image.load('images/startgame.png').convert_alpha()
    number_img = pygame.image.load('images/numplayer.png').convert_alpha()
    properties_img = pygame.image.load('images/properties.png').convert_alpha()
    board_return_img = pygame.image.load('images/board-return.png').convert_alpha()
    roll_img = pygame.image.load('images/roll.png').convert_alpha()
    icon1 = 'images/icon1.png'
    icon2 = 'images/icon2.png'
    icon3 = 'images/icon3.png'
    icon4 = 'images/icon4.png'
    icon1_img = pygame.image.load(icon1).convert_alpha()
    icon2_img = pygame.image.load(icon2).convert_alpha()
    icon3_img = pygame.image.load(icon3).convert_alpha()
    icon4_img = pygame.image.load(icon4).convert_alpha()
    next_cards_img = pygame.image.load('images/next_cards.png').convert_alpha()

    # draw buttons
    singleplayer_button = Button(singleplayer_img, 500, 210, 'Single-Player', white, 1)
    multiplayer_button = Button(multiplayer_img, 700, 210, 'Multi-Player', white, 1)
    startgame_button = Button(startgame_img, 600, 500, 'Start Game', white, 1)
    num_computers1_button = Button(number_img, 525, 310, '1', white, 1.5)
    num_computers2_button = Button(number_img, 600, 310, '2', white, 1.5)
    num_computers3_button = Button(number_img, 675, 310, '3', white, 1.5)
    icon1_button = Button(icon1_img, 450, 420, 'Icon 1', white, 1)
    icon2_button = Button(icon2_img, 550, 420, 'Icon 2', white, 1)
    icon3_button = Button(icon3_img, 650, 420, 'Icon 3', white, 1)
    icon4_button = Button(icon4_img, 750, 420, 'Icon 4', white, 1)
    properties_button = Button(properties_img, 910, 50, 'Inspect Properties', white, 1.5)
    card_button = Button(multiplayer_img, 1110, 50, 'Other cards', white, 1)
    board_return_button = Button(board_return_img, 1050, 35, 'Return to Board', white, 1.5)
    roll_button = Button(roll_img, 935, 757, 'ROLL', black, 2)
    turn_roll_button = Button(roll_img, 600, 370, 'ROLL', black, 2)
    end_button = Button(singleplayer_img, 970, 680, 'END TURN', black, .75)
    yes_button = Button(roll_img, 950, 300, 'yes', black, 1)
    no_button = Button(roll_img, 1050, 300, 'no', black, 1)
    okay_button = Button(roll_img, 950, 300, 'ok', black, 1)

    game_mode_buttons = ButtonGroup([singleplayer_button, multiplayer_button])
    computers_buttons = ButtonGroup([num_computers1_button, num_computers2_button, num_computers3_button])
    icon_buttons = ButtonGroup([icon1_button, icon2_button, icon3_button, icon4_button])

    next_cards_button = Button(next_cards_img, 1050, 770, 'Next Cards', white, 1)
    prev_cards_button = Button(next_cards_img, 1050, 770, 'Prev Cards', white, 1)

    # load board positions
    icon_positions = get_icon_positions()

    # create player objects (all start at human players)
    player1 = Player(False, 0, 'Player 1', 1, icon_positions)
    player2 = Player(False, 1, 'Player 2', 1, icon_positions)
    player3 = Player(False, 2, 'Player 3', 1, icon_positions)
    player4 = Player(False, 3, 'Player 4', 1, icon_positions)

    # turn screen variables
    players_loaded = False
    square_distance = 160
    unset_players = []  # array of players created in load_players
    players = []  # array of players w/ decided order
    turn_index = 0
    turn_rolls = []  # the holding the roll number of each unset_player
    turn = 'Player 1'
    bankruptcies = 0
    turn_summary = ''

    result = '' # start with there being no results from an interaction (no pop-ups)
    text = '' # start with there being no text message from card
    # load community chest and chance cards
    cards = load_cards()
    # load property cards
    properties = load_properties()
    # create railroad cards
    railroads = [Railroad('Locke Mountain T-bar', 5),
                 Railroad('Bonaventure Quad', 15),
                 Railroad('Aerial Tramway', 25),
                 Railroad('Gondola One', 35)]
    # create utilities cards
    utilities = [Utility('Snow Gun', 12),
                 Utility('Snow Groomer', 28)]

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
        current_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and active and game_multiplayer:
                if event.key == pygame.K_BACKSPACE:
                    if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
                        ip_address = ''
                    else:
                        ip_address = ip_address[:-1]
                elif event.key == pygame.K_RETURN:
                    active = False
                else:
                    ip_address += event.unicode
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == LEFT_CLICK:
                    game_mode_buttons.check_click()
                    computers_buttons.check_click()
                    icon_buttons.check_click()
                    startgame_button.check_click()
                    properties_button.check_click()
                    card_button.check_click()
                    board_return_button.check_click()
                    roll_button.check_click()
                    turn_roll_button.check_click()
                    end_button.check_click()
                    yes_button.check_click()
                    no_button.check_click()
                    okay_button.check_click()

        startgame_button.hide()
        properties_button.hide()
        card_button.hide()
        board_return_button.hide()
        roll_button.hide()
        turn_roll_button.hide()
        end_button.hide()
        yes_button.hide()
        no_button.hide()
        okay_button.hide()

        # Vector of all keys on keyboard.
        # keys[pygame.K_SPACE] will return True if the space-bar is pressed; False if otherwise
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

        if current_screen == screens.get('START'):
            # game_singleplayer, game_multiplayer = start_screen(screen, game_singleplayer, game_multiplayer)
            screen.fill((135, 206, 235))  # Fill screen background
            draw_text_center(screen, 'Welcome to CS205 Project: Ski Resort Monopoly!', large_v_font, black, 50)
            draw_text(screen, 'Press \'esc\' to close the program', small_v_font, black, 25, 750)
            draw_text_center(screen, 'Game Setup', medium_v_font, black, 150)

            game_mode_buttons.draw(screen)

            if singleplayer_button.clicked:
                game_singleplayer = True
                game_multiplayer = False
            if multiplayer_button.clicked:
                game_multiplayer = True
                game_singleplayer = False
            # set number of computers
            if num_computers1_button.clicked:
                num_computers = 1
                player2.computer = True
            if num_computers2_button.clicked:
                num_computers = 2
                player2.computer = True
                player3.computer = True
            if num_computers3_button.clicked:
                num_computers = 3
                player2.computer = True
                player3.computer = True
                player4.computer = True

            if game_singleplayer:
                num_players = 1
                draw_text_center(screen, "Number of Computers", medium_v_font, black, 250)
                computers_buttons.draw(screen)

                total_players = num_players + num_computers

                if num_computers > 0:
                    draw_text_center(screen, "Choose your Piece", medium_v_font, black, 350)
                    icon_buttons.draw(screen)
                    startgame_button.show()
                    startgame_button.draw(screen)

                    if icon1_button.clicked:
                        player_selected = True
                        my_icon = 0
                    elif icon2_button.clicked:
                        player_selected = True
                        my_icon = 1
                        player2.icon_num = 0
                    elif icon3_button.clicked:
                        player_selected = True
                        my_icon = 2
                        player3.icon_num = 0
                    elif icon4_button.clicked:
                        player_selected = True
                        my_icon = 3
                        player4.icon_num = 0

                    # if startgame button clicked and game setup, move to game screen
                    if player_selected and startgame_button.clicked:
                        player1 = Player(False, my_icon, "Player 1", 1, icon_positions)
                        current_screen = screens.get("TURNS")
            elif game_multiplayer:
                draw_text_center(screen, 'Enter server ip:', medium_v_font, black, 250)

                if active:
                    box_color = color_active
                else:
                    box_color = color_passive

                pygame.draw.rect(screen, box_color, input_rect)
                pygame.draw.rect(screen, pygame.Color('black'), input_rect, 3, 1)
                draw_text(screen, ip_address, medium_v_font, black, input_rect.x + 5, input_rect.y + 4)

                message = ''
                if not active and not connecting:
                    # Attempt connection to server
                    connecting = True
                    draw_text_center(screen,
                                     'Loading...',
                                     medium_v_font,
                                     black,
                                     375)
                    # Bad style
                    pygame.display.update()
                    network = Network(ip_address)
                    # print(n.get_player())
                    if network.get_player() is None:
                        error = True
                        ip_address = ''
                        active = True
                        connecting = False
                    elif network.get_player() == -1:
                        is_full = True
                        ip_address = ''
                        active = True
                        connecting = False
                    elif network.get_player() == -2:
                        has_started = True
                        ip_address = ''
                        active = True
                        connecting = False
                    else:
                        error = False
                        is_full = False
                        has_started = False
                        connected = True

                if error:
                    draw_text_center(screen, "Error connecting to server. Please re-type IP.", medium_v_font, black, 375)

                if is_full:
                    draw_text_center(screen, "Server is full. Please wait for a spot.", medium_v_font, black, 375)

                if has_started:
                    draw_text_center(screen, "Game is in play. Please wait for game to end.", medium_v_font, black, 375)

                if connected:
                    my_player = network.get_player()
                    game = network.send("get")

                    draw_text_center(screen, 'You are player ' + str(my_player) + ' of ' + str(game.get_num_players()),
                                     medium_v_font, black, 320)
                    draw_text_center(screen, 'Choose your Piece', medium_v_font, black, 350)
                    icon_buttons.draw(screen)
                    icon1_button.clicked = not game.available_icons[0]
                    icon2_button.clicked = not game.available_icons[1]
                    icon3_button.clicked = not game.available_icons[2]
                    icon4_button.clicked = not game.available_icons[3]

                    if icon1_button.clicked:
                        my_icon = 0
                        game = network.send('icon0')
                    elif icon2_button.clicked:
                        my_icon = 1
                        game = network.send('icon1')
                    elif icon3_button.clicked:
                        my_icon = 2
                        game = network.send('icon2')
                    elif icon4_button.clicked:
                        my_icon = 3
                        game = network.send('icon3')
                    startgame_button.show()
                    startgame_button.draw(screen)
                    if my_player == 1 and game.get_num_players() >= 2:
                        if startgame_button.clicked:
                            game = network.send("start")
                    else:
                        startgame_button.clicked = False

                    current_screen = game.current_screen
        elif current_screen == screens.get('TURNS'):
            if game_singleplayer:
                turn_screen(screen, total_players)
                if not players_loaded:  # (Created once) loads the number of players into each list based on the amount chosen in first screen
                    unset_players = load_players(total_players, player1, player2, player3, player4, unset_players)
                    players_loaded = True
                i = 0
                for p in unset_players:  # draw the icons into the squares
                    if total_players == 2:
                        p.draw(screen, (500 + i, 190))
                        i += square_distance
                    elif total_players == 3:
                        p.draw(screen, (420 + i, 190))
                        i += square_distance
                    elif total_players == 4:
                        p.draw(screen, (340 + i, 190))
                        i += square_distance
                for active_player in unset_players:  # determine the order by having each player roll
                    for num in range(0, len(turn_rolls)):  # - prints rolled number under icon
                        if total_players == 2:
                            draw_text(screen, str(turn_rolls[num]), medium_v_font, white, 510 + num * square_distance, 268)
                        if total_players == 3:
                            draw_text(screen, str(turn_rolls[num]), medium_v_font, white, 435 + num * square_distance, 268)
                        if total_players == 4:
                            draw_text(screen, str(turn_rolls[num]), medium_v_font, white, 350 + num * square_distance, 268)
                    if turn == active_player.name:
                        if not is_rolling:
                            if not player_has_rolled:
                                if total_players == 2 and not active_player.computer:
                                    draw_text(screen, 'Your Turn', medium_v_font, white, 450 +
                                              turn_index, 268)
                                if total_players == 3 and not active_player.computer:
                                    draw_text(screen, 'Your Turn', medium_v_font, white, 370 +
                                              turn_index, 268)
                                if total_players == 4 and not active_player.computer:
                                    draw_text(screen, 'Your Turn', medium_v_font, white, 290 +
                                              turn_index, 268)
                                # PLAYER CHOICE (roll dice to determine player order)
                                if active_player.computer:
                                    # computer automatically rolls
                                    roll_counter = 0
                                    is_rolling = True

                                else:  # human has to roll
                                    turn_roll_button.show()
                                    turn_roll_button.draw(screen)
                                    if keys[pygame.K_SPACE] or turn_roll_button.clicked:  # rolls on a space key or button click
                                        turn_roll_button.clicked = False
                                        roll_counter = 0
                                        is_rolling = True
                            else:
                                turn_index += square_distance
                                if turn_index == square_distance * len(unset_players):  # returns player text to beginning
                                    turn_index = 0
                                turn, active_player = change_turn(unset_players, turn)
                                player_has_rolled = False
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
                                die1_value = die1.roll(roll_counter)
                            if die2_value == -1:
                                die2_value = die2.roll(roll_counter)
                            if die1_value != -1 and die2_value != -1:
                                # Both dice are done rolling
                                player_has_rolled = True
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
                            roll_counter += 1
                        die1.draw(screen)
                        die2.draw(screen)
            elif game_multiplayer:
                game = network.send('get')
                total_players = game.get_num_players()
                turn_screen(screen, total_players)

                for i in range(0, total_players):  # draw the icons into the squares
                    p = game.players[i]
                    if total_players == 2:
                        p.draw(screen, (500 + i * square_distance, 190))
                        if p.name == game.get_curr_player().name:
                            draw_text(screen, game.get_curr_player().name + '\'s Turn', medium_v_font, white, 450 +
                                      i * square_distance, 268)
                        elif p.last_roll != -1:
                            draw_text(screen, str(p.last_roll), medium_v_font, white, 450 + i * square_distance, 268)
                    elif total_players == 3:
                        p.draw(screen, (420 + i * square_distance, 190))
                        if p.name == game.get_curr_player().name:
                            draw_text(screen, game.get_curr_player().name + '\'s Turn', medium_v_font, white, 370 +
                                      i * square_distance, 268)
                        elif p.last_roll != -1:
                            draw_text(screen, str(p.last_roll), medium_v_font, white, 370 + i * square_distance, 268)
                    elif total_players == 4:
                        p.draw(screen, (340 + i * square_distance, 190))
                        if p.name == game.get_curr_player().name:
                            draw_text(screen, game.get_curr_player().name + '\'s Turn', medium_v_font, white, 290 +
                                      i * square_distance, 268)
                        elif p.last_roll != -1:
                            draw_text(screen, str(p.last_roll), medium_v_font, white, 290 + i * square_distance, 268)

                if not is_rolling:
                    if not player_has_rolled:
                        turn_roll_button.show()
                        turn_roll_button.draw(screen)
                        if my_player == game.get_curr_player().name[7]:
                            print(keys[pygame.K_SPACE])
                            if keys[pygame.K_SPACE] or turn_roll_button.clicked:  # rolls on a space key or button click
                                turn_roll_button.clicked = False
                                game = network.send('roll')
                                roll_counter = 0
                                is_rolling = True
                    else:
                        turn_roll_button.hide()
                        player_has_rolled = False
                        game = network.send('done roll')
                else:
                    if die1_value == -1:
                        die1_value = die1.roll(roll_counter, value=game.dice_values[0])
                    if die2_value == -1:
                        die2_value = die2.roll(roll_counter, value=game.dice_values[1])
                    if die1_value != -1 and die2_value != -1:
                        # Both dice are done rolling
                        player_has_rolled = True
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
                    roll_counter += 1
                die1.draw(screen)
                die2.draw(screen)
                current_screen = game.current_screen
        elif current_screen == screens.get('BOARD'):
            if game_singleplayer:
                # see if human has won/lost
                if player1.bankrupt:
                    current_screen = screens.get('LOSE')
                if bankruptcies == len(players) - 1:
                    current_screen = screens.get('WIN')

                # if the active player is bankrupt, skip their turn
                if active_player.bankrupt:
                    print('skipped bankrupt player')
                    turn, active_player = change_turn(players, turn)

                board_screen(screen, icon_positions, properties, railroads, utilities)
                properties_button.show()
                properties_button.draw(screen)
                card_button.show()
                card_button.draw(screen)
                # display bank account money
                draw_text(screen, 'Money: $', medium_v_font, black, 900, 90)

                if turn == 'Player 1':
                    bank_account = player1.bank
                elif turn == 'Player 2':
                    bank_account = player2.bank
                elif turn == 'Player 3':
                    bank_account = player3.bank
                else:
                    bank_account = player4.bank
                draw_text(screen, str(bank_account.total), medium_v_font, black, 995, 90)

                # draw players and make sure no one has lost the game
                for p in players:
                    p.draw(screen)

                # print pop-ups if needed (only for human player) - computer gets summary text
                if result == 'landlord opportunity':
                    result = buy_pop_up(screen, active_player, 'Would you like to buy this property?', properties, 1, yes_button, no_button)
                    turn_summary += "Player bought property"
                # pop-up for railroad
                elif result == 'railroad opportunity':
                    result = buy_pop_up(screen, active_player, 'Would you like to buy this railroad?', railroads, 2, yes_button, no_button)
                    turn_summary += "Player bought ski lift"
                # pop-up for utility
                elif result == 'utility opportunity':
                    result = buy_pop_up(screen, active_player, 'Would you like to buy this utility?', utilities, 3, yes_button, no_button)
                    turn_summary += "Player bought machinery"
                # pop-up for community chest/chance
                elif str(result)[:8] == 'message:':
                    # save the message for later use
                    text = result[8:]
                    result = card_pop_up(screen, active_player, result, okay_button)
                    turn_summary += 'Player got card: ' + text + ' '

                # pop-up message for paying rent
                elif str(result)[:3] == 'You':
                    # change message if player is computer
                    if not active_player.computer:
                        draw_text(screen, result, medium_v_font, black, 900, 300)
                    else:
                        turn_summary += str(active_player.name) + str(result[3:])
                        result = ''
                # pop-up message to tell you if you are in jail
                elif result == 'jail':
                    result = jail_pop_up(screen, active_player, yes_button, no_button)
                    turn_summary += 'Player paid $50 to get out of jail'
                # pop-up message for paying taxes
                elif result == 'tax':
                    if not active_player.computer:
                        draw_text(screen, "Taxes due!", medium_v_font, black, 900, 300)
                    else:
                        turn_summary += 'Player paid taxes'
                # check if there was player movement from previous card pulled
                elif result == '':
                    # print message about whose movement it is
                    if active_player.computer:
                        draw_text(screen, str(active_player.name) + '\'s turn', medium_v_font, black, 910, 200)
                    else:
                        draw_text(screen, "Your turn!", medium_v_font, black, 930, 200)
                    # if the message has the words advance or go, there is another movement
                    if text.find('Advance') != -1 or text.find('Go') != -1:
                        # interact with the new square
                        result = interact(active_player, players, properties, railroads, utilities, 0, cards)

                # dice and turn
                if turn == active_player.name:
                    if not is_rolling:
                        #draw_text(screen, str(active_player.name) + '\'s turn', medium_v_font, black, 900, 700)
                        # print message that player can't roll since they are in jail
                        if active_player.jail:
                            draw_text(screen, 'You are in jail.', medium_v_font, black, 920, 450)
                        # don't roll if player is in jail
                        if not player_has_rolled:
                            roll_button.show()
                            roll_button.draw(screen)
                            # PLAYER CHOICE (to roll)
                            if active_player.computer:
                                # computer rolls automatically
                                roll_counter = 0
                                is_rolling = True
                                #record time that roll starts
                                time_of_roll = pygame.time.get_ticks()
                            # player must interact
                            else:
                                if keys[pygame.K_SPACE] or roll_button.clicked:  # rolls on a space key or button click
                                    roll_button.clicked = False
                                    roll_counter = 0
                                    is_rolling = True
                        else:
                            roll_button.hide()
                            if doubles:  # keep turn on doubles
                                player_has_rolled = False
                            else:
                                # PLAYER CHOICE (to end turn)
                                if active_player.computer:
                                    # fix spacing if text goes off of line for printing the summary of comp's turn
                                    if len(str(turn_summary)) > 65:
                                        words = turn_summary.split(' ')
                                        draw_text(screen, ' '.join(words[0:5]), medium_v_font, black, 870, 300)
                                        draw_text(screen, ' '.join(words[5:10]), medium_v_font, black, 870, 325)
                                        draw_text(screen, ' '.join(words[10:]), medium_v_font, black, 870, 350)
                                    elif 35 < len(str(turn_summary)) < 65:
                                        words = turn_summary.split(' ')
                                        draw_text(screen, ' '.join(words[0:5]), medium_v_font, black, 890, 300)
                                        draw_text(screen, ' '.join(words[5:]), medium_v_font, black, 890, 320)
                                    else:
                                        draw_text(screen, turn_summary, medium_v_font, black, 890, 300)

                                    if current_time - time_of_roll > 5000:
                                        bankruptcies = check_for_bankruptcy(active_player, bankruptcies)
                                        # end turn
                                        turn, active_player = change_turn(players, turn)
                                        player_has_rolled = False
                                        # clear all pop-ups for next turn
                                        result = ''
                                        turn_summary = ''
                                # player must hit end button to move on
                                else:
                                    end_button.show()
                                    end_button.draw(screen)
                                    if end_button.clicked:  # rolls on a space key or button click
                                        end_button.clicked = False
                                        bankruptcies = check_for_bankruptcy(active_player, bankruptcies)
                                        # change the turn once player hit the end button
                                        turn, active_player = change_turn(players, turn)
                                        player_has_rolled = False
                                        #clear all pop-ups for next turn
                                        result = ''
                                        turn_summary = ''
                    else:
                        # A die_value of -1 indicates the die is not done rolling.
                        # Otherwise, roll() returns a random value from 1 to 6.
                        if die1_value == -1:
                            die1_value = die1.roll(roll_counter)
                        if die2_value == -1:
                            die2_value = die2.roll(roll_counter)
                        if die1_value != -1 and die2_value != -1:
                            # Both dice are done rolling
                            player_has_rolled = True

                            # Return the dice to the start
                            if not die1.at_start:
                                die1.reset()
                            if not die2.at_start:
                                die2.reset()
                            if die1.at_start and die2.at_start:
                                # Both dice are at the start. Reset values
                                is_rolling = False
                                roll = die1_value + die2_value
                                # TODO -- test spaces here by changing the roll value
                                # roll = 7
                                if die1_value == die2_value:  # check if doubles were rolled
                                    doubles += 1
                                else:
                                    doubles = 0
                                if doubles >= 3:  # go to jail on 3rd double
                                    doubles = 0
                                    active_player.go_to_jail()

                                # player icon moves number of spaces rolled (only if player is not in jail)
                                if not active_player.jail:
                                    active_player.movement(roll)

                                # if icons are on the same spot, change their position on the square
                                new_players = players.copy()
                                new_players.remove(active_player)
                                for check_player in new_players:
                                    if int(active_player.location) == int(check_player.location):
                                        # icons are overlapping on the board
                                        active_player.overlap = True
                                    elif int(active_player.location) != int(check_player.location):
                                        active_player.overlap = False

                                # interact with that spot on the board
                                result = interact(active_player, players, properties, railroads, utilities, roll, cards)

                                die1_value = -1
                                die2_value = -1

                        roll_counter += 1
                    die1.draw(screen)
                    die2.draw(screen)
            if game_multiplayer:
                game = network.send('get')
                active_player = game.get_curr_player()
                board_screen(screen, icon_positions, properties, railroads, utilities)
                properties_button.show()
                properties_button.draw(screen)
                card_button.show()
                card_button.draw(screen)
                # display bank account money
                draw_text(screen, 'Money: $', medium_v_font, black, 900, 90)
                draw_text(screen, str(game.players[my_player-1].bank.total), medium_v_font, black, 995, 90)
                draw_text(screen, str(active_player.name) + '\'s turn', medium_v_font, black, 900, 700)

                if my_player == game.get_curr_player().name[8]:
                    if not is_rolling:
                        # print message that player can't roll since they are in jail
                        if active_player.jail:
                            draw_text(screen, 'You are in jail.', medium_v_font, black, 920, 450)
                        if not player_has_rolled:
                            roll_button.show()
                            roll_button.draw(screen)
                            if keys[pygame.K_SPACE] or roll_button.clicked:  # rolls on a space key or button click
                                roll_button.clicked = False
                                game = network.send('roll')
                                roll_counter = 0
                                is_rolling = True
                        else:
                            roll_button.hide()
                            player_has_rolled = False
                            game = network.send('done roll')
                    else:
                        if die1_value == -1:
                            die1_value = die1.roll(roll_counter, value=game.dice_values[0])
                        if die2_value == -1:
                            die2_value = die2.roll(roll_counter, value=game.dice_values[1])
                        if die1_value != -1 and die2_value != -1:
                            # Both dice are done rolling
                            player_has_rolled = True
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
                        roll_counter += 1
                else:
                    roll_button.hide()

                die1.draw(screen)
                die2.draw(screen)
                current_screen = game.current_screen

            if keys[pygame.K_c] or properties_button.clicked:  # press c or click to go to property screen
                properties_button.clicked = False
                current_screen = screens.get('PROPS')
            if card_button.clicked:  # click to move to property screen
                card_button.clicked = False
                current_screen = screens.get('CARDS')

        elif current_screen == screens.get('PROPS'):  # shows only first 14 properties
            # Player 1
            if turn == 'Player 1':
                prop_card_screen(screen, font, player1)
            elif turn == 'Player 2':
                prop_card_screen(screen, font, player2)
            elif turn == 'Player 3':
                prop_card_screen(screen, font, player3)
            else:
                prop_card_screen(screen, font, player4)
            board_return_button.show()
            board_return_button.draw(screen)
            if len(active_player.property_list) > 13:  # move to next properties screen if too many cards to show
                next_cards_button.show()
                next_cards_button.draw(screen)
                if next_cards_button.clicked:
                    next_cards_button.clicked = False
                    current_screen = screens.get('PROPS2')
            if keys[pygame.K_g]:  # press g to return to game
                current_screen = screens.get('BOARD')
            if board_return_button.clicked:
                board_return_button.clicked = False
                current_screen = screens.get('BOARD')

        elif current_screen == screens.get('PROPS2'):  # shows remaining properties
            # Player 1
            if turn == 'Player 1':
                prop_card_screen2(screen, font, player1)
            elif turn == 'Player 2':
                prop_card_screen2(screen, font, player2)
            elif turn == 'Player 3':
                prop_card_screen2(screen, font, player3)
            else:
                prop_card_screen2(screen, font, player4)
            board_return_button.show()
            board_return_button.draw(screen)
            prev_cards_button.show()
            prev_cards_button.draw(screen)
            if prev_cards_button.clicked:
                prev_cards_button.clicked = False
                current_screen = screens.get('PROPS')  # Go back to prev Prop screen
            if keys[pygame.K_g] or board_return_button.clicked:  # press g or click to return to board screen
                board_return_button.clicked = False
                current_screen = screens.get('BOARD')

        elif current_screen == screens.get('CARDS'):
            # Player 1
            if turn == 'Player 1':
                other_card_screen(screen, font, player1)
            elif turn == 'Player 2':
                other_card_screen(screen, font, player2)
            elif turn == 'Player 3':
                other_card_screen(screen, font, player3)
            else:
                other_card_screen(screen, font, player4)

            board_return_button.show()
            board_return_button.draw(screen)
            if keys[pygame.K_g] or board_return_button.clicked:  # press g or click to return to board screen
                board_return_button.clicked = False
                current_screen = screens.get('BOARD')

        elif current_screen == screens.get('LOSE'):
            pygame.display.set_caption('Game over :(')
            screen.fill(red)
            done = pygame.image.load('images/bankrupt.png')
            screen.blit(done, (150, 200))
            draw_text(screen, 'GAME OVER', large_v_font, black, 800, 400)
            draw_text(screen, 'You have gone bankrupt', medium_v_font, black, 750, 440)

        elif current_screen == screens.get('WIN'):
            pygame.display.set_caption('You won!')
            screen.fill(green)
            done = pygame.image.load('images/money-bag.png')
            screen.blit(done, (150, 200))
            draw_text(screen, 'You won!!', large_v_font, black, 800, 400)


        # Required to update screen
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
