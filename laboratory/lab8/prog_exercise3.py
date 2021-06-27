def first_one(L):
    begin = 0
    end = len(L)- 1

    while end - begin > 1:
        mid = (begin + end) // 2
        key = L[mid]
        if key == 0:
            begin = mid + 1
        elif key == 1:
            end = mid - 1
    if L[begin] == 1:
        return begin
    if L[end] == 1:
        return end
    return -1
