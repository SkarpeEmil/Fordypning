from turtle import width
import pygame
import sys
#Initialize all imported code in pygame modules at once 
pygame.init()

# Screen settings used for seting up the game windo 
Width, Height = 600, 600
screen =pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Get the cacke")

# variable for the grid size
tile_size = 100

# what i am doing is making the imege is Uploaded 
player_img = pygame.image.load('player.png').convert_alpha()
cake_img= pygame.image.load('cake.png').convert_alpha()
background_img = pygame.image.load('background.png').convert_alpha()


# makes the game into grids witch i can difine  
def draw_grid():
      for line in range(0, 6):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (Width, line * tile_size))
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, Height))

 
    
 #makes the platfor inside the grid 
class World():
    def __init__(self, data):
         self.tile_list = []

         #loding img for tiles
         dirt_img = pygame.image.load('dirt.png').convert_alpha()

         # draws the bloks in the girid
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
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
]

world = World(world_data)

# Clock used for FPS 
clock = pygame.time.Clock()

# speed of the player
Xspeed = 3

# gravity settings so when you jump you will fall down again
y_velocity = 0
gravity = 0.1
jump_strength = -1  
on_ground = False

background_img = pygame.transform.scale(background_img,(2400,800))


# her i make the img size smaler 
cake = pygame.transform.scale(cake_img,(50,50))
player = pygame.transform.scale(player_img,(60,60))



y = 0
x = 0



#A loop for the game to start 
while True:
    
    # Quit Loop used so you can quit the game windo with the X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            draw_grid()
          
        # Jump keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_velocity = jump_strength
         

    screen.fill((0, 0, 0)) # fill the screen with black color

  #the code makes the img picture appear on the screen 
    screen.blit(background_img,(-600,0))
    screen.blit(cake,(400,300))
    screen.blit(player,(x , y)) 

# draws the grid and the bloks 
   # world.draw()
    draw_grid()
 
  


 # Apply gravity
    y_velocity += gravity
    y += y_velocity



    # code for key press up, down, left and right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      x -= Xspeed
    if keys[pygame.K_RIGHT]:
       x += Xspeed
    if keys[pygame.K_UP]:
       y -= Xspeed
    if keys[pygame.K_DOWN]:
       y  += Xspeed
   
   
                
    



        
    pygame.display.flip()
    clock.tick(60)  