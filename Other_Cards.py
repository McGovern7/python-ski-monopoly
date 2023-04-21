class Railroad:
    #creates a railroad based on name
    def __init__(self, railroad_name, board_location):
        self.name = railroad_name
        #rent starts at 25 for one railroad
        self.rent = 25
        self.price = 200
        self.owner = 'NONE'
        #location on board
        self.location = board_location
        #starts off without a mortgage
        self.mortgaged = False

    #function to mortgage a railroad
    def mortgage(self, bank_account):
        #return half the money to the player
        bank_account.deposit(self.price/2)
        #mark the property as mortgaged (player will not collect rent anymore)
        self.mortgaged = True

    #function to remove mortgage from railroad
    def remove_mortgage(self, bank_account):
        #player owes half the price of the property + 10%
        bank_account.withdraw(self.price/2 + self.price/2*.1)
        #mark property as not mortgaged (active now)
        self.mortgaged = False
class Utility:
    #creates a railroad based on name
    def __init__(self, utility_name, board_location):
        self.name = utility_name
        self.price = 150
        self.owner = 'NONE'
        #location on board
        self.location = board_location
        #starts off without a mortgage
        self.mortgaged = False

    #function to mortgage a railroad
    def mortgage(self, bank_account):
        #return half the money to the player
        bank_account.deposit(self.price/2)
        #mark the property as mortgaged (player will not collect rent anymore)
        self.mortgaged = True

    #function to remove mortgage from railroad
    def remove_mortgage(self, bank_account):
        #player owes half the price of the property + 10%
        bank_account.withdraw(self.price/2 + self.price/2*.1)
        #mark property as not mortgaged (active now)
        self.mortgaged = False

    #Function to determine what the rent should be (based on dice roll value)
    def calculate_rent(self, utility_owner, dice_roll):
        #if the owner own only 1 utility, rent is 4 times dice roll
        print(len(utility_owner.utilities_list))
        print(dice_roll)
        if len(utility_owner.utilities_list) == 1:
            rent = 4* int(dice_roll)
            print(rent)
        #if the owner has 2 utilities, rent is 10 times dice roll
        elif len(utility_owner.utilities_list) == 2:
            rent = 10* int(dice_roll)
        else:
            print("something went wrong - too many utilities owned")
            rent = 0
        return rent