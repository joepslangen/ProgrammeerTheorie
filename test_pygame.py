import pygame

# initialize 
pygame.init()

#width and height of the window
WIDTH = 500
HEIGHT = 500

# Color codes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
GREEN = (0,255,0)
PINK = (255,0,255)
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

    # create methods to move cars
    # TO DO: create methods for algorithm solution 
    def move_right():
        pass

    def move_left():
        pass
    
    def move_up();
        pass

    def move_down():
        pass

    def is_valid():
        pass 

# instances of class Car
red_car = Car(120, 185, 120, 52)
green_car = Car(325, 305, 52, 120)
pink_car = Car(255, 180, 52, 120)

# Game Loop
running = True

# Move counter
counter = 0

while running:
    # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
    pygame.time.delay(100) 
    # This will loop through a list of any keyboard or mouse events.
    for event in pygame.event.get():  
        # Checks if the red button in the corner of the window is clicked
        if event.type == pygame.QUIT: 
            # Ends the game loop
            running = False 
    # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed 
    keys = pygame.key.get_pressed()  

   # When mouse is pressed
    if pygame.mouse.get_pressed()[0]:
        # When mouse is pressed on the red car
        if (pygame.mouse.get_pos()[0] > red_car.x) & (pygame.mouse.get_pos()[0] < red_car.x + red_car.width) & (pygame.mouse.get_pos()[1] > red_car.y) & (pygame.mouse.get_pos()[1] < red_car.y + red_car.height):
            # When mouse is pressed on the right side of the car
            if pygame.mouse.get_pos()[0] > red_car.x + (red_car.width / 2):
                # If the pink car blocks the red car, don't move
                if (0 < (pink_car.x - red_car.x - red_car.width) < 60) and ((pink_car.y + pink_car.height) >= red_car.y >= pink_car.y):
                    continue
                # If the green car does blocks the red car, don't move
                elif ((green_car.x - red_car.x - red_car.width) < 60) and ((green_car.y + green_car.height) >= red_car.y >= green_car.y):
                    continue
                # If not blocked, move to the right
                else:
                    red_car.x += 70
                    counter += 1
            # When mouse is pressed on left side of the car
            else:
                # If the pink car blocks the red car, don't move
                if (0 < (red_car.x - (pink_car.x + pink_car.width)) < 60) and ((pink_car.y + pink_car.height) >= red_car.y >= pink_car.y):
                    continue
                # If the green car does blocks the red car, don't move
                elif (0 < (red_car.x - (green_car.x + green_car.width)) < 60) and ((green_car.y + green_car.height) >= red_car.y >= green_car.y):
                    continue
                # If not blocked, move to the left
                else:
                    red_car.x -= 70
                    counter += 1

        # When mouse is pressed on the green car
        if (pygame.mouse.get_pos()[0] > green_car.x) & (pygame.mouse.get_pos()[0] < green_car.x + green_car.width) & (pygame.mouse.get_pos()[1] > green_car.y) & (pygame.mouse.get_pos()[1] < green_car.y + green_car.height):
            # When mouse is pressed on the lower half of the car, move down
            if pygame.mouse.get_pos()[1] > green_car.y + (green_car.height / 2):
                # If the red car blocks the green car, don't move
                if (0 < (red_car.y - (green_car.y + green_car.height)) < 60) and ((red_car.x + red_car.width) >= (green_car.x + green_car.width / 2) >= red_car.x):
                    continue
                # If not blocked, move down
                else:
                    green_car.y += 63
                    counter += 1
            # When mouse is pressed on the upper half of the car, move up
            else: 
                # If the red car blocks te green car, don't move
                if (0 < (green_car.y - red_car.y) < 60) and ((red_car.x + red_car.width) >= (green_car.x + green_car.width / 2) >= red_car.x):
                    continue
                # If not blocked, move up
                else:
                    green_car.y -= 63
                    counter += 1
        # When mouse is pressed on the pink car
        if (pygame.mouse.get_pos()[0] > pink_car.x) & (pygame.mouse.get_pos()[0] < pink_car.x + pink_car.width) & (pygame.mouse.get_pos()[1] > pink_car.y) & (pygame.mouse.get_pos()[1] < pink_car.y + pink_car.height):
             # When mouse is pressed on the lower half of the car, move down
            if pygame.mouse.get_pos()[1] > pink_car.y + (pink_car.height / 2):
                # If the red car blocks the pink car, don't move
                if (0 < (red_car.y - (pink_car.y + pink_car.height)) < 60) and ((red_car.x + red_car.width) >= (pink_car.x + pink_car.width / 2) >= red_car.x):
                    continue
                # If not blocked, move down
                else:
                    pink_car.y += 60
                    counter += 1
             # When mouse is pressed on the upper half of the car, move up
            else: 
                # If the red car blocks the pink car, don't move
                if (0 < (pink_car.y - red_car.y) < 60) and ((red_car.x + red_car.width) >= (pink_car.x + pink_car.width / 2) >= red_car.x):
                    continue
                # If not blocked, move up
                else:
                    pink_car.y -= 60
                    counter += 1

    # Call blit method to draw image on screen
    win.blit(picture, (0, 0))
        
    # This takes: window/surface, color, rect 

    red_car = pygame.draw.rect(win, RED, (red_car.x, red_car.y, red_car.width, red_car.height))  

    green_car = pygame.draw.rect(win, GREEN, (green_car.x, green_car.y, green_car.width, green_car.height))  

    pink_car = pygame.draw.rect(win, PINK, (pink_car.x, pink_car.y, pink_car.width, pink_car.height)) 

    # This updates the screen so we can see our rectangle 
    pygame.display.update() 
        
# If we exit the loop this will execute and close our game
pygame.quit()  
    