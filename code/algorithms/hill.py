import pickle 
from code.algorithms.semi_random import Semi_random
import sys
import os


class Hill(): 

    def __init__(self, board): 
        self.board = board

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
        

        """
        Turn printing back on
        """
        sys.stdout = old_stdout
        
        print(len(path))
        


    # NOTE: Kan mogelijk weg
    """
    def path_check(self, path):
        self.board.running = True
        self.board.load_cars(self.Rushhour_df)
        self.board.place_car(self.board._cars_init)
        for i in path: 
            car, direction = i[0], i[1]
            if direction == " ": 
                pass
            elif direction == "L": 
                self.board.moveCarLeft(car)
            elif direction == "R": 
                self.board.moveCarRight(car)
            elif direction == "U": 
                self.board.moveCarUp(car)
            elif direction == "D": 
                self.board.moveCarDown(car)
            self.board.printBoard()
        if self.board.running == False: 
            return True
        else: 
            return False
    """
            


