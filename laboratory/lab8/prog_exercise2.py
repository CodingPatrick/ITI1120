def min_or_max_index(lst, bl):
    if bl:
        return get_min(lst)
    else:
        return get_max(lst)
      
def get_max(lst):
    mx = lst[0]
    index = 0
    for i in range(len(lst)):
        if lst[i] > mx:
            mx = lst[i]
            index = i
    return (mx, index)
        

def get_min(lst):
    mn = lst[0]
    index = 0
    for i in range(len(lst)):
        if lst[i] < mn:
            mn = lst[i]
            index = i
    return (mn, index)
