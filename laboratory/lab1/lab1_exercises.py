# Course: ITI 1120
# Assignment number: Lab 1 Exercices 1-4
# Loranger, Patrick
# Student number: 300112374


import math


# Programming exercises 1

def repeater(s1, s2, n):
    c = s1 + s2
    d = c * n
    e = '_' + d + '_'
    return e


# Programming exercises 2

def roots(a, b, c): 
    root1 = ((-b + math.sqrt(b**2 - 4 * a * c)) / 2 * a)
    root2 = ((-b - math.sqrt(b**2 - 4 * a * c)) / 2 * a)
    print("The quadratic equation with coefficients a=" + str(a) , "b=" + str(b), "c=" + str(c), "has the following solutions (i.e. roots): \n" + str(root1), "and " + str(root2))


# Programming exercices 3

def real_roots(a, b, c):
    p = (b**2 - 4 * a * c >= 0)
    return p


# Programming exercises 4

def reverse(x):
    y = x // 10
    g = x % 10
    return (g * 10 + y)
