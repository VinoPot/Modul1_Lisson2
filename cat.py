import turtle as t


def draw_circle(color, radius, x, y):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def draw_ear(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("pink")
    t.begin_fill()
    t.goto(x - 20, y + 50)
    t.goto(x + 20, y + 50)
    t.goto(x, y)
    t.end_fill()


def draw_face():
    draw_circle("orange", 100, 0, 0)  # Голова

    draw_circle("white", 15, -35, 30)  
    draw_circle("white", 15, 35, 30)  

    draw_circle("black", 6, -35, 35)  
    draw_circle("black", 6, 35, 35) 

    draw_circle("pink", 10, 0, 10)  # Нос

    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.setheading(-60)  
    t.circle(20, 120)  

    # Усы
    t.penup()
    t.goto(-30, 0)
    t.pendown()
    t.goto(-70, 0)

    t.penup()
    t.goto(30, 0)
    t.pendown()
    t.goto(70, 0)


def main():
    t.speed(3)
    draw_face()

    # уши
    draw_ear(-60, 80)  # Левое ухо
    draw_ear(60, 80)  # Правое ухо

    t.hideturtle()  
    t.done()  


if __name__ == "__main__":
    main()
