import pygame

pygame.init()
# Create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

button_font = pygame.font.SysFont('Verdana', 20)
white = (255, 255, 255)
light_gray = (211, 211, 211)
gray = (175, 175, 175)


# button class
class Button():
    # initializes all button attributes
    def __init__(self, image, x, y, text_input, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_input = text_input
        self.text = button_font.render(self.text_input, True, white)
        self.text_rect = self.text.get_rect(center=(self.x, self.y))
        self.clicked = False

    # draws the button
    def draw(self):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
        self.check_click()

    def check_click(self):
        action = False
        # get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            # clicked
            if pygame.mouse.get_pressed()[0] == 1:
                self.text = button_font.render(self.text_input, True, gray)
                self.clicked = True
                action = True
            # hover
            else:
                self.text = button_font.render(self.text_input, True, light_gray)
                if self.clicked:
                    self.clicked = False
                    action = False
        else:
            self.text = button_font.render(self.text_input, True, white)

        return action
