import queue
import pickle
import timeit

class BFS(): 
    """The BFS class containing the Breadth First Search (BFS) algorithm."""
    def __init__(self, board): 
        self.board = board
        self.start, self.stop = 0, 0

    def bfs(self):
        """The BFS algorithm. 

        The BFS algorithm searches a tree datastructure. It starts at the tree root 
        and explores all nodes at the present depth before moving on to the nodes
        at the next depth level. It creates a queue, checks the first node in the queue
        and appends all children nodes to the back of the queue, eventually finding the 
        optimal solution. 
        """
        # initialize queue, path and find startposition
        moves = queue.Queue()
        moves.put("")
        path = ""
        startposion = self.board.noprintBoard()

        # start algorithm timer
        self.start = timeit.default_timer()

        while self.board.running == True:
            # place cars in initial configuration
            self.place_car_init()

            # take first path from the queue
            path = moves.get()

            # place cars corresponding to chosen path
            self.place_car_current(path)
            
            # check if currently loaded gameboard has previously been loaded, excluding start config. Skip if necessary 
            if self.board.noprintBoard() in self.board.history and self.board.noprintBoard() != startposion: 
                continue
            else: 
                self.board.history.append(self.board.noprintBoard())

            # check movable directions for each car and keep them in a list
            # these are the children of the current path
            moving_cars = self.check_car_movement()

            for i in range(0, len(moving_cars), 2):
                # combine children and parent path and add in queue
                move = moving_cars[i] + moving_cars[i + 1]
                put = path + move
                moves.put(put)
                
                # check if game has ended
                self.check_endgame(move, path)

        # stop algorithm timer
        self.stop = timeit.default_timer()

        # return runtime and found pathlength
        return self.stop - self.start, len(path)/2

    def place_car_init(self): 
        """Sets the cars to the original start configuration."""
        self.board.place_car(self.board._cars_init)
        self.board.cars = pickle.loads(pickle.dumps(self.board._cars_init))

    def place_car_current(self, path): 
        """Sets the cars to the configuration as described by the path
        
        Read through the path, determines which car should move in 
        what direction and move car accordingly. 
        """
        for i in range(0, len(path), 2):
            if path[i + 1] == 'L':
                self.board.moveCarLeft(path[i])
            elif path[i + 1] == 'R':
                self.board.moveCarRight(path[i])
            elif path[i + 1] == 'U':
                self.board.moveCarUp(path[i])
            elif path[i + 1] == 'D':
                self.board.moveCarDown(path[i])
    
    def check_car_movement(self): 
        """Check in which directions cars can move. 

        Move through the cars in self.board.cars. 
        Check if they can move left, right, up or down
        and add their name + direction to moving_cars list. 
        If the Red car (X) can move and end the game, just end the game. 
        """
        moving_cars = []
        for car in self.board.cars:
            if car._orientation == "V":  
                # if the cell below car is empty, car can move down
                if self.board.gameboard[car.row + car._length][car.column] == "0":
                    moving_cars.append(car._name)
                    moving_cars.append('D')
                # if cell above car is empty, car can move up
                if self.board.gameboard[car.row - 1][car.column] == "0":
                    moving_cars.append(car._name)
                    moving_cars.append('U')
            if car._orientation == "H":  
                # if cell on right side of car is empty, car can move right
                if self.board.gameboard[car.row][car.column + car._length] == "0":
                    moving_cars.append(car._name)
                    moving_cars.append('R')
                # if cell on left side of car is empty, car can move left
                if self.board.gameboard[car.row][car.column - 1] == "0":
                    moving_cars.append(car._name)
                    moving_cars.append('L')
        return moving_cars


    def check_endgame(self, move, path): 
        """Check if game has ended."""
        if move == "XR":
            self.board.moveCarRight('X')
            # set car variable to the red car which is always the last in the cars list
            car = self.board.cars[-1]
            # check if cell to the right of red car is the exit and end game if needed
            if self.board.gameboard[car.row][car.column + car._length] == "2":
                print("Path:", path + move)
                self.board.stop = timeit.default_timer()
                print("Time", self.board.stop - self.board.start, "seconds")
                self.board.running = False
                print("How many steps: ", len(path + move) / 2)
            else:
                self.board.moveCarLeft('X')