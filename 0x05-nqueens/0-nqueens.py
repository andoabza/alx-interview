#!/usr/bin/python3
'''n queens algorithm'''
import sys

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

if N < 4:
    print("N must be at least 4")
    sys.exit(1)

def solveNQ(N):
    '''solve N queens problem'''
    board = [-1 for i in range(N)]
    solveNQUtil(board, 0)

def solveNQUtil(board, col):
    '''solve N queens problem'''
    n = len(board)
    if col is n:
        printSolution(board)
        return
    for i in range(n):
        if isSafe(board, i, col):
            board[col] = i
            solveNQUtil(board, col + 1)
            board[col] = -1

def printSolution(board):
    '''print the solution'''
    n = len(board)
    result = []
    for i in range(n):
        result.append([i, board[i]])
    print(result)


def isSafe(board, row, col):
    '''check if a queen can be placed on board[row][col]'''
    n = len(board)
    for i in range(col):
        if board[i] is row or abs(i - col) is abs(board[i] - row):
            return False
    return True

solveNQ(N)