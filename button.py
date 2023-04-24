import pygame

pygame.init()

button_font = pygame.font.SysFont('Verdana', 20)

white = (255, 255, 255)
gray = (200, 200, 200)
dark_gray = (180, 180, 180)


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
        self.new_press = False
        self.shown = False

    # draws the button
    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                text_color = dark_gray
            else:
                text_color = gray
        elif self.clicked:
            text_color = dark_gray
        else:
            text_color = white

        screen.blit(self.image, self.rect)

        text = button_font.render(self.text_input, True, text_color)
        text_rect = text.get_rect(center=(self.x, self.y))
        screen.blit(text, text_rect)

    def check_new_press(self):
        if pygame.mouse.get_pressed()[0] and self.new_press:
            self.new_press = False
            return True
        if not pygame.mouse.get_pressed()[0]:
            self.new_press = True
            return False

    def check_click(self):
        # Check mouse position
        if self.shown and self.rect.collidepoint(pygame.mouse.get_pos()):
            print('clicked')
            # clicked
            self.clicked = True
            return True

        return False

    def show(self):
        self.shown = True

    def hide(self):
        self.shown = False