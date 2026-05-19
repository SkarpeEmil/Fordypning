import pygame

pygame.init()

screen = pygame.display.set_mode((640, 640))

Moon_img = pygame.image.load('Bilder/Moon.png').convert_alpha()

Moon_img = pygame.transform.scale(
    Moon_img,
    (Moon_img.get_width() * 2,
     Moon_img.get_height() * 2)
)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 255, 255))
    screen.blit(Moon_img, (30, 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
