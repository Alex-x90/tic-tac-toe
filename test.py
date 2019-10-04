turn = 0 #turn 0 is x(player)'s turn

def minimax(board,turn):
    if winCheck() != None:
        return winCheck()

    move = -1
    score = -2

    moves = getPossibleMoves()
    for x in moves:
        tempBoard = board.copy()
        tempBoard[x]=
        tempTurn=turn


test = [1,0,0,0,0,0,0,0,0]
minimax(test,turn)
