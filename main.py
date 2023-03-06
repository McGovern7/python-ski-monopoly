import pygame

# Initialize PyGame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Monopoly | Ski Resort Edition")
icon = pygame.image.load("ski-resort.png")
pygame.display.set_icon(icon)

# Game loop
running = True
while running:
    # Loop through all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen background
    screen.fill((135, 206, 235))

    # Required to update screen
    pygame.display.update()