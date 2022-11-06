from cmu_cs3_graphics import *
import random

"""
Each clearing of rows increases the speed of the falling pieces.
"""


def onAppStart(app):
    newGame(app)


def newGame(app):

    app.rows = 10
    app.cols = 10

    app.boardLeft = app.width / 8
    app.boardTop = 1.5 * app.height / 8
    app.boardWidth = 6 * app.width / 8
    app.boardHeight = 6 * app.height / 8

    app.cellBorderWidth = 2

    app.message = "Welcome to Tetris!"
    app.score = 0
    app.stepsPerSecond = 20
    app.steps = -4  # Allows for a pause to see tetromino in the beginning
    app.paused = False
    app.backgroundColor = "white"
    app.gameOver = False

    # Create the board:
    app.board = [[None] * app.cols for row in range(app.rows)]

    loadTetrisPieces(app)
    loadNextPiece(app)


def loadTetrisPieces(app):
    # Seven "standard" pieces (tetrominoes)
    iPiece = [[True, True, True, True]]
    jPiece = [[True, False, False], [True, True, True]]
    lPiece = [[False, False, True], [True, True, True]]
    oPiece = [[True, True], [True, True]]
    sPiece = [[False, True, True], [True, True, False]]
    tPiece = [[False, True, False], [True, True, True]]
    zPiece = [[True, True, False], [False, True, True]]
    app.tetrisPieces = [iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece]
    app.tetrisPieceColors = [
        "red",
        "yellow",
        "magenta",
        "pink",
        "cyan",
        "green",
        "orange",
    ]


def loadNextPiece(app):
    pieceIndex = random.randrange(len(app.tetrisPieces))

    app.piece = app.tetrisPieces[pieceIndex]
    app.pieceColor = app.tetrisPieceColors[pieceIndex]
    app.pieceTopRow = 1 - len(app.piece)
    app.pieceLeftCol = app.rows // 2 - (len(app.piece[0])) // 2 - 1


def redrawAll(app):
    drawRect(0, 0, app.width, app.height, fill=app.backgroundColor)
    drawLabel(app.message, app.width / 2, 0.5 * app.height / 8, size=16)
    drawLabel(f"Score: {app.score}", app.width / 2, app.height / 8, size=16)
    drawBoard(app)
    if not app.gameOver:
        drawPiece(app)
    drawBoardBorder(app)


def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            color = app.board[row][col]
            drawCell(app, row, col, color)


def drawPiece(app):
    rows = len(app.piece)
    cols = len(app.piece[0])

    for row in range(rows):
        for col in range(cols):
            if app.piece[row][col] == True and row + app.pieceTopRow >= 0:
                drawCell(
                    app, row + app.pieceTopRow, col + app.pieceLeftCol, app.pieceColor
                )


def drawBoardBorder(app):
    # draw the board outline (with double-thickness):
    drawRect(
        app.boardLeft,
        app.boardTop,
        app.boardWidth,
        app.boardHeight,
        fill=None,
        border="black",
        borderWidth=2 * app.cellBorderWidth,
    )


def drawCell(app, row, col, color):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    drawRect(
        cellLeft,
        cellTop,
        cellWidth,
        cellHeight,
        fill=color,
        border="black",
        borderWidth=app.cellBorderWidth,
    )


def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)


def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)


def onKeyPress(app, key):
    if key == "p":
        app.paused = not app.paused

    if not app.paused:
        if key == "up":
            rotatePieceClockwise(app)
        elif key == "space":
            hardDropPiece(app)

    if app.gameOver:
        if key == "r":
            newGame(app)


def onKeyHold(app, key):
    if not app.paused:
        if key == ["left"]:
            movePiece(app, 0, -1)
        elif key == ["right"]:
            movePiece(app, 0, +1)
        elif key == ["down"]:
            movePiece(app, +1, 0)


def movePiece(app, drow, dcol):
    # move the piece
    app.pieceTopRow += drow
    app.pieceLeftCol += dcol

    # check if piece is legal, undo the move if not
    if not pieceIsLegal(app):
        app.pieceTopRow -= drow
        app.pieceLeftCol -= dcol

        return False

    return True


def pieceIsLegal(app):
    rowsPiece = len(app.piece)
    colsPiece = len(app.piece[0])

    rowsBoard = len(app.board)
    colsBoard = len(app.board[0])

    for row in range(rowsPiece):
        for col in range(colsPiece):
            currentRow = row + app.pieceTopRow
            currentCol = col + app.pieceLeftCol
            if currentRow >= 0:
                if app.piece[row][col] == True:
                    if (
                        currentRow >= rowsBoard
                        or currentCol < 0
                        or currentCol >= colsBoard
                    ):
                        return False

                    if app.board[currentRow][currentCol] != None:
                        return False

    return True


def rotatePieceClockwise(app):
    # get the old piece along with its position
    oldPiece = app.piece
    oldTopRow = app.pieceTopRow
    oldLeftCol = app.pieceLeftCol

    newCols = oldRows = len(app.piece)
    newRows = oldCols = len(app.piece[0])

    # rotate the piece
    app.piece = rotate2dListClockwise(app.piece)

    # adjust the top row and left column of the new piece
    centerRow = oldTopRow + oldRows // 2
    app.pieceTopRow = centerRow - newRows // 2

    centerCol = oldLeftCol + oldCols // 2
    app.pieceLeftCol = centerCol - newCols // 2

    # check if the rotate piece is legal
    if not pieceIsLegal(app):
        app.piece = oldPiece
        app.pieceTopRow = oldTopRow
        app.pieceLeftCol = oldLeftCol


def rotate2dListClockwise(L):
    newCols = oldRows = len(L)
    newRows = oldCols = len(L[0])

    M = [[0 for i in range(newCols)] for j in range(newRows)]

    for oldRow in range(oldRows):
        for oldCol in range(oldCols):
            # We need to transpose L to M while reversing each row
            M[oldCol][-(oldRow + 1)] = L[oldRow][oldCol]

    return M


def hardDropPiece(app):
    while movePiece(app, +1, 0):
        pass


def onStep(app):
    if not app.paused:
        if app.steps % 10 == 0:
            takeStep(app)
        app.steps += 1


def takeStep(app):
    if not movePiece(app, +1, 0):
        # We could not move the piece, so place it on the board:
        placePieceOnBoard(app)
        removeFullRows(app)
        loadNextPiece(app)
    if not pieceIsLegal(app):
        app.paused = True
        app.gameOver = True
        app.message = "Game Over! Press r to restart."
        app.backgroundColor = "peachPuff"


def placePieceOnBoard(app):
    for row in range(len(app.piece)):
        for col in range(len(app.piece[0])):
            if app.piece[row][col] == True:
                app.board[row + app.pieceTopRow][
                    col + app.pieceLeftCol
                ] = app.pieceColor

    app.pieceTopRow = 1 - len(app.piece)
    app.pieceLeftCol = app.rows // 2 - (len(app.piece[0])) // 2 - 1


def removeFullRows(app):
    i = len(app.board) - 1
    scoreMultiplier = 0
    while i >= 0:
        row = app.board[i]
        if all(row):  # full row
            app.board.pop(i)
            app.board.insert(0, [None] * len(app.board[0]))

            scoreMultiplier += 1

            app.stepsPerSecond += 5
        else:
            i -= 1

    if scoreMultiplier > 0:
        app.score += 200 * scoreMultiplier - 100


def main():
    runApp(width=600, height=600)


main()
