import pandas as pd
import numpy as np


class ChessBoard:
    def __init__(self, start=(1,2)):
        self.routes = [np.array([(x,y)]) for x in range(8) for y in range(8)]
        self.startRoute = np.array([1,2])
        self.current_route = np.array([1,2])
        self.steps = [
                        np.array([-2,-1]),
                        np.array([-2,1]),
                        np.array([-1,-2]),
                        np.array([-1,2]),
                        np.array([1,-2]),
                        np.array([1,2]),
                        np.array([2,-1]),
                        np.array([2,1])
                        ]
        self.visited = [self.startRoute];
        self.available_routes = [route if any([route not in self.visited for route in self.routes])]

    def number_of_possible_steps(self):
        counter=0
        next_possible_steps = [(self.current_route+step) for step in self.steps if any(self.current_route+step in self.available_routes)]
        return len(next_possible_steps)

my_board = ChessBoard()

#print(set(my_board.routes))
print(my_board.startRoute)
print(my_board.current_route)
print(my_board.current_route+my_board.current_route)

print(my_board.number_of_possible_steps())