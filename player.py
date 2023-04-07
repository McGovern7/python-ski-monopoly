import pygame

pygame.init()


class Player:
    # Creates a player object
    # Player has a name, position on the board, bank account, property list, get out of jail free card,
    # and 'bankrupt' bool which signifies if they lose the game
    def __init__(self, player_icon, player_name, bank_account, scale, icon_positions):
        # TODO -- Need a field for player vs computer
        width = player_icon.get_width()
        height = player_icon.get_height()
        self.player_icon = pygame.transform.scale(player_icon, (int(width * scale), int(height * scale)))
        self.name = player_name
        self.bank = bank_account
        self.board_positions = icon_positions
        #start location is at icon_positions[0] (this is a coordinate)
        self.location = 0
        #all players start the game with no properties
        self.property_list = []
        #all players are created with it not being their turn to play
        self.turn = False
        self.jail= False
        self.bankrupt = False

    def draw(self, screen):
        screen.blit(self.player_icon, self.board_positions[self.location])

    def add_property(self, new_property):
        self.property_list.append(new_property)

    def check_properties(self, new_property):
        if new_property in self.property_list:
            return True
        else:
            return False

    def remove_property(self, new_property):
        #make sure this property is in the list
        if new_property not in self.property_list:
            print("this property is not in the list of owned properties")
            return
        else:
            index = self.property_list.index(new_property)
            self.property_list.remove(new_property)

    def movement(self, spaces_moved):
        #make sure icon loops back to beginning of list if it reaches the end
        if (self.location + spaces_moved) > 39:
            self.location = (self.location + spaces_moved) % 40
        else:
            self.location += spaces_moved

    def check_position(self):
        return self.board_positions[self.location]

    # Check if the player currently has a get out of jail free card
    def check_jail_free(self):
        pass
        # return self.jail_free

    # Sets the get out of jail free card to positive when the player obtains one
    def go_to_jail(self):
        self.jail = True
        #go to the jail spot
        self.location = 10

    # Sets the get out of jail free card to negative when the player uses it
    def use_jail_free(self):
        pass
        # self.jail_free = false

    # Updates bankrupt field, indicating the player loses
    def gone_bankrupt(self):
        pass
        # self.bankrupt = true


