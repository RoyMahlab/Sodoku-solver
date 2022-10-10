from sodoku_solver import SODOKU_SOLVER
import numpy as np


n = 3 # depending on sodoku size N**2 X N**2
board = np.array([[0, 0, 0, 0, 0, 0, 4, 0, 0],  # empty table at the bottom
                  [0, 5, 0, 3, 0, 0, 7, 0, 1],
                  [3, 0, 0, 0, 0, 2, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0, 0, 4, 0],
                  [0, 6, 0, 0, 0, 0, 0, 2, 0],
                  [0, 0, 7, 0, 0, 9, 1, 0, 6],
                  [0, 0, 9, 0, 8, 0, 0, 0, 0],
                  [0, 7, 0, 2, 0, 0, 3, 0, 5],
                  [0, 0, 0, 0, 0, 0, 0, 6, 0]])

sod_sol = SODOKU_SOLVER(board, n)
ro, co = sod_sol.find_next_place_on_board(0, 0)
print(board) if sod_sol.insert_new_num(ro, co) else print('didnt work')


# Board = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0, 0]])