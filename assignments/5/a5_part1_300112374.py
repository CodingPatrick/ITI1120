import string

def open_file():
    '''(None) -> file object
    Function will prompt the user for a file-name, and try to open that file. If the file exists,
    it will return the file object; otherwise it will re-prompt until it can successfully open the file.'''
    # YOUR CODE GOES HERE

    file = input('Please enter the name of the file you would like to open: ').strip()
    opened = False
    while opened == False:
        try:
            f = open(file)
            f.close()
            opened = True
        except FileNotFoundError:
            print('File does not exist')
            file = input('Please enter the name of the file you would like to open: ')
    return open(file)

def read_file(fp):
    '''(file object) -> dict
    Returns a dictionary with all the words in the file in question as keys, and the line they are in as sets.'''
    # YOUR CODE GOES HERE

    fp = fp.read() # reads the words in the file
    one = remove_punc(fp) # removes caps and punctuation
    fp2 = one.splitlines() # splits every line and makes a list
    two = splitter(fp2) # makes a 2D list
    three = get_needed(two) # takes only the needed words
    four = dictionary(three) # makes a dictionary
    return four

def find_coexistance(D, query):
    '''(dict,str) -> list
    Returns a sorted list of all the lines that the words in the query have in common inside the dictionary'''
    # YOUR CODE GOES HERE

    query = query.split()
    tmp = []
    mid = None
    net = []
    for i in query:
        if i not in D:
            return None
        tmp.append(i)
    if len(tmp) == 0:
        return None
    elif len(tmp) > 0:
        set1 = set(D[query[0]])
        for i in query:
            set2 = set(D[i])
        coexist = set.intersection(set2, set1)
        mid = list(coexist)
    for i in mid:
        if i not in net:
            net.append(i)
    net.sort()
    return net

def remove_punc(w):
    '''(string) -> string
    Removes all the punctuation and changes upper case letters to lower case'''
    newWords = ''
    for i in w:
        if i not in string.punctuation:
            newWords = newWords + i.lower()
    return newWords

def splitter(f):
    '''(list) -> 2D list
    Returns a 2D of all the words in the text file split into different list that represent each line'''
    newL = []
    for i in f:
        split = i.split()
        newL.append(split)
    return newL

def get_needed(l):
    '''(2D list) -> 2D list
    Returns a 2D list with only words that are longer or equal to 2 digits '''
    newL = []
    for i in range(len(l)):
        tmp = []
        for j in l[i]:
            if j.isalpha() and len(j) >= 2:
                tmp.append(j)
        newL.append(tmp)
    return newL

def dictionary(l):
    '''(2D list) -> dic
    Returns a dictionary based on the 2D list inserted into the function'''
    dictionary = {}
    
    for i in range(len(l)):
        for word in l[i]:
            if word not in dictionary:
                dictionary.update( {str(word) : {i+1}} )
            else:
                dictionary[word].add(i+1)
    return dictionary

def is_valid(D, query):
    '''(dict, str) -> bool or str
    Returns True if the query is in the dictionary and Returns the word if it isn't'''
    query = query.split()
    for i in query:
        if i not in D:
            return i
    return True

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()

# YOUR CODE GOES HERE

while query != 'q':
    query = remove_punc(query)

    if query == '':
        print("Word '' not in the file.")

    elif is_valid(d, query) != True:
        print("Word '" + is_valid(d, query) + "' not in the file.")

    else:
        find = find_coexistance(d, query)
        if len(find) == 0:
            print('The one or more words you entered do not coexist in this file')
        else:
            print('The one or more words you entered coexist in the following lines of the file: ')
            x = find_coexistance(d, query)
            for i in x:
                print(i, end=' ')
        print(' ')
    query = input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    

    
