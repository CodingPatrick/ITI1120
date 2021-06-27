# Programming Exercise 1

def ah(l, x, y):
    count = 0
    list1 = []
    for i in range( len(l) ):
        if l[i] >= x and l[i] <=y:
            count = count + 1
            list1.append(l[i])
    number = min(list1)

    return count,number
    

# Programming Exercise 2

def is_perfect(n):
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i = i + 1

    return (True if sum == n and n != 1 else False)
    

# Programming Exercise 3a

def arithmetic(l):
    y = l[1] - l[0]
    for i in range(1, len(l)):
        if l[i+1] - l[i] != y:
            return False
    return True
        

# Programming Exercise 3b




