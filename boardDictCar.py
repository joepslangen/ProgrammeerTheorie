##
# CHANGELOG: 13/01/2022
# First try at setting up the gameboard while representing the cars as a dictionary. 
# This does not require the Car class from car.py nor main.py
# It requires 1 for-loop less when moving in 1 direction. 
# However number of characters in the code drastically increases. 
# NOTE: Still needs a writeOutput function

 
#required imports
import pandas as pd
import numpy as np

#start creating the Board() class
class Board():

    #initialize
    def __init__(self, Rushhour_df):
        #create dictionary to save cars
        self.cars = {}
        #determine dimensions of the gameboard from the .csv file
        self.dimensions = max(Rushhour_df["col"])

        #dictionary to keep initial columns and rows
        self._rows_init = {}
        self._cols_init = {}

        #create a matrix consisting of ones with dimensions: dimension+2 x dimension+2 
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
            self.cars[Rushhour_df.loc[index, "car"]] = {}
            #extract orientation from column "orientation"
            self.cars[Rushhour_df.loc[index, "car"]]["car_orientation"] = Rushhour_df.loc[index, "orientation"]
            #extract orientation from column "col"
            self.cars[Rushhour_df.loc[index, "car"]]["car_column"] = Rushhour_df.loc[index, "col"]
            #extract orientation from column "row"
            self.cars[Rushhour_df.loc[index, "car"]]["car_row"] = Rushhour_df.loc[index, "row"]
            #extract lenght from column "length"
            self.cars[Rushhour_df.loc[index, "car"]]["car_length"] = Rushhour_df.loc[index, "length"]

            self._cols_init[Rushhour_df.loc[index, "car"]] = Rushhour_df.loc[index, "col"]
            self._rows_init[Rushhour_df.loc[index, "car"]] = Rushhour_df.loc[index, "row"]

    #place cars from self.cars onto a clean game board
    def place_car(self):
        #clear the previous game board before placing cars in new positions
        self.game_board = pd.DataFrame(self.clean_board).astype(int)
        #cycle through the cars list
        for car in self.cars: 
            #check if car is horizontal
            if self.cars[car]["car_orientation"] == "H":
                #cycle through lenght of the car
                for index in range(0, self.cars[car]["car_length"]):
                    #replace zeros in DataFrame with the carname in horizontal fashion
                    self.game_board.loc[self.cars[car]["car_row"], self.cars[car]["car_column"] + index] = car
                
            #if not horizontal, car is vertical
            else:
                #cycle through lenght of the car
                for index in range(0, self.cars[car]["car_length"]):
                    #replace zeros in DataFrame with the carname in vertical fashion
                    self.game_board.loc[self.cars[car]["car_row"] + index, self.cars[car]["car_column"]] = car.lower()
                                   
    #to move car left, change its column position
    def moveCarRight(self, carname):
        #check if the car has a valid name
        if carname in self.cars: 
            #check if the cell on the right side of the car is empty
            if self.game_board.loc[self.cars[carname]["car_row"], self.cars[carname]["car_column"] + self.cars[carname]["car_length"]] == 0: 
                #move the car 1 unit to the right
                self.cars[carname]["car_column"] += 1
                #place cars again 
                self.place_car()
                #print movement confirmation
                print("The car:", carname, "has moved to the right")
            if carname == "X":
                if self.game_board.loc[self.cars[carname]["car_row"], self.cars[carname]["car_column"] + self.cars[carname]["car_length"]] == 2: 
                    print("You did it!")

    #to move car right, change its column position
    def moveCarLeft(self, carname):
        if carname in self.cars: 
            #check if the cell on the left side of the car is empty
            if self.game_board.loc[self.cars[carname]["car_row"], self.cars[carname]["car_column"] - 1] == 0: 
                #move car 1 unit to the left
                self.cars[carname]["car_column"] -= 1
                self.place_car()
                print("The car:", carname, "has moved to the left")
    
    #to move car up, change its row position
    def moveCarUp (self, carname):
        if carname in self.cars: 
            #check if the cell above the car is empty
            if self.game_board.loc[self.cars[carname]["car_row"] - 1, self.cars[carname]["car_column"]] == 0: 
                #move car 1 unit up 
                self.cars[carname]["car_row"] -= 1
                self.place_car()
                print("The car:", carname, "has moved up")
    
    #to move car down, change its row position
    def moveCarDown(self, carname):
        if carname in self.cars: 
            #check if the cell below the car is empty
            if self.game_board.loc[self.cars[carname]["car_row"] + self.cars[carname]["car_length"], self.cars[carname]["car_column"]] == 0: 
                #move car 1 unit down
                self.cars[carname]["car_row"] += 1
                self.place_car()
                print("The car:", carname, "has moved down")
                
    #function to print game board
    def printBoard(self):
        print(self.game_board)

    def writeOutput(self):
        output = {}
        output["car"] = "move"

        for car in self.cars: 
            output[car] = (self.cars[car]["car_row"] - self._rows_init[car]) + (self.cars[car]["car_column"] - self._cols_init[car])

        #convert dict into pandas Series and write to csv
        output_series = pd.Series(data=output)
        output_series.to_csv('output/Rushhour_output.csv', header=False)
    

if __name__ == "__main__":

    #read rushhour6x6_1.csv
    Rushhour_df = pd.read_csv("gameboards/Rushhour6x6_1.csv")

    game = Board(Rushhour_df)
    game.load_cars(Rushhour_df)
    game.place_car()
    game.printBoard()
    game.moveCarLeft("X")
    game.printBoard()    
    