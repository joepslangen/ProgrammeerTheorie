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


def easyhistloop(dimensions, puzzle_number, name, runs, output): 
    """Easy way to make histograms of each puzzle number."""

    # load correct .csv file
    Rushhour_df = pd.read_csv(f"gameboards/Rushhour{dimensions}x{dimensions}_{puzzle_number}.csv")

    # create usable algorithm objects
    game = Board(dimensions)
    semi_random = Semi_random(game, hill=False)
    bfs = BFS(game)
    bfs_plus = BFS_plus(game)
    bfs_plus_prune = BFS_plus_prune(game)
    hill = Hill(game)

    algorithm_obj = eval(name)
    algorithm_func = name

    # setting up the board
    game.load_cars(Rushhour_df)
    game.place_car(game.cars)
    game.printBoard()

    def alg_loop():
        """Function to loop chosen algorithm. Results can be used to create histogram"""

        # turn printing off
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, "w")

        times = []
        moves = []
        for i in range(runs): 
            game.running = True
            # for each iteration, run chosen algorithm and save runtime & moves
            time, move = getattr(algorithm_obj, algorithm_func)()
            times.append(time)
            moves.append(move)
        nbins = 50

        # add found values to output dictionary
        output["Name"].append(f"Puzzle: {dimensions}x{dimensions}-{puzzle_number} - Algorithm: {name}")
        output["Mean time"].append(round(np.mean(times), 2))
        output["Mean moves"].append(round(np.mean(moves), 2))

        histogram_print(times, moves, nbins)

        # turn printing on
        sys.stdout = old_stdout


    def histogram_print(times, moves, nbins):
        """Creates and saves the histogram"""
        # draw moves histogram
        plt.hist(moves, range = [min(moves), max(moves)], bins=nbins)
        plt.title(f"Puzzle: {dimensions}x{dimensions}-{puzzle_number} | Algorithm: {name}")
        plt.figtext(0.01, 0.01, f"Min: {round(min(moves), 2)}, Max: {round(max(moves), 2)}, Mean: {round(np.mean(moves), 2)}, SD: {round(np.std(moves), 2)}, N: {runs}, Tot. time: {round(game.stop - game.start, 2)}s", fontsize=6)
        plt.xlabel(f"# of Moves", horizontalalignment = 'right', x = 1)
        plt.ylabel(f"Count")
        plt.grid()
        plt.savefig(f"figures/Puzzle: {dimensions}x{dimensions}-{puzzle_number} - Algorithm: {name} - moves")
        plt.clf()

        # draw times histogram
        plt.hist(times, range = [min(times), max(times)], bins=nbins)
        plt.title(f"Puzzle: {dimensions}x{dimensions}-{puzzle_number} | Algorithm: {name}")
        plt.figtext(0.01, 0.01, f"Min: {round(min(times), 2)}, Max: {round(max(times), 2)}, Mean: {round(np.mean(times), 2)}, SD: {round(np.std(times), 2)}, N: {runs}, Tot. time: {round(game.stop - game.start, 2)}s", fontsize=6)
        plt.xlabel(f"Runtime (s)", horizontalalignment = 'right', x = 1)
        plt.ylabel(f"Count")
        plt.grid()
        plt.savefig(f"figures/Puzzle: {dimensions}x{dimensions}-{puzzle_number} - Algorithm: {name} - time")
        plt.clf()

    # initiate histogram function
    alg_loop()

    # print end-game board and write output
    game.printBoard()
    game.writeOutput()


output = {"Name": [], "Mean time": [], "Mean moves": []}
for i in range(len(dimensions_list)):
    easyhistloop(dimensions = dimensions_list[i], puzzle_number = puzzle_number_list[i], name = "semi_random", runs = 10, output = output)

# write output
output = pd.DataFrame(output)
output.to_csv('output/compare.csv')