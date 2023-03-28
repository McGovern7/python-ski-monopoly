class Card:
    #create card that is either chance/community chest, has a message, and result in a payment (can also be negative)
    def __init__(self, type_of_card, card_message, resulting_payment, resulting_movement):
        self.kind = type_of_card
        self.message = card_message
        self.payment = resulting_payment
        self.movement = resulting_movement

    #TODO - need a function to move the player however many spaces (for chance cards), AND
    #TODO calculate how many spaces to certain property and move the player
    #function to return the message of the card and impact your bank account
    def play_card(self, bank_account):
        #if the payment is positive, deposit money
        if self.payment > 0:
            bank_account.deposit(self.payment)
        else:
            bank_account.withdraw(-1*self.payment)
        #if negative withdraw money from account
        return self.message
    def print(self):
        print(self.kind + ": " + self.message)


