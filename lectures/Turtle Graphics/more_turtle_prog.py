import turtle
import time

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

alex.penup()
alex.pendown()


alex.reset()


# drawing a square
for sideNum in [1,2,3,4]:
     alex.forward(200)
     alex.left(90)

alex.reset()

# drawing a square
for sideNum in range(4):
     alex.forward(250)
     alex.left(90)

alex.reset()

## How would you draw an octagon?
##
## what was wrong here?
for sideNum in range(8):
     alex.forward(100)
     alex.left(135)
## you used interior angle when in fact the turn you make is interiro angle

alex.reset()

for sideNum in range(8):
     alex.forward(100)
     alex.left(180-135)

alex.reset()

## what if I do not want to rewrite every time this 
## the most general solution with variables

numberOfSides=8

for sideNum in range(numberOfSides):
     alex.forward(100)
     alex.left(360/numberOfSides)

alex.reset()

##CIRCLE:
numberOfSides=100

for sideNum in range(numberOfSides):
     alex.forward(1)
     alex.left(360/numberOfSides)

alex.reset()

##### MISSALENIOUS
alex.shape("turtle") 
##alex.reset()
##alex.backward(100) 
##alex.up() 
alex.color("red") 
alex.pensize(7) 
##alex.penup()
##alex.pendown() 
##alex.stamp() 
alex.circle(50)



for aColor in ["red", "blue", "yellow", "green", "purple"]:
     alex.shape("circle")
     alex.stamp() 
     alex.color(aColor)
     alex.forward(100)
     alex.left(72)

####################################################
### CRUCIAL BELOW ALLIGNMENT. If you move alex.forward in into else
#### it would do something completely different. show them

for sideNum in range(8):
     if sideNum % 2 == 0:
          alex.color("red")
     else:
          alex.color("green")
     alex.forward(100)
     alex.left(180-135)

##################################################

alex.reset()
### more general plus time.sleep

numberOfSides=8
for sideNum in range(numberOfSides):
     if sideNum % 2 == 0:
          alex.color("red")
     else:
          alex.color("green")
     time.sleep(1.5)
     alex.forward(100)
     alex.left(360/numberOfSides)

#####################

alex.reset()

###############################################
## ask user for input
#########
numberOfSides=int(input("Please enter the number of sides:\n"))
for sideNum in range(numberOfSides):
     if sideNum % 2 == 0:
          alex.color("red")
     else:
          alex.color("green")
     time.sleep(1.5)
     alex.forward(100)
     alex.left(360/numberOfSides)

#########################################
alex.reset()

print("Should I renumberOfSidesdraw all in red?")
colorAnswer=input()


if colorAnswer=="yes" or colorAnswer=="Yes":
     alex.color("red")

for i in range(numberOfSides):
     alex.forward(100)
     alex.left(360/numberOfSides)


wn.exitonclick()
