from Bank_Account import Bank_Account


class Property:
    # creates a new property based on ski resort name, region(color) the resort is in, cost to buy property,
    # house price, hotel price, rent_amount
    def __init__(self, resort_name, resort_region, cost, house_cost, hotel_cost, rent_amount,
                 rent_with_1_house, rent_with_2_houses, rent_with_3_houses, rent_with_4_houses,
                 rent_with_hotel, board_location):
        self.property_name = resort_name
        self.region = resort_region
        self.price = cost
        self.house_price = house_cost
        self.hotel_price = hotel_cost
        self.original_rent = rent_amount
        self.rent_1house = rent_with_1_house
        self.rent_2house = rent_with_2_houses
        self.rent_3house = rent_with_3_houses
        self.rent_4house = rent_with_4_houses
        self.rent_hotel = rent_with_hotel
        # location on the board (this aligns with icon_positions[location])
        self.location = board_location
        # start with no houses or hotels on property
        self.num_houses = 0
        self.num_hotels = 1
        # start with no owner
        self.owner = 'NONE'
        # current rent is the original rent (at the start)
        self.rent = self.original_rent
        # starts not being part of a monopoly
        self.part_of_monopoly = False
        # starts off having no mortgage
        self.mortgaged = False
        # how many players are on the square
        self.occupancy = 0

    # function to double rent if the property becomes part of a monopoly
    def in_monopoly(self):
        self.part_of_monopoly = True
        # this doubles the cost of rent
        self.rent *= 2

    # function to buy a house on property using player's bank account
    def buy_house(self, bank_account):
        # property must be a part of a monopoly, have less than 4 houses on it, and not have a hotel
        if self.part_of_monopoly and self.num_houses < 4 and self.num_hotels == 0:
            bank_account.withdraw(self.house_price)
            self.num_houses += 1
            # this changes the rent based on how many houses you have
            if self.num_houses == 1:
                self.rent = self.rent_1house
            elif self.num_houses == 2:
                self.rent = self.rent_2house
            elif self.num_houses == 3:
                self.rent = self.rent_3house
            elif self.num_houses == 4:
                self.rent = self.rent_4house
            else:
                print("Something went wrong!")

        else:
            print("You cannot put a house on this property right now (must be part of monopoly, have < 4 houses, "
                  "no hotels)")

    # function to sell house using player's bank account to give them back the money
    def sell_house(self, bank_account):
        # can only sell a house if you have one
        if self.num_houses > 0:
            # put money back in the bank account (only get half the price back)
            bank_account.deposit(int(self.house_price) / 2)
            # decrease number of houses owned
            self.num_houses -= 1
            # this changes the rent depending on how many houses you own
            if self.num_houses == 0:
                self.rent = self.original_rent
            elif self.num_houses == 1:
                self.rent = self.rent_1house
            elif self.num_houses == 2:
                self.rent = self.rent_2house
            elif self.num_houses == 3:
                self.rent = self.rent_3house
            elif self.num_houses == 4:
                self.rent = self.rent_4house
            else:
                print("Something went wrong!")

        else:
            print("You cannot sell a house")

    # function to buy a hotel on property using player's bank account
    def buy_hotel(self, bank_account):
        # must have 4 houses to buy a hotel and no other hotels, otherwise print message
        if self.num_houses == 4 and self.num_hotels == 0:
            bank_account.withdraw(self.hotel_price)
            self.num_hotels += 1
            # have to give all houses back to the bank
            self.num_houses = 0
            # this changes the rent
            self.rent = self.rent_hotel
        else:
            print("You must have 4 houses on the property before you can purchase ONE hotel.")

    # function to sell the hotel using player's bank account to give back the money
    def sell_hotel(self, bank_account):
        # can only sell a hotel if you have one
        if self.num_hotels == 1:
            # get the money back in your account (only get half the price back)
            bank_account.deposit(int(self.hotel_price) / 2)
            # go back to having 4 houses
            self.num_houses = 4
            # this changes the rent
            self.rent = self.rent_4house
        else:
            print("You cannot sell a hotel")

    # function to mortgage a property
    def mortgage(self, bank_account):
        # return half the money to the player
        bank_account.deposit(int(self.price) / 2)
        self.sell_hotel(bank_account)
        for i in range(0, self.num_houses):
            self.sell_house(bank_account)
        # mark the property as mortgaged (player will not collect rent anymore)
        self.mortgaged = True

    # function to remove mortgage
    def remove_mortgage(self, bank_account):
        # player owes half the price of the property + 10%
        bank_account.withdraw(int(self.price) / 2 + int(self.price) / 2 * .1)
        # mark property as not mortgaged (active now)
        self.mortgaged = False

    # function to print property info
    def print(self):
        print("Property name: " + self.property_name + "\nRent: " + str(format(self.rent)))
