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

    #prints total amount in player's bank account
    def print(self):
        print(str(self.name) + ": $" + str(format(self.total,'.2f')))