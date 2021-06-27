# Course: ITI 1120
# Assignment number: a3
# Loranger, Patrick
# Student number: 300112374
# Year: 2019

########################################
# 1.3 - QUESTION #3
########################################

# function

def longest_run(l):
    '''
    (list of numbers) -> int

    Returns the length of the longest run in the list

    Preconditions: l has to be a list of numbers
    '''
    final = 0
    run = 1
    L = len(l)
    for i in range(0, L-1):
        if (l[i]) != (l[i+1]):
            if final < run:
                final = run
            run = 1
        else:
            final = final + 1
    if L == 1:
        final = run 
    return final


# main

list1 = input('Please input a list of numbers separated by spaces: ').strip().split()

list2 = [float(i) for i in list1] # This line of code has been declared in the declaration file

print(longest_run(list2))
