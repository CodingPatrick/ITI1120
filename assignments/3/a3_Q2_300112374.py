# Course: ITI 1120
# Assignment number: a3
# Loranger, Patrick
# Student number: 300112374
# Year: 2019

########################################
# 1.2 - QUESTION #2
########################################

# function

def two_length_run(l):
    '''
    (list of numbers) -> bool

    Returns a bool statement given is the list has at least one run or not.

    Preconditions: l has to be a list of numbers
    '''
    for i in range(0, len(l)):
        if i == (len(l) - 1):
            return False
        elif l[i] != l[i+1]:
            i = i + 1
        else:
            return True

    
# main

list1 = input('Please input a list of numbers separated by spaces: ').strip().split()

list2 = [float(i) for i in list1] # This line of code has been declared in the declaration file

print(two_length_run(list2))

