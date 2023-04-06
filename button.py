import pygame

pygame.init()

button_font = pygame.font.SysFont('Verdana', 20)

white = (255, 255, 255)
gray = (170, 170, 170)


# button class
class Button:
    # initializes all button attributes
    def __init__(self, image, x, y, text_input, text_color, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_color = text_color
        self.text_input = text_input
        self.text = button_font.render(self.text_input, True, self.text_color)
        self.text_rect = self.text.get_rect(center=(self.x, self.y))
        self.clicked = False

    # draws the button
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
        self.check_click()

    def check_click(self):
        # get mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            # clicked
            if pygame.mouse.get_pressed()[0] == 1:
                return True
            else:
                self.text = button_font.render(self.text_input, True, gray)
                return False
        else:
            self.text = button_font.render(self.text_input, True, self.text_color)

