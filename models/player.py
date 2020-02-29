from piece import piece
from dice import dice
class player:
    def __init__(self):
        self.name=None
        self.owns=None

    def createPlayer(self,name):
        self.name=name
    
    def allotApiece(self):
        self.owns=piece()
        self.owns.owner=self.name

    def rollDice(self,d):
        return d.roll()
