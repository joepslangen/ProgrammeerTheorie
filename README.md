# Rush Hour - Programmeertheorie 01-2022
## Table of contents
* [General Info](#general-info)
* [Requirements](#requirements)
* [Usage](#usage)
* [Contributors](#contributors)



## General info
Rush hour is a sliding block logic game. You have to battle the gridlock as you slide the blocking vehicles out of the way for the red car to exit. Originally the game is played on a 6x6 grid with you to 16 vehicles. Cars of different length and colour block the red cars' path to the exit. The goal of the game is to get only the red car out through the exit by sliding other vehicles out of its way, without rotating them. 

In this repo we present a an algorithm able to solve rush hour games, not only on a 6x6 but up to 12x12 grid. 

## Requirements
Before running, make sure you have the required python packages installed. 
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the following packages:
```bash
pip install pandas
pip install numpy
pip install termcolor
pip install random 
pip install timeit
```

## Usage
In main.py set the desired dimensions and puzzle number: 


```python
dimensions = 6
puzzle_number = 1
```
Finally run the main.py file:
```bash 
python3 main.py
```
## Contributors
* Eva
* Joep 
* Jasper
