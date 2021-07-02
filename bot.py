# assuming that the tic tac toe game is a class with methods like game.makeMove() 
# and attributes like game.board, game.playerX, game.playerO, game.legalmoves, game.state etc, this is the bot and stuff


positive_inf = float('inf')
negative_inf = float('-inf')

def minimax(position, depth, maxPlayer):
# returns the best move from the legal moves available
# i dont get the beta and alpha thing that much

#OK BAD NEWS, MINIMAX IS GIVING RANDOM OUTPUTS FOR THE SAME CALL WHAT FIX IMMEDIATELY

#the legalMoves function outputs legal moves in different orders each time, it's probably the cause of the problem


    state = gameState(position, depth) #check the position of the current board
    if state != None:
        if state == 'X':
            return 1
        elif state == 'O':
            return -1
        elif state == 'DRAW':
            return 0
    

    if maxPlayer:
        maxEval = negative_inf
        moves = legalMoves(position)
        for child in moves:
            #play the possible moves and return the position
            position = moveTree(position, child, 'x')

            evaluation = minimax(position, depth+1, False)
            maxEval = max(maxEval, evaluation)
            #alpha = max(alpha, evaluation)
            # if beta <= alpha:
            #     break
            position[child] = ' '
        return maxEval

    else:
        minEval = positive_inf
        moves = legalMoves(position)
        for child in moves:
            #play the possible moves and return the position
            position = moveTree(position, child, 'o')

            evaluation = minimax(position, depth+1, True)
            minEval = min(minEval, evaluation)
            #beta = min(beta, evaluation)
            # if beta <= alpha:
            #     break
            position[child] = ' '
        return minEval

def moveTree(position, move, player):
    #newPosition = position.copy()
    #newPosition[move] = player
    position[move] = player
    return position

def legalMoves(position):
    legalMoves = []
    for i in position:
        if position[i] == ' ':
            legalMoves.append(i)
    return legalMoves

def gameState(position, depth):
    gameWins = [['a1', 'a2', 'a3'],
                ['b1', 'b2', 'b3'],
                ['c1','c2', 'c3'],
                ['a1', 'b1', 'c1'],
                ['a2', 'b2', 'c2'],
                ['a3', 'b3', 'c3'],
                ['a1', 'b2', 'c3'],
                ['a3', 'b2', 'c1']]

    for line in gameWins:
        if position[line[0]] == position[line[1]] == position[line[2]] == 'x':
            return 'X'
        elif position[line[0]] == position[line[1]] == position[line[2]] == 'o':
            return 'O'

    if depth == 9:
        return 'DRAW'
    



























