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
Rushhour_df = pd.read_csv("/mnt/c/Users/jaspe/ProgrammeerTheorie/gameboards/Rushhour12x12_7.csv")

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

#create 6x6 data consisting only of zeros using numpy
zero_data = np.zeros((dimensions, dimensions))

#use pandas to create 6x6 DataFrame from the zeros matrix
game_board = pd.DataFrame(zero_data).astype(int)

#cycle through the cars list
for car in cars: 
    #check if car is horizontal
    if car._orientation == "H":
        #cycle through lenght of the car
        for index in range(0, car._length):
            #replace zeros in DataFrame with the carname in horizontal fashion
            game_board[car.column + index][car.row] = car._name
    #if not horizontal, car is vertical
    else:
        #cycle through lenght of the car
        for index in range(0, car._length):
            #replace zeros in DataFrame with the carname in vertical fashion
            game_board[car.column][car.row + index] = car._name

#show gameboard
print(game_board)

