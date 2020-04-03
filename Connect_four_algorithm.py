#START
from turtle import *
from time import *
class game:
res = []
def __init__(self):
self.turn = 0
self.board = [[None] * 6 for i in range(7)]
self.count = [0] * 7
self.colour = ['','','','']
#color1,color2,bgcolor,boardcolor
self.name1 = ''
self.name2 = ''
self.winner = ''
self.moves = 0
self.timestart = 0
self.timeend = 0
self.points1 = 0
self.points2 = 0
def colorchoice(self):
cl =['black','gray','navy','red','green','yellow','maroon','white']
i=0
print '\n\t1.BLACK 2.GRAY 3.NAVY
4.RED'
print '\t5.GREEN 6.YELLOW 7.MAROON
8.WHITE'
print '\nFROM THE ABOVE COLOR CODES:'
while i!=4:
l = [self.name1+', Enter your
coin',self.name2+', Enter your coin','Enter
background','Enter board']
n = input(l[i]+' color code:')
try:
n = int(n)
if 0<n<9 and (cl[n-1] not in
self.colour):
self.colour[i] = cl[n-1]
i+=1
else:
print 'MAKE SURE THE CODE IS
CORRECT AND IS UNUSED!\n'
except:
print 'ENTER THE COLOUR CODE
CONSISTING OF NUMERIC VALUES ONLY.\n'
def tutorial(self):
print '\n',('*'*70)
18 | P a g e
print '\nWELCOME TO OUR CONNECT FOUR GAME.WE
ARE GLAD YOU CHOSE US.\n'
print 'Connect 4 is a game involving a 7x6 grid
where a winner is the player who matches four coins
first:horizontally,vertically or diagonally.'
print '\nHere are a few rules:'
print '1.The grid consists of 7 columns and 6
rows.A coin gets placed at the bottom of each column
considering there is no coin in that row.In case a coin
is present in the column,the input coin is placed above
the coin present.'
print '2.Wait for your turn before placing the
coin in order to avoid faulty placement of coins.'
print '3.The looser of the game gets 10 points
by default while the winner gets a minimum of 50 points
which increases with lesser amoiunt of moves.'
print '4.Please follow the instructions at
every step.'
print '\nHope you enjoy the game.Have fun.'
print '*'*70
print '\n'
sleep(5)
def drawboard(self):
pencolor(self.colour[3])
pu()
setpos(-245,270)
pd()
rt(90)
fd(540)
lt(90)
19 | P a g e
fd(490)
lt(90)
fd(540)
lt(90)
fd(490)
pu()
setpos(-175,270)
pd()
lt(90)
fd(540)
pu()
setpos(-105,270)
pd()
fd(540)
pu()
setpos(-35,270)
pd()
fd(540)
pu()
setpos(35,270)
pd()
fd(540)
pu()
setpos(105,270)
pd()
fd(540)
pu()
setpos(175,270)
20 | P a g e
pd()
fd(540)
pu()
setpos(245,270)
pd()
fd(540)
pu()
setpos(-245,180)
lt(90)
pd()
fd(490)
pu()
setpos(-245,90)
pd()
fd(490)
pu()
setpos(-245,0)
pd()
fd(490)
pu()
setpos(-245,-90)
pd()
fd(490)
pu()
setpos(-245,-180)
pd()
fd(490)
def draw_c1(self):
21 | P a g e
pencolor(self.colour[0])
fillcolor(self.colour[0])
begin_fill()
circle(10)
end_fill()
def draw_c2(self):
pencolor(self.colour[1])
fillcolor(self.colour[1])
begin_fill()
circle(10)
end_fill()
def getwinner(self):
# Check rows for winner
for y in range(6):
for x in range(4):
if self.board[x][y]==self.board[x+1][y]==
self.board[x+2][y]==self.board[x+3][y] and
self.board[x][y]!=None:
return self.board[x][y]
# Check columns for winner
for x in range(7):
for y in range(3):
if self.board[x][y] == self.board[x][y+1]
== self.board[x][y+2]==self.board[x][y+3]
and self.board[x][y] !=None:
return self.board[x][y]
22 | P a g e
# Check diagonal (bottom-left to top-right) for
winner
for row in range(4):
for col in range(3,6):
if (self.board[row][col] == self.board[row +
1][col - 1] == self.board[row + 2][col - 2]
==\
self.board[row + 3][col - 3]) and
(self.board[row][col] != None):
return self.board[row][col]
# Check diagonal (top-left to bottom-right) for
winner
for row in range(4):
for col in range(3):
if (self.board[row][col] == self.board[row
+ 1][col + 1] == self.board[row + 2][col +
2] ==\
self.board[row + 3][col + 3]) and
(self.board[row][col] != None):
return self.board[row][col]
l=1
for row in self.board:
for i in row:
if i==None:
l=0
if l:
return 'D'
23 | P a g e
# No winner: return the empty string
return False
def declare(self,code):
sleep(10)
self.timeend = time()
ht()
speed(100)
pencolor(self.colour[3])
pu()
setpos(-200,100)
pd()
if code == 'X':
write("THE GAME IS WON BY "+self.name1,font
= ('Arial',21,"bold"))
self.winner = self.name1
self.points2 = 10
self.points1=50+(50-self.moves)
elif code == 'Y':
write("THE GAME IS WON BY "+self.name2,font
= ('Arial',21,"bold"))
self.winner = self.name2
self.points2 = 50+(50-self.moves)
self.points1 = 10
else:
write("THE GAME IS DRAWN",font =
('Arial',21,"bold"))
self.winner = 'Drawn'
24 | P a g e
self.points2 = 10
self.points1 = 10
pu()
setpos(-200,-200)
pd()
write("CLICK TO EXIT",font =
('Arial',18,"bold"))
self.cont = False
def place1(self,row):
self.board[row][self.count[row]] = 'X'
pu()
setpos(-210+(row*70),-230+(self.count[row]*90))
pd()
self.draw_c1()
self.count[row]+=1
w = self.getwinner()
pu()
setpos(0,310)
pd()
self.draw_c2()
if w == 'X':
self.screen.reset()
self.declare('X')
elif w=='D':
self.screen.reset()
self.declare('D')
25 | P a g e
def place2(self,row):
speed(1000)
self.board[row][self.count[row]] = 'Y'
pu()
setpos(-210+(row*70),-230+(self.count[row]*90))
pd()
self.draw_c2()
self.count[row]+=1
w = self.getwinner()
pu()
setpos(0,310)
pd()
self.draw_c1()
if w == 'Y':
self.screen.reset()
self.declare('Y')
elif w=='D':
self.screen.reset()
self.declare('D')
def stats(self):
print '*'*70
print
if self.winner!='Drawn':
print 'Winner:',self.winner
print 'Moves played entirely:',self.moves
26 | P a g e
print 'Points scored
by',self.name1,':',self.points1
print 'Points scored
by',self.name2,':',self.points2
print 'Time elapsed:',int(self.timeend-
self.timestart),'secs'
else:
print 'MATCH IS DRAWN.Well played both of
you!'
print 'Time elapsed:'
print '*'*70
print
game.res.append([max(self.points1,self.points2),self.wi
nner])
def place(self,x,y):
row = 0
if self.cont == False:
bye()
self.stats()
elif 270>y>-270:
if -240<x<-180:
row =1
elif -170<x<-110:
row=2
elif -100<x<-40:
row =3
elif -30<x<30:
row =4
27 | P a g e
elif 40<x<100:
row=5
elif 110<x<170:
row=6
elif 180<x<240:
row=7
if row!=0 and self.count[row-1]<6:
self.moves+=1
if self.turn == 0:
self.place1(row-1)
self.turn = 1
else:
self.place2(row-1)
self.turn=0
def main(self):
self.timestart = time()
self.screen.clear()
bgcolor(self.colour[2])
pensize('5')
ht()
speed(200)
self.drawboard()
self.cont = True
pu()
setpos(-100,310)
pd()
write('TURN:\t',font=('Arial',17,'bold'))
pu()
28 | P a g e
setpos(0,310)
pd()
self.draw_c1()
pu()
self.screen.onclick(self.place)
def choice(self):
self.tutorial()
i=0
l = [None,None]
while i<2:
l[i] = raw_input('Player '+str(i+1)+',
enter your name:')
if l[i].isalpha():
i+=1
else:
print 'Make sure you only use alphabets
while entering your name!\n'
self.name1 = l[0]
self.name2 = l[1]
self.colorchoice()
t = Turtle()
ht()
t.ht()
t.speed(200)
speed(200)
setup(height= 700, width = 700)
self.screen = Screen()
29 | P a g e
title('Connect-4')
bgcolor('black')
pencolor('red')
pu()
setpos(-175,0)
pd()
write('CLICK \'SPACE\' TO
PLAY..',font=('Arial',17,'bold'))
self.screen.onkey(self.main,'space')
self.screen.listen()
mainloop()
count = 0
while True:
obj = game()
obj.choice()
cho = raw_input('Enter \'Y\' to play again:')
if cho != 'Y':
break
print '*'*70
print 'Session stats:\n'
game.res.sort()
for i in range(len(game.res)):
if game.res[i][1]!= 'Drawn':
print str(i+1)+'.',game.res[i][1]+':
',game.res[i][0]
print '\nTHANK YOU FOR PLAYING WITH US.HOPE YOU ENJOYED
:)!'
#END