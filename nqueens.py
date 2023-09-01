def printSolution(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end="")
        print()

def isSafe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col, n):
    if col >= n:
        return True

    for i in range(n):
        if isSafe(board, i, col, n):
            board[i][col] = 1
            if solve(board, col+1, n):
                return True
            board[i][col] = 0
    return False

def main():
    n = 4
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    if not solve(board, 0, n):
        print("Solution does not exist")
        return False
 
    printSolution(board, n)
    return True

main()