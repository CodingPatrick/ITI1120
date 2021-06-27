def aha(l, x):
    '''
    (list, number) -> None
    Precondition: list has at least 1 element
    '''
    l[0] = 999
    x = 888

# main 
num = 100
t = [1,1,1]
aha(t, num)
print(num)
print(t)
