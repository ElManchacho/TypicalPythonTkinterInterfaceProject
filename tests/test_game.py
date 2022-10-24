from game import *
from cacheFlushGame import *

def test_startGame():
    gameTest:Game=Game()
    assert gameTest.startGame()==True