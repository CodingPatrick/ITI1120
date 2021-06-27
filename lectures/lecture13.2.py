def swap(a,b):
    tmp = a
    a = b
    b= tmp

##def swap_firstlast(l):
##    '''
##    Precondition: l has 2 elements
##    '''
##    tmp = l[0]
##    l[0] = l[1]
##    l[1] = tmp

def swap_firstlast(l):
    '''
    Precondition: l has 2 elements
    '''
    l = [l[1], l[0]]

l = [100,1]
print(l)
swap_firstlast(l)
print(l)

# swap

##a = 100
##b = 1
##
##print(a,b)
##
##swap(a,b)
##
##print(a,b)


def triplicates(l):
    '''
    (list) -> bool
    '''
    n = len(l)
    for i in range(n): # n
        for j in range(i+1, n): # < n^2
            for k in range(j+1, n): # < n^3
                if l[i] == l[j] and l[j] == l[k]: #< n^3
                    return True
    return False

# 1 + n + n^2 + 2*n^3 = O(n^3)

def count(l,x):
    '''
    (list of objects, object) -> int
    '''
    counter = 0
    for item in l:
        if item == x:
            counter = counter + 1
    return counter

def k_thesame(l,k):
    '''
    (list, int) -> bool
    '''
    for item in l: # n
        if count(l, item) >= k: # n * n = n^2
            return True
    return False

# 1 + n + n^2 = O(n^2)

def k_thesame_viasort(l,k):
    l.sort() #O(n* log n)
    for i in range(len(l)-k+1): # <= n
        if l[i] == l[i+k-1]: # <= n
            return True
    return False

# n* log n + 2n + 1 = O(n * log n)
    
