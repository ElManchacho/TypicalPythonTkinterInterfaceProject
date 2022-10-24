import datetime
from screen import *
import pathlib, sys, json

class Game:

    screen : Screen

    def __init__(self) -> None:
        
        self.screen = Screen()

    def exceptionLog(self,error):

        logsFolderPath = str(pathlib.Path(__file__).parent.resolve()).replace('tests\\Game','')+'logs\\exceptions\\'

        logFileLocation = logsFolderPath + str(datetime.datetime.today().timestamp())+ '.log'

        logFile = open(logFileLocation, 'w')

        error = {
                    "error" : {
                        "errorTime":str(datetime.datetime.today()),
                        "errorMsg":str(error)
                    }
                }

        json.dump(error,logFile)

        logFile.close()

        print("\n\nException encountered when starting the game. Please check the following log file :\n\n'"+ logFileLocation+"'\n\n")

    def startGame(self) -> bool:

        try:
    
            self.screen.displayScreen()
            return True

        except:

            self.exceptionLog(sys.exc_info())
            return False