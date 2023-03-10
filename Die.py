import pygame
import random
import math

FRICTION = 0.996


class Die:
    def __init__(self, screen, start_x, start_y, dimensions):
        self.start_x = self.x = start_x
        self.start_y = self.y = start_y
        self.x_vel = random.uniform(-2, 2)
        self.y_vel = random.uniform(-2, -1)

        size = screen.get_size()
        self.left_bound = size[0] - (0.2 * size[0])
        self.right_bound = size[0]
        self.upper_bound = size[1] - (0.2 * size[0])
        self.lower_bound = size[1]

        self.faces = []
        for i in range(1, 7):
            self.faces.append(pygame.image.load("dice/still/" + str(i) + ".png"))
            self.faces[i-1] = pygame.transform.scale(self.faces[i-1], dimensions)
        self.face = self.faces[0]

        self.rolling = []
        for i in range(1, 9):
            self.rolling.append(pygame.image.load("dice/rolling/" + str(i) + ".png"))
            self.rolling[i-1] = pygame.transform.scale(self.rolling[i-1], (dimensions[0] * 1.5, dimensions[1] * 1.5))

    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.x_vel = random.uniform(-1, 1)
        self.y_vel = random.uniform(-1, -1)

    def get_vel(self):
        return math.sqrt(self.x_vel**2 + self.y_vel**2)

    def roll(self, counter):
        if -0.2 < self.get_vel() < 0.2:
            self.x_vel = 0
            self.y_vel = 0

        self.x += self.x_vel
        self.y += self.y_vel

        if self.x + self.face.get_width() > self.right_bound:
            self.x_vel *= -1
            self.x += self.x_vel

        if self.y + self.face.get_height() > self.lower_bound:
            self.y_vel *= -1
            self.y += self.y_vel

        self.x_vel *= FRICTION
        self.y_vel *= FRICTION

        if counter % 25 == 0:
            self.face = self.rolling[random.randint(0, 7)]

        if self.x_vel == 0 and self.y_vel == 0:
            value = random.randint(0, 5)
            self.face = self.faces[value]
            return value + 1
        else:
            return -1

    def draw(self, screen):
        screen.blit(self.face, (self.x, self.y))
