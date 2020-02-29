from snake import snake
from ladder import ladder
class board:
    def __init__(self):
        self.snakes={}
        self.ladders={}

    def placeSnake(self, head, tail):
        if (head>tail) and (head not in self.snakes) and (head<100) and (head not in self.ladders):
            s=snake()
            s.head=head
            s.tail=tail
            self.snakes[head]=tail
        else:
            return -1

    def placeLadder(self, start, end):
        if (start<end) and (start not in self.ladders) and (end<=100) and (start not in self.snakes):
            l=ladder()
            l.start=start
            l.end=end
            self.ladders[start]=end
        else:
            return -1

    def movePiece(self, piece, value):
        if (piece.initial+value in self.snakes):
            print(piece.owner+ " rolled a " + str(value) + " and moved  from " +str(piece.initial) + " to " + str(self.snakes[piece.initial+value]))
            piece.initial= self.snakes[piece.initial+value]
            while (piece.initial in self.snakes) or (piece.initial in self.ladders):
                movePiece(self,piece,0)
            return 0
        
        elif piece.initial+value in self.ladders:
            if self.ladders[piece.initial+value]<100:
                print(piece.owner+ " rolled a " + str(value) + " and moved  from " +str(piece.initial) + " to " + str(self.ladders[piece.initial+value]))
                piece.initial=self.ladders[piece.initial+value]
                while (piece.initial in self.snakes) or (piece.initial in self.ladders):
                    movePiece(self,piece,0)
                return 0
            else:
                print(piece.owner +" rolled a " + str(value)+ " and won the game.")
                return 1
            
        elif piece.initial<100 and (piece.initial+value<100):
            if value!=0:
                print(piece.owner+ " rolled a " + str(value) + " and moved  from " +str(piece.initial) + " to " + str(piece.initial+value))
                piece.initial=piece.initial+value
            return 0
        
        elif piece.initial+value==100:
            print(piece.owner +" rolled a " + str(value)+ " and won the game.")
            return 1

        '''elif piece.initial+value>100:
            print(piece.owner + " doesn't move.")
            print(value)
            piece.initial=piece.initial
            return 0'''
