import turtle as t

screen = t.Screen()
screen.bgcolor("white")
t.speed(2)

# Рисование прямоугольника
t.fillcolor("blue")
t.begin_fill()

for _ in range(2):
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)

t.end_fill()

# перемещение
t.penup()
t.goto(120, 130)
t.pendown()

t.fillcolor("lightgreen")
t.begin_fill()

# Рисуем ромб

for _ in range(2):
   t.forward(100)
   t.right(60)
   t.forward(100)
   t.right(120)

t.end_fill()


# перемещение
t.penup()
t.goto(-120, -120)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()

# Рисуем трапецию
t.forward(50)
t.left(60)
t.forward(100)
t.left(120)
t.forward(150)
t.left(120)
t.forward(100)

t.end_fill()

t.hideturtle()
screen.exitonclick()
