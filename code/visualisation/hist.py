from unicodedata import name
import pandas as pd
from pkg_resources import run_script
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

class Hist():
    """Hist class required to run main.py"""
    def __init__(self, dimensions, puzzle_number, name, runs, output):
        self.dimensions = dimensions
        self.puzzle_number = puzzle_number
        self.name = name
        self.runs = runs 
        self.output = output

    def easyhistloop(self): 
        """Easy way to make histograms of each puzzle number."""

        # load correct .csv file
        Rushhour_df = pd.read_csv(f"gameboards/Rushhour{self.dimensions}x{self.dimensions}_{self.puzzle_number}.csv")

        # create usable algorithm objects
        game = Board(self.dimensions)
        semi_random = Semi_random(game, hill=False)
        bfs = BFS(game)
        bfs_plus = BFS_plus(game)
        bfs_plus_prune = BFS_plus_prune(game)
        hill = Hill(game)

        algorithm_obj = eval(self.name)
        algorithm_func = self.name

        # setting up the board
        game.load_cars(Rushhour_df)
        game.place_car(game.cars)
        game.printBoard()

        def alg_loop(self):
            """Function to loop chosen algorithm. Results can be used to create histogram"""

            # turn printing off
            old_stdout = sys.stdout
            sys.stdout = open(os.devnull, "w")

            times = []
            moves = []
            for i in range(self.runs): 
                game.running = True
                # for each iteration, run chosen algorithm and save runtime & moves
                time, move = getattr(algorithm_obj, algorithm_func)()
                times.append(time)
                moves.append(move)
            nbins = 50

            # add found values to self.output dictionary
            self.output["Name"].append(f"Puzzle: {self.dimensions}x{self.dimensions}-{self.puzzle_number} - Algorithm: {self.name}")
            self.output["Min time"].append(round(min(times), 2))
            self.output["Max time"].append(round(max(times), 2))
            self.output["Mean time"].append(round(np.mean(times), 2))
            self.output["SD time"].append(round(np.std(times), 2))
            self.output["Min moves"].append(round(min(moves), 2))
            self.output["Max moves"].append(round(max(moves), 2))
            self.output["Mean moves"].append(round(np.mean(moves), 2))
            self.output["SD moves"].append(round(np.std(moves), 2))
            self.output["Tot runtime"].append(round(game.stop - game.start, 2))

            histogram_print(self, times, moves, nbins)

            # turn printing on
            sys.stdout = old_stdout


        def histogram_print(self, times, moves, nbins):
            """Creates and saves the histogram"""
            # draw moves histogram
            plt.hist(moves, range = [min(moves), max(moves)], bins=nbins)
            plt.title(f"Puzzle: {self.dimensions}x{self.dimensions}-{self.puzzle_number} | Algorithm: {self.name}")
            plt.figtext(0.01, 0.01, f"Min: {round(min(moves), 2)}, Max: {round(max(moves), 2)}, Mean: {round(np.mean(moves), 2)}, SD: {round(np.std(moves), 2)}, N: {self.runs}, Tot. time: {round(game.stop - game.start, 2)}s", fontsize=6)
            plt.xlabel(f"# of Moves", horizontalalignment = 'right', x = 1)
            plt.ylabel(f"Count")
            plt.grid()
            plt.savefig(f"figures/Puzzle: {self.dimensions}x{self.dimensions}-{self.puzzle_number} - Algorithm: {self.name} - moves")
            plt.clf()

            # draw times histogram
            plt.hist(times, range = [min(times), max(times)], bins=nbins)
            plt.title(f"Puzzle: {self.dimensions}x{self.dimensions}-{self.puzzle_number} | Algorithm: {self.name}")
            plt.figtext(0.01, 0.01, f"Min: {round(min(times), 2)}, Max: {round(max(times), 2)}, Mean: {round(np.mean(times), 2)}, SD: {round(np.std(times), 2)}, N: {self.runs}, Tot. time: {round(game.stop - game.start, 2)}s", fontsize=6)
            plt.xlabel(f"Runtime (s)", horizontalalignment = 'right', x = 1)
            plt.ylabel(f"Count")
            plt.grid()
            plt.savefig(f"figures/Puzzle: {self.dimensions}x{self.dimensions}-{self.puzzle_number} - Algorithm: {self.name} - time")
            plt.clf()

        # initiate histogram function
        alg_loop(self)

        # print end-game board and write self.output
        game.printBoard()
        game.writeOutput()