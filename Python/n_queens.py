import queue
import copy

class Queen_Board:
    def __init__(self, size, board = None):
        if board:
            self.board = copy.deepcopy(board)
        else:
            self.board = [[0 for i in range(size)] for i in range(size)]

    def fill_queen_movements(self, row, queen_x):
        spacing = row
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if (abs(queen_x - j) == abs(spacing) or j == queen_x) and self.board[i][j] != 2:
                    self.board[i][j] = 1
                elif i == row and self.board[i][j] != 2:
                    self.board[i][j] = 1
            spacing -= 1

    def place_queen_in_row(self, row, col):
        if row > len(self.board) - 1 or col > len(self.board) - 1:
            return 0
        
        if self.board[row][col] <= 0:
            self.board[row][col] = 2
            self.fill_queen_movements(row, col)
            return 1
        
        return -1
    
    def print_board(self):
        board_string = ""
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                board_string += f"{self.board[i][j]} "
            board_string += "\n"
        
        print(board_string)

def n_queens(n):
    root_solution = Queen_Board(n)
    
    q = queue.Queue()
    q.put((0, root_solution))

    while not q.empty():
        solution = q.get()
        row = solution[0]
        original_board = solution[1]

        for i in range(n):
            new_board = Queen_Board(n, original_board.board)
            b = new_board.place_queen_in_row(row, i)

            match b:
                case 1:
                    q.put((row + 1, new_board))
                case 0:
                    break
        
    return original_board

def main():
    board = n_queens(4)
    board.print_board()

if __name__ == "__main__":
    main()