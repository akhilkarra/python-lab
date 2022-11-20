import copy


def solveMiniSudoku(board):
    boardCopy = copy.deepcopy(board)
    return solveMiniSudokuCopy(boardCopy)


def solveMiniSudokuCopy(boardCopy):
    rows = len(boardCopy)
    cols = len(boardCopy[0])
    for line in boardCopy:
        print(line)
    print("\n")
    # base case
    if isSolvedSudoku(boardCopy):
        return boardCopy
    else:
        for row in range(rows):
            for col in range(cols):
                if boardCopy[row][col] == 0:
                    # check all possible values
                    for value in range(1, rows+1):
                        boardCopy[row][col] = value
                        # continue if board is legal
                        if isLegalSudoku(boardCopy):
                            return solveMiniSudokuCopy(boardCopy)
                        # backtracking step
                        boardCopy[row][col] = 0
        return boardCopy


def isSolvedSudoku(grid):
    if not isLegalSudoku(grid):
        return False
    else:
        rows, cols = len(grid), len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    return False
        return True


def isLegalSudoku(grid):
    rows, cols = len(grid), len(grid[0])
    if rows != 4 and rows != 9:
        return False
    if rows != cols:
        return False
    for row in range(rows):
        if not isLegalRow(grid, row):
            return False
    for col in range(cols):
        if not isLegalCol(grid, col):
            return False
    blocks = rows
    for block in range(blocks):
        if not isLegalBlock(grid, block):
            return False
    return True


def isLegalRow(grid, row):
    return areLegalValues(grid[row])


def isLegalCol(grid, col):
    columnList = [grid[row][col] for row in range(len(grid))]
    return areLegalValues(columnList)


def isLegalBlock(grid, block):
    n = len(grid)
    blockSize = round(n ** 0.5)
    startRow = block // blockSize * blockSize
    startCol = block % blockSize * blockSize
    values = []
    for drow in range(blockSize):
        for dcol in range(blockSize):
            row, col = startRow + drow, startCol + dcol
            values.append(grid[row][col])
    return areLegalValues(values)


def areLegalValues(L):
    n = len(L)
    seen = set()
    for value in L:
        if not isinstance(value, int):
            return False
        if value < 0 or value > n:
            return False
        if value != 0 and value in seen:
            return False
        seen.add(value)
    return True


def testSolveMiniSudoku():
    print("Testing...")
    board1 = [[4, 3, 0, 0],
              [1, 2, 3, 0],
              [0, 0, 2, 0],
              [2, 1, 0, 0]]
    solved1 = [[4, 3, 1, 2],
               [1, 2, 3, 4],
               [3, 4, 2, 1],
               [2, 1, 4, 3]]
    board1Copy = copy.deepcopy(board1)
    assert (solveMiniSudoku(board1) == solved1)
    assert (board1 == board1Copy)  # verify we do not mutate the original board
    board2 = [[3, 0, 0, 2],
              [0, 4, 1, 0],
              [0, 3, 2, 0],
              [4, 0, 0, 1]]
    solved2 = [[3, 1, 4, 2],
               [2, 4, 1, 3],
               [1, 3, 2, 4],
               [4, 2, 3, 1]]
    board2Copy = copy.deepcopy(board2)
    assert (solveMiniSudoku(board2) == solved2)
    assert (board2 == board2Copy)  # verify we do not mutate the original board
    print("Passed")


def main():
    testSolveMiniSudoku()


main()
