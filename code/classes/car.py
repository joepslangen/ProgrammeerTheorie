class Car():
    """Car class used to hold properties of cars"""
    def __init__(self, name, orientation, column, row, length):
        self._name = name
        self._orientation = orientation
        self._length = length
        self.column = column
        self.row = row