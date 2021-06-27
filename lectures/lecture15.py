def is_diagonal(m):
    ''' (2D list of ints) -> bool '''
    # raws = len(m)
    for i in range(len(m)):
        # m[i] is a raw
        if len(m) != len(m[i]):
            return False
    for i in range(len(m)):
        # m[i] in a row
        for j in range(len(m[i])):
            # m[i][j] items in matrix
            if m[i][j] != 0 and i != j:
                return False
    return True

#############################################################################################

def frequency(a):
    ''' (list of objects) -> 2D list '''
    f=[]
    for i in range(len(a)):
        # a[i] city
        flag = False
        for j in range(len(f)):
            # f[j] little list if 2 elements
            if a[i] == f[j][0]:
                f[j][1] = f[j][1]+1
                flag = True
        if flag == False:
            f.append([a[i],1])
    return f

def distinct(l):
    ''' (list of objects) -> int '''
    return len(frequency(l))

def unique(l):
    ''' (list of objects) -> bool '''
    return len(frequency(l)) == len(l)


cities = ['mostar', 'sarajevo', 'paris', 'melbourne', 'mostar', 'melbourne', 'melbourne']
# [ ['mostar', 2], ['sarajevo', 1], ['paris', 1], ['melbourne', 3] ]

# l1 = ['mostar', 'sarajevo', 'paris', 'melbourne']
# l2 = [2,1,1,2]

print(frequency(cities))
