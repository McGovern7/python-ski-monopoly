class ButtonGroup:
    def __init__(self, buttons=[]):
        self.buttons = buttons

    def add_button(self, button):
        self.buttons.append(button)

    def draw(self, screen):
        for button in self.buttons:
            button.show()
            button.draw(screen)

    def hide(self):
        for button in self.buttons:
            button.hide()

    def check_click(self):
        number = -1
        for i in range(0, len(self.buttons)):
            if self.buttons[i].check_click():
                number = i
            else:
                self.buttons[i].clicked = False
        # if number != -1:
        #     for i in range(0, len(self.buttons)):
        #         if i == number:
        #             self.buttons[i].clicked = True
        #         else:
        #             self.buttons[i].clicked = False
