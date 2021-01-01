import matplotlib.pyplot as plt
import numpy as np
from chess_objects import *
from plot import *


start_position = (1,4)
my_board = ChessBoard(start=start_position)
my_board.fill_board()
plot(my_board)