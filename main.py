"""
Importing required packages
"""
from ast import AsyncFunctionDef
import timeit
import pandas as pd
from code.algorithms.semi_random import Semi_random
from code.algorithms.BFS import BFS
from code.algorithms.BFS_plus import BFS_plus
from code.algorithms.BFS_plus_prune import BFS_plus_prune
from code.algorithms.hill import Hill
from code.classes.board import Board
import matplotlib.pyplot as plt
import numpy as np
import sys
import os
"""
Setting the dimensions and puzzle number to load correct configuration file 
"""
dimensions = 6
puzzle_number = 1
Rushhour_df = pd.read_csv(f"gameboards/Rushhour{dimensions}x{dimensions}_{puzzle_number}.csv")

"""
Creation of the different elements
"""
game = Board(dimensions)
semi_random = Semi_random(game)
bfs = BFS(game)
bfs_plus = BFS_plus(game)
bfs_plus_prune = BFS_plus_prune(game)
hill = Hill(game)

"""
Setting up the board to run algorithm
"""
game.load_cars(Rushhour_df)
game.place_car(game.cars)
game.printBoard()

"""
Run chosen algorithm
"""
#hill.hill()
#bfs_plus.bfs_plus()
#bfs.bfs()
#bfs_plus_prune.bfs_plus_prune()
#semi_random.semi_random()


"""
Set correct output
"""
game.printBoard()
game.writeOutput()


def histogram(name, algorithm_obj, algorithm_func, runs):

    """
    Turn printing off
    """
    old_stdout = sys.stdout
    sys.stdout = open(os.devnull, "w")

    times = []
    moves = []
    for i in range(runs): 
        game.running = True
        time, move = getattr(algorithm_obj, algorithm_func)()
        times.append(time)
        moves.append(move)
    nbins = 50

    """
    Turn printing back on
    """
    sys.stdout = old_stdout

    """
    Plotting of histogram
    """

    plt.hist(moves, range = [min(moves), max(moves)], bins=nbins)
    plt.title(f"Puzzle: {dimensions}x{dimensions}-{puzzle_number} | Algorithm: {name}")
    plt.figtext(0.01, 0.01, f"Mean: {round(np.mean(moves), 2)}, SD: {round(np.std(moves), 2)}, N: {runs}, Tot. time: {round(game.stop - game.start, 2)}s")
    plt.xlabel(f"# of Moves", horizontalalignment = 'right', x = 1)
    plt.ylabel(f"Count")
    plt.grid()
    plt.savefig(f"figures/Puzzle: {dimensions}x{dimensions}-{puzzle_number} - Algorithm: {name} - moves")
    plt.clf()

    plt.hist(times, range = [min(times), max(times)], bins=nbins)
    plt.title(f"Puzzle: {dimensions}x{dimensions}-{puzzle_number} | Algorithm: {name}")
    plt.figtext(0.01, 0.01, f"Mean: {round(np.mean(times), 2)}, SD: {round(np.std(times), 2)}, N: {runs}, Tot. time: {round(game.stop - game.start, 2)}s")
    plt.xlabel(f"Runtime (s)", horizontalalignment = 'right', x = 1)
    plt.ylabel(f"Count")
    plt.grid()
    plt.savefig(f"figures/Puzzle: {dimensions}x{dimensions}-{puzzle_number} - Algorithm: {name} - time")

histogram("semi-random", semi_random, "semi_random", 1000)