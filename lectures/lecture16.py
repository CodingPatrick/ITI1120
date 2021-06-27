# O(n)
def linear_search(L, v):
    '''(list of Obj, Obj) -> int'''
    n = len(L)
    for i in range(n):
        if L[i] == v:
            return i
        return -1

def binary_search(L, v):
    '''(list of Obj, Obj) -> int
    Precondition: L is sorted'''
    b = 0
    e = len(L) - 1
    while b <= e:
        mid = (b + e) // 2
        if v < L[mid]:
            e = mid - 1
        elif v > L[mid]:
            b = mid + 1
        else: # v == L[mid]
            return mid
    return -1
        
    
# k largest: L, k

# Algorithm 1
  # Step 1. sort L #O(n*log n)
  # Step 2. return the last k elements #O(k)
# O(n*log n)


# Algorithm 2
# repeat k times:
  # Step 1. find the max #O(n)
  # Step 2. add that max to the results #O(1)
  # Step 3. remove that max from L #O(n)
# O(k*n)

# When is n*k < n*log n


def selection_sort(L):
    '''(list) -> None'''
    for i in range(len(L)-1):
        # repeat
        # find the min in the current list [i, ..., end]
        index_min = i
        for j in range(i+1,len(L)):
            if L[j] > L[index_min]:
                index_min = j
        # Swap L[i] and the min of current
        tmp = L[i]
        L[i] = current_min
        L[index_min] = tmp





