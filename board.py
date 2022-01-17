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
from termcolor import colored, cprint
import random
from car import Car
import timeit

"""
Start class for the game board. 
Includes board init, car loading, 
car placement, car movement, 
board printing and output functions. 
"""
class Board():

    def __init__(self, dimensions):

        self.running = True
        self.start = timeit.default_timer()
        self.stop = 0
        self.movecounter = 0

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
        self.cars = []
        self._rows_init = {}
        self._cols_init = {}
        self.dimensions = dimensions

        """
        Creation of matrices containing ones and zeros in the correct dimensions. 
        The ones matrix will provide a barrier around the board, needed to prevent out of range
        errors. The zeros will form the empty board.
        """
        ones_matrix = np.ones((self.dimensions + 2, self.dimensions + 2))
        zeros_matrix = np.zeros((self.dimensions, self.dimensions))
        ones_matrix[1:self.dimensions + 1, 1:self.dimensions + 1] = zeros_matrix
        
        """
        Set one of the ones in the barrier to a two. This is needed to define the exit, 
        which the red car should reach. 
        """
        col_out = self.dimensions + 1
        row_out = (self.dimensions + 1) // 2
        ones_matrix[row_out][col_out] = 2
        
        """"
        Finally define a emptygameboard and set the current gameboard to 
        the empty one. 
        """
        self.empty_board = ones_matrix
        self.gameboard = pd.DataFrame(self.empty_board).astype(int)

    
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
            self.cars.append(car)

    """
    Define function to place cars from the self.cars list onto the gameboard. 
    """
    def place_car(self):
        """
        First clear the previous game board. Cycle through the cars in self.cars 
        list and check their current rows, collumns, orientation and lenght. 
        Replace the zeroes in the empty gameboard with the car name. 
        """
        self.gameboard = pd.DataFrame(self.empty_board).astype(int)
        for car in self.cars: 
            if car._orientation == "H":
                for index in range(0, car._length):
                    self.gameboard.loc[car.row, car.column + index] = car._name
            else:
                for index in range(0, car._length):
                    self.gameboard.loc[car.row + index, car.column] = car._name.lower()

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
                    if self.gameboard.loc[car.row, car.column - 1] == 0:
                        car.column -= 1
                        self.place_car()
                        print("The car:", carname, "has moved to the left")
                        self.printBoard()
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
                    if self.gameboard.loc[car.row, car.column + car._length] == 0:
                        car.column += 1
                        self.place_car()
                        print("The car:", carname, "has moved to the right")
                        self.printBoard()
                        self.movecounter += 1
                    """
                    If the car willing to move is X (Red car), check if the cell on the right
                    equals 2,, meaning the exit has been reached. 
                    """
                    if car._name == 'X':
                        if self.gameboard.loc[car.row, car.column + car._length] == 2:
                            print("You did it!")
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
                    if self.gameboard.loc[car.row - 1, car.column] == 0:
                        car.row -= 1
                        self.place_car()
                        print("The car:", car._name, "has moved up")
                        self.printBoard()
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
                    if self.gameboard.loc[car.row + car._length, car.column] == 0:
                        car.row += 1
                        self.place_car()
                        print("The car:", car._name, "has moved down")
                        self.printBoard()
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
        gameboard = self.gameboard.values.tolist()
        for row in gameboard: 
            for cell in row: 
                if cell == 1 or cell == 0: 
                    cprint(int(cell), 'grey', end = "  ")
                elif cell == 2: 
                    cprint(int(cell), 'red', end = '  ')
                elif cell == "X": 
                    cprint(cell, 'red', end = '  ')
                else: 
                    if cell not in self.colourdict: 
                        self.colourdict[cell] = random.choice(self.colour_list)
                    cprint(cell, self.colourdict[cell], end = " " * int(2/len(cell)))
            print(' ')
    
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
        output_series.to_csv('output/Rushhour_output.csv', header=False)
    
    def randomGameLoop(self):
        while self.running == True: 
            self.moveCarLeft(random.choice(random.choice(self.cars)._name))
            self.moveCarRight(random.choice(random.choice(self.cars)._name))
            self.moveCarUp(random.choice(random.choice(self.cars)._name))
            self.moveCarDown(random.choice(random.choice(self.cars)._name))
        self.stop = timeit.default_timer()
        print("Time", self.stop - self.start, "seconds")
        print("Number of moves", self.movecounter)
