import pygame
import random
import math

FRICTION = 0.96
ROLL_SPEED = 6


class Die:
    def __init__(self, screen, start_x, start_y, dimensions):
        self.start_x = self.x = start_x
        self.start_y = self.y = start_y - 1
        self.at_start = True

        self.x_vel = random.uniform(-10, 10)
        self.y_vel = random.uniform(-20, -1)

        size = screen.get_size()
        self.left_bound = size[0] - (0.2 * size[0])
        self.right_bound = size[0]
        self.upper_bound = size[1] - (0.2 * size[0])
        self.lower_bound = size[1]

        self.faces = []
        for i in range(1, 7):
            self.faces.append(pygame.image.load("images/dice/still/" + str(i) + ".png"))
            self.faces[i-1] = pygame.transform.scale(self.faces[i-1], dimensions)
        self.face = self.faces[0]

        self.rolling = []
        for i in range(1, 9):
            self.rolling.append(pygame.image.load("images/dice/rolling/" + str(i) + ".png"))
            self.rolling[i-1] = pygame.transform.scale(self.rolling[i-1], (dimensions[0] * 1.5, dimensions[1] * 1.5))

    def reset(self):
        mod = 10
        self.x_vel = (self.start_x - self.x) / mod
        self.y_vel = (self.start_y - self.y) / mod

        self.move()

        if -2 < self.start_x - self.x < 2 and -2 < self.start_y - self.y < 2:
            self.x = self.start_x
            self.y = self.start_y

    def get_vel(self):
        return math.sqrt(self.x_vel**2 + self.y_vel**2)

    def roll(self, counter, value=None):
        """

        :param counter:
        :param value:
        :return:
        """

        if not value:
            value = random.randint(1, 6)

        self.x_vel *= FRICTION
        self.y_vel *= FRICTION

        self.move()

        if counter % ROLL_SPEED == 0:
            self.face = self.rolling[random.randint(0, 7)]

        if -0.3 < self.get_vel() < 0.3:
            self.face = self.faces[value-1]
            return value + 1
        else:
            return -1

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

        if self.x + self.face.get_width() > self.right_bound:
            self.x_vel *= -1
            self.x += self.x_vel

        if self.y + self.face.get_height() > self.lower_bound:
            self.y_vel *= -1
            self.y += self.y_vel

        if self.x == self.start_x and self.y == self.start_y:
            self.at_start = True
            self.x_vel = random.uniform(-10, 10)
            self.y_vel = random.uniform(-20, -1)
        else:
            self.at_start = False

    def draw(self, screen):
        screen.blit(self.face, (self.x, self.y))
