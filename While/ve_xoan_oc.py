import turtle
import math

t = turtle.Turtle()
d = int(input("input values: "))
n = 0
while True :
    vt = n/20 * math.pi
    x = (vt * 10)* math.cos(vt)
    y = (vt * 10)* math.sin(vt)
    t.goto(x,y)
    n +=1
    if n > d:
       break
t.speed(0)
turtle.done()