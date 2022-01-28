import pickle 
from code.algorithms.semi_random import Semi_random
import sys
import os


class Hill(): 

    def __init__(self, board, Rushhour_df): 
        self.board = board
        self.Rushhour_df = Rushhour_df

    def hill(self): 
        semi_random = Semi_random(self.board)
        path = semi_random.semi_random()

        print(len(path))

        """
        Turn printing off
        """
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

        """
        
        """
        for i in range(0, 100): 
            self.board.running = True
            self.board.cars = pickle.loads(pickle.dumps(self.board._cars_init))
            self.board.place_car(self.board.cars)
            temp_path = semi_random.semi_random()
            if len(temp_path) < len(path): 
                path = temp_path
        

        """
        Turn printing back on
        """
        sys.stdout = old_stdout
        
        print(len(path))
        



