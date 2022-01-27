"""
Required imports: 
pandas for correct matrix operations
numpy for generating matrices used for empty board
sys, termcolor and random for colour printing cars
car for using Car() class
"""
import pandas as pd
import numpy as np
import sys
from termcolor import cprint
import random
from code.classes.car import Car
import timeit
import os
import pickle

"""
Start class for the game board. 
Includes board init, car loading, 
car placement, car movement, 
board printing and output functions. 
"""
class Board():

    def __init__(self, dimensions):

        self.history = []
        self.running = True
        self.start, self.stop, self.movecounter = timeit.default_timer(), 0, 0

        """
        Colour list and dictionary. Required for colour printing cars. 
        """
        self.colour_list = ['green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
        self.colourdict = {}

        """
        Car list to contain cars. Initial row and column dictionaries to 
        keep track of cars' starting positions. Dimensions to determine the correct
        board size. 
        """
        self.cars, self._cars_init = [], []
        self._rows_init, self._cols_init = {}, {}

        self.empty_board = self.create_empty_gameboard(dimensions)
        self.gameboard, self.empty_board_string = self.create_gameboard(self.empty_board)

    def create_empty_gameboard(self, dimensions):
        """
        Creation of matrices containing ones and zeros in the correct dimensions. 
        The ones matrix will provide a barrier around the board, needed to prevent out of range
        errors. The zeros will form the empty board.
        """
        ones_matrix = np.ones((dimensions + 2, dimensions + 2))
        zeros_matrix = np.zeros((dimensions, dimensions))
        ones_matrix[1:dimensions + 1, 1:dimensions + 1] = zeros_matrix
        
        """
        Set one of the ones in the barrier to a two. This is needed to define the exit, 
        which the red car should reach. 
        """
        col_out = dimensions + 1
        row_out = (dimensions + 1) // 2
        ones_matrix[row_out][col_out] = 2
        
        """"
        Finally define a emptygameboard and set the current gameboard to 
        the empty one. 
        """
        return ones_matrix
        

    def create_gameboard(self, empty_board):
        empty_board_string = []
        for i in empty_board: 
            row = []
            for j in i: 
                row.append(str(int(j)))
            empty_board_string.append(row)
        gameboard = pickle.loads(pickle.dumps(empty_board_string))
        return gameboard, empty_board_string

    
    """
    Define function to load cars from .csv file into 
    self.cars list. 
    """
    def load_cars(self, Rushhour_df):
        """
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

            self._cols_init[car_name] = car_column
            self._rows_init[car_name] = car_row
            
            """
            Use the Car() class to define the car and append it to 
            self.cars list. 
            """
            car = Car(car_name, car_orientation, car_column, car_row, car_length)
            car_init = Car(car_name, car_orientation, car_column, car_row, car_length)
            self.cars.append(car)
            # self._cars_init.append(car)
        
            self._cars_init.append(car_init)

    """
    Define function to place cars from the self.cars list onto the gameboard. 
    """
    def place_car(self, cars):
        """
        First clear the previous game board. Cycle through the cars in self.cars 
        list and check their current rows, collumns, orientation and lenght. 
        Replace the zeroes in the empty gameboard with the car name. 
        """
        self.gameboard = pickle.loads(pickle.dumps(self.empty_board_string))
        for car in cars: 
            if car._orientation == "H":
                for index in range(0, car._length):
                    self.gameboard[car.row][car.column + index] = car._name
            else:
                for index in range(0, car._length):
                    self.gameboard[car.row + index][car.column] = car._name.lower()

    """
    Define function to move cars to the left.
    """
    def moveCarLeft(self, carname):
        """
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

    """
    Define function to move cars to the right.
    """
    def moveCarRight (self, carname):
        """
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
                    """
                    If the car willing to move is X (Red car), check if the cell on the right
                    equals 2,, meaning the exit has been reached. 
                    """
                    if car._name == 'X':
                        if self.gameboard[car.row][car.column + car._length] == "2":
                            self.stop = timeit.default_timer()
                            print("You did it!")
                            print(f"Time: {self.stop - self.start} seconds")
                            self.running = False
    
    """
    Define function to move cars up.
    """
    def moveCarUp (self, carname):
        """
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

    """
    Define function to move cars down.
    """
    def moveCarDown(self, carname):
        """
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

                
    """
    Define function to print the current game board. 
    """
    def printBoard(self):
        """
        Convert the current self.gameboard to a list of lists into 
        a temp. variable called gameboard. Cycle through the rows and cells
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
                    cprint(int(cell), 'grey', end = "  ")
                    screenshot += str(cell)
                elif cell == "2" or cell =="X": 
                    cprint(cell, 'red', end = '  ')
                    screenshot += str(cell)
                else: 
                    if cell not in self.colourdict: 
                        self.colourdict[cell] = random.choice(self.colour_list)
                    cprint(cell, self.colourdict[cell], end = " " * int(2/len(cell)))
                    screenshot += str(cell)
            print(' ')
        return screenshot


    """
    Define function cycle through the board in similar way as self.printBoard
    only without printing. 
    """
    def noprintBoard(self):
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
    
    """
    Define function to write the desired output file. 
    """
    def writeOutput(self):
        """
        Create an output dictionary to store the carname 
        and corresponding moves. 
        """
        output = {}
        output['car'] = 'move'

        """
        Cycle through the cars in self.cars list and compare their 
        current row/column with the initial row/column. 
        Determine the number of cells it has moved and convert 
        their values to a .csv file.
        """
        for car in self.cars:
            output[car._name] = (car.row - self._rows_init[car._name]) + (car.column - self._cols_init[car._name])
        
        output_series = pd.Series(data=output)
        output_series.to_csv('output/output.csv', header=False)