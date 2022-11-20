import copy
import itertools


def solveSudoku(board: list[list[int]]) -> list[list[int]]:
    boardCopy = copy.deepcopy(board)
    solvedByRule1 = solveSudokuRule1(boardCopy)
    for line in solvedByRule1:
        print(str(line).strip('[]'))
    print("\n")
    finalSolution = solveSudokuRule2(solvedByRule1)
    return finalSolution


def solveSudokuRule1(board: list[list[int]]) -> list[list[int]]:
    rows = len(board)
    cols = len(board[0])
    # base case
    if isSolvedSudoku(board):
        return board
    else:
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 0:
                    # check all possible values
                    for value in range(1, rows+1):
                        board[row][col] = value
                        # continue if board is legal
                        if isLegalSudoku(board):
                            return solveSudokuRule1(board)
                        else:
                            # backtracking step
                            board[row][col] = 0
        # after applying rule 1, this line will return the final state of the
        # board. It may be solved or contain some 0s to apply rule 2. This will
        # be taken care of in solveSudokuRule2.
        return board


def solveSudokuRule2(board: list[list[int]]) -> list[list[int]]:
    rows = len(board)
    cols = len(board[0])
    # base case: if board is actually a fully solved board
    if isSolvedSudoku(board):
        return board
    else:
        # search for 0s in each row
        for row in range(rows):
            rowList = board[row]
            if 0 in rowList:
                allPossibleNums = list(range(1, rows+1))
                numsLeft = [n for n in allPossibleNums if n not in rowList]
                # verify that number of 0s equals the number of numbers left
                if rowList.count(0) == len(numsLeft):
                    n = len(numsLeft)
                    print(list(itertools.permutations(numsLeft, n)))
                    for combination in itertools.permutations(numsLeft, n):  # type: ignore
                        locations = list()
                        for col in range(cols):
                            if board[row][col] == 0:
                                locations.append((row, col))
                        print(combination, locations)
                        for i in range(len(locations)):
                            row, col = locations[i]
                            board[row][col] = combination[i]
                        if isLegalSudoku(board):
                            return solveSudokuRule2(board)
                        else:
                            for row, col in locations:
                                board[row][col] = 0
        # search for 0s in each col
        for col in range(cols):
            colList = createColList(board, col)
            if 0 in colList:
                allPossibleNums = list(range(1, rows+1))
                numsLeft = [n for n in allPossibleNums if n not in colList]
                # verify that number of 0s equals the number of numbers left
                if colList.count(0) == len(numsLeft):                
                    n = len(numsLeft)
                    print(list(itertools.permutations(numsLeft, n)))
                    for combination in itertools.combinations(numsLeft, n):  # type: ignore
                        locations = list()
                        for row in range(rows):
                            if board[row][col] == 0:
                                locations.append((row, col))
                        print(combination, locations)
                        for i in range(len(locations)):
                            row, col = locations[i]
                            board[row][col] = combination[i]
                        if isLegalSudoku(board):
                            return solveSudokuRule2(board)
                        else:
                            for row, col in locations:
                                board[row][col] = 0
        # search for 0s in each block (remember, there are as many blocks as
        # rows and cols)
        for block in range(rows):
            blockList = createBlockList(board, block)
            if 0 in blockList:
                allPossibleNums = list(range(1, rows+1))
                numsLeft = [n for n in allPossibleNums if n not in blockList]
                # verify that number of 0s equals the number of numbers left
                if blockList.count(0) == len(numsLeft):
                    n = len(numsLeft)
                    print(list(itertools.permutations(numsLeft, n)))
                    for combination in itertools.permutations(numsLeft, n):  # type: ignore
                        blockSize = round(rows ** 0.5)
                        startRow = block // blockSize * blockSize
                        startCol = block % blockSize * blockSize
                        locations = list()
                        for drow in range(blockSize):
                            for dcol in range(blockSize):
                                row, col = startRow + drow, startCol + dcol
                                if board[row][col] == 0:
                                    locations.append((row, col))
                        print(combination, locations)
                        for i in range(len(locations)):
                            row, col = locations[i]
                            board[row][col] = combination[i]
                        if isLegalSudoku(board):
                            return solveSudokuRule2(board)
                        else:
                            for row, col in locations:
                                board[row][col] = 0
        return board


def isSolvedSudoku(grid):
    """Check if Sudoku grid is legal and all values are nonzero."""
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


def createColList(grid, col):
    return [grid[row][col] for row in range(len(grid))]


def isLegalCol(grid, col):
    return areLegalValues(createColList(grid, col))


def createBlockList(grid, block):
    n = len(grid)
    blockSize = round(n ** 0.5)
    startRow = block // blockSize * blockSize
    startCol = block % blockSize * blockSize
    values = []
    for drow in range(blockSize):
        for dcol in range(blockSize):
            row, col = startRow + drow, startCol + dcol
            values.append(grid[row][col])
    return values


def isLegalBlock(grid, block):
    return areLegalValues(createBlockList(grid, block))


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


def main():
    board = [[0, 6, 0, 5, 2, 0, 0, 0, 7],
             [0, 0, 0, 0, 0, 1, 0, 0, 0],
             [8, 0, 0, 0, 0, 0, 0, 4, 0],
             [0, 0, 6, 0, 0, 0, 5, 0, 0],
             [0, 0, 0, 9, 0, 0, 0, 0, 0],
             [0, 5, 0, 7, 3, 0, 0, 0, 2],
             [0, 3, 0, 0, 0, 9, 0, 0, 0],
             [0, 0, 4, 3, 1, 0, 0, 7, 0],
             [0, 0, 0, 0, 0, 6, 0, 0, 1]]
    solved = solveSudoku(board)
    for line in solved:
        print(str(line).strip('[]'))


main()
