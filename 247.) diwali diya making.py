#importing modules
from tkinter.font import ITALIC
from tkinter.ttk import Style
import turtle
import colorsys
import random

#screen setup
screen=turtle.Screen()
screen.setup(1350,650)
screen.bgcolor('#7fffd4')
t=turtle.Turtle()
turtle.title("Diwali wishes to everyone.....")

#function for crackers
def draw_firecrackers(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#diya making
t.up()
t.color("BROWN")
t.fillcolor("BROWN")
t.setpos(-200,150)
t.down()
t.right(90)
t.begin_fill()
t.circle(200,180)
t.left(90)
t.forward(400)
t.end_fill()
t.up()
t.color("BLACK")
t.back(200)
t.right(90)
t.down()
t.forward(50)
t.right(90)
t.up()
t.color("#e6e854")
t.fillcolor("#e6e854")
t.begin_fill()
t.setpos(-50,250)
t.right(90)
t.down()
t.circle(50,180)
t.left(30)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()
#font writing
t.up()
t.setpos(-340,-200)
t.color("#808000")
t.down()
t.write("HAPPY DIWALI  ❁💥❁💥", font = ("Lucida Handwriting",55))
t.hideturtle()
#patakhee
t.color("red")
angle=0
for i in range(20):
    #move in forward direction
    t.fd(50)

    #calling the function and initializing the values
    draw_firecrackers(300,180)

    #changing the angle of pointer
    angle+=18

    t.left(angle)
draw_firecrackers(450,180)

#color of the firecracker
t.color("blue")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(450,180)
draw_firecrackers(375,300)

#color of the firecracker
t.color("green")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(375,300)
draw_firecrackers(375,-300)

#color of the firecracker
t.color("orange")
angle=0
for i in range(20):
    t.fd(50)
    angle+=18
    t.left(angle)
    draw_firecrackers(375,-300)
draw_firecrackers(330,300)


#credit xddd
t.up()
t.setpos(10,-230)
t.color("#808000")
t.down()
t.write("-----Prachiiiiiii❁", font = ("Lucida Handwriting",20))
t.hideturtle()
