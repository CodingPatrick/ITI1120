# Course: ITI 1120
# Assignment number: Lab 2 Exercice 3b
# Loranger, Patrick
# Student number: 300112374

def is_divisible(n, m):
    return n % m == 0

def is_divisible23n8(t):
    if((is_divisible(t,2) or is_divisible(t,3)) and not (is_divisible(t,8))):
       return "yes"
    else:
        return "no"

f = int(input("Enter an integer: "))

if (is_divisible23n8(f) == 'yes'):
    print(f, "is divisible by 2 or 3 but not 8")
else:
    print("It is not true that ", f, " is divisible by 2 or 3 but not 8")
