import turtle as t

screen = t.Screen()
screen.bgcolor("white")
t.speed(2)


for _ in range(4):
    t.forward(30)
    t.left(90)

t.penup()
t.goto(60, 0)
t.pendown()

for _ in range(4):
    t.forward(30)
    t.left(90)

t.penup()
t.goto(120, 0)
t.pendown()

for _ in range(4):
    t.forward(30)
    t.left(90)


t.hideturtle()
screen.exitonclick()


