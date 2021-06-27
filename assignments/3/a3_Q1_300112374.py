# Course: ITI 1120
# Assignment number: a3
# Loranger, Patrick
# Student number: 300112374
# Year: 2019

########################################
# 1.1 - QUESTION #1
########################################

# function

def number_divisible(l, n):
    '''
    (list of ints) -> int

    Returns the number of elements in the list that are divisible by n

    Preconditions: l has to be a list of numbers
    '''
    num = 0
    for i in l:
        if i % n == 0:
            num = num + 1
    return num


# main

list1 = input('Please input a list of numbers separated by spaces: ').strip().split()

list2 = [int(i) for i in list1] # This line of code has been declared in the declaration file

n = int(input('Please input and integer: '))
print('The number of elements divisible by', n, 'is ', number_divisible(list2, n))

