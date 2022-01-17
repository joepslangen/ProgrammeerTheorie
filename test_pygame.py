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
# Red car
x = 120
y = 185

# Green car
a = 325
b = 305

# Pink car
c = 255
d = 180


# Width and height of the car
# Red car
width_1 = 120
height_1 = 52

# Green Car
width_2 = 52
height_2 = 120

# Pink car
width_3 = 52
height_3 = 120


# Movement speed the car moves over the board
movement_speed = 5

# instances of class Car
red_car = Car(120, 185, 120, 52)
green_car = Car(325, 305, 52, 120)
pink_car = Car(255, 180, 52, 120)


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
    if keys[pygame.K_LEFT] and red_car.x > red_car.movement_speed: 
        red_car.x -= movement_speed
    # Move character right, however make sure car goes not out of bounds
    if keys[pygame.K_RIGHT] and red_car.x < 500 - red_car.movement_speed - red_car.width:
        red_car.x += red_car.movement_speed
    # Move character up, however make sure car goes not out of bounds
    # if keys[pygame.K_UP] and car.y > car.movement_speed:
    #     car.y -= movement_speed
    # # Move character down, however make sure car goes not out of bounds
    # if keys[pygame.K_DOWN] and car.y < 500 - car.height - car.movement_speed:
    #     car.y += movement_speed

    # Green object 
    # if keys[pygame.K_LEFT] and a > movement_speed: 
    #     a -= movement_speed
    # # Move character right, however make sure car goes not out of bounds
    # if keys[pygame.K_RIGHT] and a < 500 - movement_speed - width_2:
    #     a += movement_speed
    # # Move character up, however make sure car goes not out of bounds
    if keys[pygame.K_UP] and green_car.y > green_car.movement_speed:
        green_car.y -= green_car.movement_speed
    # # Move character down, however make sure car goes not out of bounds
    if keys[pygame.K_DOWN] and green_car.y < 500 - green_car.height - green_car.movement_speed:
        green_car.y += green_car.movement_speed

    # if mouse is pressed
    if pygame.mouse.get_pressed()[0]:
        # When mouse is pressed on the red car
        if (pygame.mouse.get_pos()[0] > red_car.x) & (pygame.mouse.get_pos()[0] < red_car.x + red_car.width) & (pygame.mouse.get_pos()[1] > red_car.y) & (pygame.mouse.get_pos()[1] < red_car.y + red_car.height):
            # When mouse is pressed on the right side of the car
            if pygame.mouse.get_pos()[0] > red_car.x + (red_car.width / 2):
                print(((pink_car.y + pink_car.height) > red_car.y > pink_car.y))
                # if the pink car blocks the red car, don't move
                if (0 < (pink_car.x - red_car.x - red_car.width) < 60) and ((pink_car.y + pink_car.height) >= red_car.y >= pink_car.y):
                    continue
                # if the green car does blocks the red car, don't move
                elif ((green_car.x - red_car.x - red_car.width) < 60) and ((green_car.y + green_car.height) >= red_car.y >= green_car.y):
                    continue
                # if not blocked, move to the right
                else:
                    red_car.x += 70
            # When mouse is pressed on left side of the car
            else:
                # if the pink car blocks the red car, don't move
                if (0 < (red_car.x - (pink_car.x + pink_car.width)) < 60) and ((pink_car.y + pink_car.height) >= red_car.y >= pink_car.y):
                    continue
                # if the green car does blocks the red car, don't move
                elif (0 < (red_car.x - (green_car.x + green_car.width)) < 60) and ((green_car.y + green_car.height) >= red_car.y >= green_car.y):
                    continue
                # if not blocked, move to the left
                else:
                    red_car.x -= 70
    # if mouse is pressed
    if pygame.mouse.get_pressed()[0]:
        # When mouse is pressed on the green car
        if (pygame.mouse.get_pos()[0] > green_car.x) & (pygame.mouse.get_pos()[0] < green_car.x + green_car.width) & (pygame.mouse.get_pos()[1] > green_car.y) & (pygame.mouse.get_pos()[1] < green_car.y + green_car.height):
            # When mouse is pressed on the upper half of the car, move up
            if pygame.mouse.get_pos()[1] > green_car.y + (green_car.height / 2):
                green_car.y += 63
            # When mouse is pressed on the lower half of the car, move down
            else: 
                green_car.y -= 63
    # if mouse is pressed
    if pygame.mouse.get_pressed()[0]:
        # When mouse is pressed on the pink car
        if (pygame.mouse.get_pos()[0] > pink_car.x) & (pygame.mouse.get_pos()[0] < pink_car.x + pink_car.width) & (pygame.mouse.get_pos()[1] > pink_car.y) & (pygame.mouse.get_pos()[1] < pink_car.y + pink_car.height):
             # When mouse is pressed on the upper half of the car, move up
            if pygame.mouse.get_pos()[1] > pink_car.y + (pink_car.height / 2):
                pink_car.y += 60
             # When mouse is pressed on the lower half of the car, move down
            else: 
                pink_car.y -= 60

    # Call blit method to draw image on screen
    win.blit(picture, (0, 0))

    # Fills the screen with white
    # win.fill((255, 255, 255))
        
    # This takes: window/surface, color, rect 

    pygame.draw.rect(win, (255,0,0), (red_car.x, red_car.y, red_car.width, red_car.height))  

    pygame.draw.rect(win, (0,255,0), (green_car.x, green_car.y, green_car.width, green_car.height))  

    pygame.draw.rect(win, (255,0,255), (pink_car.x, pink_car.y, pink_car.width, pink_car.height)) 

    # This updates the screen so we can see our rectangle 
    pygame.display.update() 
        
# If we exit the loop this will execute and close our game
pygame.quit()  
    