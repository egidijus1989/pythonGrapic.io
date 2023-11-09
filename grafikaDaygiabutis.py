import turtle 

s = turtle.Screen() 
t = turtle.Turtle()

t.pensize(1) 
t.speed(0) # 0 greiciausias, 1 leciausias 10 greitas 

t.penup() 
t.goto(100, -350) 
t.pendown() 

aukstisNamo = 600
plotisNamo = 300
color = "magenta"
langaiAukste = 6
aukstai = 6


def aukstis(x):
    t.lt(90)
    t.forward(x)
def plotis(x):
    t.lt(90)
    t.forward(x)

def daugiabutis(a, x, y):
    t.fillcolor(a)
    t.begin_fill()
    aukstis(x)
    plotis(y)  
    aukstis(x)
    plotis(y)
    t.end_fill()
    t.backward(y * 0.85)
    t.penup()
    t.lt(90)
    t.forward(x * 0.85)
    t.pendown()
    t.rt(90)

def langas(x, y):
    aukstis(x/10)
    plotis(y/10)  
    aukstis(x/10)
    plotis(y/10)
    t.lt(90)
    t.forward(x/20)
    t.lt(90)
    t.forward(y/10)
    t.backward(y/20)
    t.lt(90)
    t.forward(x/20)
    t.lt(90)

def languEile(x, y, z):
    for i in range(x):
        langas(y, z)
        t.penup()
        t.forward(z * 0.2)
        t.pendown()

def languStulpelis(x, y, z, a):
    for i in range (x):
        t.penup()
        t.rt(90)
        t.forward(y * 0.15)
        t.lt(90)
        t.backward(z * 0.9)
        t.pendown()
        for i in range(a):
            langas(y, z)
            t.penup()
            t.forward(z * 0.2)
            t.pendown()

def daugiabutisPilnas():
    daugiabutis(color, aukstisNamo, plotisNamo)
    languEile(langaiAukste, aukstisNamo, plotisNamo)
    languStulpelis(aukstai -1, aukstisNamo, plotisNamo, langaiAukste)
# daugiabutis(color, aukstisNamo, plotisNamo)
# languEile(langaiAukste, aukstisNamo, plotisNamo)
# languStulpelis(aukstai, aukstisNamo, plotisNamo)

daugiabutisPilnas()
s.exitonclick() 