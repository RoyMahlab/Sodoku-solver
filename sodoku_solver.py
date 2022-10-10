
class SODOKU_SOLVER:
    def __init__(self, board, n):
        self.board = board
        self.n = n

    def insert_new_num(self, row, col):
        for i in range(1, self.n ** 2 + 1):
            if not self.check_board(row, col, i): continue
            self.board[row, col] = i
            if row == self.n ** 2 - 1 and col == self.n ** 2 - 1: return True
            n_row, n_col = self.find_next_place_on_board(row, col)
            if n_row is None and n_col is None: return True
            if self.insert_new_num(n_row, n_col): return True
            self.board[row, col] = 0
        return False

    def find_next_place_on_board(self, row, col):
        i, j = row, col
        while True:
            while j != self.n ** 2:
                if self.board[i, j] == 0: return i, j
                j += 1
            if i == self.n ** 2 - 1: return None, None
            i += 1
            j = 0

    def check_board(self, row, col, i):
        if not self.check_row_col(row, col, i): return False
        if not self.check_square(row, col, i): return False
        return True

    def check_row_col(self, row, col, i):
        if any(self.board[row, :] == i) or any(self.board[:, col] == i): return False
        return True

    def check_square(self, row, col, k):
        s_row, s_col = (row // self.n) * self.n, (col // self.n) * self.n
        for i in range(s_row, s_row + self.n):
            for j in range(s_col, s_col + self.n):
                if self.board[i, j] == k: return False
        return True
