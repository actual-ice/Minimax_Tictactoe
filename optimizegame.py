
'''
IT WORKS IT ACTUALLY WORKS OMG YEAAAAAAAAAAAAAAAAAAAAAA

the only problem now is that even if it can win in one move it will win in more moves
'''

import bot
from bot import minimax
from bot import moveTree
from bot import legalMoves
from bot import gameState

positive_inf = float('inf')
negative_inf = float('-inf')
class game:
    def __init__(self, gametype='single'):
        
        self.gametype = gametype
        self.gameboard = {'a1':' ', 'a2':' ', 'a3':' ',
                        'b1':' ', 'b2':' ', 'b3':' ',
                        'c1':' ', 'c2':' ', 'c3':' '}

    def makeMove(self, move, player):
        self.gameboard[move] = player

    def print_game(self):
        game_moves = self.gameboard
        row0 = '***********'
        row1 = '   |     |   '
        row2 = ' {} |  {}  | {} '.format(game_moves['a1'], game_moves['a2'], game_moves['a3'])
        row3 = '___|___|___'
        row4 = '   |     |   '
        row5 = ' {} |  {}  | {} '.format(game_moves['b1'], game_moves['b2'], game_moves['b3'])
        row6 = '___|___|___'
        row7 = '   |     |   '
        row8 = ' {} |  {}  | {} '.format(game_moves['c1'], game_moves['c2'], game_moves['c3'])
        row9 = '   |     |   '
        row10 = '***********'

        game = [row0, row1, row2, row3, row4, row5, row6, row7, row8, row9, row10]

        printGameboard = ''

        for i in game:
            printGameboard += i + '\n'

        print(printGameboard)
        return printGameboard

def initializeGame():
    player = input('are you x or o?')
    if player == 'x':
        aiPlayer = 'o'
        maxPlayer = True
    else:
        aiPlayer = 'x'
        maxPlayer = False

    return player, aiPlayer, maxPlayer


def aiMove(aiPlayer, mainGame, depth, maxPlayer):


    possibleMoves = legalMoves(mainGame.gameboard)
    minEval = positive_inf
    maxEval = negative_inf
    for possibleMove in possibleMoves:
        mainGame.makeMove(possibleMove, aiPlayer)
        evaluation = minimax(mainGame.gameboard, depth, maxPlayer)

        mainGame.gameboard[possibleMove] = ' ' #reset the board position
        if aiPlayer == 'x':
            if maxEval < max(maxEval, evaluation):
                maxEval = max(maxEval, evaluation)
                bestMove = possibleMove
        elif minEval > min(minEval, evaluation):
            minEval = min(minEval, evaluation)
            bestMove = possibleMove
    # mainGame.makeMove(bestMove, aiPlayer) # play the best move evaluated
    # mainGame.print_game()

    state = gameState(mainGame.gameboard, depth)#check if the game is over
    if state != None:
        return state
    
    depth +=1
    
    
    
    

    return bestMove

def humanMove(mainGame):
    print('make a move from a1 - c3, the letters being the rows and the numbers being the columns')

    while True:
        playerMove = input()
        if playerMove not in mainGame.gameboard or mainGame.gameboard[playerMove] != ' ':
            print('not a legal move!')
        else:
            break

    return playerMove

def main():
    mainGame = game()
    #initialize the main game
    player, aiplayer, maxplayer = initializeGame()
    playing = 'x'
    
    depth = 1
    
    while True:
        


        if playing == player:
            playerMove = humanMove(mainGame)
            mainGame.makeMove(playerMove, player)
            mainGame.print_game()

            state = gameState(mainGame.gameboard, depth)#check if the game is over
            if state != None:
                return state
            
            depth += 1

            playing = aiplayer
            

        else:
            compMove = aiMove(aiplayer, mainGame, depth, maxplayer)
            mainGame.makeMove(compMove, aiplayer)
            mainGame.print_game()

            state = gameState(mainGame.gameboard, depth)#check if the game is over
            if state != None:
                return state
            
            depth += 1

            playing = player

        
    

            

        










#         currentGame = mainGame.gameboard.copy() #copy the current board position to avoid changing the maingame's board

#         state = gameState(currentGame, depth) #check the position of the current board
#         if state != None: #if the game isn't ongoing, then return who won, or if it's a draw
#             if state == 'X':
#                 print('X WON')
#                 break
#             elif state == 'O':
#                 print('O WON')
#                 break
#             elif state == 'DRAW':
#                 print('DRAW')
#                 break
         
#         if playing == player: #if it's the human's turn, ask for input
#             move = input("make a move:\n")
#             mainGame.makeMove(move, player)
        
#         else:
#             possibleMoves = legalMoves(currentGame) #get all the legal moves you can do

#             minEval = positive_inf
#             for possibleMove in possibleMoves: #iterate through the possible moves
#                 position = moveTree(currentGame, possibleMove, aiPlayer)
#                 evalutaion = minimax(position, depth, False)
#                 if minEval >= min(minEval, evalutaion):
#                     #if the move is a better move than the last, store the move, and change the max eval
#                     minEval = min(minEval, evalutaion)
#                     bestCurrentMove = possibleMove
#             #make the best move evaluated
#             mainGame.makeMove(bestCurrentMove, aiPlayer)

#         mainGame.print_game()
#         debuggame = mainGame.gameboard

#         if playing == 'x':
#             playing = 'o'
#         else:
#             playing = 'x'

#         depth +=1

if __name__ == "__main__":
    main()





























