import matplotlib.pyplot as plt
import numpy as np
from chess_objects import *
from plot import *

size = 8
start_position = (1,2)
my_board = ChessBoard(start=start_position)
my_board.fill_board()
plot(size, my_board)