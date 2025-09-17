#TurtleGraphics.py
#Name: Tessa Horn
#Date: 09/17/25
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle()
def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)
def drawPolygon5(tessa, sides):
    for s in range(sides):
        tessa.forward(90)
        tessa.right(45)
def drawPolygon8(tessa, sides):
    for s in range(sides):
        tessa.forward(60)
        tessa.right(45) 
def fillCorner(tessa, corner):
    drawSquare(tessa, 100)
    if corner==1:
        tessa.begin_fill()
        drawSquare(tessa, 50)
        tessa.end_fill()
    elif corner==2:
        tessa.forward(50)
        tessa.begin_fill()
        drawSquare(tessa, 50)
        tessa.end_fill()
    elif corner==3:
        tessa.right(90)
        tessa.forward(50)
        tessa.left(90)
        tessa.begin_fill()
        drawSquare(tessa, 50)
        tessa.end_fill()
def drawSquare2(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.left(90)
def squaresInSquares(tessa, numSquares):
    size = 30
    for i in range(numSquares):
        tessa.penup()
        tessa.goto(-size/2, -size/2)
        tessa.pendown()
        drawSquare2(tessa, size)
        size += 30
def main():
    myTurtle = turtle.Turtle()
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon
    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in
    # squaresInSquares(myTurtle, 5) #draws 5 cocentric squares
   #squaresInSquares(myTurtle, 3 #draws 3 cocentric squares


main()
