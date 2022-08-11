import random

player = 'x'
validMoves = [1,2,3,4,5,6,7,8,9]
isGameOver = False

board = [
    [[" "], [" "], [" "]],
    [[" "], [" "], [" "]],
    [[" "], [" "], [" "]],
]

def printBoard(board):
    i = 0
    for row in board:
        print(f" {row[0][0]} | {row[1][0]} | {row[2][0]}")
        i += 1
        if i < 3:
            print(f"---+---+---")

def convertMoveToTwoDimensionalArray(move):
    return [move//3, move%3]

def updateBoard(position, player):
    board[position[0]][position[1]] = player
    validMoves.remove(int(move))

def switchPlayer(player):
    if player == 'x':
        return 'o'
    else:
        return 'x'

def validateMove(move):
    if move in validMoves:
        return True
    return False

def playWithFakeAi():
    return random.choice(validMoves)

def determineResult(activePlayer):
    i = 0
    j = 0
    if i < 3:
        if board[i][0] == activePlayer and board[i][1] == activePlayer and board[i][2] == activePlayer:
            i += 1
            return True
    if j < 3:
        if board[0][j] == activePlayer and board[1][j] == activePlayer and board[2][j] == activePlayer:
            j += 1
            return True
    if board[0][0] == activePlayer and board[1][1] == activePlayer and board[2][2] == activePlayer:
        return True
    if board[0][2] == activePlayer and board[1][1] == activePlayer and board[2][0] == activePlayer:
        return True
    if len(validMoves) == 0:
        print(f"Tie game!")
        isGameOver == True
    return False

print("x is human, o is a robot. Let the games begin!")
while isGameOver == False:
    if player == 'x':
        move = input(f"Player {player} Make a move. Available moves are {validMoves} ")
    else:
        move = playWithFakeAi()
        print(f"Ai picked {move}")

    if validateMove(int(move)) == True:
        updateBoard(convertMoveToTwoDimensionalArray(int(move) - 1), player)
        isGameOver = determineResult(player)
        if isGameOver == True:
            print(f"Player {player} has won!")
        player = switchPlayer(player)
        printBoard(board)
    else:
        print("Move invalid, please try again")