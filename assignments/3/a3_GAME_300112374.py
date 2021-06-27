# Course: ITI 1120
# Assignment number: a3
# Loranger, Patrick
# Student number: 300112374
# Year: 2019

# In this implementation a card (that is not a 10) is represented by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

######################################################################################################## 

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

########################################################################################################  

def deal_cards(deck):
    
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    dealer=[]
    other=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
        
    for card in range(0, len(deck), 1):
        if card % 2 == 0:
            dealer.append(deck[card])
        else:
            other.append(deck[card])

    return (dealer, other)
 
########################################################################################################  

def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''
    
    no_pairs=[]
    
    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    # the following code has been declared in the declaration file (the next 6 lines of code)
    finder = [l[0][0]]
    for i in l[1:]:
        if i[0] not in finder:
            finder.append(i[0])
    s = [[x for x in l if x[0] == i] for i in finder]
    no_pairs = [i[-1] for i in s if len(i)%2]
    
    random.shuffle(no_pairs)
    return no_pairs


########################################################################################################  

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE

    for items in deck:
        print(str(items), end=' ')

########################################################################################################

def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     num = int(input('Give me an integer between 1 and ' + str(n) + ': '))

     while ( num < 1 ) or ( num > n ):
         num = int(input('Invalid number. Give me an integer between 1 and ' + str(n) + ': '))

     return num

########################################################################################################  

def play_game():
    '''()->None
    This function plays the game'''
    
    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is: \n")
    print_deck(human)
    print("\n\nDo not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()
     
    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    # COMPLETE THE play_game function HERE
    # YOUR CODE GOES HERE

    game = True
    while game:

        ## HUMAN TURN
        
        print('***********************************************************\nYour turn.')
        print("\nYour current deck of cards is: \n")
        print_deck(human)
        print('\n\nI have', str(len(dealer)), 'cards. If 1 stands for my first card and\n'+
              str(len(dealer))+ ' for my last card, which of my cards would you like?')

        choice_h = get_valid_input(len(dealer))

        if choice_h == 1:
            print('You asked for my 1st card \nHere it is. It is', str(dealer[0]))
        elif choice_h == 2:
            print('You asked for my 2nd card \nHere it is. It is', str(dealer[1]))
        elif choice_h == 3:
            print('You asked for my 3rd card \nHere it is. It is', str(dealer[2]))
        else:
            print('You asked for my',str(choice_h) + 'th card. \nHere it is. It is ' + str(dealer[choice_h-1]))

        print('\nWith', dealer[(choice_h)-1], 'added, your current deck of cards is:\n')  
        
        human.append(dealer[choice_h - 1])
        del dealer[choice_h - 1]
        print_deck(human)

        print('\n\nAnd after discarding pairs and shuffling, your deck is: \n')

        human = remove_pairs(human)
        print_deck(human)
        
        if len(human) == 0:
            print('Ups. You do not have any more cards \nCongratulations! You, Human, win')
            game = False
        else: 
            print('')
            print('')
            wait_for_player()

        ## ROBOT TURN

            print('***********************************************************\nMy turn.')

            choice_d = random.randint(1, len(human))

            if choice_d == 1:
                print('\nI took your 1st card.')
            elif choice_d == 2:
                print('\nI took your 2nd card.')
            elif choice_d == 3:
                print('\nI took your 3rd card.')
            else:
                print('\nI took your ' + str(choice_d) + 'th card.')

            dealer.append(human[choice_d - 1])
            del human[choice_d - 1]
            dealer = remove_pairs(dealer)

            if len(dealer) == 0:
                print('Ups. I do not have any more cards \nYou lost! I, Robot, win')
                game = False
            else: 
                wait_for_player()

########################################################################################################  
	 
# main
play_game()
