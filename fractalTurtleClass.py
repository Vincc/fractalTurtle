import turtle
from time import sleep

phase = int(input("??? "))
directionArray = []
tempARY=[]
length = 150
def tmparrayappend():
    for i in tempARY:
        directionArray.append(i)
#left = 1   right = 0
for i in range(phase):
    directionArray = []
    tmparrayappend()
    directionArray.append(1)
    tmparrayappend()
    directionArray.append(0)
    tmparrayappend()
    directionArray.append(1)
    tmparrayappend()
    tempARY = directionArray.copy()

frankTheTurtle = turtle.Turtle()
lengthSPLIT = length * 1 / (3 ** phase)
wn = turtle.Screen()
class TurtleDraw:
    def __init__(self, turtlee):
        self.turtlee = turtlee
    def drawSide(self):
        for i in range(3):
            for i in range((4 ** phase) - 1):
                self.turtlee.forward(lengthSPLIT)
                # change angle too!!!
                if not directionArray[i]:
                    self.turtlee.left(120)
                    continue
                self.turtlee.right(60)
            self.turtlee.forward(lengthSPLIT)
            self.turtlee.left(120)
        self.turtlee.ht()
one = TurtleDraw(frankTheTurtle)
one.drawSide()
turtle.done()
wn.mainloop
