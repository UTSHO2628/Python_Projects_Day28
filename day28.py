# "Why did you breal my heart?" Grhpics show project 
from turtle import *
bgcolor('white')
pencolor('red')
fillcolor('red')
pensize(10)

penup()
goto(0, -70)
pendown()
begin_fill()
lt(42)
fd(180)
circle(82, 200)
rt(127)
circle(82, 200)
fd(180)


pencolor('black')
penup()
goto(6, 162)
pendown()
right(70)
fd(40)
left(80)
fd(30)
right(80)
fd(35)
left(80)
fd(30)
right(90)
fd(30)
left(90)
fd(20)
right(68)
fd(100)

penup()
goto(-220, -150)
pendown()
pencolor('black')
style = ("arial", 25, "bold",)
txt = "Why did you breal my heart?"
write(txt, font=style)
hideturtle()
done()