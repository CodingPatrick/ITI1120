import math

# Exercice 5.16
def indexes(word, letter):
    place = []
    for i in range(len(word)):
        if word[i] == letter:
            place.append(i)
    return place

# Exercice 5.17
def doubles(o):
    for i in range(len(o)-1):
        if o[i]*2 == o[i+1]:
            print(o[i+1])

# Exercice 5.18
def four_letter(l):
    fourletter = []
    for i in l:
        if len(i) == 4:
            fourletter.append(i)
    return fourletter

# Exercice 5.19
def inBoth(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

# Exercice 5.20
def intersect(list1, list2):
    newlist = []
    for i in list1:
        for j in list2:
            if i == j:
                newlist.append(i)
    return newlist

# Exercice 5.21
def pair(list1, list2, n):
    for i in list1:
        for j in list2:
            if int(i) + int(j) == n:
                print(str(i) + ' ' + str(j))

# Exercice 5.22
def pairSum(list1, n):
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            if list1[i] + list1[j] == n:
                print(str(i) + ' ' + str(j))

# Exercice 5.29
def lastfirst(l):
    firstnames = []
    lastnames = []
    for i in l:
        firstnames.append(i[i.find(',')+2:])
        lastnames.append(i[:i.find(',')])
    return [firstnames, lastnames]

# Exercice 5.31
def subsetSum(l, t):
    for i in l:
        for j in l:
            for y in l:
                if int(i) + int(j) + int(y) == t:
                    return True
    return False

# Exercice 5.33
def mystery(n):
    return int(math.floor(math.log(n,2)))

# Exercice 5.46
def inversions(string):
    count = 0
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] > string[j]:
                count = count +1
    return count

# Exercice 5.48
def sublist(list1, list2):
    newlist = []
    for i in list1:
        if i not in list2:
                return False
        else:
            newlist.append(list2.index(i))
    for p in range(len(newlist)-1):
        if newlist[p] > newlist[p+1]:
            return False
    return True

# Exercice 5.37
def mssl(l):
    total = 0
    temp = 0
    for i in range(1,len(l)+1):
        for u in range(len(l)):
            for j in range(len(l[u:u+i])):
                temp = temp + (l[u:u+i])[j]
            if temp > total:
                total = temp
            temp = 0
    return total
