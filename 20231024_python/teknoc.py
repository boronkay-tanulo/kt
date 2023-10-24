import turtle # ez a szükséges gyűjtemény
# innentől a turtle él. Ezzel együtt használhatjuk OOP
# alapokon is a tekit!

ablak = turtle.Screen()
# Ablak alapbeállítások
ablak.bgcolor("lightgreen")
ablak.setup(700, 700)
# Változók használata:
a = int(input("Kérem a téglalap hosszát! "))
b = int(input("Kérem a téglalap magasságát! "))
# teki.fd(mennyit) .left() .right() .fillcolor("szín") .begin_fill() .end_fill() .penup() .pendown()

def rajzol():
    teki.fillcolor("red")
    teki.begin_fill()
    teki.forward(a)
    teki.left(90)
    teki.forward(b)
    teki.left(90)
    teki.forward(a)
    teki.left(90)
    teki.forward(b)
    teki.end_fill()

def kilep():
    turtle.bye()

#ablak.onkey(eseménykezelő, "meghívó billentyű felirata")
#ablak.onscreenclick(eseménykezelő, 1-2-3) 1-bal, 3-jobb

ablak.onkey(rajzol, "1") # az 1 gomb lenyomására meghívja a rajzol() metódust
ablak.onkey(kilep, "2")

ablak.title("OTT A TEKI!!!")
teki = turtle.Turtle()
turtle.listen()

ablak.mainloop()