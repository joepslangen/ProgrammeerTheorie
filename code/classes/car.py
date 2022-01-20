## Jasper Paul
## Helper file board_setup.py
## Defines the Car() class

#define class "Car()"
class Car():
    
    #initialize and set car properties
    #properties will be extracted from the .csv files
    def __init__(self, name, orientation, column, row, length):
        self._name = name
        self._orientation = orientation
        self._length = length
        self.column = column
        self.row = row