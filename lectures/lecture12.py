def maximum(l):
    '''
    (list of int) -> int
    '''

    # n = len(l)

    current_max = l[0] # 1 operation
    
    for item in l:                  # n operations
        if item > current_max:      # n operations
            current_max = item      # <= n operations
    return current_max              # 1 operation
    
# <= 3n + 2 = O(n)

def maximum_v2(l):
    l.sort()        # X
    return l[-1]    # 1 operation

def positional_min(l1, l2):
    '''
    (list of ints, list of ints) -> bool
    Precondition: n = len(l1) == len(l2)
    '''

    # l1 : 1 3 10 22
    # l2 : 4 5  8 24
    
    for i in range(len(l1)):    # <= (at most) n operations
        if l1[i] >= l2[i]:      # <= n operations
            return False        # 1 operation
    return True

# <2n + 1 = O(n)

def duplicates(l):
    '''
    (list of ints) -> bool
    '''
    for i in range(len(l)):
        # i = 0     n
        # i = 1     n
        # i = 2     n
        # ...
        # i = n - 1 n
        for j in range(i + 1, len(l)): # n**2/2 + n/2
            if l[i] == l[j]:           # n**2/2 + n/2
                return True
    return False

< 1 + 2 + 3... (n-1) + n = (n + 1) * n/2
    
        
