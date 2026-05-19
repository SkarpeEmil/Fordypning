from turtle import width
import pygame
import sys
#Initialize all imported code in pygame modules at once 
pygame.init()

y = 0
x = 0

# Screen settings used for seting up the game windo 
Width, Height = 640, 640
screen =pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Get the cacke")

# variable for the grid size
tile_size = 20
clock = pygame.time.Clock()

# what i am doing is making the imege is Uploaded 



# makes the game into grids witch i can difine
def draw_grid():
      for line in range(0, 6):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (Width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, Height))


class World():
    def __init__(self, data):
         self.tile_list = []

         #loding img for tiles
         dirt_img = pygame.image.load('dirt.png').convert_alpha()

         #
         row_count = 0
         for row in data:
             col_count = 0
             for tile in row:
                 if tile == 1:
                     img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                     img_rect = img.get_rect()
                     img_rect.x = col_count * tile_size
                     img_rect.y = row_count * tile_size
                     tile = (img, img_rect)
                     self.tile_list.append(tile)
                     col_count += 1
                 row_count += 1
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

world_data = [
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1]
]

world = World(world_data)
#A loop for the game to start 
while True:
    
    # Quit Loop used so you can quit the game windo with the X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    world.draw()
    draw_grid()
    
    








       
    pygame.display.flip()
    clock.tick(60)       