from random import seed
from random import choice

class dice:
    def __init__(self):
        self.value=0
        self.x=[i for i in  range(1,7)]
    def roll(self):
        self.value=choice(self.x)
        return self.value
