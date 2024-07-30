from cmu_graphics import *

def isLegal(board, cell, val):
    return (rowIsLegal(board, cell, val) and colIsLegal(board, cell, val) and
           blockIsLegal(board, cell, val))

def rowIsLegal(board, cell, val):
    row = cell.row
    for col in range(len(board[0])):
        if col == cell.col:
            continue
        if board[row][col].value == val:
            return False
    return True

def colIsLegal(board, cell, val):
    col = cell.col
    for row in range(len(board)):
        if row == cell.row:
            continue
        if board[row][col].value == val:
            return False
    return True

def blockIsLegal(board, cell, val):
    size = len(board)
    blockSize = int(size ** 0.5)
    startRow = (cell.row//blockSize) * blockSize
    startCol = (cell.col//blockSize) * blockSize
    for row in range(startRow, startRow + blockSize):
        for col in range(startCol, startCol + blockSize):
            if row == cell.row and col == cell.col:
                continue
            if board[row][col].value == val:
                return False
    return True