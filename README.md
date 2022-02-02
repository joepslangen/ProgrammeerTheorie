# Rush Hour - Programmeertheorie 01-2022
## Table of contents
* [General Info](#general-info)
* [Requirements](#requirements)
* [Usage](#usage)
* [Structure](#structure)
* [Contributors](#contributors) 



## General info
Rush Hour is a sliding block logic game where blocks represent cars stuck in traffic. Invented by Nob Yoshigahara in 1970 as a childrens game, but nowadays also very popular in the realm of computer science. Originally the game is played on a 6x6 grid with up to 16 vehicles. Cars of different length and colour block the red cars' path to the exit. Moreover, cars can only move up and down or left and right. The goal of the game is to get only the red car out through the exit by sliding other vehicles out of its way, without rotating them. 

### State Space
Rush hour is a NP-hard problem. NP-hard problems are the most difficult problems in computer science. They are both hard to solve and hard to check. Furthermore, the state space can be huge. The state space is a set of all the possible configurations of the game. On a normal 6x6 grid assuming car lenghts are 1 block and all blocks are either full or empty. The state space is 2^(6x6) = 6.9 * 10^9 possible configurations. The algorithm has to check all these possible configurations to find a solution which can take a lot of time. Luckily, there are ways to reduce the state space of the game so it is possible to solve this problem using a normal laptop.

![rush_hour_board](https://user-images.githubusercontent.com/90269748/151796919-3fa5c988-74ea-486c-9b36-08c6178d9c87.png)

In this repo we present four python algorithms able to solve Rush Hour games. 

## Requirements
Before running, make sure you have the required python packages installed. 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages:
```bash
pip install numpy
pip install pandas
pip install pickle
pip install random 
pip install termcolor
pip install timeit
```

## Usage
In main.py set the desired dimensions, puzzle number and algorithm: 


```python
dimensions = 6
puzzle_number = 1

# Available Algorithms: 
semi_random.semi_random()
hill.hill()
bfs.bfs()
bfs_plus.bfs_plus()
```
Finally run the main.py file:
```bash 
python3 main.py
```

## Structure 

The following list describes the most important folders and files and where to find them in the repository:

* /code: contains all the code from the project
  * /code/algorithms: contains the code for the algorithms
  * /code/classes: contains the classes necessary to run this project 
  * /code/visualisation: contains a pygame visualisation of Rush Hour 
* /figures: contains all the graph results of the algorithms
* /output: contains csv files with the results displayed in the graphs

For more in depth information on the algorithms see [algorithms](https://github.com/joepslangen/ProgrammeerTheorie/blob/main/code/algorithms/algorithms.md) in the algorithms folder.

## Contributors
* Eva
* Joep 
* Jasper
