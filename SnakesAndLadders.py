import sys
sys.path.append(sys.path[0]+'\models')

from board import board
from dice import dice
from player import player
from ladder import ladder
from piece import piece
from snake import snake

b=board()
d=dice()
s=int(input()) #number of snakes
snake=[]
for i in range(s):
    snake.append([int(x) for x in input().split(' ')])

l=int(input()) #numbr of ladders
ladder=[]
for i in range(l):
    ladder.append([int(x) for x in input().split(' ')])

for m in snake:
    b.placeSnake(m[0],m[1])

for l in ladder:
    b.placeLadder(l[0],l[1])

p=int(input()) #number of players

players=[]
for i in range(p):
    p1=player()
    p1.createPlayer(input())
    p1.allotApiece()
    players.append(p1)

flag=0
while not flag:
    i=0
    for p in players:
        v=p.rollDice(d)
        flag=b.movePiece(p.owns,v)
        if flag==1:
            break
