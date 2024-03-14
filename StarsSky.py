import turtle
import random

window = turtle.Screen()
window.bgcolor('black')
window.setup(900, 700)

tur = turtle.Turtle()
tur.hideturtle()
colors = ['red', 'green', 'blue', 'yellow', 'purple']
tur.width(2)
orient = 0
tursp = 10


def starfill(n, dlina):
    tur.fillcolor(random.choice(colors))
    tur.color(tur.fillcolor())
    tur.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            tur.forward(dlina)
            angle = n // 2 * 360 / n
            tur.left(angle)
    tur.end_fill()


def move(x, y):
    angle = random.randint(1, 80)
    tur.left(angle)
    tur.speed(20)
    tur.teleport(x, y)
    size = random.randint(10, 200)
    versh = random.choice([5, 7, 9])
    starfill(versh, size)


window.onclick(move)
window.listen()
window.mainloop()
