import pickle 
from code.algorithms.semi_random import Semi_random
import sys
import os
import timeit


class Hill(): 

    def __init__(self, board): 
        self.board = board
        self.start = 0
        self.stop = 0

    def hill(self): 
        self.start = timeit.default_timer()

        semi_random = Semi_random(self.board)
        path = semi_random.semi_random()

        print(len(path))

        """
        Turn printing off
        """
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

        """
        Set gameboard to running. Load cars and place on fresh board. 
        Generate random path and check lenght. If path is shorter keep 
        this path as shortest path.
        """

        for i in range(0, 100): 
            self.board.running = True
            self.board.cars = pickle.loads(pickle.dumps(self.board._cars_init))
            self.board.place_car(self.board.cars)
            temp_path = semi_random.semi_random()
            if len(temp_path) < len(path): 
                path = temp_path
        self.stop = timeit.default_timer()
        

        """
        Turn printing back on
        """
        sys.stdout = old_stdout
        
        print(len(path))
        return self.stop - self.start, len(path)