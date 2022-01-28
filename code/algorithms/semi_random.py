import random
import timeit

class Semi_random(): 
    """
    Define function for semi-random game loop.
    """
    def __init__(self, board):
        self.board = board
    
    def semi_random(self):
        path = []
        while self.board.running == True: 
            self.moveLeft(path)
            self.moveRight(path)
            self.moveUp(path)
            self.moveDown(path)
        self.board.stop = timeit.default_timer()
        #print(f"Time {self.board.stop - self.board.start} seconds")
        #print(f"Number of moves: {self.board.movecounter}")
        return path

    def moveLeft(self, path): 
        car = random.choice(random.choice(self.board.cars)._name)
        if self.board.moveCarLeft(car) == True: 
            self.board.moveCarLeft(car)
            path.append(f"{car}L")
            self.board.movecounter += 1

    def moveRight(self, path): 
        car = random.choice(random.choice(self.board.cars)._name)
        if self.board.moveCarRight(car) == True: 
            self.board.moveCarRight(car)
            path.append(f"{car}R")
            self.board.movecounter += 1

    def moveUp(self, path):
        car = random.choice(random.choice(self.board.cars)._name)
        if self.board.moveCarUp(car) == True:
            self.board.moveCarUp(car)
            path.append(f"{car}U")
            self.board.movecounter += 1

    def moveDown(self, path): 
        car = random.choice(random.choice(self.board.cars)._name)
        if self.board.moveCarDown(car) == True: 
            self.board.moveCarDown(car)
            path.append(f"{car}D")
            self.board.movecounter += 1