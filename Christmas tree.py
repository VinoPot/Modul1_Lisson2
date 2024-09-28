import turtle as t

screen = t.Screen()
screen.bgcolor("white")
t.speed(2)

t.color("green")
t.begin_fill()

for i in range(3):
    t.fd(50)
    t.lt(120)
t.end_fill()

t.penup()
t.goto(0, 25)
t.pendown()

t.begin_fill()

for i in range(3):
    t.fd(50)
    t.lt(120)

t.end_fill()

t.penup()
t.goto(0, 50)
t.pendown()

t.begin_fill()

for i in range(3):
    t.fd(50)
    t.lt(120)

t.end_fill()

t.hideturtle()
screen.exitonclick()