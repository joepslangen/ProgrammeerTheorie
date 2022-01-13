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

# Load background image Rush Hour board
background_image = pygame.image.load('rush_hour2.png')

# scaling picture so it fits the whole window
picture = pygame.transform.scale(background_image, (500, 500))

# variables to represent cars

class Car(object):
    def __init__(self, x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.movement_speed = 5

# x and y coordinates on the screen 
x = 100
y = 100

a = 300
b = 300


# width and height of the car
width = 40
height = 60

# movement speed the car moves over the board
movement_speed = 5

# Game Loop
running = True

while running:
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
    # if keys[pygame.K_LEFT] and x > movement_speed: 
    #     x -= movement_speed
    # # Move character right, however make sure car goes not out of bounds
    # if keys[pygame.K_RIGHT] and x < 500 - movement_speed - width:
    #     x += movement_speed
    # Move character up, however make sure car goes not out of bounds
    if keys[pygame.K_UP] and y > movement_speed:
        y -= movement_speed
    # Move character down, however make sure car goes not out of bounds
    if keys[pygame.K_DOWN] and y < 500 - height - movement_speed:
        y += movement_speed

    if keys[pygame.K_LEFT] and a > movement_speed: 
        a -= movement_speed
    # Move character right, however make sure car goes not out of bounds
    if keys[pygame.K_RIGHT] and a < 500 - movement_speed - width:
        a += movement_speed
    # # Move character up, however make sure car goes not out of bounds
    # if keys[pygame.K_UP] and b > movement_speed:
    #     b -= movement_speed
    # # Move character down, however make sure car goes not out of bounds
    # if keys[pygame.K_DOWN] and b < 500 - height - movement_speed:
    #     b += movement_speed

    # Call blit method to draw image on screen
    win.blit(picture, (0, 0))

    # Fills the screen with white
    # win.fill((255, 255, 255))
        
    # This takes: window/surface, color, rect 
    for i in range(8):
        pygame.draw.rect(win, (255,0,0), (x, y, width, height))  

        pygame.draw.rect(win, (0,255,0), (a, b, width, height))  
   
    # This updates the screen so we can see our rectangle 
    pygame.display.update() 
        
# If we exit the loop this will execute and close our game
pygame.quit()  
    