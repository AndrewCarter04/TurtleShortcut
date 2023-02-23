import turtle
import turtleshortcut

t = turtle.Turtle()
ts = turtleshortcut.TurtleShortcut(t)

t.pencolor('blue')

ts.square(50)
ts.square(75)
ts.square(100)

t.pencolor('orange')

ts.triangle(50)
ts.triangle(75)
ts.triangle(100)

t.pencolor('green')

ts.pentagon(50)
ts.pentagon(75)
ts.pentagon(100)
