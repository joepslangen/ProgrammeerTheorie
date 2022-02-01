import random
import timeit

class Semi_random(): 
    """The Semi_random class containing the semi-random algorithm."""
    def __init__(self, board, hill):
        self.board = board
        self.start, self.stop = 0, 0 
        # used to check if semi-random will be used on its own or in hillclimber
        self.hill = hill
    
    def semi_random(self):
        """Semi-random algorithm: move random cars in predetermined directions."""
        path = []
        self.start = timeit.default_timer()
        # while game is running move random car left, right, up & down
        while self.board.running == True: 
            self.moveLeft(path)
            self.moveRight(path)
            self.moveUp(path)
            self.moveDown(path)
        # stop own and boards timers
        self.board.stop = timeit.default_timer()
        self.stop = timeit.default_timer()
        if self.hill == True: 
            return path                                                 # return this return when using hillclimber algorithm
        else:                                               
            return self.stop - self.start, self.board.movecounter       # return this return to create histogram from semi-random results

    def moveLeft(self, path): 
        """Choose random car and move left. 
        
        Take a random car on the board and try to move it left. If 
        possible append the car and direction to the path and increase 
        the number of moves by one. 
        """
        car = random.choice(random.choice(self.board.cars)._name)
        if self.board.moveCarLeft(car) == True: 
            self.board.moveCarLeft(car)
            path.append(f"{car}L")
            self.board.movecounter += 1

    def moveRight(self, path): 
        """Choose random car and move right. 
        
        Take a random car on the board and try to move it right. If 
        possible append the car and direction to the path and increase 
        the number of moves by one. 
        """
        car = random.choice(random.choice(self.board.cars)._name)
        if self.board.moveCarRight(car) == True: 
            self.board.moveCarRight(car)
            path.append(f"{car}R")
            self.board.movecounter += 1

    def moveUp(self, path):
        """Choose random car and move up. 
        
        Take a random car on the board and try to move it up. If 
        possible append the car and direction to the path and increase 
        the number of moves by one. 
        """
        car = random.choice(random.choice(self.board.cars)._name)
        if self.board.moveCarUp(car) == True:
            self.board.moveCarUp(car)
            path.append(f"{car}U")
            self.board.movecounter += 1

    def moveDown(self, path): 
        """Choose random car and move down. 
        
        Take a random car on the board and try to move it down. If 
        possible append the car and direction to the path and increase 
        the number of moves by one. 
        """
        car = random.choice(random.choice(self.board.cars)._name)
        if self.board.moveCarDown(car) == True: 
            self.board.moveCarDown(car)
            path.append(f"{car}D")
            self.board.movecounter += 1