import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
t.speed(100)

""" t.forward(100) """
""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200) """


""" def equal(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equal(200) 

def right():
    t.forward(100)
    t.left(90)
    t.forward(100)
    t.left(135)
    t.forward(142)
right()

 """


""" def rectangle (x):
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(125)
    t.left(90)
    t.forward(100)
    t.left(90)
rectangle (200)
turtle.done() """


""" def equal(x):
    t.forward(90)
    t.left(120)
    t.forward(90)
    t.left(120)
    t.forward(90)
equal(200) 
turtle.done() """

""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)

t.speed (100)
for i in range (60):
    square (200)
    t.right (5) """

""" 
t. speed (100)
def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
square(200)
def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length)
        length += 25
addSquares(5)
turtle.done """


""" def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
length = 5
for i in range (60):
    square(length)
    length += 5
    t.right (5)

turtle.done() """

def star(x):
    for i in range(5):
        t.forward(x)
        t.right(144)

def addStars(iRange):
    length = 25
    for i in range(iRange):
       addStars(length,144)
    length += 5
    addStars (5)

turtle.done()
