import turtle
import random

window = turtle.Screen()
window.bgcolor('black')
window.setup(900, 700)

tur = turtle.Turtle()
# tur.hideturtle()
colors = ['red', 'green', 'blue', 'yellow', 'purple']
tur.width(1)
orient = 0
tur.speed(10)
radius = 30

while radius <300:
    r = random.random()
    g = random.random()
    b = random.random()
    tur.color(r, g, b)
    tur.right(10)
    tur.circle(radius)
    radius += 5

window.mainloop()
