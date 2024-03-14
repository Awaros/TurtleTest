import turtle

window = turtle.Screen()
window.bgcolor('black')
window.setup(900, 700)

tur = turtle.Turtle()
tur.shape('turtle')
tur.color('yellow')
tur.fillcolor('yellow')
colors = ['red', 'green', 'blue', 'yellow', 'purple']
tur.width(2)
orient = 0
tursp = 10


def moveup():
    global orient
    if int(orient) == 0:
        tur.left(90)
        orient = 90
        print(orient)
    if int(orient) == 180:
        tur.right(90)
        orient = 90
        print(orient)
    if int(orient) == 270:
        tur.left(180)
        orient = 90
        print(orient)
    x, y = tur.position()
    tur.setposition(x, y + tursp)
    return orient


def movedown():
    global orient
    if int(orient) == 0:
        tur.right(90)
        orient = 270
        print(orient)
    if int(orient) == 90:
        tur.left(180)
        orient = 270
        print(orient)
    if int(orient) == 180:
        tur.left(90)
        orient = 270
        print(orient)
    x, y = tur.position()
    tur.setposition(x, y - tursp)


def moveleft():
    global orient
    if int(orient) == 90:
        tur.left(90)
        orient = 180
        print(orient)
    if int(orient) == 0:
        tur.left(180)
        orient = 180
        print(orient)
    if int(orient) == 270:
        tur.right(90)
        orient = 180
        print(orient)
    x, y = tur.position()
    tur.setposition(x - tursp, y)


def moveright():
    global orient
    if int(orient) == 90:
        tur.right(90)
        orient = 0
        print(orient)
    if int(orient) == 180:
        tur.right(180)
        orient = 0
        print(orient)
    if int(orient) == 270:
        tur.left(90)
        orient = 0
        print(orient)
    x, y = tur.position()
    tur.setposition(x + tursp, y)


window.onkeypress(moveup, 'Up')
window.onkeypress(movedown, 'Down')
window.onkeypress(moveleft, 'Left')
window.onkeypress(moveright, 'Right')

window.listen()
window.mainloop()
