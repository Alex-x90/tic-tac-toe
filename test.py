turn = 1 #turn -1 is x(player)'s turn

def minimax(board,turn):
    if winCheck() != None:
        return winCheck()

    move = -1
    score = -2

    moves = getPossibleMoves(board)
    for x in moves:
        tempBoard = board.copy()
        tempBoard[x]= turn
        tempTurn = not turn
        scoreMove = -self.minimax(tempBoard,tempTurn)
        if scoreMove>score:
            score=scoreMove
            move = x

    if move==-1:
        return 0

    return score

test = [-1,0,0,0,0,0,0,0,0]
minimax(test,turn)
