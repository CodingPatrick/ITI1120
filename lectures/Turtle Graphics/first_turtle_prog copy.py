import turtle

wn=turtle.Screen()

alex=turtle.Turtle()

# drawing a rectangle
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.left(90)
alex.forward(150)
alex.left(90)
alex.forward(75)
alex.shape("turtle") 

alex.penup()
alex.goto(-100,-100)
alex.color("red", "green")
alex.pensize(7)
alex.pendown()
alex.begin_fill()
alex.circle(50)
alex.end_fill()

wn.exitonclick()



