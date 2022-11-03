import turtle

t = turtle.Turtle()
s = turtle.Screen()
t.shape("turtle")
s.bgcolor("orange")

def triangle(x, y, color):
    t.penup()
    t.goto(x,y)
    t.begin_fill()
    t.color(color)
    t.pendown()
    for count in range(3):
        t.forward(50)
        t.left(120)
    t.end_fill()

def square(x, y, color):
    t.penup()
    t.goto(x,y)
    t.begin_fill()
    t.color(color)
    t.pendown()
    for i in range(3):
        t.forward(50)
        t.left(90)
    t.end_fill()

# capu
t.penup()
t.goto(0, -150)
t.color('#ff6600')
t.begin_fill()
t.circle(150)
t.end_fill()
t.left(180)

triangle(-35, -20, "black")
triangle(0, -20, "black")
triangle(35, -20, "black")
t.left(180)

triangle(-70,50,"black")
triangle(0,50,"black")

square(-20,125,'#663300')














turtle.mainloop()