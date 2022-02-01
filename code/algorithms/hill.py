import pickle 
from code.algorithms.semi_random import Semi_random
import sys
import os
import timeit


class Hill(): 
    """The Hill class, containing the hillclimber-like algorithm"""

    def __init__(self, board): 
        self.board = board
        self.start, self.stop = 0, 0

    def hill(self): 
        """Hillclimber-like algorithm. 
        
        Runs the semi-random algorithm and remembers the length of found path. 
        Then runs semi-random 100 times more, only to keep the shortest path. 
        """

        # start algorithm timer
        self.start = timeit.default_timer()

        # run semi-random algorithm and save found path
        semi_random = Semi_random(self.board, hill=True)
        path = semi_random.semi_random()

        # turn off printing
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

        for i in range(0, 100): 
            # set gamestatus back to running, reload inital position and place cars
            self.board.running = True
            self.board.cars = pickle.loads(pickle.dumps(self.board._cars_init))
            self.board.place_car(self.board.cars)

            # run semi-random algorithm and remember path
            temp_path = semi_random.semi_random()
            
            #check if newly found path is shorter, if so replace older path
            if len(temp_path) < len(path): 
                path = temp_path

        # stop algorithm timer
        self.stop = timeit.default_timer()
        
        # turn printing back on
        sys.stdout = old_stdout

        # return runtime and found path-length        
        return self.stop - self.start, len(path)