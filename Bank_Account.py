class Bank_Account:
    #creates a players bank account with start amount ($1500)
    def __init__(self, player):
        self.name = player
        self.total = 1500
    #function to deposit money from the bank into player account
    def deposit(self, payment):
        self.total += payment
    #function that gives money back to the bank
    def withdraw(self, payback):
        self.total -= payback
    #function to pay another player rent when you land on their property
    #pass the property owner's bank account and the rent you owe them
    def pay_rent(self, property_owner_account, rent_owed):
        self.withdraw(rent_owed)
        property_owner_account.deposit(rent_owed)
    #function to call everytime a player goes over "GO" board space
    def go(self):
        self.total += 200
    #function pay taxes -- pays either 10% of your income or $200 (whichever is smaller)
    def pay_taxes(self):
        #10% of income
        percentage_tax = self.total * .1
        #if 10% of income is less than $200, pay this
        if percentage_tax < 200:
            self.withdraw(percentage_tax)
        else:
            self.withdraw(200)

    #prints total amount in player's bank account
    def print(self):
        print(str(self.name) + ": $" + str(format(self.total,'.2f')))
P1BA = Bank_Account("Player 1")