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
from collections import deque
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
        self._cars_init = []
        # self._cars_init_dict = {}

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
        self.empty_board_string = []
        for i in self.empty_board: 
            row = []
            for j in i: 
                row.append(str(int(j)))
            self.empty_board_string.append(row)
        self.gameboard = pickle.loads(pickle.dumps(self.empty_board_string))

    
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
                        #print("The car:", carname, "has moved to the left")
                        #self.printBoard()
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
                        #print("The car:", carname, "has moved to the right")
                        #self.printBoard()
                        self.movecounter += 1
                    """
                    If the car willing to move is X (Red car), check if the cell on the right
                    equals 2,, meaning the exit has been reached. 
                    """
                    if car._name == 'X':
                        if self.gameboard[car.row][car.column + car._length] == "2":
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
                    if self.gameboard[car.row - 1][car.column] == "0":
                        car.row -= 1
                        self.place_car(self.cars)
                        #print("The car:", car._name, "has moved up")
                        #self.printBoard()
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
                        #print("The car:", car._name, "has moved down")
                        #self.printBoard()
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
                elif cell == "2": 
                    cprint(int(cell), 'red', end = '  ')
                    screenshot += str(cell)
                elif cell == "X": 
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
                elif cell == "2": 
                    screenshot += str(cell)
                elif cell == "X": 
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
        output_series.to_csv('output/Rushhour_output.csv', header=False)
    
    """
    Define function for semi-random game loop.
    """
    def randomGameLoop(self):
        while self.running == True: 
            """
            Choose random car from self.cars and move it left. 
            Same for other directions untill "X" (Red car) reaches exit. 
            """
            self.moveCarLeft(random.choice(random.choice(self.cars)._name))
            self.moveCarRight(random.choice(random.choice(self.cars)._name))
            self.moveCarUp(random.choice(random.choice(self.cars)._name))
            self.moveCarDown(random.choice(random.choice(self.cars)._name))
        self.stop = timeit.default_timer()
        print("Time", self.stop - self.start, "seconds")
        print("Number of moves", self.movecounter)
        return [self.movecounter, self.stop - self.start]


    """
    Define function for breadth first algorithm. 
    """
    def breadthFirst(self, heuristic):
        """
        Creation of the BFS queue moves and required variables containing the path, 
        the next possible states and the start configuration of the board. 
        """
        moves = deque()
        moves.appendleft("")
        path = ""
        states = {""}
        startposion = self.noprintBoard()

        while self.running == True:
            """
            Set the cars to the original start configuration and create
            a deep copy of this state. 
            """
            self.place_car(self._cars_init)
            self.cars = pickle.loads(pickle.dumps(self._cars_init))

            """
            Take the first state from the queue and print
            path length. 
            """
            path = moves.popleft()
            #print(len(path) / 2)

            """
            Read through the chosen path. 
            Determine car name and which direction to move in. 
            Move car in correct directions to update game board. 
            """
            for i in range(0, len(path), 2):
                if path[i + 1] == 'L':
                    self.moveCarLeft(path[i])
                elif path[i + 1] == 'R':
                    self.moveCarRight(path[i])
                elif path[i + 1] == 'U':
                    self.moveCarUp(path[i])
                elif path[i + 1] == 'D':
                    self.moveCarDown(path[i])
            
            """
            Check if the currently loaded gameboard has previously been loaded,
            excluding the start configuration. Continue and add to history or skip
            this board.
            """
            if self.noprintBoard() in self.history and self.noprintBoard() != startposion: 
                #print("duplicate")
                continue
            else: 
                self.history.append(self.noprintBoard())


            """
            Move through the cars in self.cars. 
            Check if they can move left, right, up or down
            and add their name + direction to moving_cars list. 
            If the Red car (X) can move and end the game, just end the game. 
            """
            moving_cars = []
            for car in self.cars:
                if car._orientation == "V":  
                    if self.gameboard[car.row + car._length][car.column] == "0":
                        moving_cars.append(car._name)
                        moving_cars.append('D')
                    if self.gameboard[car.row - 1][car.column] == "0":
                        moving_cars.append(car._name)
                        moving_cars.append('U')
                if car._orientation == "H":  
                    if self.gameboard[car.row][car.column + car._length] == "0":
                        moving_cars.append(car._name)
                        moving_cars.append('R')
                    if self.gameboard[car.row][car.column - 1] == "0":
                        moving_cars.append(car._name)
                        moving_cars.append('L')
                    if car._name == "X" and self.gameboard[car.row][car.column + car._length] == "2":
                        self.stop = timeit.default_timer()
                        print("Time", self.stop - self.start, "seconds")
                        print(len(path) / 2)
                        self.running = False

            """
            Simple introduction of heuristics. Determine if the Red car
            could move to the right. If so, this move is brings us 
            closer to the endgame and thus this configuration will 
            have priority over the others and will be placed in the prio1 queue. 
            Moving cars to the left creates space on the right of the Red car, 
            improving future movement posibilities. So place these configs in prio2. 
            Moving cars up and down also creates space for the Red car, so prio3. Finally
            moving cars other than the Red one to the right most likely does not improve the 
            configuration, so no priority. 

            The priority queues will ensure that promising configurations will be explored first, 
            which greatly reduces search time. 
            """
            if heuristic == True: 
                prio1 = deque("")
                prio2 = deque("")
                prio3 = deque("")
                for i in range(0, len(moving_cars), 2):
                    if moving_cars[i] == "X" and moving_cars[i + 1] == "R": 
                        move = moving_cars[i] + moving_cars[i + 1]
                        put = path + move
                        states.add(put)
                        prio1.appendleft(put)
                    elif moving_cars[i + 1] == "L" and moving_cars[i] != "X": 
                        move = moving_cars[i] + moving_cars[i + 1]
                        put = path + move
                        states.add(put)
                        prio2.appendleft(put)
                    elif moving_cars[i + 1] == "U" or moving_cars[i + 1] == "D": 
                        move = moving_cars[i] + moving_cars[i + 1]
                        put = path + move
                        states.add(put)
                        prio3.appendleft(put)
                    else:
                        move = moving_cars[i] + moving_cars[i + 1]
                        put = path + move
                        states.add(put)
                        moves.append(put)
                    
                    """
                    Again a end-game check function. 
                    """
                    if move == "XR":
                        self.moveCarRight('X')
                        if self.gameboard[car.row][car.column + car._length] == "2":
                            print("Path:", path + move)
                            self.stop = timeit.default_timer()
                            print("Time", self.stop - self.start, "seconds")
                            self.running = False
                            print("How many steps: ", len(path + move) / 2)
                        else:
                            self.moveCarLeft('X')
                """
                Combine the priority queues with the normal queue 
                to feed to the next cycle of the bfs algorithm. 
                """
                moves = prio1 + prio2 + prio3 + moves
            else: 
                """
                If heuristic is false. Run without heuristics and 
                treat every board as equal. 
                """
                for i in range(0, len(moving_cars), 2):
                    move = moving_cars[i] + moving_cars[i + 1]
                    put = path + move
                    states.add(put)
                    moves.append(put)

                    """
                    Again a end-game check function. 
                    """
                    if move == "XR":
                        self.moveCarRight('X')
                        if self.gameboard[car.row][car.column + car._length] == "2":
                            print("Path:", path + move)
                            self.stop = timeit.default_timer()
                            print("Time", self.stop - self.start, "seconds")
                            self.running = False
                            print("How many steps: ", len(path + move) / 2)
                        else:
                            self.moveCarLeft('X')