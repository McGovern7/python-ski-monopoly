class Card:
    # create card that is either chance/community chest, has a message, and result in a payment (can also be negative)
    def __init__(self, type_of_card, card_message, resulting_payment, resulting_movement):
        self.kind = type_of_card
        self.message = card_message
        self.payment = resulting_payment
        self.movement = resulting_movement

    # function to do what the card says (move player/gain or lose money)
    def play(self, player):
        bank = player.bank
        # if the payment is positive, deposit money
        if int(self.payment) > 0:
            bank.deposit(self.payment)
        elif int(self.payment) == 0:
            pass
        else:
            # if negative withdraw money from account
            # take off negative sign
            amount = self.payment[1:]
            bank.withdraw(int(amount))
        # if there is a movement forward
        if self.movement[0] == '+':
            player.movement(int(self.movement[1]))
        # if there is a movement backwards
        elif self.movement[0] == '-':
            player.movement(int(self.movement))
        # if there is no movement
        elif self.movement == '*':
            return
        # if there is a movement to a spot
        else:
            player.location = int(self.movement)

    def print(self):
        print(self.kind + ": " + self.message)
