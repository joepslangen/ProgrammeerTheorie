import pandas as pd
import numpy as np
import sys
from termcolor import cprint
import random
from code.classes.car import Car
import timeit
import os
import pickle

class Board():
    """The Board class, containing everything related to the board"""
    def __init__(self, dimensions):
        # history, gamestatus, timer and move counter variables
        self.history = []
        self.running = True
        self.start, self.stop, self.movecounter = timeit.default_timer(), 0, 0

        # list and dictionary of colours, required for colour printing in terminal
        self.colour_list = ['green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        self.colourdict = {}

        # lists and dictionaries to store cars
        self.cars, self._cars_init = [], []
        self._rows_init, self._cols_init = {}, {}

        # creation of the (empty) game board in differing formats
        self.empty_board = self.create_empty_gameboard(dimensions)
        self.gameboard, self.empty_board_string = self.create_gameboard(self.empty_board)

    def create_empty_gameboard(self, dimensions):
        """Creation of an emtpy gameboard. 

        Create matrices containing ones and zeros in the correct dimensions. 
        The ones matrix will provide a barrier around the board, needed to prevent out of range
        errors. The zeros will form the empty board.
        """
        ones_matrix = np.ones((dimensions + 2, dimensions + 2))
        zeros_matrix = np.zeros((dimensions, dimensions))
        ones_matrix[1:dimensions + 1, 1:dimensions + 1] = zeros_matrix
        
        # replace one of the one's in the barrier with a two to indicate exit
        col_out = dimensions + 1
        row_out = (dimensions + 1) // 2
        ones_matrix[row_out][col_out] = 2
        
        # return the empty gameboard + barrier + exit
        return ones_matrix
        

    def create_gameboard(self, empty_board):
        """Take the empty gameboard and turn it into usable gameboards.
        
        Cycle through the empty game board and transform each float into strings. 
        """
        empty_board_string = []
        for row in empty_board: 
            row = []
            for cell in row: 
                row.append(str(int(cell)))
            empty_board_string.append(row)
        gameboard = pickle.loads(pickle.dumps(empty_board_string))
        return gameboard, empty_board_string

    
    def load_cars(self, Rushhour_df):
        """Load cars from .csv file. 

        Cylce through the rows in the .csv file. 
        Extract the carname, orientation, row, column and lenght.
        Add carname and the corresponding starting row & column 
        to the initial column dictionary. 
        """
        for index in range(len(Rushhour_df)):
            car_name = Rushhour_df.loc[index, "car"]
            car_orientation = Rushhour_df.loc[index, "orientation"]
            car_column = Rushhour_df.loc[index, "col"]
            car_row = Rushhour_df.loc[index, "row"]
            car_length = Rushhour_df.loc[index, "length"]

            # keep track of initial rows and columns
            self._cols_init[car_name] = car_column
            self._rows_init[car_name] = car_row
            
            # use Car() class to define cars and store them in the correct lists
            car = Car(car_name, car_orientation, car_column, car_row, car_length)
            car_init = Car(car_name, car_orientation, car_column, car_row, car_length)
            self.cars.append(car)
            self._cars_init.append(car_init)

    """
    Define function to place cars from the self.cars list onto the gameboard. 
    """
    def place_car(self, cars):
        """Place cars from list onto the gameboard. 

        First clear the previous game board. Cycle through the cars in self.cars 
        list and check their current rows, collumns, orientation and lenght. 
        Replace the zeroes in the empty gameboard with the car name. 
        """
        self.gameboard = pickle.loads(pickle.dumps(self.empty_board_string))
        for car in cars: 
            if car._orientation == "H":
                for length in range(0, car._length):
                    # replace the strings in the empty gameboard with the car name
                    self.gameboard[car.row][car.column + length] = car._name
            else:
                for length in range(0, car._length):
                    # replace the strings in the empty gameboard with the car name
                    self.gameboard[car.row + length][car.column] = car._name.lower()


    def moveCarLeft(self, carname):
        """Move car left. 

        Cycle through the cars in self.cars list. Check orientation. 
        Check if the cell left of the car is empty. If so, move the car
        one column to the left. 
        """
        for car in self.cars: 
            if car._orientation == "H": 
                if car._name == carname:
                    if self.gameboard[car.row][car.column - 1] == "0": 
                        car.column -= 1
                        self.place_car(self.cars)
                        self.movecounter += 1
                        return True

    def moveCarRight (self, carname):
        """Move car right. 

        Cycle through the cars in self.cars list. Check orientation. 
        Check if the cell right of the car is empty. If so, move the car
        one column to the right. 
        """
        for car in self.cars: 
            if car._orientation == "H": 
                if car._name == carname: 
                    if self.gameboard[car.row][car.column + car._length] == "0":
                        car.column += 1
                        self.place_car(self.cars)
                        self.movecounter += 1
                        return True
                    # if the car to move is the red car, check if it reaches the exit with this move, 
                    # if so end the game
                    if car._name == 'X':
                        if self.gameboard[car.row][car.column + car._length] == "2":
                            self.stop = timeit.default_timer()
                            print("You did it!")
                            print(f"Time: {self.stop - self.start} seconds")
                            self.running = False
                            return True
    

    def moveCarUp (self, carname):
        """Move car up. 

        Cycle through the cars in self.cars list. Check orientation. 
        Check if the cell above the car is empty. If so, move the car
        one row up. 
        """
        for car in self.cars: 
            if car._orientation == "V":
                if car._name == carname: 
                    if self.gameboard[car.row - 1][car.column] == "0":
                        car.row -= 1
                        self.place_car(self.cars)
                        self.movecounter += 1
                        return True 


    def moveCarDown(self, carname):
        """Move car down. 

        Cycle through the cars in self.cars list. Check orientation. 
        Check if the cell below the car is empty. If so, move the car
        one row down.
        """
        for car in self.cars: 
            if car._orientation == "V": 
                if car._name == carname: 
                    if self.gameboard[car.row + car._length][car.column] == "0":
                        car.row += 1
                        self.place_car(self.cars)
                        self.movecounter += 1
                        return True


    def printBoard(self):
        """Print the game board in colour. 

        Cycle through the rows and cells
        in the current gameboard. If the cell represents a barrier or empty 
        spot, print in gray. If it represents the exit or "X" (Red car), print 
        in red. Otherwise assign random colour to the car, place it in 
        self.courdict and print. 
        """
        screenshot = ""
        gameboard = self.gameboard
        for row in gameboard: 
            for cell in row: 
                if cell == "1" or cell == "0": 
                    # if cell is barrier or empty print in gray
                    cprint(int(cell), 'grey', end = "  ")
                    screenshot += str(cell)
                elif cell == "2" or cell =="X": 
                    # if cell is exit or red car, print in red
                    cprint(cell, 'red', end = '  ')
                    screenshot += str(cell)
                else: 
                    if cell not in self.colourdict: 
                        # if the cell has not been seen yet, pick random available 
                        # colour and assign it to this specific car. duplicates possible
                        self.colourdict[cell] = random.choice(self.colour_list)
                    cprint(cell, self.colourdict[cell], end = " " * int(2/len(cell)))
                    screenshot += str(cell)
            print(' ')
        return screenshot


    def noprintBoard(self):
        """Cycle through board similar way as self.printBoard without printing"""
        screenshot = ""
        gameboard = self.gameboard
        for row in gameboard: 
            for cell in row: 
                if cell == "1" or cell == "0": 
                    screenshot += str(cell)
                elif cell == "2" or cell == "X": 
                    screenshot += str(cell)
                else: 
                    if cell not in self.colourdict: 
                        self.colourdict[cell] = random.choice(self.colour_list)
                    screenshot += str(cell)
        return screenshot
    

    def writeOutput(self):
        """Write requested output to output file in .csv file format"""
        
        # create output dictionary
        output = {}
        output['car'] = 'move'

        # cycle through current position of cars and calculate distance travelled from initial position
        for car in self.cars:
            output[car._name] = (car.row - self._rows_init[car._name]) + (car.column - self._cols_init[car._name])
        
        # write output file
        output_series = pd.Series(data=output)
        output_series.to_csv('output/output.csv', header=False)