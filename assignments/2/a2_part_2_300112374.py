# Course: ITI 1120
# Assignment number: a2 part 2
# Loranger, Patrick
# Student number: 300112374
# Year: 2019

import math

##############################################
# Question 2.1
##############################################

def min_enclosing_rectangle(radius, x, y):
    '''
    (float, float, float) -> float, float

    Returns the x and y coordinates of the bottom-left corner of the smallest rectangle
    that would enclose the circle radius given.

    Preconditions: the radius has to be bigger or equal to zero to return something

    >>> min_enclosing_rectangle(4.5, 10, 2)
    (5.5, -2.5)
    '''
    returnx = x - radius
    returny = y - radius
    if radius >= 0:
        return returnx, returny
    else:
        return None

##############################################
# Question 2.2
##############################################

def series_sum():
    '''
    (none) -> float

    Asks the user to input a non-negative integer, the return the sum of the equation:
    1000 + 1/1**2 + 1/2**2 ...  + 1/h**2

    Preconditions: s_sum has to be a non-negative integer

    >>> series_sum()
    Please enter a non-negative integer: 5
    1001.463611111111
    '''
    seriessum = 1000
    s_sum = int(input('Please enter a non-negative integer: '))
    if s_sum >= 0:
        for h in range(1, s_sum + 1):
            seriessum = seriessum + (1/h**2)
        return seriessum
    else:
        return None

##############################################
# Question 2.3
##############################################

def pell(n):
    '''
    (int) -> int

    Returns the pell number of the value of n

    Preconditons: n has to be an integer, and for the function to return a number,
    n has to be a positive integer

    >>> pell(3)
    5
    '''
    
    n = int(n)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        # the rest of this code has been declared in declaration-PATRICK-LORANGER.txt
        a = 1
        b = 2
        for i in range(3, n+1) : 
            c = 2 * b + a 
            a = b 
            b = c 
        return b 

##############################################
# Question 2.4
##############################################

def countMembers(s):
    '''
    (str) -> int

    Returns the amount of extraordinary characters in the string s

    Preconditions: s has to be a string
    
    >>> countMember("one, Two")
    3
    '''
    
    members = 0
    for extra in s:
        if extra in 'efghijFGHIJKLMNOPQRSTUVWX23456!,\\':
            members = members + 1
    return members

##############################################
# Question 2.5
##############################################

def casual_number(s):
    '''
    (str) -> int

    Returns the value of the string s with an integer without any spaces or commas

    Preconditions: for it to return, s must not have any letters and must ressemble a number

    >>> casual_number("-1,000,001")
    -1000001
    '''
    
    ex = '-0123456789,'
    s = s.replace(',', '')
    for characters in s:
        if characters not in ex:
            return None
        else:
            return int(s)

##############################################
# Question 2.6
##############################################

def alienNumbers(s):
    '''
    (str) -> int

    Returns the integer value represented by the string s in alien communication

    Preconditions: s has to be only in the characters 'Ty!aNU' since aliens can only
    communicate with those symbols

    >>> alienNumbers("aaaUUU")
    129
    '''
    return (s.count("T") * 1024) + (s.count("y") * 598) + (s.count("!") * 121) + (s.count("a") * 42) +  (s.count("N") * 6) + (s.count("U") * 1)

##############################################
# Question 2.7
##############################################

def alienNumbersAgain(s):
    '''
    (str) -> int

    Returns the integer value represented by the string s in alien communication

    Preconditions: s has to be only in the characters 'Ty!aNU' since aliens can only
    communicate with those symbols

    >>> alienNumbers("aaaUUU")
    129
    '''
    
    add = 0
    for alien in s:
        if alien in 'T':
            add = add + 1024
        elif alien in 'y':
            add = add + 598
        elif alien in '!':
            add = add + 121
        elif alien in 'a':
            add = add + 42
        elif alien in 'N':
            add = add + 6
        elif alien in 'U':
            add = add + 1
    return add

##############################################
# Question 2.8
##############################################

def encrypt(s):
    '''
    (str) -> str

    Returns an encrypted version of the string s inputted into the function

    Preconditions: s has to be a string

    >>> encrypt("Hello, world")
    'dHlerlolwo ,'
    '''
    
    p = s[::-1]
    t = ''
    for i in range(len(s) // 2):
        t = t + p[i] + s[i]
    if len(s) % 2 != 0:
        t = t + s[len(s) // 2]
    return t

##############################################
# Question 2.9
##############################################

def oPify(s):
    '''
    (str) -> str

    Returns a string with the letters o and p inserted in between every pair of consecutive
    characters in s. The o and the p are capitalized depending on if the characters in s are
    capitalized or not.

    Preconditions: s has to be string

    >>> oPify(oOo)
    'ooPOOpo'
    '''
    inserter = ""
    characters = 1
    
    if len(s) > 1:
        for i in s:
            if characters > 1:
                if i in 'abcdefghijklmnopqrstuvwxyz':
                    if s[characters - 2] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        inserter = inserter + 'p' + i
                    else:
                        inserter = inserter + i  
                    if characters != len(s) and s[characters] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        inserter = inserter + 'o'
                elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if s[characters - 2] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                        inserter = inserter + 'P' + i 
                    else:
                        inserter = inserter + i 
                    if characters != len(s) and s[characters] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                        inserter = inserter + 'O'

            elif i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                if i in 'abcdefghijklmnopqrstuvwxyz':
                    if s[characters] in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        inserter = inserter + i + 'o'
                    else:
                        inserter = inserter + i
                elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    if s[characters] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
                        inserter = inserter + i + 'O'  
                    else:
                        inserter = inserter + i 
            else:
                inserter = inserter + i

            characters = characters + 1
                
    else:
        inserter = s

    return inserter

##############################################
# Question 2.10
##############################################

# don't know how to do it

def nonrepetitive(s):
    '''
    (str) -> bool (True or False)

    Returns a bool statement on wether the string s inserted into the function is
    repetitive or not. It will return True if the string is non repetitive and
    False otherwise.

    Preconditions: s has to be a string

    >>> nonrepetitive("abab")
    False
    '''
    for i in range(len(s)):
        return None
