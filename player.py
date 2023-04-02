import pygame

pygame.init()


class Player:
    # Creates a player object
    # Player has a name, position on the board, bank account, property list, get out of jail free card,
    # and 'bankrupt' bool which signifies if they lose the game
    def __init__(self, player_icon, player_name, x, y, turn, is_computer, scale):
        # TODO -- Need a field for player vs computer
        width = player_icon.get_width()
        height = player_icon.get_height()
        self.player_icon = pygame.transform.scale(player_icon, (int(width * scale), int(height * scale)))
        self.name = player_name
        self.x = x
        self.y = y
        self.rect = self.player_icon.get_rect(center=(self.x, self.y))
        self.turn = turn
        self.is_computer = is_computer
        # self.property_list = []
        # self.jail_free = False
        # self.bankrupt = False
        # self.cash = 300000

    def draw(self, screen):
        screen.blit(self.player_icon, self.rect)

    # TODO -- Update the property list
    def update_properties(self, new_property):
        pass
        # self.property_list.append(new_property)

    # TODO -- Check if a certain property is owned
    def check_properties(self, new_property):
        pass

    # TODO -- Remove a property
    def remove_property(self, new_property):
        pass

    # TODO -- Update board position
    def movement(self, ):
        # if self.turn = True:
        pass
    # TODO -- Check board position

    # Check if the player currently has a get out of jail free card
    def check_jail_free(self):
        pass
        # return self.jail_free

    # Sets the get out of jail free card to positive when the player obtains one
    def set_jail_free(self):
        pass
        # self.jail_free = true

    # Sets the get out of jail free card to negative when the player uses it
    def use_jail_free(self):
        pass
        # self.jail_free = false

    # Updates bankrupt field, indicating the player loses
    def gone_bankrupt(self):
        pass
        # self.bankrupt = true
