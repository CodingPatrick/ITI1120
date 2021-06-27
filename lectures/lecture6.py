def temp_suggestions(temp):
    if temp > 29:
        print('It is hot!')
        print('Drink more water')
    else:
        print('It is not hot!')
        print('Bring a jacket')
    print('Goodbye')

############################################

def negative_positive(x):
    if x < 0:
        print("I am negative number")
        print("x = ", x)
    if x > 0:
        print("I am a positive number")
        print("x = ", x)
    else:
        print("I am zero")
        print(x, " is 0")
    print("Goodbye")
    

############################################

def abs(x):
    '''
    (float) -> (float)
    '''
    if x < 0:
        return -x
    print("whatever")
    return x

############################################

def format_age(age):
    '''
    (int) -> (str)

    Returning a formatted age

    Preconditons: age >= 0 and age < 150
    '''
    if age < 20:
        result = age
    elif age < 30:
        result = "twenty something years old"
    elif age < 40:
        result = "thirty something years old"
    else:
        result = "forty + years old"
    return result

############################################

def letter_grade(grade):
    '''
    (float) -> (str)
    A -> 80+, B -> 70-80, C -> 60-70, F -> < 60
    '''
    if grade >= 80 and grade <= 100:
        lg = 'A'
    elif grade >= 70 and grade < 80:
        lg = 'B'
    elif grade >= 60 and grade < 70:
        lg = 'C'
    elif grade >= 0 and grade < 60:
        lg = 'F'
    else:
        lg = 'invalid grade'
    return lg

############################################

def passed_all_and_one_aboveA(g1, g2, g3):
    '''
    (float, float, float) -> bool

    Student got over 60 on all courses, and at least an 80+ grade.
    '''
    if (g1 >= 60 and g2 >= 60 and g3 >= 60) \
       and (g1 >= 80 or g2 >= 80 or g3 >= 80):
        return True
    else:
        return False

############################################

def qe_solver(a, b, c):
    '''
    (float, float, float) -> none
    '''
    if a == 0:
        #linear equation
        if b != 0:
            print("The equation is: ", b, "* x + ", c, "= 0")
            print("The solution is: x= ", -c/b)
        else:
            if c == 0:
                print("All x verify the eq")
            else:
                print("No solutions")
    else:
        discriminant = b**2 - 4 * a * c
        if discriminant > 0:
            print("Real solutions: x1, x2)
        else:
            print("Complex solutions x1, x2")






    














    
