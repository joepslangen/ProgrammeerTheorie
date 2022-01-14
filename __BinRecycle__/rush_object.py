import pandas as pd

class Car():

    def __init__(self, name, orientation, length, row, col):
        self.name = name
        self.orientation = orientation
        self.length = length
        self.row = row
        self.col = col


class Board():

    def __init__(self):
        self.cars = []
        self.board = pd.DataFrame('.', index=range(6), columns=range(6))
    
    # Add cars to board
    def load_cars(self):
        cars = pd.read_csv('gameboards/Rushhour6x6_1.csv', index_col = False)

        for car in cars.iterrows():
            car_cur = Car(car[1]['car'], car[1]['orientation'], car[1]['length'], car[1]['row'], car[1]['col'])
            self.cars.append(car_cur)

            # If orientation is horizontal
            if car[1]['orientation'] == 'H':
                # Add car
                for i in range(car[1]['length']):
                    self.board.iloc[car[1]['row'] - 1, car[1]['col'] - 1 + i] = car[1]['car']
            
            # If orientation is vertical
            if car[1]['orientation'] == 'V':
                # Add car
                for i in range(car[1]['length']):
                    self.board.iloc[car[1]['row'] - 1 + i, car[1]['col'] - 1] = car[1]['car']


if __name__ == "__main__":
    print("start")

    game = Board()

    game.load_cars()

    print(game.board)


    