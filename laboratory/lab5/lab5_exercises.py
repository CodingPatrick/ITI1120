
# Programming exercise #1

def sum_odd_while_v2(n):
    '''
    (int) -> int
    Returns the sum of all odd integers between 5 and n
    '''
    i = 5
    num = 0
    while i <= n:
        num = num + i
        i = i + 2
    return num


# Programming exercise #2

answer = 'yes'
while answer.lower().strip() == 'yes':
    number1 = input('Enter a first integer: ')
    number2 = input("Enter a second integer: ")
    add = int(number1) + int(number2)
    print('The sum of', number1, 'and', number2, 'is', add)
    answer = input('Enter \'yes\' if want to add two more numbers: ')


# Programming exersise #3

def first_neg(l):
    '''
    (list of numbers) -> int or none
    Returns the index (i.e. the position in the list) of the first
    negative number in the list.
    '''

    i = 0
    while (i + 1) < len(l):
        if l[i + 1] < 0:
            return i + 1
        i = i + 1

# Programming exercise #4

def sum_5_consecutive(l):
    '''
    (list of numbers) -> bool (True, False)
    Returns True if there are 5 consecutive numbers in the list that sum to zero.
    Otherwise it returns False. The function should also return False if the list
    has less than 5 elements
    '''
    i = 0
    for i in range(len(l)):
        if (i + 4) >= len(l):
            return False
        if l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4] == 0:
            return True
    return False

def sum_5_consecutive_v2(l):
    '''
    (list of numbers) -> bool (True, False)
    Returns True if there are 5 consecutive numbers in the list that sum to zero.
    Otherwise it returns False. The function should also return False if the list
    has less than 5 elements
    '''
    i = 0
    while (i + 4) < len(l):
        if l[i] + l[i+1] + l[i+2] + l[i+3] + l[i+4] == 0:
            return True
        i = i + 1
    return False 


# Programming execise #6






    
