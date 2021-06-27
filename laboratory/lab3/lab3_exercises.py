
# Programming exercise 1

def is_eligible(age, citizenship, prison):
     if age >= 18 and citizenship.lower() == 'canadian' and prison.lower() == 'no' or age >= 18 and citizenship.lower() == 'canada' and prison.lower() == 'no':
          return True
     else:
          return False
     
name = input("What is your name? ")
age = int(input("How old are you? "))
citizenship = input("What is your citizenship? / Where are you from? ")
prison = input("Are you currently in prison convicted for a criminal offence? ")

if is_eligible(age, citizenship, prison) == True:
     print(name,", you are eligible to vote!")
else:
     print(name,", you are ineligible to vote!") 



# Programming exercise 2

def mess(sentence):
    
    new_sentence = ''
    for ch in sentence:
        if ch in 'rstvwxyz':
            new_sentence = new_sentence + ch.capitalize()
        elif ch == ' ':
            new_sentence = new_sentence + '-'
        else:
            new_sentence = new_sentence + ch
    return new_sentence
    


# Programming exercise 3

def is_divisible(n,m):
     return n % m == 0

def is_divisible23n8(n):
     if ( (is_divisible(n,2) or is_divisible(n,3)) and not (is_divisible(n,8))):
          return True
     else:
          return False

def print_all_23n8(num):
    for i in range(num):
        if is_divisible23n8(i):
            print (i, end = " ")
    print()
    


# Programming exercise 4

def draw_pyramid():
    positive_int = int(input("Enter a positive integer: "))
    character = input("Enter a character: ")
                   
    for i in range(positive_int + 1):
                       print(i * character)
    


# Programming exercise 5

