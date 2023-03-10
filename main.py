import sys
import pygame as pg
from Bank_Account import Bank_Account


def player1():
    screen.blit(player1_icon, (player1_x, player1_y))


# house graphic
def create_house(x, y):
    house = pygame.image.load("home.png")
    screen.blit(house, (x, y))


# hotel graphic
def create_hotel(x, y):
    hotel = pygame.image.load("hotel.png.png")
    screen.blit(hotel, (x, y))


def create_card(x, y, region_color):
    # text on every property card
    deed_text = small_font_4.render("TITLE DEED", True, black)
    property_text = small_font_1.render("Property Name", True, black)
    rent_text = small_font_2.render("Rent: $", True, black)
    house_1_text = small_font_3.render("With 1 House", True, black)
    house_2_text = small_font_3.render("With 2 Houses", True, black)
    house_3_text = small_font_3.render("With 3 Houses", True, black)
    house_4_text = small_font_3.render("With 4 Houses", True, black)
    hotel_text = small_font_3.render("With Hotel", True, black)
    cost_text_1 = small_font_3.render("Houses cost $", True, black)
    cost_text_2 = small_font_3.render("Hotel costs $", True, black)
    # draw
    pygame.draw.rect(screen, white, (x, y, 150, 200))
    pygame.draw.rect(screen, region_color, (x + 5, y + 5, 140, 50))
    screen.blit(deed_text, (90, 160))
    screen.blit(property_text, (70, 180))
    screen.blit(rent_text, (90, 215))
    screen.blit(house_1_text, (60, 235))
    screen.blit(house_2_text, (60, 250))
    screen.blit(house_3_text, (60, 265))
    screen.blit(house_4_text, (60, 280))
    screen.blit(hotel_text, (60, 295))
    screen.blit(cost_text_1, (60, 320))
    screen.blit(cost_text_2, (60, 330))


def roll_dice(pg):
    '''

    :return:
    '''


# SCREENS
# start screen
def start_screen():
    # game title and icon
    pygame.display.set_caption("Monopoly | Ski Resort Edition")
    icon = pygame.image.load("ski-resort.png")
    pygame.display.set_icon(icon)
    while True:
        return True


# board screen
def board_screen():
    while True:
        return True


# card screen
def card_screen():
    pygame.display.set_caption("Your cards")
    text1 = font.render("Available money: ", True, white)
    text2 = font.render("Properties: ", True, white)
    while True:
        screen.fill(green)
        screen.blit(text1, (50, 50))
        screen.blit(text2, (50, 100))
        # create card
        create_card(50, 150, blue)
        create_house(100, 500)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        return True


def main():
    # Initialize PyGame
    pygame.init()

    # make screen
    screen = pygame.display.set_mode((1200, 800))

    # constants
    # TODO - which font should we use?
    # print(pygame.font.get_fonts())
    FONT_NAME = "times"
    font = pygame.font.SysFont(FONT_NAME, 30)
    small_font_1 = pygame.font.SysFont(FONT_NAME, 16)
    small_font_2 = pygame.font.SysFont(FONT_NAME, 15)
    small_font_3 = pygame.font.SysFont(FONT_NAME, 12)
    small_font_4 = pygame.font.SysFont(FONT_NAME, 10)
    green = (0, 100, 0)
    white = (255, 255, 255)
    black = (0, 0, 0)
    blue = (30, 144, 225)

    # TODO - was just messing around with player icons (definitely feel free to change)
    # Players
    # P1
    player1_icon = pygame.image.load("skiing.png")
    player1_x = 300
    player1_y = 600
    # # P2
    # player2_icon = pygame.image.load("deposit.png")
    # player2_x= 500
    # player2_y= 600
    # # P3
    # player3_icon = pygame.image.load("deposit.png")
    # player3_x = 300
    # player3_y = 300
    # # P4
    # player4_icon = pygame.image.load("deposit.png")
    # player4_x = 300
    # player4_y = 300

    # Game loop
    TEST_DICE = True
    while True:
        # start_screen()
        card_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if TEST_DICE:
            roll_dice(pygame)

        pygame.display.update()


if __name__ == "__main__":
    main()
