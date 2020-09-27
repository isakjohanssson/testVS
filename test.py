import matplotlib.pyplot as plt
import numpy as np

size = 8
chessboard = np.zeros((size,size))

chessboard[1::2,0::2] = 1
chessboard[0::2,1::2] = 1

plt.imshow(chessboard, cmap='binary')

for _ in range(20):
    i, j = np.random.randint(0, 8, 2)
    plt.text(i, j, '♕', fontsize=20, ha='center', va='center', color='black' if (i - j) % 2 == 0 else 'white')

plt.show()