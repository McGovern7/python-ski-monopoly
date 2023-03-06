from Bank_Account import Bank_Account
class Property:
    #creates a new property based on ski resort name, region(color) the resort is in, cost to buy property,
    # house price, hotel price, rent_amount
    def __init__(self, resort_name, resort_region, cost, house_cost, hotel_cost, rent_amount,
                 rent_with_1_house, rent_with_2_houses, rent_with_3_houses, rent_with_4_houses,
                 rent_with_hotel):
        self.property_name = resort_name
        self.region = resort_region
        self.price = cost
        self.house_price = house_cost
        self.hotel_price = hotel_cost
        self.original_rent = rent_amount
        self.rent_1house = rent_with_1_house
        self.rent_2house= rent_with_2_houses
        self.rent_3house = rent_with_3_houses
        self.rent_4house = rent_with_4_houses
        self.rent_hotel = rent_with_hotel
        #start with no houses or hotels on property
        self.num_houses = 0
        self.num_hotels = 0
        #current rent is the original rent (at the start)
        self.rent = self.original_rent
        #starts not being part of a monopoly
        self.part_of_monopoly = False
    #function to double rent if the property becomes part of a monopoly
    def in_monopoly(self):
        self.part_of_monopoly = True
        #this doubles the cost of rent
        self.rent *= 2
    #function to buy a house on property using player's bank account
    def buy_house(self, bank_account):
        #property must be a part of a monopoly, have less than 4 houses on it, and not have a hotel
        if self.part_of_monopoly == True and self.num_houses < 4 and self.num_hotels==0:
            bank_account.withdraw(self.house_price)
            self.num_houses += 1
            #this changes the rent based on how many houses you have
            if self.num_houses == 1:
                self.rent = self.rent_1house
            elif self.num_houses ==2:
                self.rent = self.rent_2house
            elif self.num_houses ==3:
                self.rent = self.rent_3house
            elif self.num_houses ==4:
                self.rent = self.rent_4house
            else:
                print("Something went wrong!")

        else:
            print("You cannot put a house on this property right now (must be part of monopoly, have < 4 houses, no hotels)")

    #function to sell house using player's bank account to give them back the money
    def sell_house(self, bank_account):
        #can only sell a house if you have one
        if self.num_houses > 0 :
            #put money back in the bank account
            bank_account.deposit(self.house_price)
            #decrease number of houses owned
            self.num_houses -= 1
            #this changes the rent depending on how many houses you own
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
    #function to buy a hotel on property using player's bank account
    def buy_hotel(self, bank_account):
        #must have 4 houses to buy a hotel and no other hotels, otherwise print message
        if self.num_houses == 4 and self.num_hotels == 0:
            bank_account.withdraw(self.hotel_price)
            self.num_hotels += 1
            # have to give all houses back to the bank
            self.num_houses=0
            #this changes the rent
            self.rent = self.rent_hotel
        else:
            print("You must have 4 houses on the property before you can purchase a hotel.")
    #function to sell the hotel using player's bank account to give back the money
    def sell_hotel(self, bank_account):
        #can only sell a hotel if you have one
        if self.num_hotels == 1:
            #get the money back in your account
            bank_account.deposit(self.hotel_cost)
            #go back to having 4 houses
            self.num_houses = 4
            #this changes the rent
            self.rent = self.rent_4house
        else:
            print("You cannot sell a hotel")

    #function to print property info
    def print(self):
        print("Property name: " + self.property_name + "\nRent: " + str(format(self.rent)))

#TEST
# P1BA = Bank_Account("Player 1")
# Boardwalk = Property("Boardwalk", "Blue", 400, 200, 200, 50,  200, 600, 1400, 1700, 2000)
# Boardwalk.in_monopoly()
# Boardwalk.buy_house(P1BA)
# Boardwalk.print()
