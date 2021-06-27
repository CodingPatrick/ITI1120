import random

def merge_sort(L):
    '''list -> list
    Return sorted copy of L'''

    if len(L) <= 1:
        return L[:]

    middle = len(L) // 2
    left = merge_sort(L[:middle])
    right = merge_sort(L[middle:])
    return merge(left, right)
