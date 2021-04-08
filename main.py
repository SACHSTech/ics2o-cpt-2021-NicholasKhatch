
import pygame
import random
import time
 
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

RED      = ( 255,   0,   0)
dark_red = (156, 6, 6)
dark_red_2 = (105, 6, 6)

BLUE     = (0, 0, 255)
dark_blue = (7, 9, 115)

GREEN    = (0, 179, 39)
dark_green = (0, 102, 22)

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

#gpu text
gpu_text_1 = pygame.image.load("gpu text 1.png").convert()
gpu_text_1.set_colorkey(BLACK)
gpu_text_2 = pygame.image.load("gpu text 2.png").convert()
gpu_text_2.set_colorkey(BLACK)
gpu_text_3 = pygame.image.load("gpu text 3.png").convert()
gpu_text_3.set_colorkey(BLACK)

#cpu text
cpu_text_1 = pygame.image.load("cpu text 1.png").convert()
cpu_text_1.set_colorkey(BLACK)
cpu_text_2 = pygame.image.load("cpu text 2.png").convert()
cpu_text_2.set_colorkey(BLACK)
cpu_text_3 = pygame.image.load("cpu text 3.png").convert()
cpu_text_3.set_colorkey(BLACK)

#fans text
fans_text_1 = pygame.image.load("fans text 1.png").convert()
fans_text_1.set_colorkey(BLACK)
fans_text_2 = pygame.image.load("fans text 2.png").convert()
fans_text_2.set_colorkey(BLACK)
fans_text_3 = pygame.image.load("fans text 3.png").convert()
fans_text_3.set_colorkey(BLACK)

#power supply text
power_text_1 = pygame.image.load("power text 1.png").convert()
power_text_1.set_colorkey(BLACK)
power_text_2 = pygame.image.load("power text 2.png").convert()
power_text_2.set_colorkey(BLACK)
power_text_3 = pygame.image.load("power text 3.png").convert()
power_text_3.set_colorkey(BLACK)

#ram text
ram_text_1 = pygame.image.load("ram text 1.png").convert()
ram_text_1.set_colorkey(BLACK)
ram_text_2 = pygame.image.load("ram text 2.png").convert()
ram_text_2.set_colorkey(BLACK)
ram_text_3 = pygame.image.load("ram text 3.png").convert()
ram_text_3.set_colorkey(BLACK)

customer_correct = pygame.image.load("correct text.png").convert()
customer_correct.set_colorkey(BLACK)

customer_false = pygame.image.load("false text.png").convert()
customer_false.set_colorkey(BLACK)
 
#selected pc parts
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

#collision box active or not
collision_box = True

#keeping track of amount of corrects
correct_counter = -100
part_correct = False

#keeping track of player lives
player_lives = 3
lives_lost = False

#toggle if the player has to restart the game
restart_game = False

#start menu toggle
start_menu = True

#toggle for getting a new part
new_part = True

#keeping track of if the player gets the right or wrong answer
player_true = False
player_false = False

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

    if new_part == True:
      gpu_selected = False
      cpu_selected = False
      pc_cooler_selected = False
      power_selected = False
      ram_selected = False
      gpu_required = False
      cpu_required = False
      pc_cooler_required = False
      power_required = False
      ram_required = False
      gpu_clicked = False
      cpu_clicked = False
      pc_cooler_clicked = False
      power_clicked = False
      ram_clicked = False
      player_true = False
      player_false = False
      random_part = (random.randint(0,14))
      collision_box = True
      customer_x = 500
      correct_counter = correct_counter + 100
      new_part = False

    #bringing costumers into the middle of the screen
    if collision_box == True:
      if customer_x < 230:
        customer_x_velocity = customer_x_velocity * 0
      elif customer_x == 500:
        customer_x_velocity = -5
      #print("colliding")
      #print(customer_x_velocity)
      customer_x = customer_x + customer_x_velocity

    elif collision_box == False:
      #if customer_x < 230:
      customer_x_velocity = -5
      customer_x = customer_x + customer_x_velocity
      
    #functions with the parts
    if random_part == 0:
      gpu_required = True
      #print("gpu is true")
    else:
      gpu_required == False
   
    if random_part == 1:
      cpu_required = True
      #print("cpu is true")
    else:
      cpu_required == False

    if random_part == 2:
      pc_cooler_required = True
      #print("fans are true")
    else:
      pc_cooler_required == False
   
    if random_part == 3:
      power_required = True
      #print("power supply is true")
    else:
      power_required == False

    if random_part == 4:
      ram_required = True
      #print("ram is true")
    else:
      ram_required == False

    if random_part == 5:
      gpu_required = True
      #print("gpu is true")
    else:
      gpu_required == False
   
    if random_part == 6:
      cpu_required = True
      #print("cpu is true")
    else:
      cpu_required == False

    if random_part == 7:
      pc_cooler_required = True
      #print("fans are true")
    else:
      pc_cooler_required == False
   
    if random_part == 8:
      power_required = True
      #print("power supply is true")
    else:
      power_required == False

    if random_part == 9:
      ram_required = True
      #print("ram is true")
    else:
      ram_required == False

    if random_part == 10:
      gpu_required = True
      #print("gpu is true")
    else:
      gpu_required == False
   
    if random_part == 11:
      cpu_required = True
      #print("cpu is true")
    else:
      cpu_required == False

    if random_part == 12:
      pc_cooler_required = True
      #print("fans are true")
    else:
      pc_cooler_required == False
   
    if random_part == 13:
      power_required = True
      #print("power supply is true")
    else:
      power_required == False

    if random_part == 14:
      ram_required = True
      #print("ram is true")
    else:
      ram_required == False

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
      pygame.draw.rect(screen, dark_green, (15,340,110,110))
      if player_click[0] == True:
        gpu_selected = True
    else:
      pygame.draw.rect(screen, GREEN, (15,340,110,110))

    text_font = pygame.font.SysFont("Roboto", 50, False, False)
    gpu_button = text_font.render("GPU", True, BLACK)

    screen.blit(gpu_button, [32, 375])

    #cpu button
    pygame.draw.rect(screen, GREEN, (150,340,110,110))

    if 150 + 110 > player_pos[0] > 150 and 340 + 110 > player_pos[1] > 340:
      pygame.draw.rect(screen, dark_green, (150,340,110,110))
      if player_click[0] == True:
        cpu_selected = True
    else:
      pygame.draw.rect(screen, GREEN, (150,340,110,110))

    cpu_button = text_font.render("CPU", True, BLACK)

    screen.blit(cpu_button, [167, 375])

    #pc cooler button
    pygame.draw.rect(screen, GREEN, (285,340,110,110))

    if 285 + 110 > player_pos[0] > 285 and 340 + 110 > player_pos[1] > 340:
      pygame.draw.rect(screen, dark_green, (285,340,110,110))
      if player_click[0] == True:
        pc_cooler_selected = True
    else:
      pygame.draw.rect(screen, GREEN, (285,340,110,110))

    pc_cooler_button = text_font.render("Fans", True, BLACK)

    screen.blit(pc_cooler_button, [297, 375])

    #power supply button
    pygame.draw.rect(screen, GREEN, (420,340,110,110))

    if 420 + 110 > player_pos[0] > 420 and 340 + 110 > player_pos[1] > 340:
      pygame.draw.rect(screen, dark_green, (420,340,110,110))
      if player_click[0] == True:
        power_selected = True
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
      pygame.draw.rect(screen, dark_green, (555,340,110,110))
      if player_click[0] == True:
        ram_selected = True
    else:
      pygame.draw.rect(screen, GREEN, (555,340,110,110))

    pc_cooler_button = text_font.render("RAM", True, BLACK)

    screen.blit(pc_cooler_button, [567, 375])

    #importing hand image
    screen.blit(player_image, [player_x, player_y])

    #determining if the player the player lost a live
    if not restart_game:
      if lives_lost == True:
        player_lives = player_lives - 1
        gpu_clicked = False
        cpu_clicked = False
        pc_cooler_clicked = False
        power_clicked = False
        ram_clicked = False        
        lives_lost = False
        if player_lives == 0:
          restart_game = True

    #outputs gpu text requirements to screen
    if customer_x_velocity == 0 and gpu_required == True and random_part == 0:
      screen.blit(gpu_text_1, [-20,-80])
    elif customer_x_velocity == 0 and gpu_required == True and random_part == 5:
      screen.blit(gpu_text_2, [-20,-80])
    elif customer_x_velocity == 0 and gpu_required == True and random_part == 10:
      screen.blit(gpu_text_3, [-20,-80])
    
    #possible events to take place with getting gpu as the option
    if gpu_required == True and gpu_selected == True:
      player_true = True
      collision_box = False
    
    #cpu
    elif gpu_required == True and 150 + 110 > player_pos[0] > 150 and 340 + 110 > player_pos[1] > 340:
        if player_click[0] == True:
            cpu_clicked = True
    
    if gpu_required == True and cpu_clicked == True:
      player_false = True
      lives_lost = True

      if gpu_required == True and gpu_selected == True:
        player_true = True
        collision_box = False
    
    #fans
    elif gpu_required == True and 285 + 110 > player_pos[0] > 285 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        pc_cooler_clicked = True
    
    if gpu_required == True and pc_cooler_clicked == True:
      player_false = True
      lives_lost = True

      if gpu_required == True and gpu_selected == True:
        player_true = True
        collision_box = False

    #power supply
    elif gpu_required == True and 420 + 110 > player_pos[0] > 420 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        power_clicked = True
      
    if gpu_required == True and power_clicked == True:
      player_false = True
      lives_lost = True

      if gpu_required == True and gpu_selected == True:
        part_correct = True
        player_true = True
        collision_box = False
    
    #ram
    elif gpu_required == True and 555 + 110 > player_pos[0] > 555 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        ram_clicked = True
    
    if gpu_required == True and ram_clicked == True:
      player_false = True
      lives_lost = True

      if gpu_required == True and gpu_selected == True:
        player_true = True
        collision_box = False

    #outputs cpu text requirements to screen
    if customer_x_velocity == 0 and cpu_required == True and random_part == 1:
      screen.blit(cpu_text_1, [-20,-80])
    elif customer_x_velocity == 0 and cpu_required == True and random_part == 6:
      screen.blit(cpu_text_2, [-20,-80])
    elif customer_x_velocity == 0 and cpu_required == True and random_part == 11:
      screen.blit(cpu_text_3, [-20,-80])

    #possible events to take place with getting cpu as the option
    if cpu_required == True and cpu_selected == True:
      player_true = True
      collision_box = False
    
    #gpu
    elif cpu_required == True and 15 + 110 > player_pos[0] > 15 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        gpu_clicked = True
    
    if cpu_required == True and gpu_clicked == True:
      player_false = True
      lives_lost = True

      if cpu_required == True and cpu_selected == True:
        player_true = True
        collision_box = False

    #fans
    elif cpu_required == True and 285 + 110 > player_pos[0] > 285 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        pc_cooler_clicked = True
      
    if cpu_required == True and pc_cooler_clicked == True:
      player_false = True
      lives_lost = True
      pc_cooler_clicked = False

      if cpu_required == True and cpu_selected == True:
        player_true = True
        collision_box = False

    #power supply
    elif cpu_required == True and 420 + 110 > player_pos[0] > 420 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        power_clicked = True
    
    if cpu_required == True and power_clicked == True:
      player_false = True
      lives_lost = True

      if cpu_required == True and cpu_selected == True:
        player_true = True
        collision_box = False

    #ram
    elif cpu_required == True and 555 + 110 > player_pos[0] > 555 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        ram_clicked = True
    
    if cpu_required == True and ram_clicked == True:
      player_false = True
      lives_lost = True

      if cpu_required == True and cpu_selected == True:
        player_true = True
        collision_box = False
        if customer_x < 0:
          new_part = True
    
    #outputs pc cooler text requirements to screen
    if customer_x_velocity == 0 and pc_cooler_required == True and random_part == 2:
      screen.blit(fans_text_1, [-20,-80])
    if customer_x_velocity == 0 and pc_cooler_required == True and random_part == 7:
      screen.blit(fans_text_2, [-20,-80])
    if customer_x_velocity == 0 and pc_cooler_required == True and random_part == 12:
      screen.blit(fans_text_3, [-20,-80])
    
    #possible events to take place with getting fans as the option
    if pc_cooler_required == True and pc_cooler_selected == True:
      player_true = True
      collision_box = False
      if customer_x < 0:
        new_part = True
    
    #gpu
    elif pc_cooler_required == True and 15 + 110 > player_pos[0] > 15 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        gpu_clicked = True
       
    if pc_cooler_required == True and gpu_clicked == True:
      player_false = True
      lives_lost = True

      if pc_cooler_required == True and pc_cooler_selected == True:
        player_true = True
        collision_box = False
        if customer_x < 0:
          new_part = True
    
    #cpu
    elif pc_cooler_required == True and 150 + 110 > player_pos[0] > 150 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
          cpu_clicked = True
    
    if pc_cooler_required == True and cpu_clicked == True:
      player_false = True
      lives_lost = True

      if pc_cooler_required == True and pc_cooler_selected == True:
        player_true = True
        collision_box = False
        if customer_x < 0:
          new_part = True
    
    #power supply
    elif pc_cooler_required == True and 420 + 110 > player_pos[0] > 420 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        power_clicked = True
    
    if pc_cooler_required == True and power_clicked == True:
      player_false = True
      lives_lost = True

      if pc_cooler_required == True and pc_cooler_selected == True:
        part_correct = True
        player_true = True
        collision_box = False
        if customer_x < 0:
          new_part = True

    #ram
    elif pc_cooler_required == True and 555 + 110 > player_pos[0] > 555 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        ram_clicked = True
    
    if pc_cooler_required == True and ram_clicked == True:
      player_false = True
      lives_lost = True

      if pc_cooler_required == True and pc_cooler_selected == True:
        player_true = True
        collision_box = False
        if customer_x < 0:
          new_part = True
    
    #outputs power supply text requirements to screen
    if customer_x_velocity == 0 and power_required == True and random_part == 3:
      screen.blit(power_text_1, [-20,-80])
    if customer_x_velocity == 0 and power_required == True and random_part == 8:
      screen.blit(power_text_2, [-20,-80])
    if customer_x_velocity == 0 and power_required == True and random_part == 13:
      screen.blit(power_text_3, [-20,-80])

    #possible events to take place with getting power supply as the option
    if power_required == True and power_selected == True:
      player_true = True
      collision_box = False
      if customer_x < 0:
        new_part = True
    
    #gpu
    elif power_required == True and 15 + 110 > player_pos[0] > 15 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        gpu_clicked = True
       
    if power_required == True and gpu_clicked == True:
      player_false = True
      lives_lost = True

      if power_required == True and power_selected == True:
        player_true = True
        collision_box = False
        if customer_x < 0:
          new_part = True
    
    #cpu
    elif power_required == True and 150 + 110 > player_pos[0] > 150 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
          cpu_clicked = True
    
    if power_required == True and cpu_clicked == True:
      player_false = True
      lives_lost = True

      if power_required == True and power_selected == True:
        player_true = True
        collision_box = False
    
    #fans
    elif power_required == True and 285 + 110 > player_pos[0] > 285 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        pc_cooler_clicked = True
      
    if power_required == True and pc_cooler_clicked == True:
      player_false = True
      lives_lost = True

      if power_required == True and power_selected == True:
        player_true = True
        collision_box = False
    
    #ram
    elif power_required == True and 555 + 110 > player_pos[0] > 555 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        ram_clicked = True
    
    if power_required == True and ram_clicked == True:
      player_false = False
      lives_lost = True

      if power_required == True and power_selected == True:
        player_true = True
        collision_box = False

    #outputs ram text requirements to screen
    if customer_x_velocity == 0 and ram_required == True and random_part == 4:
      screen.blit(ram_text_1, [-20,-80])
    if customer_x_velocity == 0 and ram_required == True and random_part == 9:
      screen.blit(ram_text_2, [-20,-80])
    if customer_x_velocity == 0 and ram_required == True and random_part == 14:
      screen.blit(ram_text_3, [-20,-80])

    #possible events to take place with getting ram as the option
    if ram_required == True and ram_selected == True:
      player_true = True
      collision_box = False
    
    #gpu
    elif ram_required == True and 15 + 110 > player_pos[0] > 15 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        gpu_clicked = True
       
    if ram_required == True and gpu_clicked == True:
      player_false = True
      lives_lost = True

      if ram_required == True and ram_selected == True:
        player_true = True
        collision_box = False

    #cpu
    elif ram_required == True and 150 + 110 > player_pos[0] > 150 and 340 + 110 > player_pos[1] > 340:
        if player_click[0] == True:
            cpu_clicked = True
    
    if ram_required == True and cpu_clicked == True:
      player_false = True
      lives_lost = True

      if ram_required == True and ram_selected == True:
        player_true = True
        collision_box = False
    
    #fans
    elif ram_required == True and 285 + 110 > player_pos[0] > 285 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        pc_cooler_clicked = True
    
    if ram_required == True and pc_cooler_clicked == True:
      player_false = True
      lives_lost = True

      if ram_required == True and ram_selected == True:
        player_true = True
        collision_box = False

    #power supply
    elif ram_required == True and 420 + 110 > player_pos[0] > 420 and 340 + 110 > player_pos[1] > 340:
      if player_click[0] == True:
        power_clicked = True
      
    if ram_required == True and power_clicked == True:
      player_false = True
      lives_lost = True

      if ram_required == True and ram_selected == True:
        player_true = True
        collision_box = False

    if player_true == True:
      screen.blit(customer_correct, [-20,-80])
      if customer_x < 0:
        new_part = True

    if player_false == True:
      screen.blit(customer_false, [-20,-80])

    #setting up and outputting the score of the player
    score_text = text_font.render("Score:", True, BLACK)
    score_number = text_font.render(str(correct_counter), True, BLACK)

    screen.blit(score_text, [0,0])
    screen.blit(score_number, [120,1])

    #setting up and outputting the lives of a player
    lives_text = text_font.render("Lives: ", True, BLACK)
    lives_number = text_font.render(str(player_lives), True, BLACK)
    
    screen.blit(lives_text, [550, 0])
    screen.blit(lives_number, [670, 1])

    #determines what happens when the player has to restart the game
    if restart_game == True:
      #game over background
      pygame.draw.rect(screen, BLACK, (0,0,700,500))

      #game over title and text
      title_font = pygame.font.SysFont("Roboto", 100, False, False)
      subtitle_font = pygame.font.SysFont("Roboto", 40, False, False)
      gameover_title = title_font.render("Game Over", True, RED)
      gameover_text = subtitle_font.render("You got too many wrong and have been fired!", True, RED)
      gameover_text_2 = subtitle_font.render("Click retry to try for a better score!", True, RED)
      gameover_text_3 = subtitle_font.render("Final Score: " + str(correct_counter), True, RED)

      #outputting game over text to screen
      screen.blit(gameover_title, [150,0])
      screen.blit(gameover_text, [40,100])
      screen.blit(gameover_text_2, [90,130])
      screen.blit(gameover_text_3, [240, 280])

      #retry button
      pygame.draw.rect(screen, RED, (250,190,200,80))

      if 250 + 200 > player_pos[0] > 250 and 190 + 80 > player_pos[1] > 100:
        pygame.draw.rect(screen, dark_red, (250,190,200,80))
        if player_click[0] == True:
          restart_game = False
          new_part = True
          correct_counter = -100
          player_lives = 3
      else:
        pygame.draw.rect(screen, RED, (250,190,200,80))

      retry_button_text = text_font.render("Retry", True, BLACK)
      screen.blit(retry_button_text, [305, 210])

    #setting up the start menu and various buttons on it
    if start_menu == True:
      #background
      pygame.draw.rect(screen, WHITE, (0,0,700,500))

      #title
      title_font = pygame.font.SysFont("Roboto", 100, False, False)
      title_text = title_font.render("PC Part Picker", True, BLACK)

      screen.blit(title_text, [110, 0])

      subtitle_font = pygame.font.SysFont("Roboto", 40, False, False)
      subtitle_text_1 = subtitle_font.render("Help customers by picking the PC part", True, BLACK)
      subtitle_text_2 = subtitle_font.render("that would fix their problem", True, BLACK)

      screen.blit(subtitle_text_1, [85, 80])
      screen.blit(subtitle_text_2, [145, 110])

      #play button
      pygame.draw.rect(screen, GREEN, (250,150,200,80))

      if 250 + 200 > player_pos[0] > 250 and 150 + 80 > player_pos[1] > 100:
        pygame.draw.rect(screen, dark_green, (250,150,200,80))
        if player_click[0] == True:
          start_menu = False
      else:
        pygame.draw.rect(screen, GREEN, (250,150,200,80))

      play_button_text = text_font.render("Play", True, BLACK)
      screen.blit(play_button_text, [315, 170])

    #if correct_counter > 0 and customer_x < 0:
      #customer_correct == False

    #pygame.draw.rect(screen, GREEN, (collision_x, collision_y, collision_width, collision_height))

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)


# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()