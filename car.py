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

    #define move functions (not in use yet)
    def move_up(self):
        self.row -=1

    def move_down(self):
        self.row += 1

    def move_right(self):
        self.column -= 1

    def move_right(self):
        self.column += 1