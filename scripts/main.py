import atexit
from Game.game import Game
from Game.cacheFlushGame import *

def launch()->None:

    atexit.register(cacheFlushGame)

    game = Game()

    started = game.startGame()

if __name__ == "__main__":

    launch()
