import turtle

ablak = turtle.Screen()
teki = turtle.Turtle()

ablak.title("Feladatok")

def feladat1():
    # 1. háromszög
    teki.fillcolor("blue")
    teki.begin_fill()
    teki.left(60)
    for i in range(3):
        teki.forward(60)
        if i < 2: teki.right(120)
    teki.end_fill()
    # 2. háromszög
    teki.fillcolor("red")
    teki.begin_fill()
    teki.forward(90)
    for i in range(2):
        teki.right(120)
        teki.forward(90)
    teki.end_fill()
    # 3. háromszög
    teki.fillcolor("yellow")
    teki.begin_fill()
    for i in range(3):
        teki.forward(120)
        teki.right(120)
    teki.end_fill()
    teki.left(150)

def feladat2():
    def kor(r):
        fej = teki.heading()
        teki.setheading(0)
        teki.sety(teki.ycor() + r)
        teki.pendown()
        for _ in range(120):
            teki.right(3)
            teki.fd(3)
        teki.penup()
        teki.sety(teki.ycor() - r)
        teki.setheading(fej)
    ablak.bgcolor("yellow")
    teki.pencolor("brown")
    teki.right(90)
    teki.penup()
    for _ in range(3):
        kor(60)
        teki.right(120)
        teki.fd(80)
    teki.bk(80)
    teki.fd(55)
    teki.left(90)

def feladat3():
    szinek = {3: "yellow", 4: "red", 5: "green", 6: "blue", 7: "cyan", 8: "violet", 9: "orange"}
    def rajzol(n):
        teki.fillcolor(szinek[n])
        teki.begin_fill()
        for _ in range(n):
            teki.forward(100)
            teki.left(360 / n)
        teki.end_fill()
    ablak.onkey(turtle.bye, '1')
    ablak.onkey(turtle.bye, '2')
    ablak.onkey(lambda: rajzol(3), '3')
    ablak.onkey(lambda: rajzol(4), '4')
    ablak.onkey(lambda: rajzol(5), '5')
    ablak.onkey(lambda: rajzol(6), '6')
    ablak.onkey(lambda: rajzol(7), '7')
    ablak.onkey(lambda: rajzol(8), '8')
    ablak.onkey(lambda: rajzol(9), '9')
    ablak.listen()

ablak.onkey(feladat1, '1')
ablak.onkey(feladat2, '2')
ablak.onkey(feladat3, '3')
ablak.listen()
ablak.mainloop()
