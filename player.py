import pygame
from bank_account import Bank_Account

pygame.init()

icons = ['images/icon1.png',
         'images/icon2.png',
         'images/icon3.png',
         'images/icon4.png']


class Player:
    # Creates a player object
    # Player has a name, position on the board, bank account, property list, get out of jail free card,
    # and 'bankrupt' bool which signifies if they lose the game
    def __init__(self, is_computer, icon_num, player_name, scale, icon_positions):
        self.computer = is_computer
        self.icon_num = icon_num
        self.name = player_name
        self.number = int(player_name[7]) - 1
        self.scale = scale
        self.bank = Bank_Account(self.name)
        self.board_positions = icon_positions
        # Start location is at icon_positions[0] (this is a coordinate)
        self.location = 0
        # All players start the game with no properties, railroads, or utilities
        self.property_list = []
        self.railroad_list = []
        self.utility_list = []
        # All players are created with it not being their turn to play
        self.jail = False
        self.rolls_in_jail = -1
        self.jail_free = 1
        self.bankrupt = False
        self.overlap = False
        self.last_roll = -1

    def draw(self, screen, coordinates=0):
        if not self.bankrupt:
            image = icons[self.icon_num]
            player_icon = pygame.image.load(image).convert_alpha()
            width = player_icon.get_width()
            height = player_icon.get_height()

            # Get coordinate for where to draw player (only need this if want to chance their position)
            if coordinates == 0:
                coordinates = str(self.board_positions[int(self.location)])
                coordinates_split = coordinates[1:len(coordinates)-1].split(', ')
                coordinates = (float(coordinates_split[0]), float(coordinates_split[1]))
            x_coord = float(coordinates[0])
            y_coord = float(coordinates[1])

            # Have a different location for if player is in jail/just visiting
            if self.jail and self.location == 10:
                # In jail
                screen.blit(pygame.transform.scale(player_icon, (int(width * self.scale), int(height * self.scale))),
                            (x_coord + 20, y_coord + 20))
            elif not self.jail and self.location == 10:
                # Just visiting jail
                screen.blit(pygame.transform.scale(player_icon, (int(width * self.scale), int(height * self.scale))),
                            (x_coord - 30, y_coord))
            elif self.overlap:
                screen.blit(pygame.transform.scale(player_icon, (int(width * self.scale), int(height * self.scale))),
                            (x_coord + 30, y_coord))

            # If there are no edits to position on a square
            else:
                screen.blit(pygame.transform.scale(player_icon, (int(width * self.scale), int(height * self.scale))),
                            coordinates)

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

    # function to buy railroad
    def buy_railroad(self, new_railroad):
        # withdraw the money from player's account
        self.bank.withdraw(new_railroad.price)
        # add this player's railroad list
        self.railroad_list.append(new_railroad)
        # update the owner
        new_railroad.owner = self.name

        # If this is the first railroad, rent is the same
        if len(self.railroad_list) > 1:
            # Update what the rent is for every railroad if owns more than 1 railroad
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
        self.utility_list.append(new_utility)
        # update the owner
        new_utility.owner = self.name

        # function to sell a railroad

    def sell_utility(self, utility):
        # remove property from player's property list
        self.utility_list.remove(utility)
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
        # Make sure icon loops back to beginning of list if it reaches the end
        if (self.location + spaces_moved) > 39:
            # Player passed go
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
        # Go to the jail spot
        self.location = 10
        # Increment number of times player rolled in jail
        self.rolls_in_jail += 1
        # If the number of rolls is 3, the player must get out by paying a fine of $50
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
        # Get out of jail
        self.jail = False
        # Once used, you lose the card
        self.jail_free -= 1