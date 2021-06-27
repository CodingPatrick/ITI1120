# set is an UNORDERED collection of UNIQUE elements

#O(n)
def palindrom(words):
    '''(list of str) -> list of str'''
    pal = [] #1
    for item in words: #O(n)
        if item == item[::-1]: #O(n)
            pal.append(item) #O(n)
    return pal #1

#O(n^2)
def anonim(words):
    '''(list of str) -> list of str'''
    ano = [] #1
    for item in words: #O(n)
        if item[::-1] in words: #O(n^2)
            ano.append(item) #O(n)
    return ano #1
    

# ADD, REMOVE, IN

#racecar


wordlist = open('/usr/share/dict/words').read().lower()
print('The number of words in the English dictionary is ' + str(len(wordlist)))

p = palindrom(wordlist)
a = anonim(wordlist)
