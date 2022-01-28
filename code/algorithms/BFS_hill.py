import pickle 
from code.algorithms.semi_random import Semi_random
import copy
import sys
import os
import random


class BFS_hill(): 

    def __init__(self, board): 
        self.board = board

    def bfs_hill(self): 
        #semi_random = Semi_random(self.board)
        #path = semi_random.semi_random()
        

        path = [ "XRa", "XRb", "XRc", "XRd", "XRe"]
        print(self.path_check(path))
        del path[random.randint(0, len(path) - 1)]
        print(path)
        print(self.path_check(path))
        """
        old_stdout = sys.stdout
        #sys.stdout = open(os.devnull, "w")
        for i in range(len(path)): 
            move = path[i]
            path_copy[i] = "  "
            if self.path_check(path_copy) == True:
                print("Good run")
            else:
                path_copy[i] = move
                print("Bad run")

        sys.stdout = old_stdout

        print(path_copy)
        """
        

    def path_check(self, path):
        self.board.running = True
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
        if self.board.running == False: 
            return True
        else: 
            return False
            


