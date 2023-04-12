import pygame

pygame.init()

button_font = pygame.font.SysFont('Verdana', 20)

white = (255, 255, 255)
gray = (170, 170, 170)
dark_gray = (150, 150, 150)


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
        self.clicked = False

    # draws the button
    def draw(self, screen):
        self.check_click()

        screen.blit(self.image, self.rect)

        text = button_font.render(self.text_input, True, self.text_color)
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)

    def check_click(self):
        # Check mouse position
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.text_color = gray
            # clicked
            if pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                self.text_color = dark_gray
                return True
        elif self.clicked:
            self.text_color = dark_gray
        else:
            self.text_color = white

        return False
