import random

from die import Die
from player import Player
from Property import Property
from Other_Cards import Railroad
from Other_Cards import Utility
from card import Card

MAX_PLAYERS = 4
MIN_PLAYERS = 2

screens = {
    'START': 1,
    'TURNS': 2,
    'BOARD': 3,
    'PROPS': 4,
    'CARDS': 5
}


class Game:
    def __init__(self, id):
        self.game_id = id
        self.players = []
        self.player_turn = 0  # The index of the players array that holds the player whose turn it is
        self.dice_values = [1, 1]
        self.is_playing = False
        self.current_screen = screens.get('START')
        self.available_icons = [True, True, True, True]
        self.turn_rolls = []
        self.cards = self.load_cards()
        self.properties = self.load_properties()
        self.railroads = [Railroad('Locke Mountain T-bar', 5),
                          Railroad('Bonaventure Quad', 15),
                          Railroad('Aerial Tramway', 25),
                          Railroad('Gondola One', 35)]
        self.utilities = [Utility('Snow Gun', 12),
                          Utility('Snow Groomer', 28)]

    def get_id(self):
        return self.game_id

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)

    def roll(self):
        self.dice_values = [random.randint(1, 6), random.randint(1, 6)]

    def done_roll(self, die1_value, die2_value):
        self.players[self.player_turn].last_roll = die1_value + die2_value
        if self.current_screen == screens.get('TURNS'):
            self.turn_rolls.append(die1_value + die2_value)
            self.next_player()
            if len(self.turn_rolls) == len(self.players):
                unset_players = self.players.copy()
                self.players.clear()
                for j in range(0, len(unset_players)):
                    largest = self.turn_rolls.index(max(self.turn_rolls))
                    self.players.append(unset_players[largest])  # appends correct player to empty list
                    self.turn_rolls[largest] = -1  # get rid of the largest element in list
                self.current_screen = screens.get('BOARD')
        elif self.current_screen == screens.get('BOARD'):
            self.get_curr_player().movement(die1_value + die2_value)
            if die1_value != die2_value:
                self.next_player()

    def next_player(self):
        self.player_turn = (self.player_turn + 1) % self.get_num_players()
        if self.get_curr_player().bankrupt:
            print('next player')
            self.next_player()

    def set_screen(self, screen_name):
        self.current_screen = screens.get(screen_name)

    def screen_is(self, screen_name):
        return self.current_screen == screens.get(screen_name)

    def get_curr_player(self):
        return self.players[self.player_turn]

    def get_icon_positions(self):
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

    def add_player(self):
        icon_num = 0
        while not self.available_icons[icon_num]:
            icon_num = (icon_num + 1) % len(self.available_icons)
        self.players.append(Player(False, icon_num, 'Player ' + str(self.get_num_players() + 1), 1, self.get_icon_positions()))
        self.available_icons[icon_num] = False

    def set_icon(self, player_num, icon_num):
        """
        Changes the given player's icon
        :param player_num:
        :param icon_num:
        :return:
        """
        player = self.players[player_num]
        # Make old icon available for other players
        self.available_icons[player.icon_num] = True
        player.icon_num = icon_num
        # Make new icon unavailable
        self.available_icons[icon_num] = False

    def load_properties(self):
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
                                property_features[8], property_features[9], property_features[10],
                                property_features[11])
            properties.append(new_prop)

        file.close()
        return properties

    def load_cards(self):
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
