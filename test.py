from fbchat import Client, log
from fbchat.models import *
import json
from getpass import getpass

import optimizegame
from optimizegame import game
from optimizegame import humanMove
from optimizegame import aiMove
from optimizegame import initializeGame

from bot import legalMoves
from bot import gameState


'''THE MAGIC CODE I COPIED THAT MAKES THE CODE WORK LMAOOOOOOOO'''
import fbchat # type: ignore
### see https://github.com/fbchat-dev/fbchat/issues/615#issuecomment-710127001 
import re
fbchat._util.USER_AGENTS    = ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"]
fbchat._state.FB_DTSG_REGEX = re.compile(r'"name":"fb_dtsg","value":"(.*?)"')
''''''

cookies = {}
try:
    # Load the session cookies
    with open('session.json', 'r') as f:
        cookies = json.load(f)
except:
    # If it fails, never mind, we'll just login again
    pass





playing = 'x'
    
depth = 1
player = None

aiplayer = None
maxplayer = None

mainGame = game() #if a game isn's ongoing, start a new game
class testBot(Client):

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        """
        Called when the client is listening, and somebody sends a message   
        :param author_id: The ID of the author
        :param message_object: The message (As a `Message` object)
        :param thread_id: Thread ID that the message was sent to. See :ref:`intro_threads`
        :param thread_type: Type of thread that the message was sent to. See :ref:`intro_threads`
        :type message_object: models.Message
        :type thread_type: models.ThreadType
        """

        global player, aiplayer, maxplayer, depth

        log.info("{} from {} in {}".format(message_object, thread_id, thread_type.name))
        
        
        msgText=message_object.text
        msgText.lower()
        f = open("gamestate.txt", "r")
        gamecurrentStatus = f.read() #read the current status of the game
        f.close()

        #check if there's a game currently ongoing
        if gamecurrentStatus == 'ongoing' and "@tictactoe" in msgText: #if the game is ongoing 
            if '@tictactoe' in msgText and msgText in legalMoves(mainGame.gameboard):
                messages = msgText.split()
                move = messages[1] #get the 2nd word and make that the move
                if move not in legalMoves(mainGame.gameboard):
                    self.send(Message('not a move'), thread_id=thread_id,thread_type=thread_type)
                    return


                if playing == player:
                    playerMove = move
                    mainGame.makeMove(playerMove, player)
                    self.send(Message(mainGame.print_game()), thread_id=thread_id,thread_type=thread_type)

                    state = gameState(mainGame.gameboard, depth)#check if the game is over
                    if state != None:
                        self.send(Message(state), thread_id=thread_id,thread_type=thread_type) #send message if game is over
                        f = open("gamestate.txt", "w")
                        f.write("not ongoing")
                        f.close()
                    depth += 1

                    playing = aiplayer
                    

                else:
                    compMove = aiMove(aiplayer, mainGame, depth, maxplayer)
                    mainGame.makeMove(compMove, aiplayer)
                    self.send(Message(mainGame.print_game()), thread_id=thread_id,thread_type=thread_type)

                    state = gameState(mainGame.gameboard, depth)#check if the game is over
                    if state != None:
                        self.send(Message(state), thread_id=thread_id,thread_type=thread_type) #send message if game is over
                        f = open("gamestate.txt", "w")
                        f.write("not ongoing")
                        f.close()
                    depth += 1

                    playing = player


        #if there's no game currently ongoing then start a new one
        else:
            if msgText == '@tictactoe start':

                


                self.send(Message(mainGame.print_game()), thread_id=thread_id,thread_type=thread_type) #send the gameboard
                f = open("gamestate.txt", "w")
                f.write("ongoing")
                f.close()

                player, aiplayer, maxplayer = initializeGame()












client=testBot(r"tictactoe.icebot@gmail.com", getpass())
client.listen()

# 'a     b     c'
# '        |     |       '     
# '1  -  |  -  |  -   '  
# ' ______|____|______'
# '        |     |     '
# 2  -  |  -  |  -  
#  ______|____|_
#         |     |     
# 3  -  |  -  |  -  
#         |     |'
