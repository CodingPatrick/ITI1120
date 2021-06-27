import string

# Programming exercise 1

def m(i):
    if i == 1:
        return i / (2 * i + 1)
    else:
        return (i / (2 * i + 1)) + m(i-1)

##i = 1
##while i < 11:
##    print('m('+str(i)+') =', end=' ')
##    print(m(i))
##    i = i + 1

# Programming exercise 2

def count_digits(n):
    if n // 10 == 0:
        return 1
    else:
        return 1 + count_digits(n//10)

# Programming exercise 3

def is_palindrome(word):
    word = word.lower()
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])

# Programming exercise 4

def is_palindrome_v2(word):
    word = word.lower()
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return is_palindrome(word[1:-1])

# Programming exercise 5

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
