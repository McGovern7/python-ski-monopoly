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
        #all player start the game with no railroads
        self.railroad_list = []
        # all player start the game with no utilities
        self.utilities_list = []
        #all players are created with it not being their turn to play
        self.jail= False
        self.rolls_in_jail = -1
        self.jail_free = 0
        #TODO - have an end to the game if someone goes bankrupt
        self.bankrupt = False

    def draw(self, screen):
        #get coordinate for where to draw player (only need this if want to chance their position)
        coordinates = str(self.board_positions[int(self.location)])
        coordinates_list = coordinates[1:len(coordinates) - 1].split(',')
        x_coord = float(coordinates_list[0])
        y_coord = float(coordinates_list[1])

        #have a different location for if player is in jail/just visiting
        if self.jail and self.location == 10:
            #in jail
            screen.blit(self.player_icon, (x_coord+20, y_coord+20))
        elif not self.jail and self.location == 10:
            #just visiting jail
            screen.blit(self.player_icon, (x_coord-30, y_coord))

        #if there are no edits to position on a square
        else:
            screen.blit(self.player_icon, self.board_positions[int(self.location)])
    # function to buy a property
    def buy_property(self, new_property):
        new_property.owner = self.name
        # add it to their property list
        self.property_list.append(new_property)
        self.bank.withdraw(int(new_property.price))

    # function to sell a property
    def sell_property(self, property):
        # remove property from player's property list
        self.property_list.remove(property)
        # give them the money back
        self.bank.deposit(property.price)
        # if there are hotels/houses, sell these back too
        if property.num_hotels > 0:
            property.sell_hotel(self.bank)
        if property.num_houses > 0:
            for i in range(0, property.num_houses):
                property.sell_house(self.bank)

    def check_properties(self, new_property):
        if new_property in self.property_list:
            return True
        else:
            return False

    # function to buy railroad
    def buy_railroad(self, new_railroad):
        # withdraw the money from player's account
        self.bank.withdraw(new_railroad.price)
        # add this player's railroad list
        self.railroad_list.append(new_railroad)
        # update the owner
        new_railroad.owner = self.name

        #if this is the first railroad, rent is the same
        if len(self.railroad_list) > 1:
            #update what the rent is for every railroad if owns more than 1 railroad
            if len(self.railroad_list) == 2:
                new_rent = 50
            elif len(self.railroad_list) == 3:
                new_rent = 100
            elif len(self.railroad_list) == 4:
                new_rent = 200
            else:
                print('Too many railroads')
                new_rent = 200
            for railroad in self.railroad_list:
                railroad.rent = new_rent

    # function to sell a railroad
    def sell_railroad(self, railroad):
        # remove property from player's property list
        self.railroad_list.remove(railroad)
        # give them the money back
        self.bank.deposit(railroad.price)

    # function to buy utility
    def buy_utility(self, new_utility):
        # withdraw the money from player's account
        self.bank.withdraw(new_utility.price)
        # add this player's railroad list
        self.utilities_list.append(new_utility)
        # update the owner
        new_utility.owner = self.name

        # function to sell a railroad
    def sell_utility(self, utility):
        # remove property from player's property list
        self.utilities_list.remove(utility)
        # give them the money back
        self.bank.deposit(utility.price)


    # function pay taxes -- pays either 10% of your income or $200 (whichever is smaller)
    def pay_taxes(self):
        # 10% of income
        percentage_tax = self.bank.total * .1
        # if 10% of income is less than $200, pay this
        if percentage_tax < 200:
            self.bank.withdraw(percentage_tax)
        else:
            self.bank.withdraw(200)

    def movement(self, spaces_moved):
        #make sure icon loops back to beginning of list if it reaches the end
        if (self.location + spaces_moved) > 39:
            #player passed go
            self.go()
            self.location = (self.location + spaces_moved) % 40
        else:
            self.location += spaces_moved

    def check_position(self):
        return self.board_positions[self.location]

    # function to pay another player rent when you land on their property
    # pass the property owner's bank account and the rent you owe them
    def pay_rent(self, landlord, rent_owed):
        self.bank.withdraw(rent_owed)
        landlord_bank = landlord.bank
        landlord_bank.deposit(rent_owed)

    # function to call everytime a player goes over "GO" board space
    def go(self):
        self.bank.total += 200

    # Check if the player currently has a get out of jail free card
    def check_jail_free(self):
        pass
        # return self.jail_free

    # Sets the get out of jail free card to positive when the player obtains one
    def go_to_jail(self):
        self.jail = True
        #go to the jail spot
        self.location = 10
        #increment number of times player rolled in jail
        self.rolls_in_jail += 1
        #if the number of rolls is 3, the player must get out by paying a fine of $50
        if self.rolls_in_jail >= 3:
            self.bank.withdraw(50)
            self.jail = False
            return ''
        return 'jail'

    # Sets the get out of jail free card to negative when the player uses it
    def use_jail_free(self):
        if self.jail_free == 0:
            print('You don\'t have this card to use')
            return
        #get out of jail
        self.jail = False
        #once used, you lose the card
        self.jail_free -= 1


    # Updates bankrupt field, indicating the player loses
    def gone_bankrupt(self):
        pass
        # self.bankrupt = true


