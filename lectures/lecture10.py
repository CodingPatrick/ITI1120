if condition:
    statement(s)

while condition:
    statement(s)

for i in range(10, 0, -1):
    print(i)
print("blastoff")

i = 10
while i > 0 :
    print(i)
    i = i -1
print("blastoff")

answer = input("Yes, or no, do you want to play one more time? ").strip().lower()
while answer != 'yes' and answer != 'no':
    print("Incorrect input. Please answer yes or no.")
    answer = input("Yes, or no, do you want to play one more time? ").strip().lower()

def print_until_vowel(s):
    '''
    (str) -> none

    >>> print_until_vowel("Today")
    T
    '''
    i = 0
    while i < len(s) and s[i] not in 'aeiouAEIOU':
        print(s[i], end = '')
        i = i + 1
        
def collatz(n):

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else: # odd
            n = 3 * n + 1
    
    return True

N = 1
while N <= 2000000:
    collatz(N)
    N = N + 1

print("If this is printed then we know that Collatz conjecture is true for all positive integers 1 ... 2 000 000")

##import random
##
##def guessing_game():
##    '''
##    () -> none
##    '''
##    print('I am thinking of a number between 1 and 1000')
##    x = random.randint(1,1000)
##
##    tries = 10
##    guess = int(input('Try and guess the number: '))
##    tries = tries - 1
##
##    while tries > 0 and guess != x:
##        if guess < x:
##            print('Wrong! Too low')
##        elif guess > x:
##            print('Wrong! Too high')
##        guess = int(input('Try and guess the number: '))
##        tries = tries - 1
##
##    if guess == x:
##        print('Congratulations!! You won!!')
##    else:
##        print('You lose!! Go read up on binary search.')
##
### main
##guessing_game()
