import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
Width, Height = 650, 650
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Get the cake")

# Grid size
tile_size = 67

# Load images
player_img = pygame.image.load('player.png').convert_alpha()
cake_img = pygame.image.load('cake.png').convert_alpha()
background_img = pygame.image.load('background.png').convert_alpha()

# Scale images
background_img = pygame.transform.scale(background_img, (2400, 800))
cake = pygame.transform.scale(cake_img, (50, 50))
player = pygame.transform.scale(player_img, (60, 60))

# Draw grid
def draw_grid():
    for line in range(0, 11):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (0, line * tile_size),
            (Width, line * tile_size)
        )

        pygame.draw.line(
            screen,
            (255, 255, 255),
            (line * tile_size, 0),
            (line * tile_size, Height)
        )

# World class
class World():
    def __init__(self, data):
        self.tile_list = []

        # Load tile image
        dirt_img = pygame.image.load('dirt.png').convert_alpha()

        row_count = 0

        for row in data:
            col_count = 0

            for tile in row:

                if tile == 1:
                    img = pygame.transform.scale(
                        dirt_img,
                        (tile_size, tile_size)
                    )

                    img_rect = img.get_rect()

                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size

                    self.tile_list.append((img, img_rect))

                col_count += 1

            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

# World data
world_data = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Create world
world = World(world_data)

# Ground settings
ground_y = Height - 50

# Clock / FPS
clock = pygame.time.Clock()

# Player speed
Xspeed = 3

# Gravity settings
y_velocity = 0
gravity = 0.1
jump_strength = -5
on_ground = False

# Player position
x = 0
y = 0

# Game loop
while True:

    # Events
    for event in pygame.event.get():

        # Quit game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and on_ground:
                y_velocity = jump_strength
                on_ground = False

    # Apply gravity
    y_velocity += gravity
    y += y_velocity

    # Ground collision
    if y + 60 >= ground_y:
        y = ground_y - 60
        y_velocity = 0
        on_ground = True

    # Fill screen
    screen.fill((0, 0, 0))

    # Draw background
    screen.blit(background_img, (-600, 0))

    # Draw cake
    screen.blit(cake, (400, 300))

    # Draw player
    screen.blit(player, (x, y))

    # Draw world
    world.draw()

    # Draw grid
    draw_grid()

    # Ground
    pygame.draw.rect(
        screen,
        (0, 255, 0),
        (0, ground_y, Width, Height - ground_y)
    )

    # Movement
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= Xspeed

    if keys[pygame.K_RIGHT]:
        x += Xspeed

    # Update screen
    pygame.display.flip()

    # FPS
    clock.tick(60)