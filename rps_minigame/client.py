import pygame
from network import Network
import pickle
pygame.font.init()

width = 700
height = 700


class Button:
    def __init__(self, text, x, y, color):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 20)
        text = font.render(self.text, True, (255, 255, 255))
        win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), (self.y + round(self.height/2) - round(text.get_height()/2))))

    def click(self, pos):
        mouse_x = pos[0]
        mouse_y = pos[1]
        if self.x <= mouse_x <= self.x + self.width and self.y <= mouse_y <= self.y + self.height:
            return True
        else:
            return False


def redraw_window(win, game, p, game_id):
    win.fill((128, 128, 128))

    if not game.connected():
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render("Waiting for Opponent...", 1, (255, 0, 0), True)
        win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
    else:
        font = pygame.font.SysFont("comicsans", 30)

        text = font.render("Game " + str(game_id + 1), 1, (0, 255, 255))
        win.blit(text, (width / 2 - text.get_width() / 2, 50))

        text = font.render("You are player " + str(p + 1), 1, (0, 255, 255))
        win.blit(text, (width/2 - text.get_width()/2, 100))

        text = font.render("Your Move", 1, (0, 255, 255))
        win.blit(text, (80, 200))

        text = font.render("Opponent", 1, (0, 255, 255))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.both_went():
            text1 = font.render(move1, 1, (0, 0, 0))
            text2 = font.render(move2, 1, (0, 0, 0))
        else:
            if game.p1_went and p == 0:
                text1 = font.render(move1, 1, (0, 0, 0))
            elif game.p1_went:
                text1 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = font.render("Waiting...", 1, (0, 0, 0))

            if game.p2_went:
                if p == 1:
                    text2 = font.render(move2, 1, (0, 0, 0))
                else:
                    text2 = font.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = font.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))

        for btn in btns:
            btn.draw(win)

    pygame.display.update()


btns = [Button("Rock", 50, 500, (0, 0, 0)), Button("Scissors", 250, 500, (255, 0, 0)), Button("Paper", 450, 500, (0, 255, 0))]
def main():
    run = True
    clock = pygame.time.Clock()
    ip = input("Enter your ip: ")
    n = Network(ip)
    player = n.get_p()
    game_id = n.get_game_id()
    print("You are player", player)

    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Client")

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.both_went():
            redraw_window(win, game, player, game_id)
            pygame.time.delay(200)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game")
                break

            font = pygame.font.SysFont("comicsans", 45)
            if game.winner() == player:
                text = font.render("You Won!", 1, (255, 0, 0))
            elif game.winner() == -1:
                text = font.render("Tie Game!", 1, (255, 0, 0))
            else:
                text = font.render("You Lost...", 1, (255, 0, 0))

            win.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(2000)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        if player == 0:
                            if not game.p1_went:
                                n.send(btn.text)
                        else:
                            if not game.p2_went:
                                n.send(btn.text)

        redraw_window(win, game, player, game_id)


main()
