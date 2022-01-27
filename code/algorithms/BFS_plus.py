from collections import deque
import pickle 
import timeit


class BFS_plus(): 
    """
    Define function for breadth first algorithm. 
    """
    def __init__(self, board): 
        self.board = board
    
    """
    Define function for breadth first algorithm with heuristics
    """
    def bfs_plus(self):
        """
        Creation of the BFS queue moves and required variables containing the path, 
        the next possible states and the start configuration of the board. 
        """
        moves = deque()
        moves.appendleft("")
        path = ""
        startposion = self.board.noprintBoard()

        while self.board.running == True:
            """
            Place cars in initial configuration
            """
            self.place_car_init()

            """
            Take the first state from the queue and print
            path length. 
            """
            path = moves.popleft()

            """
            Place cars in configuration as states in the path
            """
            self.place_car_current(path)
            
            """
            Check if the currently loaded gameboard has previously been loaded,
            excluding the start configuration. Continue and add to history or skip
            this board.
            """
            if self.board.noprintBoard() in self.board.history and self.board.noprintBoard() != startposion: 
                continue
            else: 
                self.board.history.append(self.board.noprintBoard())

            """
            Check which car can move in which directions 
            and keep the info in a list
            """
            moving_cars = self.check_car_movement()

            """
            Go through with the BFS algorithm while applying heuristics
            """
            moves = self.heuristics(moving_cars, path, moves)

    def place_car_init(self): 
        """
        Set the cars to the original start configuration and create
        a deep copy of this state. 
        """
        self.board.place_car(self.board._cars_init)
        self.board.cars = pickle.loads(pickle.dumps(self.board._cars_init))
    
    def place_car_current(self, path): 
        """
        Read through the chosen path. 
        Determine car name and which direction to move in. 
        Move car in correct directions to update game board. 
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
        """
        Move through the cars in self.board.cars. 
        Check if they can move left, right, up or down
        and add their name + direction to moving_cars list. 
        If the Red car (X) can move and end the game, just end the game. 
        """
        moving_cars = []
        for car in self.board.cars:
            if car._orientation == "V":  
                if self.board.gameboard[car.row + car._length][car.column] == "0":
                    moving_cars.append(car._name)
                    moving_cars.append('D')
                if self.board.gameboard[car.row - 1][car.column] == "0":
                    moving_cars.append(car._name)
                    moving_cars.append('U')
            if car._orientation == "H":  
                if self.board.gameboard[car.row][car.column + car._length] == "0":
                    moving_cars.append(car._name)
                    moving_cars.append('R')
                if self.board.gameboard[car.row][car.column - 1] == "0":
                    moving_cars.append(car._name)
                    moving_cars.append('L')
        return moving_cars

    def heuristics(self, moving_cars, path, moves): 
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
        prio1 = deque("")
        prio2 = deque("")
        prio3 = deque("")
        for i in range(0, len(moving_cars), 2):
            move = moving_cars[i] + moving_cars[i + 1]
            put = path + move
            if moving_cars[i] == "X" and moving_cars[i + 1] == "R": 
                prio1.appendleft(put)
            elif moving_cars[i + 1] == "L" and moving_cars[i] != "X": 
                prio2.appendleft(put)
            elif moving_cars[i + 1] == "U" or moving_cars[i + 1] == "D": 
                prio3.appendleft(put)
            else:
                moves.append(put)
                
            self.check_endgame(move, path)
        """
        Combine the priority queues with the normal queue 
        to feed to the next cycle of the bfs algorithm. 
        """
        moves = prio1 + prio2 + prio3 + moves
        return moves

    def check_endgame(self, move, path): 
        """
        Again a end-game check function. 
        """
        if move == "XR":
            self.board.moveCarRight('X')
            car = self.board.cars[-1]
            if self.board.gameboard[car.row][car.column + car._length] == "2":
                print("Path:", path + move)
                self.board.stop = timeit.default_timer()
                print("Time", self.board.stop - self.board.start, "seconds")
                self.board.running = False
                print("How many steps: ", len(path + move) / 2)
            else:
                self.board.moveCarLeft('X')
