
import turtle
import random


#goal landscape is to draw a night mountain/forest scene
#functions
#shape 1--trees
def trees(x,y, leaves_color, trunk_color):
    #bottom
    turtle.penup()
    turtle.goto(x,y-75)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.fillcolor(leaves_color)
    turtle.goto(x+125,y-75)
    turtle.goto(x,y+50)
    turtle.goto(x-125,y-75)
    turtle.goto(x,y-75)
    turtle.penup()
    turtle.end_fill()
    
    #middle
    turtle.penup()
    turtle.goto(x,y)
    turtle.color("black")
    turtle.begin_fill()
    turtle.fillcolor(leaves_color)
    turtle.pensize(8)
    turtle.pendown()
    turtle.goto(x+100,y)
    turtle.goto(x,y+100)
    turtle.goto(x-100,y)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.penup()
    #top
    turtle.goto(x,y+75)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.fillcolor(leaves_color)
    turtle.goto(x+50,y+75)
    turtle.goto(x,y+120)
    turtle.goto(x-50,y+75)
    turtle.goto(x,y+75)
    turtle.penup()
    turtle.end_fill()

    #bark
    turtle.goto(x,y-100)
    turtle.pendown()
    turtle.color("black")
    turtle.begin_fill()
    turtle.fillcolor(trunk_color)
    for i in range(0,4):
        turtle.left(90)
        turtle.forward(20)
    turtle.penup()
    turtle.end_fill()
#shape 2--clouds
def clouds(x,y,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.color(color)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pensize(8)
    turtle.circle(50)
    turtle.penup()
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x,y-20)
    turtle.color(color)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pensize(8)
    turtle.circle(50)
    turtle.penup()
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x+30,y+10)
    turtle.color(color)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pensize(8)
    turtle.circle(50)
    turtle.penup()
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x+50,y-10)
    turtle.color(color)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pensize(8)
    turtle.circle(50)
    turtle.penup()
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x-30,y+10)
    turtle.color(color)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pensize(8)
    turtle.circle(50)
    turtle.penup()
    turtle.end_fill()

    turtle.penup()
    turtle.goto(x-50,y-10)
    turtle.color(color)
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pensize(8)
    turtle.circle(50)
    turtle.penup()
    turtle.end_fill()

    
#shape 3--mountains
def mountains(x,y, color, snow_color):
    #mountain
    turtle.penup()
    turtle.goto(x,y)

    turtle.color("black")
    turtle.begin_fill()
    turtle.fillcolor(color)
    turtle.pensize(8)
    turtle.pendown()
    turtle.goto(x+200,y)

    turtle.goto(x,y+300)
    turtle.goto(x-200,y)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.penup()

    turtle.goto(x,y+250)
    
    #snow
    turtle.color("black")
    turtle.begin_fill()
    turtle.fillcolor(snow_color)
    turtle.pendown()
    turtle.goto(x+35,y+250)
    turtle.goto(x,y+300)
    turtle.goto(x-35,y+250)
    turtle.goto(x,y+250)
    turtle.penup()
    turtle.end_fill()
#shape 4--flowers
def flowers(x,y, center_color, petal_color, num_petals):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    for i in range(num_petals):
        turtle.forward(40)
        turtle.dot(200/num_petals, petal_color)
        turtle.forward(-40)
        turtle.right(360/num_petals)
    turtle.color(center_color)
    turtle.dot(75)
    turtle.penup()

#shape 5--stars
def stars(x,y,color):
    count = 1
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    while count <= 5:
        turtle.forward(60)
        turtle.right(144)
        count = count + 1
    turtle.end_fill()
    turtle.penup()


#shape 6--moon
def moon(x,y,typ,color):
    if typ == "crescent":
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()
        turtle.goto(x+50,y)
        turtle.pendown()
        turtle.color("black")
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()
    elif typ == "full":
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(100)
        turtle.end_fill()
        turtle.penup()
    elif typ == "half":
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown
        turtle.color(color)
        turtle.begin_fill()
        turtle.circle(100, -180)
        turtle.end_fill()
        turtle.penup()
    else:
        return

#set up turtle, make background black
turtle.setup(1000,1000,0,0)
turtle.speed(10)
turtle.penup()
turtle.goto(-500,-500)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(1000)
    turtle.left(90)
turtle.end_fill()
turtle.penup()

#draw stars
try:
    num=int(turtle.textinput("stars" ,"Enter how many stars you would like from 1 to 30:"))
    color=turtle.textinput("stars" ,"Enter what color the stars should be:")
    for i in range(0,num):
        x=random.randint(-500,500)
        y=random.randint(-200,500)
        stars(x,y,color)
except:
    turtle.textinput("Invalid Entry" ,"Sorry! Invalid entry. Enter in any value and press OK to continue.")
#draw moon
typ=turtle.textinput("moon" ,"Enter what kind of moon you want (i.e. crescent, full, or half")
color=turtle.textinput("moon" ,"Enter what color the moon should be:")
moon(-300,300,typ,color)
#draw clouds
try:
    num=int(turtle.textinput("clouds" ,"Enter how many clouds you would like (from 1 to 2):"))
    color=turtle.textinput("clouds" ,"Enter what color the clouds should be:")
    for i in range(0,num):
        x=random.randint(-500,500)
        y=random.randint(-200,300)
        clouds(x,y,color)
except:
    turtle.textinput("Invalid Entry" ,"Sorry! Invalid entry. Enter in any value and press OK to continue.")
#draw grass
turtle.goto(-500,-500)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
turtle.forward(1000)
turtle.left(90)
turtle.forward(300)
turtle.left(90)
turtle.forward(1000)
turtle.left(90)
turtle.forward(300)
turtle.end_fill()
turtle.penup()

#draw mountains
try:
    num=int(turtle.textinput("mountains" ,"Enter how many mountains you would like (from 1 to 3):"))
    color=turtle.textinput("mountains" ,"Enter what color the mountains should be:")
    snow_color=turtle.textinput("mountains" ,"Enter what color the snow on the mountains should be:")

    for i in range(0,num):
        x=random.randint(-500,500)
        mountains(x,-200,color,snow_color)
except:
    turtle.textinput("Invalid Entry" ,"Sorry! Invalid entry. Enter in any value and press OK to continue.")
#draw trees
try:
    num=int(turtle.textinput("trees" ,"Enter how many trees you would like (from 1 to 10):"))
    leaves=turtle.textinput("trees" ,"Enter what color the leaves of the tree should be:")
    bark=turtle.textinput("trees" ,"Enter what color the tree bark should be:")

    for i in range(0,num):
        x=random.randint(-500,500)
        y=random.randint(-300,-100)
        trees(x, y, leaves, bark)

except:
    turtle.textinput("Invalid Entry" ,"Sorry! Invalid entry. Enter in any value and press OK to continue.")
#draw flowers
try:
    num=int(turtle.textinput("flowers" ,"Enter how many flowers you would like (from 1 to 10):"))
    num_petals=int(turtle.textinput("flowers" ,"Enter how many petals you would like (from 1 to 10):"))
    petal_color=turtle.textinput("flowers" ,"Enter what color the petals are:")
    center=turtle.textinput("flowers" ,"Enter what color the center of the flower is:")

    for i in range(0,num):
        x=random.randint(-500,500)
        y=random.randint(-450,-250)
        flowers(x, y, center,petal_color,num_petals)

except:
    turtle.textinput("Invalid Entry" ,"Sorry! Invalid entry. Enter in any value and press OK to continue.")

