def power_set(L):
    ''' (list) -> 2D list
    >>> power_set([1,2,3])
    [ [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3] ]'''

    if len(L) == 0:
        return [ [] ]

    pps = power_set(L[1:])

    fps = pps[:]

    for item in pps:
        fps.append(item + [ L [0] ])

    return fps

##########
## Power recursion : 

def mypow(x, n):
    '''(int, int) -> int
    Preconditions: x is non 0 and n is non negative'''

    if n == 0:
        return 1
    return x * my_power(x, n-1)

def mypow_v2(x, n):
    '''(int, int) -> int
    Preconditions: x is non 0 and n is non negative'''

    if n == 0:
        return 1
    res = mypow_v2(x, n//2)
    if n == 1:
        return res * res
    else:
        return x * res * res

def mypow_v3(x, n):
    p = 1
    for i in range(n):
        p = p * x
    return p
