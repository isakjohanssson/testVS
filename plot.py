# Contains a plot function
import matplotlib.pyplot as plt
import numpy as np

def plot(my_board):
    size = 8
    chessboard = np.zeros((size,size))
    chessboard[1::2,0::2] = 1
    chessboard[0::2,1::2] = 1
    plt.imshow(chessboard, cmap='binary')

    for route in my_board.visited:
        i, j = route.position
        plt.text(i, j, '♘', fontsize=20, ha='center', va='center', color='black' if (i - j) % 2 == 0 else 'white')
        plt.draw()
        #plt.pause(0.5)