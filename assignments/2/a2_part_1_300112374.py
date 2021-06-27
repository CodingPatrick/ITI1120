# Course: ITI 1120
# Assignment number: a2 part 1
# Loranger, Patrick
# Student number: 300112374
# Year: 2019

################################################
# split_tester(N, d) function
################################################

def split_tester(N, d):
    '''
    (str, str) -> bool (True or False)

    Returns a bool statement on wether the splits created by the function are increasing or not

    Preconditions: N and d have to be strings that only contain numbers (integers)

    >>> split_tester("1234", "2")
    12, 34
    True
    '''
    splitsize = int(d)
    length = len(N)
    for substrings in range (0, length, splitsize):
        if substrings + splitsize >= length:
            print(N[substrings:substrings + splitsize])
        else:
            print(N[substrings:substrings + splitsize], end = ', ')
    return True

################################################   
# ascii_name_plaque code from assignment 1
################################################

def ascii_name_plaque(name):
    '''
    (string) -> print

    Returns a print of a name plaque with the name inserted into the function. 

    Precondition: 'name' has to be a string
    '''
    spaces = len(name) + 6
    line1 = '*' * (spaces + 8)
    line2 = '\n*' + (' ' * (spaces + 6)) + '*'
    line3 = '\n*''    __' + name + '__    *'
    line4 = '\n*' + (' ' * (spaces + 6)) + '*'
    line5 = '\n' + ('*' * (spaces + 8))
    plaque = '\n' + line1 + line2 + line3 + line4 + line5
    return print(plaque)

################################################
# main part of the code
################################################

ascii_name_plaque("Welcome to my increasing-splits tester")

name = input("\nWhat is your name? ")

ascii_name_plaque(name + ", welcome to my increasing-splits tester. ")

flag = True
while flag:
    question = input('\n' + name + ', would you like to test if a number admits an increasing-split of give size? ')
    question = (question.strip()).lower()

    if question == 'yes':
        print('\nGood Choice!!')
        a = input('\nEnter a positive integer: ')
        a = str(a).strip()
            
        if int(a) > 0:
            s = input('\nInput the split. The split has to divide the length of ' + str(a) + ' i.e. ' + str(len(a)) + '\n')
                
            if len(a) % int(s) == 0:
                
                if split_tester(str(a), str(s)) == False:
                    print('\nThe sequence is not increasing.')
                
                else:
                    print('\nThe sequence is increasing.')
                
            else:
                print('\n' + s + ' does not divide ' + str(len(a)) + '. Try again.')
                
        elif int(a) <= 0:
            print('\nThe input has to be a positive integer. Try again.')

    elif question == 'no':
        ascii_name_plaque("Goodbye " + name + "!")
        flag = False
            
    else:
        print('\nPlease enter yes or no. Try again.')
    

