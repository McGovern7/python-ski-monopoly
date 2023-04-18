from player import Player
from die import Die

MAX_PLAYERS = 4
MIN_PLAYERS = 2


class Game:
    def __init__(self, id):
        self.game_id = id
        self.players = []
        self.player_turn = 0
        self.dice = []
        self.is_playing = False
        self.current_screen = "TURNS"
        self.icons = ['images/icon1.png',
                      'images/icon2.png',
                      'images/icon3.png',
                      'images/icon4.png']

    def get_id(self):
        return self.game_id

    def get_players(self):
        return self.players

    def get_num_players(self):
        return len(self.players)

    def get_dice(self):
        return self.dice

    def add_player(self):
        player_num = len(self.players)
        self.players[player_num] = Player(self.icons[player_num], 'Player ' + str(player_num), .6, [])
