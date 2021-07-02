
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
    #initialize the main game
    mainGame = game()
    
    #initialize the players for "x" and "o"
    player = input('are you x or o? \n')
    print('make a move from a1 - c3, the letters being the rows and the numbers being the columns')
    
    
    if player == 'x':
        aiPlayer = 'o'
        maxPlayer = True
    else:
        aiPlayer = 'x'
        maxPlayer = False


    #main loop
    
    return mainGame, player, aiPlayer, maxPlayer

def main():
    mainGame, player, aiPlayer, maxPlayer = initializeGame()
    playing = 'x'
    depth = 1
    while True:    
        
        if player == playing:
            possibleMoves = legalMoves(mainGame.gameboard)
            while True:
                playerMove = input()
                if playerMove not in possibleMoves:
                    print(r"that's not a legal move!")
                else:
                    break

            mainGame.makeMove(playerMove, player)
            mainGame.print_game()
            playing = aiPlayer
            
            state = gameState(mainGame.gameboard, depth)#check if the game is over
            if state != None:
                return state
            
            depth += 1

            
            
            
        
        else:

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
            mainGame.makeMove(bestMove, aiPlayer) # play the best move evaluated
            mainGame.print_game()

            state = gameState(mainGame.gameboard, depth)#check if the game is over
            if state != None:
                return state
            
            depth +=1
            
            
            
            playing = player

            

        










if __name__ == "__main__":
    main()





























