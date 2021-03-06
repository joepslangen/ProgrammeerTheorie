## Introduction

In main.py, there are four different algorithms to choose from: 1. Semi-Random, 2. Hillclimber-esque, 3. Breadth First Search, 4. Breadth First Search with Heuristics. Each algorithm should find a solution to the given problem depending on the goal. For instance, Breadth First Search will be extremely slow, but will find an optimal solution, while the others will return a less optimal solution in a shorter time frame. Therefore, all the algorithms make a trade-off between time and efficiency.

## Semi-random

The semi-random algorithm is the most simplistic algorithm available. It requires the board object, made by the Board() class, to be initialized. When the semi-random algorithm is called it creates an empty list which will contain the cars and their moving direction. Then, as long as the red car has not reached the exit, it will choose a random car on the board and will try to move it to the left. If movement in this direction is allowed, the car will move and the car-name plus moving direction will be saved in the list. If the car can not move it will skip this step. A new random car is chosen and will be moved to the right if possible. The same mechanics apply to the up and down directions. When by chance the red car reaches the exit, the game will end and the list containing the movements will be returned.

NOTE: Although the car which will be moved is randomly chosen, the moving direction is fixed in a repeating pattern being: left, right, up & down.

Path: 'code/algorithms/semi_random.py'.

## Hillclimber-esque

The hillclimber algorithm is based on the semi-random algorithm and is also initialized with a board object. The hillclimber calls the semi-random algorithm to generate a solution. Number of moves, or path length, the semi-random algorithm returns are saved. It then resets the board to the initial configuration and uses the semi-random again to find a solution. If this solution has a shorter path length compared to the previously saved path, the new path will replace the old path. This will be repeated a hundred times in a for-loop. Finally the solution with the shortest path length will be returned.

NOTE: Since this algorithm is based on the semi-random, the obtained solutions will differ with every run.

Path: 'code/algorithms/hill.py'.

## Breadth First Search

The Breadth First Search (BFS) algorithm is the first "intelligent" algorithm and requires a board object to be initialized. The BFS runs until a valid solution is found. The BFS places the cars in their initial configuration and takes the first path from a path-queue containing different board configurations. The cars are placed in their correct positions according to the obtained path. If this configuration has been seen before, it will be skipped. Otherwise this configuration will be added to the history and the BFS continues. The BFS cycles through every car on the board to determine possible moving directions. For every move possible the new board configuration, or child, will be saved and added to the queue. The fist item from the queue is obtained and the BFS-loop starts over.

NOTE: The BFS will explore all board configurations possible with a certain number of moves. Eventually it will find the first possibility to end the game, with a certain number of moves. Thus finding the optimal solution. The drawback is that BFS will be quite slow.

Path: 'code/alogithms/BFS.py'.

## Breadth First Search with Heuristics

Finally there is the BFS with heuristics (BFS+). BFS+ functions similar to BFS, however some simple heuristics are introduced which change the way the queue is implemented. The heuristics will identify "good" and "bad" moves as follows. If the red car is able to move to the right, this indicates a "good" move. This move brings us closer to game-end and the children of this board configuration get priority over all other board configurations. These children will be placed at the front of the queue. A second "good" move is the placement of horizontal cars, other than the red car, to the left. This creates space on the right side of the board, which could help the red car find the exit faster. The children of these configurations where placed at the front of the queue, behind the children of the board placing the red car to the right. A third "good" move is the movement of vertical cars up and/or down. This clears up the horizontal-middle of the board which benefits the red car. Their children where placed behind the children of the second "good" move. Finally we are left with two "bad" moves, moving the red car to the left and/or moving other horizontal cars to the right. These moves are perceived as moves which worsen the current state of the game and will be placed at the back of the queue.

NOTE: BFS+ is essentially a combination of breadth first search and depth first search (DFS). Starting out as BFS and turning into selective-DFS when bumping into an interesting board. It continues with interesting boards until no more potentially "good" moves are possible, after which it returns to the point it left off and starts BFS again. Applying BFS+ is a guess, if the perceived "good" moves are actually good this algorithm will be significantly faster than BFS. However if the problem requires to move the red car to the left a few times, BFS+ might be slower since it perceives these moves as "bad".

Path: 'code/algorithms/BFS_plus'.

## Conclusion

The four algorithms all find a solution. While semi-random and hillclimber-esque find a sub-optimal solution extremely fast on average in less than 0,02 seconds. Breadth First Search finds an optimal solution, but this can take hours. Therefore, Breadth First Search with Heuristics finds a middle ground between effiency and time. It finds a better solution than the hillclimber-esque and in less time than the Breadth First Search, however it all depends on the type of heuristics and the configuration of the board. 

