##
# Jasper Paul
# First try at reading the .csv files and setting up the game board
# requires the Car() class and car.py

 
#required imports
import pandas as pd
import numpy as np

#import car.py
from car import Car

class Board():

    def __init__(self, Rushhour_df):
        self.cars = []
        self.dimensions = max(Rushhour_df["col"])

        #create a ones matrix with dimensions of: dimension+2 x dimension+2 
        #to provide a barrier around the drivable gameboard
        ones_matrix = np.ones((self.dimensions + 2, self.dimensions + 2))

        #actual drivable gameboard consists of zeros with dimensions: dimension x dimension
        zeros_matrix = np.zeros((self.dimensions, self.dimensions))

        #combine the ones matrix and the zeros matrix to create empty board with barriers
        ones_matrix[1:self.dimensions + 1, 1:self.dimensions + 1] = zeros_matrix

        #use pandas to create 6x6 DataFrame from the board matrix matrix
        self.game_board = pd.DataFrame(ones_matrix).astype(int)

    def load_cars(self, Rushhour_df):
        # cycle through every row in the dataframe
        for index in range(len(Rushhour_df)):
            #extrac name from the column "car"
            car_name = Rushhour_df.loc[index, "car"]
            #extract orientation from column "orientation"
            car_orientation = Rushhour_df.loc[index, "orientation"]
            #extract orientation from column "col"
            car_column = Rushhour_df.loc[index, "col"]
            #extract orientation from column "row"
            car_row = Rushhour_df.loc[index, "row"]
            #extract lenght from column "length"
            car_length = Rushhour_df.loc[index, "length"]
            
            #define car using Car() class and extracted properties
            car = Car(car_name, car_orientation, car_column, car_row, car_length)

            #add car to cars list
            self.cars.append(car)

    def place_car(self):
        #cycle through the cars list
        for car in self.cars: 
            #check if car is horizontal
            if car._orientation == "H":
                #cycle through lenght of the car
                for index in range(0, car._length):
                    #replace zeros in DataFrame with the carname in horizontal fashion
                    #correction of 1 since we added a 1 thick layer of barrier around the board
                    self.game_board.loc[car.row, car.column + index] = car._name
            #if not horizontal, car is vertical
            else:
                #cycle through lenght of the car
                for index in range(0, car._length):
                    #replace zeros in DataFrame with the carname in vertical fashion
                    #correction of 1 since we added a 1 thick layer of barrier around the board
                    self.game_board.loc[car.row + index, car.column] = car._name
    
        #show gameboard
        print(self.game_board)

    #start of a function able to move cars
    def moveCheck(self):
        #cycle through the cars in the cars lists
        for car in self.cars: 
            #again check for orientation if horizontal
            if car._orientation == "H": 
                #check if the spot on the right of the car is free
                if self.game_board.loc[car.row, car.column + car._length] == 0:
                    #if so notify that movement to the right is possible
                    print("The car:", car._name, "can move to the right")
                if self.game_board.loc[car.row, car.column - 1] == 0: 
                    print("The car:", car._name, "can move to the left")
            if car._orientation == "V":
                if self.game_board.loc[car.row - 1, car.column] == 0:
                    print("The car:", car._name, "can move up")
                if self.game_board.loc[car.row + car._length, car.column] == 0:
                    print("The car:", car._name, "can move down")

if __name__ == "__main__":

    #read rushhour6x6_1.csv
    Rushhour_df = pd.read_csv("gameboards/Rushhour12x12_7.csv")

    game = Board(Rushhour_df)
    game.load_cars(Rushhour_df), 
    game.place_car()
    game.moveCheck()