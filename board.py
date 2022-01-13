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
        self._rows_init = {}
        self._cols_init = {}
        self.dimensions = max(Rushhour_df["col"])

        #create a ones matrix with dimensions of: dimension+2 x dimension+2 
        #to provide a barrier around the drivable gameboard 
        #this was needed to prevent out of range errors ocurring in the moveCheck function
        ones_matrix = np.ones((self.dimensions + 2, self.dimensions + 2))
        #actual drivable gameboard consists of zeros with dimensions: dimension x dimension
        zeros_matrix = np.zeros((self.dimensions, self.dimensions))
        #combine the ones matrix and the zeros matrix to create empty board with barriers
        ones_matrix[1:self.dimensions + 1, 1:self.dimensions + 1] = zeros_matrix
        #add 2 to ones matrix to show exit
        col_out = self.dimensions + 1
        row_out = self.dimensions // 2
        ones_matrix[row_out][col_out] = 2
        #define a clean board with barrier with the correct dimensions
        self.clean_board = ones_matrix
        #set the game board to the clean board 
        self.game_board = pd.DataFrame(self.clean_board).astype(int)

    #load cars from csv file into self.cars
    #self.cars car properties will be changed by moving the cars
    #this loop will only run once
    def load_cars(self, Rushhour_df):
        # cycle through every row in the dataframe
        for index in range(len(Rushhour_df)):
            #extrac name from the column "car"
            car_name = Rushhour_df.loc[index, "car"]
            #extract orientation from column "orientation"
            car_orientation = Rushhour_df.loc[index, "orientation"]
            #extract orientation from column "col"
            car_column = Rushhour_df.loc[index, "col"]

            self._cols_init[car_name] = car_column

            #extract orientation from column "row"
            car_row = Rushhour_df.loc[index, "row"]

            self._rows_init[car_name] = car_row

            #extract lenght from column "length"
            car_length = Rushhour_df.loc[index, "length"]
            #define car using Car() class and extracted properties
            car = Car(car_name, car_orientation, car_column, car_row, car_length)
            #add car to cars list
            self.cars.append(car)

    #place cars from self.cars onto a clean game board
    def place_car(self):
        #clear the previous game board before placing cars in new positions
        self.game_board = pd.DataFrame(self.clean_board).astype(int)
        #cycle through the cars list
        for car in self.cars: 
            #check if car is horizontal
            if car._orientation == "H":
                #cycle through lenght of the car
                for index in range(0, car._length):
                    #replace zeros in DataFrame with the carname in horizontal fashion
                    self.game_board.loc[car.row, car.column + index] = car._name
            #if not horizontal, car is vertical
            else:
                #cycle through lenght of the car
                for index in range(0, car._length):
                    #replace zeros in DataFrame with the carname in vertical fashion
                    self.game_board.loc[car.row + index, car.column] = car._name.lower()

    #to move car left, change its column position
    def moveCarLeft(self, carname):
        for car in self.cars: 
            if car._orientation == "H": 
                if car._name == carname:
                    if self.game_board.loc[car.row, car.column - 1] == 0:
                        car.column -= 1
                        self.place_car()
                        print("The car:", carname, "has moved to the left")

    #to move car right, change its column position
    def moveCarRight (self, carname):
        for car in self.cars: 
            if car._orientation == "H": 
                if car._name == carname: 
                    if self.game_board.loc[car.row, car.column + car._length] == 0:
                        car.column += 1
                        self.place_car()
                        print("The car:", carname, "has moved to the right")
                    if car._name == 'X':
                        if self.game_board.loc[car.row, car.column + car._length] == 2:
                            print("You did it!")
    
    #to move car up, change its row position
    def moveCarUp (self, carname):
        for car in self.cars: 
            if car._orientation == "V":
                if car._name == carname: 
                    if self.game_board.loc[car.row - 1, car.column] == 0:
                        car.row -= 1
                        self.place_car()
                        print("The car:", car._name, "has moved up")
    
    #to move car down, change its row position
    def moveCarDown(self, carname):
        for car in self.cars: 
            if car._orientation == "V": 
                if car._name == carname: 
                    if self.game_board.loc[car.row + car._length, car.column] == 0:
                        car.row += 1
                        self.place()
                        print("The car:", car._name, "has moved down")
                
    #function to print game board
    def printBoard(self):
        print(self.game_board)
    
    #write output to csv
    def writeOutput(self):
        #create dict to store output
        output = {}
        #create headers
        output['car'] = 'move'

        #calculate movement and add to output dict
        for car in self.cars:
            output[car._name] = (car.row - self._rows_init[car._name]) + (car.column - self._cols_init[car._name])
        
        #convert dict into pandas Series and write to csv
        output_series = pd.Series(data=output)
        output_series.to_csv('output/Rushhour_output.csv', header=False)
