"""
This module generates a user class to keep track of points and such

by:00nray
"""
class user:
    def __init__(self):
        self.usedCommands = list()
        self.name = ""
        self.email = ""
        self.phone = ""
        self.points = 0
        self.gameStarted = False

user=user()


def getPoints():
    return user.points


def addPoints(Points,command):
    if command not in user.usedCommands:
        user.points = getPoints()+Points
        user.usedCommands.append(command)


def gameStarted():
    return gameStarted


def setGameStarted(self):
        """flag to signal that user has been added to db and is readdy to play the game
                effects the Flask applications
                see the Flask app Factory for more info
        """
        user.gameStarted = True

def setGameStopped(self):
        """same as setGameAsStarted(), stops the game"""
        user.gameStarted = False

