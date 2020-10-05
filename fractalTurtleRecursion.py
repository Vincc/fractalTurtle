import turtle
from time import sleep

phase = int(input("??? "))
directionArray = []

length = 150
lengthSPLIT = length * 1 / (3 ** phase)
frankTheTurtle = turtle.Turtle()
wn = turtle.Screen()
def draw(phase):
    if phase == 0:
        frankTheTurtle.forward(lengthSPLIT)
    else:
        draw(phase-1)
        frankTheTurtle.left(60)
        draw(phase - 1)
        frankTheTurtle.right(120)
        draw(phase - 1)
        frankTheTurtle.left(60)
        draw(phase - 1)

draw(phase)
turtle.done()
wn.mainloop
