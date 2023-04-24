import random

from die import Die
from player import Player

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

    def get_id(self):
        return self.game_id

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)

    def roll(self):
        self.dice_values = [random.randint(0, 5), random.randint(0, 5)]

    def done_roll(self, last_roll):
        if self.current_screen == screens.get('TURNS'):
            self.turn_rolls.append(last_roll)
        if len(self.turn_rolls) == len(self.players):
            unset_players = self.players.copy()
            for j in range(0, len(unset_players)):
                largest = self.turn_rolls.index(max(self.turn_rolls))
                self.players[j] = unset_players[largest]  # appends correct player to empty list
                self.turn_rolls[largest] = -1  # get rid of the largest element in list
            self.current_screen = screens.get('BOARD')
        self.players[self.player_turn].last_roll = last_roll

    def next_player(self):
        self.player_turn = (self.player_turn + 1) % self.get_num_players()

    def set_screen(self, screen_name):
        self.current_screen = screens.get(screen_name)

    def screen_is(self, screen_name):
        return self.current_screen == screens.get(screen_name)

    def get_curr_player(self):
        return self.players[self.player_turn]

    def add_player(self):
        icon_num = 0
        while not self.available_icons[icon_num]:
            icon_num = (icon_num + 1) % len(self.available_icons)
        self.players.append(Player(icon_num, 'Player ' + str(self.get_num_players() + 1), .6, []))
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
