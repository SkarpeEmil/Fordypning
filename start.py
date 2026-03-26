import pygame
import sys
#Initialize all imported code in pygame modules at once 
pygame.init()

# Screen settings used for seting up the game windo 
Width, Height = 640, 640
screen =pygame.display.set_mode((Width, Height))
pygame.display.set_caption("Get the cacke")




# what i am doing is making the imege is Uploaded 
player_img = pygame.image.load('player.png').convert()
cake_img= pygame.image.load('cake.png').convert()
background_img = pygame.image.load('background.png').convert()

# Clock used for FPS 
clock = pygame.time.Clock()

# speed of the player
speed = 5


# her i make the img size smaler 
cake = pygame.transform.scale(cake_img,(50,50))
player = pygame.transform.scale(player_img,(60,60))


x = 0
#A loop for the game to start 
while True:
    
    # Quit Loop used so you can quit the game windo with the X button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

 
   
   
    #player 
    screen.blit(player,(x, 30))
    #the background image 
    screen.blit(background_img,(0,0))




    # code for key press up, down left right
    # i am trying to make the player move with the arrow keys but it is not working
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      player -= speed
    if keys[pygame.K_RIGHT]:
       player += speed
    if keys[pygame.K_UP]:
       player -= speed
    if keys[pygame.K_DOWN]:
       player  += speed
        




       
    pygame.display.flip()
    clock.tick(60)  