import random
import timeit

class Semi_random(): 
    """
    Define function for semi-random game loop.
    """
    def __init__(self, board):
        self.board = board
    
    def semi_random(self):
        while self.board.running == True: 
            """
            Choose random car from self.board.cars and move it left. 
            Same for other directions untill "X" (Red car) reaches exit. 
            """
            self.board.moveCarLeft(random.choice(random.choice(self.board.cars)._name))
            self.board.moveCarRight(random.choice(random.choice(self.board.cars)._name))
            self.board.moveCarUp(random.choice(random.choice(self.board.cars)._name))
            self.board.moveCarDown(random.choice(random.choice(self.board.cars)._name))
        """
        When game is stopped, return runtime and number of moves
        """
        self.board.stop = timeit.default_timer()
        print("Time", self.board.stop - self.board.start, "seconds")
        print("Number of moves", self.board.movecounter)
