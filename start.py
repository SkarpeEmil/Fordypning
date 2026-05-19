import pygame
import sys
#Initialize all imported code in pygame modules at once 
pygame.init()

# Screen settings used for seting up the game windo 
Width, Height = 640, 640
screen =pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Get the cacke")




# what i am doing is making the imege is Uploaded 
player_img = pygame.image.load('player.png').convert_alpha()
cake_img= pygame.image.load('cake.png').convert_alpha()
background_img = pygame.image.load('background.png').convert_alpha()


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
          
        # Jump keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                y_velocity = jump_strength
         

    screen.fill((0, 0, 0)) # fill the screen with black color
 
    #the code makes the img picture appear on the screen 
    screen.blit(background_img,(-600,0))
    screen.blit(cake,(300,300))
    screen.blit(player,(x , y))

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