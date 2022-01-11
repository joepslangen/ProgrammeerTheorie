##
# Jasper Paul
# First try at reading the .csv files and setting up the game board
# requires the Car() class and car.py

 
#required imports
import pandas as pd
import numpy as np

#import car.py
from car import Car

#read rushhour6x6_1.csv
Rushhour_df = pd.read_csv("gameboards/Rushhour9x9_4.csv")

#determine dimensions of the game board
dimensions = max(Rushhour_df["col"])

#create list to contain cars
cars = []

# cycle through every row in the dataframe
for index in range(len(Rushhour_df)):
    #extrac name from the column "car"
    car_name = Rushhour_df.loc[index, "car"]
    #extract orientation from column "orientation"
    car_orientation = Rushhour_df.loc[index, "orientation"]
    #extract orientation from column "col"
    #correction since python names the first column "0", but the .csv file names the first column "1"
    car_column = Rushhour_df.loc[index, "col"] - 1
    #extract orientation from column "row"
    #correction since python names the first row "0", but the .csv file names the first row "1"
    car_row = Rushhour_df.loc[index, "row"] - 1
    #extract lenght from column "length"
    car_length = Rushhour_df.loc[index, "length"]
    

    #define car using Car() class and extracted properties
    car = Car(car_name, car_orientation, car_column, car_row, car_length)

    #add car to cars list
    cars.append(car)

#create a ones matrix with dimensions of: dimension+2 x dimension+2 
#to provide a barrier around the drivable gameboard
ones_matrix = np.ones((dimensions + 2, dimensions + 2))

#actual drivable gameboard consists of zeros with dimensions: dimension x dimension
zeros_matrix = np.zeros((dimensions, dimensions))

#combine the ones matrix and the zeros matrix to create empty board with barriers
ones_matrix[1:dimensions + 1, 1:dimensions + 1] = zeros_matrix

#use pandas to create 6x6 DataFrame from the board matrix matrix
game_board = pd.DataFrame(ones_matrix).astype(int)

#cycle through the cars list
for car in cars: 
    #check if car is horizontal
    if car._orientation == "H":
        #cycle through lenght of the car
        for index in range(0, car._length):
            #replace zeros in DataFrame with the carname in horizontal fashion
            #correction of 1 since we added a 1 thick layer of barrier around the board
            game_board.loc[car.row + 1, car.column + index + 1] = car._name
    #if not horizontal, car is vertical
    else:
        #cycle through lenght of the car
        for index in range(0, car._length):
            #replace zeros in DataFrame with the carname in vertical fashion
            #correction of 1 since we added a 1 thick layer of barrier around the board
            game_board.loc[car.row + index + 1, car.column + 1] = car._name

#show gameboard
print(game_board)

#start of a function able to move cars
def moveCar(game_board, cars):
    #cycle through the cars in the cars lists
    for car in cars: 
        #again check for orientation if horizontal
        if car._orientation == "H": 
            #check if the spot on the right of the car is free
            if game_board.loc[car.row + 1, car.column + car._length + 1] == 0:
                #if so notify that movement to the right is possible
                print("The car:", car._name, "can move to the right")

moveCar(game_board, cars)
