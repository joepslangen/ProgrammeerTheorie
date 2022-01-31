"""
Importing required packages
"""
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

dimensions_list = [6, 6, 6, 9, 9, 9]
puzzle_number_list = [1, 2, 3, 4, 5, 6]

def easyhistloop(dimensions, puzzle_number, output): 
    """
    Setting the dimensions and puzzle number to load correct configuration file 
    """

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

        output["Name"].append(f"Puzzle: {dimensions}x{dimensions}-{puzzle_number} - Algorithm: {name}")
        output["Mean time"].append(round(np.mean(times), 2))
        output["Mean moves"].append(round(np.mean(moves), 2))

        """
        Turn printing back on
        """
        sys.stdout = old_stdout

        """
        Plotting of histogram
        """

        plt.hist(moves, range = [min(moves), max(moves)], bins=nbins)
        plt.title(f"Puzzle: {dimensions}x{dimensions}-{puzzle_number} | Algorithm: {name}")
        plt.figtext(0.01, 0.01, f"Min: {round(min(moves), 2)}, Max: {round(max(moves), 2)}, Mean: {round(np.mean(moves), 2)}, SD: {round(np.std(moves), 2)}, N: {runs}, Tot. time: {round(game.stop - game.start, 2)}s", fontsize=6)
        plt.xlabel(f"# of Moves", horizontalalignment = 'right', x = 1)
        plt.ylabel(f"Count")
        plt.grid()
        plt.savefig(f"figures/Puzzle: {dimensions}x{dimensions}-{puzzle_number} - Algorithm: {name} - moves")
        plt.clf()

        plt.hist(times, range = [min(times), max(times)], bins=nbins)
        plt.title(f"Puzzle: {dimensions}x{dimensions}-{puzzle_number} | Algorithm: {name}")
        plt.figtext(0.01, 0.01, f"Min: {round(min(times), 2)}, Max: {round(max(times), 2)}, Mean: {round(np.mean(times), 2)}, SD: {round(np.std(times), 2)}, N: {runs}, Tot. time: {round(game.stop - game.start, 2)}s", fontsize=6)
        plt.xlabel(f"Runtime (s)", horizontalalignment = 'right', x = 1)
        plt.ylabel(f"Count")
        plt.grid()
        plt.savefig(f"figures/Puzzle: {dimensions}x{dimensions}-{puzzle_number} - Algorithm: {name} - time")
        plt.clf()

    histogram("semi-random", semi_random, "semi_random", 10)

    """
    Set correct output
    """
    game.printBoard()
    game.writeOutput()

output = {"Name": [], "Mean time": [], "Mean moves": []}
for i in range(len(dimensions_list)):
    easyhistloop(dimensions_list[i], puzzle_number_list[i], output)
output = pd.DataFrame(output)
output.to_csv('output/compare.csv')