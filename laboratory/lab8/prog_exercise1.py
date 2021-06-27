def linear_search_v1(lst, value):
    i = len(lst) - 1
    while i != -1 and lst[i] != value:
        i = i - 1
    if i == -1:
        return -1
    else:
        return i

def linear_search_v2(lst, value):
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == value:
            return i
    return -1

def linear_search_v3(lst, value):
    i = len(lst) - 1
    while lst[i] != value:
        i = i - 1
    lst.pop()
    if i == len(lst):
        return -1
    else:
        return i
    
