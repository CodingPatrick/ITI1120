# recursive version of silly printer that prints:
# n n-1 .... 2 1 Blastoff
# Hight/Depth of recursion of function silly_printer1 (i.e the maximum number of functions silly_printer1
# running at the same time on the stack) is n+1
def silly_printer1(n):
    '''Precondition: n is positive integer'''
    if(n==0):
        print("Blastoff")
    else:
        print(n)
        silly_printer1(n-1)

# recursive version of silly printer that prints
# Blastoff 1 2 ... n
# Hight/Depth of recursion of function silly_printer2 (i.e the maximum number of functions silly_printer2
# running at the same time on the stack) is n+1
def silly_printer2(n):
    '''Precondition: n is a positive integer'''
    if(n==0):
        print("Blastoff")
    else:
        silly_printer2(n-1)
        print(n)


# recursive solution to factorial
# Hight/Depth of recursion of function fact (i.e the maximum number of functions fact
# running at the same time on the stack) is n+1
def fact(n):
    ''' (int)->int
    Returns n! = n*(n-1) .... 2*1
    Precondition: n>=1
    '''
    if n==0: # base case
        return 1
    else:
        partial=fact(n-1) # make recursive call to a smaller problem and then merge solutions           
        return n*partial

# iterative solution to factorial
def fact_i(n):
    ''' (int)->int
    Returns n! = n*(n-1) .... 2*1
    Precondition: n>=1
    '''
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    return fact


# rucursive solution; 
# Hight/Depth of recursion of function summer (i.e the maximum number of functions summer
# running at the same time on the stack) is n+1
def summer(a):
    '''(list)->number
    Returns the sum of the elements in the list a'''
    if len(a) == 0:
        return 0
    return a[0] + summer(a[1:])


# better solutiohn with smaller recurions depth:
# Hight/Depth of recursion of function summer2 (i.e the maximum number of functions summer2
# running at the same time on the stack) is O(log n),
# more specifically it is 1 + log_2 n
def summer2(a):
    '''(list)->number
    Returns the sum of the elements in the list a'''
    if len(a) == 1:
        return a[0]
    if len(a) == 0:
        return 0
    return summer2(a[:len(a)//2]) + summer2(a[len(a)//2:])
