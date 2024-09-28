import turtle as t

t.speed(3)


t.color("red")
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(100, 0)
t.pendown()

t.color("green")
t.begin_fill()
t.circle(75)
t.end_fill()

t.penup()
t.goto(0, -160)
t.pendown()

t.color("blue")
t.begin_fill()
t.circle(100)
t.end_fill()
