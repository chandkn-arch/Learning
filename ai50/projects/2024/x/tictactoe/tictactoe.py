"""
Tic Tac Toe Player
"""

import math
import copy 

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
   """ 
    xcount=0
    ocount=0
    for row in board:
        for cell in row:
            if cell == X:
                xcount +=1
            if cell == O:
                ocount +=1

    if xcount == 1 :
        return O
    elif xcount <= ocount:
        return X
    else :
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = set()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                action.add((i,j))
    return action

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    print ("board :",board)
    print("action :",action)
    if action not in actions(board):
        raise ValueError
    newboard =copy.deepcopy(board)
    newboard[action[0]][action[1]] = player(newboard)
    return newboard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    wins = [[(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]]

    for row_col in wins:
        xcheck=0
        ocheck=0
        for row,col in row_col:
            if board[row][col] == X:
                xcheck +=1
            if board[row][col] == O:
                ocheck +=1
        if xcheck == 3:
            return X
        if ocheck == 3:
            return O
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or not actions(board):
        return True
    else :
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    gamewinner = winner(board)
    if gamewinner == X :
        return 1
    elif gamewinner == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    # Optimization by hardcoding the first move
    if board == initial_state():
        return 0, 1

    currentplayer = player(board)
    bestvalue = float("-inf") if currentplayer == X else float("inf")

    for action in actions(board):
        newvalue = minimax_value(result(board, action), bestvalue)

        if currentplayer == X:
            newvalue = max(bestvalue, newvalue)

        if currentplayer == O:
            newvalue = min(bestvalue, newvalue)

        if newvalue != bestvalue:
            bestvalue = newvalue
            bestaction = action

    return bestaction

def minimax_value(board, bestvalue):
    """
    Returns the best value for each recursive minimax iteration.
    Optimized using Alpha-Beta Pruning: If the new value found is better
    than the best value then return without checking the others.
    """
    if terminal(board):
        return utility(board)

    currentplayer = player(board)
    value = float("-inf") if currentplayer == X else float("inf")

    for action in actions(board):
        newvalue = minimax_value(result(board, action), value)

        if currentplayer == X:
            if newvalue > bestvalue:
                return newvalue
            value = max(value, newvalue)

        if currentplayer == O:
            if newvalue < bestvalue:
                return newvalue
            value = min(value, newvalue)

    return value
