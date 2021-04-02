
import pygame
import random
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
RED      = ( 255,   0,   0)

GREEN    = (0, 179, 39)
Dark_Green = (0, 102, 22)

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

customer_text_1 = pygame.image.load("text placeholder.jpg").convert()
customer_text_1.set_colorkey(BLACK)

customer_correct = pygame.image.load("true placeholder.png").convert()
customer_correct.set_colorkey(BLACK)

customer_false = pygame.image.load("false placeholder.png").convert()
customer_false.set_colorkey(BLACK)
#customer_image = pygame.image.load()
 
#selecting pc parts
gpu_selected = False
cpu_selected = False
pc_cooler_selected = False
power_selected = False
ram_selected = False

#part required
gpu_required = False
cpu_required = False
pc_cooler_required = False
power_required = False
ram_required = False

#clicked part
gpu_clicked = False
cpu_clicked = False
pc_cooler_clicked = False
power_clicked = False
ram_clicked = False

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

#generating random part
for i in range(1):
  print(random.randint(1,5))
  random_part = (random.randint(1,5))

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True

    # --- Game logic should go here
    player_pos = pygame.mouse.get_pos()
    player_click = pygame.mouse.get_pressed()
    #print(player_pos)
    #print(player_click)
    user_x = player_pos[0]
    user_y = player_pos[1]
    player_x = player_pos[0] - 300
    player_y = player_pos[1] - 40

    #bringing costumers into the middle of the screen
    if customer_x < 230:
      customer_x_velocity = customer_x_velocity * 0
      #print("colliding")
      #print(customer_x_velocity)
    customer_x = customer_x + customer_x_velocity

    #functions with the parts
    if random_part == 0:
      gpu_required = True
      print("gpu is true")
    else:
      gpu_required == False
   
    if random_part == 1:
      cpu_required = True
      print("cpu is true")
    else:
      cpu_required == False
    
    # --- Drawing code should go here
    screen.fill(WHITE)

    #importing background image
    screen.blit(background_image, [0,0])
     
    #importing customer image
    screen.blit(customer_image, [customer_x,customer_y])
    
    #importing counter image
    screen.blit(counter_image, [0,0])

    #buttons for selecting computer part
    #gpu button
    pygame.draw.rect(screen, GREEN, (15,340,110,110))

    if 15 + 110 > player_pos[0] > 15 and 340 + 110 > player_pos[1] > 340:
      pygame.draw.rect(screen, Dark_Green, (15,340,110,110))
      if player_click[0] == True:
        gpu_selected = True
        print(gpu_selected)
    else:
      pygame.draw.rect(screen, GREEN, (15,340,110,110))

    text_font = pygame.font.SysFont("Roboto", 50, False, False)
    gpu_button = text_font.render("GPU", True, BLACK)

    screen.blit(gpu_button, [32, 375])

    #cpu button
    pygame.draw.rect(screen, GREEN, (150,340,110,110))

    if 150 + 110 > player_pos[0] > 150 and 340 + 110 > player_pos[1] > 340:
      pygame.draw.rect(screen, Dark_Green, (150,340,110,110))
      if player_click[0] == True:
        cpu_selected = True
        print(cpu_selected)
    else:
      pygame.draw.rect(screen, GREEN, (150,340,110,110))

    cpu_button = text_font.render("CPU", True, BLACK)

    screen.blit(cpu_button, [167, 375])

    #pc cooler button
    pygame.draw.rect(screen, GREEN, (285,340,110,110))

    if 285 + 110 > player_pos[0] > 285 and 340 + 110 > player_pos[1] > 340:
      pygame.draw.rect(screen, Dark_Green, (285,340,110,110))
      if player_click[0] == True:
        pc_cooler_selected = True
        print(pc_cooler_selected)
    else:
      pygame.draw.rect(screen, GREEN, (285,340,110,110))

    pc_cooler_button = text_font.render("Fans", True, BLACK)

    screen.blit(pc_cooler_button, [297, 375])

    #power supply button
    pygame.draw.rect(screen, GREEN, (420,340,110,110))

    if 420 + 110 > player_pos[0] > 420 and 340 + 110 > player_pos[1] > 340:
      pygame.draw.rect(screen, Dark_Green, (420,340,110,110))
      if player_click[0] == True:
        power_selected = True
        print(power_selected)
    else:
      pygame.draw.rect(screen, GREEN, (420,340,110,110))

    small_font = pygame.font.SysFont("Roboto", 40, False, False)
    power_supply_button = small_font.render("Power", True, BLACK)
    power_supply_button_2 = small_font.render("Supply", True, BLACK)

    screen.blit(power_supply_button, [432, 365])
    screen.blit(power_supply_button_2, [428, 390])

    #ram button
    pygame.draw.rect(screen, GREEN, (555,340,110,110))

    if 555 + 110 > player_pos[0] > 555 and 340 + 110 > player_pos[1] > 340:
      pygame.draw.rect(screen, Dark_Green, (555,340,110,110))
      if player_click[0] == True:
        ram_selected = True
        print(ram_selected)
    else:
      pygame.draw.rect(screen, GREEN, (555,340,110,110))

    pc_cooler_button = text_font.render("RAM", True, BLACK)

    screen.blit(pc_cooler_button, [567, 375])

    #importing hand image
    screen.blit(player_image, [player_x, player_y])

    #outputs gpu text requirements to screen
    if customer_x_velocity == 0 and gpu_required == True:
      screen.blit(customer_text_1, [50,70])
    
    #possible events to take place with getting gpu as the option
    if gpu_required == True and gpu_selected == True:
      print("gpu all true")
      screen.blit(customer_correct, [0,0])

    #cpu
    elif gpu_required == True and 150 + 110 > player_pos[0] > 150 and 340 + 110 > player_pos[1] > 340:
        print("wrong button")
        if player_click[0] == True:
            cpu_clicked = True
    
    if gpu_required == True and cpu_clicked == True:
      screen.blit(customer_false, [0,0])
    
    #fans
    elif gpu_required == True and 285 + 110 > player_pos[0] > 285 and 340 + 110 > player_pos[1] > 340:
      print("wrong button")
      if player_click[0] == True:
        pc_cooler_clicked = True
    
    if gpu_required == True and pc_cooler_clicked == True:
      screen.blit(customer_false, [0,0])

    #power supply
    elif gpu_required == True and 420 + 110 > player_pos[0] > 420 and 340 + 110 > player_pos[1] > 340:
      print("wrong button")
      if player_click[0] == True:
        power_clicked = True
      
    if gpu_required == True and power_clicked == True:
      screen.blit(customer_false, [0,0])
    
    #ram
    elif gpu_required == True and 555 + 110 > player_pos[0] > 555 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        ram_clicked = True
    
    if gpu_required == True and ram_clicked == True:
      screen.blit(customer_false, [0,0])
    
    #outputs cpu text requirements to screen
    if customer_x_velocity == 0 and cpu_required == True:
      screen.blit(customer_text_1, [50,70])

    #possible events to take place with getting cpu as the option
    if cpu_required == True and cpu_selected == True:
      print("cpu all true")
      screen.blit(customer_correct, [0,0])
    
    elif cpu_required == True and 15 + 110 > player_pos[0] > 15 and 340 + 110 > player_pos[1] > 340:
      print("wrong button")
      if player_click[0] == True:
        gpu_clicked = True
    
    if cpu_required == True and gpu_clicked == True:
      screen.blit(customer_false, [0,0])
    #pygame.draw.rect(screen, GREEN, (collision_x, collision_y, collision_width, collision_height))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()