
import pygame
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
 
pygame.init()
  
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Part Picker")

#Loading graphics
background_image = pygame.image.load("Image168.jpg").convert()
background_image.set_colorkey(BLACK)

counter_image = pygame.image.load("counter.png").convert()
counter_image.set_colorkey(BLACK)

player_image = pygame.image.load("silicone-male-arm.png").convert()
player_image.set_colorkey(BLACK)

customer_image = pygame.image.load("Image168www.png").convert()
customer_image.set_colorkey(BLACK)

#customer_image = pygame.image.load()
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#customer values
customer_x = 450
customer_y = 100
customer_x_velocity = -5
customer_width = 235
customer_height = 238

#customer collision box
collision_x = 230
collision_y = 0
collision_width = 1
collision_height = 500

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
  
    # --- Game logic should go here
    player_pos = pygame.mouse.get_pos()
    player_x = player_pos[0] - 300
    player_y = player_pos[1] - 40

    #bringing costumers into the middle of the screen
    if customer_x < 230:
      customer_x_velocity = customer_x_velocity * 0
      print("colliding")

    customer_x = customer_x + customer_x_velocity

    # --- Drawing code should go here
    screen.fill(WHITE)

    #importing background image
    screen.blit(background_image, [0,0])
     
    #importing customer image
    screen.blit(customer_image, [customer_x,customer_y])
    
    #importing counter image
    screen.blit(counter_image, [0,0])

    #importing hand image
    screen.blit(player_image, [player_x, player_y])

    #pygame.draw.rect(screen, GREEN, (collision_x, collision_y, collision_width, collision_height))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
     
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()