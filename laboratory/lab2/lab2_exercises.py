# Course: ITI 1120
# Assignment number: Lab 2 Exercices 1-3a
# Loranger, Patrick
# Student number: 300112374

####################################
# Question 1
####################################

def pay(wage, hours):
    if hours <= 40:
        p = wage * hours
    elif hours > 40 and hours <= 60:
        p = (wage * 40) + (wage * 1.5 * (hours - 40))
    else:
        p = (wage * 40) + (wage * 1.5 * 20) + (wage * 2 * (hours - 60))
    return p

####################################
# Question 2
####################################

def rps(choice1, choice2):
    if choice1 == 'R' and choice2 == 'S':
        d = -1
    elif choice1 == 'R' and choice2 == 'P':
        d = 1
    elif choice1 == 'P' and choice2 == 'R':
        d = -1
    elif choice1 == 'P' and choice2 == 'S':
        d = 1
    elif choice1 == 'S' and choice2 == 'P':
        d = -1
    elif choice1 == 'S' and choice2 == 'R':
        d = 1
    else:
        d = 0
    return d

####################################
# Question 3a
####################################

def is_divisible(n, m):
    return n % m == 0

n = int(input("Enter 1st integer: "))
m = int(input("Enter 2nd integer: "))

if (is_divisible(n, m)):
    print(n, "is divisible by", m)
else:
    print(n, "is not divisible by", m)
