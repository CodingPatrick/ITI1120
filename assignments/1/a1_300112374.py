# Course: ITI 1120
# Assignment number: a1
# Loranger, Patrick
# Student number: 300112374
# Year: 2019

import math

####################################
# Question 1
####################################

def pythagorean_pair(a, b):
    '''
    (int, int) -> bool (true, false)

    Returns a bool statement validating or falsifying the numbers as a pythagorean pair. 

    Precondition:
    '''
    c = (math.sqrt(a**2 + b**2) % 1 == 0)
    return bool(c)

####################################
# Question 2
####################################

def mh2kh(s):
    '''
    (number) -> number

    Returns the number of kilometers per hour given a number of miles per hour. 

    Precondition: s has to be a number
    '''
    k = s * 1.60934
    return k

####################################
# Question 3
####################################
 
def in_out(xs, ys, side):
    '''
    (float, float, positive number) -> bool (true, false)

    Returns a bool statement regarding if the given query point is inside the given square
    
    Preconditions: "side" has to be a positive number
    '''
    side >= 0
    a = input("Enter a number for the x coordinate of a query point: ")
    b = input("Enter a number for the y coordinate of a query point: ")
    a = (xs <= side) and (ys <= side)
    print (bool(a))

####################################
# Question 4
####################################

def safe(n):
    '''
    (float) -> bool (true, false)

    Returns a bool statement regarding if the function is safe or not
    
    Preconditions: n has to be within 0 and 100
    '''
    g = (n // 10 != 9) and (n % 10 != 9) and (n % 9 != 0) and (n >= 0) and (n <=100) and (n != [9, 19, 29, 39, 49, 59, 69, 79, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
    return bool(g)

####################################
# Question 5
####################################

def quote_maker(quote, name, year):
    '''
    (string, string, int) -> string

    Returns a sentence that states when the quote was said, who said the quote and the quote
    
    Preconditions: none
    '''
    st1 = str(quote)
    st2 = str(name)
    st3 = str(year)
    l = 'In ' + st3 + ', a person called ' + name + ' said: "' + quote + '"'
    return str(l)

####################################
# Question 6
####################################

def quote_displayer():
    '''
    (none) -> none

    Prints a sentence that states when the quote was said, who said the quote and the quote
    
    Preconditions: the year has to be an integer
    '''
    u = input("Enter any quote: ")
    e = input("Who said that? ")
    b = int (input("In what year did he or she say that? "))
    print (quote_maker(u, e, b))

####################################
# Question 7
####################################

def rps_winner():
    '''
    (none) -> print

    Retunrs a print of a two sentences declare who won the rock paper scissors game, or if it was a tie.
    
    Preconditions: the input has to be either "rock", "paper" or "scissors" in all lower case letters
    '''
    p = input("What is player 1's choice? \nType one of the following options: rock, paper, scissors: ")
    r = input("What is player 2's choice? \nType one of the following options: rock, paper, scissors: ")
    l = (p == 'rock' and r == 'scissors') or (p == 'paper' and r == 'rock' ) or (p == 'scissors' and r == 'paper')
    m = (p == 'rock' and r == 'rock') or (p == 'paper' and r == 'paper') or (p == 'scissors' and r == 'scissors')
    return print("Player 1 wins. That is " + str(bool(l)) + "\nIt is a tie. That is not " + str(bool(m)))

####################################
# Question 8
####################################

def fun(x):
    '''
    (float) -> float

    Returns the value 'y' of the equation 10**(4y) = x + 3

    Precondition: none
    '''
    f = (math.log10 (x + 3) / math.log10 (10)) / 4
    return f

####################################
# Question 9
####################################

def ascii_name_plaque(name):
    '''
    (string) -> print

    Returns a print of a name plaque with the name inserted into the function. 

    Precondition: 'name' has to be a string
    '''
    spaces = len(name) + 6
    line1 = "*" * (spaces + 8)
    line2 = "\n*" + (" " * (spaces + 6)) + "*"
    line3 = "\n*    __" + name + "__    *"
    line4 = "\n*" + (" " * (spaces + 6)) + "*"
    line5 = "\n" + ("*" * (spaces + 8))
    plaque = line1 + line2 + line3 + line4 + line5
    return print(plaque)

####################################
# Question 10
####################################

import turtle

def draw_train():
    '''
    (None) -> None

    Draws a train in turtle graphics when called upon

    Preconditions: none
    '''
    patrick = turtle.Screen()
    loranger = turtle.Turtle()
    turtle.bgcolor("light green")
    # move the pen
    loranger.up()
    loranger.pensize(6)
    loranger.goto(185, 35)
    loranger.pendown()
    # big box
    loranger.color("black", "dark red")
    loranger.begin_fill()
    loranger.forward(22.5)
    loranger.left(90)
    loranger.forward(160)
    loranger.left(90)
    loranger.forward(115)
    loranger.left(90)
    loranger.forward(160)
    loranger.left(90)
    loranger.forward(22.5)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(198, 115)
    loranger.pendown()
    # window
    loranger.color("black", "light blue")
    loranger.begin_fill()
    loranger.left(90)
    loranger.forward(70.5)
    loranger.left(90)
    loranger.forward(96)
    loranger.left(90)
    loranger.forward(70.5)
    loranger.left(90)
    loranger.forward(96)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(-25, 120)
    loranger.pendown()
    # light
    loranger.color("black", "light blue")
    loranger.begin_fill()
    loranger.left(180)
    loranger.circle(25, 180)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(92.5, 35)
    loranger.pendown()
    # small box
    loranger.color("black", "red")
    loranger.begin_fill()
    loranger.left(180)
    loranger.forward(130)
    loranger.right(90)
    loranger.forward(90)
    loranger.right(90)
    loranger.forward(130)
    loranger.right(90)
    loranger.forward(90)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(-25, 30)
    loranger.pendown()
    # small wheel 1
    loranger.color("black", "light grey")
    loranger.pensize(14)
    loranger.begin_fill()
    loranger.circle(20)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(35, 30)
    loranger.pendown()
    # small wheel 2
    loranger.begin_fill()
    loranger.circle(20)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(115, 40)
    loranger.pendown()
    # big wheel
    loranger.begin_fill()
    loranger.circle(35)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.pensize(6)
    loranger.goto(80, 195)
    loranger.pendown()
    # small box
    loranger.color("black", "dark red")
    loranger.begin_fill()
    loranger.left(90)
    loranger.forward(135)
    loranger.left(90)
    loranger.forward(10)
    loranger.left(90)
    loranger.forward(135)
    loranger.left(90)
    loranger.forward(10)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(65, 125)
    loranger.pendown()
    # pipe 1
    loranger.color("black", "red")
    loranger.begin_fill()
    loranger.right(90)
    loranger.forward(20)
    loranger.right(90)
    loranger.forward(25)
    loranger.right(90)
    loranger.forward(20)
    loranger.right(90)
    loranger.forward(25)
    loranger.end_fill()
    loranger.up()
    loranger.goto(65, 150)
    loranger.pendown()
    loranger.begin_fill()
    loranger.right(180)
    loranger.circle(10, 180)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(20, 125)
    loranger.pendown()
    # pipe 2
    loranger.begin_fill()
    loranger.right(90)
    loranger.forward(15)
    loranger.right(90)
    loranger.forward(20)
    loranger.right(90)
    loranger.forward(15)
    loranger.right(90)
    loranger.forward(20)
    loranger.end_fill()
    loranger.up()
    loranger.goto(20, 145)
    loranger.pendown()
    loranger.begin_fill()
    loranger.right(180)
    loranger.circle(7.5, 180)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(-25, 125)
    loranger.pendown()
    # steam pipe
    loranger.begin_fill()
    loranger.left(90)
    loranger.forward(10)
    loranger.left(90)
    loranger.forward(40)
    loranger.left(90)
    loranger.forward(10)
    loranger.left(90)
    loranger.forward(40)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(-25, 165)
    loranger.pendown()
    # triangle and top
    loranger.begin_fill()
    loranger.right(150)
    loranger.forward(40)
    loranger.right(120)
    loranger.forward(50)
    loranger.right(120)
    loranger.forward(40)
    loranger.end_fill()
    loranger.up()
    loranger.left(180)
    loranger.forward(40)
    loranger.pendown()
    loranger.begin_fill()
    loranger.left(60)
    loranger.forward(10)
    loranger.left(60)
    loranger.forward(40)
    loranger.left(60)
    loranger.forward(10)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(-40, 75)
    loranger.pendown()
    # wheel guard
    loranger.color("black", "light grey")
    loranger.begin_fill()
    loranger.forward(80)
    loranger.left(120)
    loranger.forward(40)
    loranger.left(90)
    loranger.forward(70)
    loranger.end_fill()
    # move the pen
    loranger.up()
    loranger.goto(-25, 30)
    loranger.pendown()
    # wheel attachment
    loranger.begin_fill()
    loranger.right(90)
    loranger.forward(80)
    loranger.right(90)
    loranger.forward(10)
    loranger.right(90)
    loranger.forward(80)
    loranger.right(90)
    loranger.forward(10)
    loranger.end_fill()

####################################
# Question 11
####################################

def alogical(u):
    '''
    (float) -> int

    Returns the number of times the number "u" can be divided by 2 to become less than 1. 

    Precondition: 'u' has to be bigger than 1
    '''
    u = round ((math.log (u, 2)) // 1 + 1)
    return u

####################################
# Question 12
####################################

# doesn't work for every case

def time_format(h, m):
    '''
    (int, int) -> string

    Returns a string that says the time inserted into the function, rounded up into a fancy way.

    Preconditions: h and m have to be integers that can be found on an english clock, which means from hour 0 to 24
    '''
    rounder = ((m // 5) * 5)
    if rounder == 0:
        return str(h) + " o' clock"
    elif rounder == 30:
        return "half past " + str(h) + " o' clock"
    elif rounder > 30:
        return str(rounder) + " minutes past " + str(h) + " o' clock"
    else:
        return str(60 - rounder) + " minutes to " + str(h + 1) + " o' clock"

####################################
# Question 13
####################################

def cad_cashier(price, payment):
    '''
    (float, float) -> float

    Returns a number with 2 decimals that shows how much change you should receive in CAD.

    Preconditions: price and payment have to be real positve numbers with 2 decimals only. Payment has to be bigger than price. 
    '''
    v = price / 5
    h = round(v, 2)
    w = payment - h * 5
    q = round(w, 2)
    return q

####################################
# Question 14
####################################

def min_CAD_coins(price, payment):
    '''
    (float, float) -> (int, int, int, int, int)

    Returns the smallest amount of coins necessary amount to the number of coins owed to the person who paid.

    Preconditions: price and payment have to be real positve numbers with 2 decimals only. Payment has to be bigger than price.
    '''
    money = cad_cashier(price, payment) * 100 // 1
    t = round( (money / 200) // 1 )
    money = money - (t * 200)
    l = round( (money / 100) // 1 )
    money = money - (l * 100)
    q = round( (money / 25) // 1 )
    money = money - (q * 25)
    d = round( (money / 10) // 1 )
    money = money - (d * 10)
    n = round( (money / 5) // 1 )
    return (t, l, q, d, n)
    
