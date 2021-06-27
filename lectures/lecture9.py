##s = 'today'
##for ch in s:
##    print(ch)

l = [1,2,3]

##for item in l:
##    print(item)

print(l)

total = 0
for item in l:
    total = total + item
print(total)

total = 0
for i in range( len(l) ):
    total = total + l[i]
print(total)
