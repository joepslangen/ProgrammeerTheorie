import pandas as pd
from code.visualisation.hist import Hist
import sys
import argparse

dimensions_list = [6, 6, 6, 9, 9, 9]
puzzle_number_list = [1, 2, 3, 4, 5, 6]
puzzle_dict = {1: 6, 2: 6, 3 : 6, 4: 9, 5: 9, 6: 9}

algorithm_names = {"semi_random", "hill", "bfs", "bfs_plus", "bfs_plus_prune"}

# start argparser
parser = argparse.ArgumentParser(description = "Run chosen algorithm on all puzzels and return histograms")

# add arguments name and runs
parser.add_argument("Name", metavar = "name", type = str, help = "Name of algorithm. Available algorithms: \n semi_random, hill, bfs, bfs_plus, bfs_plus_prune")
parser.add_argument("Runs", metavar = "runs", type = int, help = "Number of algorithm runs per puzzle")
parser.add_argument("-p", metavar = "--puzzle_number", type = int, help = "Number of requested puzzle")

# extract arguments
args = parser.parse_args()

# set name and runs variables to given args
name = args.Name

# check if given algorithm name is correct
if name not in algorithm_names: 
    print("Please choose one of the avaiable algorithm names: \n semi_random, hill, bfs, bfs_plus, bfs_plus_prune" )
    sys.exit()

runs = args.Runs
puzzle_number = args.p
# check if given puzzle number is available
if puzzle_number != None and puzzle_number not in puzzle_number_list: 
    print("Please choose a puzzle number from 1 to 6")
    sys.exit()
if puzzle_number != None: 
    dimensions = puzzle_dict[puzzle_number]

# start ouput dictionary
output = {"Name": [], "Min time": [], "Max time" : [], "Mean time": [], "SD time": [], "Min moves" : [], "Max moves" : [], "Mean moves": [], "SD moves" : [], "Tot runtime": []}

# loop through every puzzle and run the algorithm the requested number of times
if puzzle_number == None: 
    for i in range(len(dimensions_list)):
        hist = Hist(dimensions = dimensions_list[i], puzzle_number = puzzle_number_list[i], name = name, runs = runs, output = output)
        hist.easyhistloop()
# is specific puzzle is requested, only loop over that one
else: 
    hist = hist = Hist(dimensions = dimensions, puzzle_number = puzzle_number, name = name, runs = runs, output = output)
    hist.easyhistloop()

# write output
output = pd.DataFrame(output)
output.to_csv(f"output/{name}.csv")