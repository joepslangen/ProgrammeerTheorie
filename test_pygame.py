import pygame
# initialize 
pygame.init()

#width and height of the window
WIDTH = 500
HEIGHT = 500

# Color codes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# this creates a window of 500 width and 500 height
win = pygame.display.set_mode((500, 500))

#create a caption for the pygame window
pygame.display.set_caption("Rush Hour visualisation")

# variables to represent cars
x = 50
y = 50
width = 40
height = 60
vel = 5

run = True

while run:
    # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
    pygame.time.delay(100) 
    # This will loop through a list of any keyboard or mouse events.
    for event in pygame.event.get():  
        # Checks if the red button in the corner of the window is clicked
        if event.type == pygame.QUIT: 
            # Ends the game loop
            run = False 
    # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed 
    keys = pygame.key.get_pressed()  

    # We can check if a key is pressed like this
    # Move character left, however make sure car goes not out of bounds
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
    # Move character right, however make sure car goes not out of bounds
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
    # Move character up, however make sure car goes not out of bounds
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    # Move character down, however make sure car goes not out of bounds
    if keys[pygame.K_DOWN] and y < 500 - height - vel:
        y += vel

    # Fills the screen with black
    win.fill((0, 0, 0))
        
    # This takes: window/surface, color, rect 
    for i in range(8):
        pygame.draw.rect(win, (255,0,0), (x, y, width, height))  
   
    # This updates the screen so we can see our rectangle 
    pygame.display.update() 
        
# If we exit the loop this will execute and close our game
pygame.quit()  
    
def draw_Grid():
    # Set the size of the grid block 6x6
    grid_size = 6 
    for x in range(0, WIDTH, grid_size):
        rect = pygame.rect(x, y, grid_size, grid_size)
        pygame.draw.rect(win, WHITE, rect, 1)