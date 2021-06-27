##############################################

def only_vowels(phrase):
    '''
    (str) -> str

    Returns new string containing all the vowels from the phrase
    
    >>> only_vowels("August")
    'Auu'
    >>> only_vowels("TcDf")
    ''
    '''
    vowels = ''
    for ch in phrase:
        if ch in 'aeiouAEIOU':
            vowels = vowels + ch
    return vowels

##############################################

def count_vowels_v2(word):
    return len( only_vowels(word) )
    

##############################################

def count_vowels(phrase):
    '''
    (str) -> int

    Returns the number of vowels in the given phrase
    
    >>> count_vowels("August")
    3
    >>> count_vowels("BCD")
    0
    '''
    num_of_vowels = 0
    for ch in phrase:
        if ch in 'aeiouAEIOU':
            num_of_vowels = num_of_vowels + 1
            # num_of_vowels += 1
            # same thing ^, just removes the second call to num_of_vowels
    return num_of_vowels

##############################################

def print_vowels(phrase):
    '''
    (str) -> none

    Prints vowels in a given phrase
    '''
    for char in phrase:
        if char in 'aeiouAEIOU':
            print(char)
    print('Goodbye')

##############################################

for c in range(10,0,-1):
    print(c)
print("blastoff")
    
##############################################

for i in range(10**100):
    if i % 2 == 0:
        print(i)

##############################################


