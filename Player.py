class Player:
    #Creates a player object
    #Player has a name, position on the board, bank account, property list, get out of jail free card,
    #and 'bankrupt' bool which signifies if they lose the game
    def __init__(self, player_icon, player_name, board_position, bank_account):
        ##TODO -- Need a field for player vs computer
        self.icon = player_icon
        self.name = player_name
        self.board_position = board_position
        self.bank_account = bank_account
        self.property_list = []
        self.jail_free = false
        self.bankrupt = false

    ##TODO -- Update the property list
    def update_properties(self, new_property):
        self.property_list.append(new_property)

    ##TODO -- Check if a certain property is owned
    def check_properties(self, new_property):
        pass
    ##TODO -- Remove a property
    def remove_property(self, new_property):
        pass

    ##TODO -- Update board position

    ## TODO -- Check board position

    #Check if the player currently has a get out of jail free card
    def check_jail_free(self):
        return self.jail_free

    #Sets the get out of jail free card to positive when the player obtains one
    def set_jail_free(self):
        self.jail_free = true

    # Sets the get out of jail free card to negative when the player uses it
    def use_jail_free(self):
        self.jail_free = false

    #Updates bankrupt field, indicating the player loses
    def gone_bankrupt(self):
        self.bankrupt = true
