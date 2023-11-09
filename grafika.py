import turtle 

s = turtle.Screen() 

t = turtle.Turtle() 

colors1 = ['green', 'blue', 'violet', 'red'] 

colors2 = ['indigo', 'magenta', 'powderblue', 'khaki', 'salmon', 'tomato', 'lime'] 

laipsniai = 360 

kampas1 = 4 

kampas2 = 6 

 
 

t.pensize(5) 

t.speed(0) # 0 greiciausias, 1 leciausias 10 greitas 

t.penup() 

t.goto(100, -350) 

t.pendown() 

 
 

# t.penup() 

# t.goto(-450, 300) 

# t.pendown() 

# for i in range(5): 

#     t.penup() 

#     t.forward(150) 

#     t.pendown() 

#     for j in range(kampas1): 

#         t.lt(laipsniai/kampas1) 

#         t.pencolor(colors1[j%len(colors1)]) 

#         t.fd(100) 

             

# t.penup() 

# t.goto(-100, 0) 

# t.pendown() 

# for a in range(6): 

#     t.fillcolor(colors2[a%len(colors2)]) 

#     t.begin_fill() 

#     for b in range(kampas2): 

#         t.lt(laipsniai/kampas2) 

#         t.fd(100)    

#     t.end_fill() 

#     t.rt(laipsniai/kampas2) 

#     t.forward(100) 

 
 

plotisN = 300 

aukstisN = 600 

t.penup() 

t.goto(-450, 300) 

t.pendown() 

t.fillcolor('powderblue') 

t.begin_fill() 

t.forward(plotisN) 

t.rt(90) 

t.forward(aukstisN) 

t.rt(90) 

t.forward(plotisN) 

t.rt(90) 

t.forward(aukstisN) 

t.rt(90) 

t.end_fill() 

 
 

def langas(x): 

    t.pensize(1) 

    t.forward(plotisN/10) 

    t.rt(90) 

    t.forward(aukstisN/10) 

    t.rt(90) 

    t.forward(plotisN/10) 

    t.rt(90) 

    t.forward(aukstisN/10) 

    t.rt(90) 

    t.penup() 

    t.rt(90) 

    t.forward(aukstisN/20) 

    t.pendown() 

    t.lt(90) 

    t.forward(plotisN/10) 

    t.rt(90) 

    t.forward(aukstisN/20) 

    t.rt(90) 

    t.forward(plotisN/20) 

    t.rt(90) 

    t.forward(aukstisN/20) 

    t.penup() 

    t.forward(aukstisN/20) 

    t.rt(90) 

    t.forward(plotisN/20) 

    t.pendown() 

     

for j in range(6): 

    t.rt(90) 

    t.forward(aukstisN/20) 

    t.lt(90) 

    for i in range(6): 

        t.forward(plotisN/20) 

        langas(i) 

 
 

     

s.exitonclick() 
