
import pygame
import sys
#Initialize all imported code in pygame modules at once 
pygame.init()

# Screen settings used for seting up the game window
Width, Height = 650, 650
screen =pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Get the cacke")

# variable for the grid size
tile_size = 67

# what i am doing is making the imege is Uploaded 
player_img = pygame.image.load('player.png').convert_alpha()
cake_img= pygame.image.load('cake.png').convert_alpha()
background_img = pygame.image.load('background.png').convert_alpha()
dirt_img = pygame.image.load('dirt.png').convert_alpha()

# her i can change the size of the inmg 
cake = pygame.transform.scale(cake_img,(50,50))

player = pygame.transform.scale(player_img,(60,60))

dirt_img = pygame.transform.scale(dirt_img, (tile_size, tile_size))





# makes the game into grids witch i can difine  
def draw_grid():
      for line in range(0, 11):
        pygame.draw.line(screen, (255, 255, 255), (0, line * tile_size), (Width, line * tile_size))
        
        pygame.draw.line(screen, (255, 255, 255), (line * tile_size, 0), (line * tile_size, Height))

 
    
 #makes the platfor inside the grid 
class World():
    def __init__(self, data): 
         self.tile_list = []

         #loding img that is used for tiles
        

         # code that makes the dirt img insaid the grid
         row_count = 0

         for row in data:
            col_count = 0
           
            for tile in row:

                if tile == 1:
                    img = pygame.transform.scale(dirt_img,(tile_size, tile_size))

                    img_rect = img.get_rect()

                    img_rect.x = col_count * tile_size
                    

                    img_rect.y = row_count * tile_size

                    self.tile_list.append((img, img_rect))

                col_count += 1

            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])

# the list lets me place dirt img wher i want in the grid
world_data = [
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
]
world = World(world_data)




#setting for the groubd
ground_y = Height - 50
# Clock used for FPS 
clock = pygame.time.Clock()

# speed of the player
Xspeed = 3

# gravity settings so when you jump you will fall down again
y_velocity = 0
gravity = 0.1
jump_strength = -5  
on_ground = False
ground_y = Height - 50

 
# the code just makes the background img bigger in witdh and hight
background_img = pygame.transform.scale(background_img,(2400,800))




# adds values to y x so if used it will start ther 
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
                on_ground = False
                

    #applays gravity
    y_velocity += gravity
    y += y_velocity


    player_rect = pygame.Rect(x, y, 60, 60)


    # makes the dirt img a platform in my game
    for tile in world.tile_list:

        tile_rect = tile[1] 

        if player_rect.colliderect(tile_rect):

             # makes it when landing on the dirt IMG it behaves like the ground code (aka a platforme)
            if y_velocity > 0:
                y = tile_rect.top - 60
                y_velocity = 0
                on_ground = True

            
            # makes it so i cant jump tgrough the bottom of the dirt img
            if y_velocity < 0:
                y = tile_rect.bottom
                y_velocity = 0

            
            
                
 # code for when the player thist the ground
    if y + 60 >= ground_y:
        y = ground_y - 60
        y_velocity = 0
        on_ground = True

# Keep player inside screen on both sides 
    if x < 0:
        x = 0

    if x > Width - 60:
        x = Width - 60

    screen.fill((0, 0, 0)) # fill the screen with black color

  #the code makes the img picture appear on the screen 
    screen.blit(background_img,(-600,0))
    screen.blit(cake,(6,5))
    screen.blit(player,(x , y))


# draws the grid and the bloks 
    world.draw()

   # draw_grid()

      # Ground to stand on so you dont fall through the map fllor
    pygame.draw.rect(screen, (0, 255, 0), (0, ground_y, Width, Height - ground_y))
    


    # code for key press for left and right
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      x -= Xspeed

    if keys[pygame.K_RIGHT]:
       x += Xspeed
    

  
   
   
                
    



        
    pygame.display.flip()
    clock.tick(60)  