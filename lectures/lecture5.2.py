import math


def area_of_triangle(base, height):
    '''
    (number, number) -> number

    Returns the area of triangle with the given base and height

    Precondition: base and height are non-negative.
    '''
    area = base * height / 2
    return area


def s_to_ms(s):
    '''
    (int) -> (int, int)

    Returns the number of minutes and seconds given the number of seconds s

    Precondition: s is non negative.
    '''
    m = s //60
    s = s % 60
    return (m,s)


def s_to_ms_v2(s):
    '''
    (int) -> None

    Returns the number of minutes and seconds given the number of seconds s

    Precondition: s is non negative.
    '''
    m = s //60
    s = s % 60
    print (m,s)


def draw_rec():
    '''
    () -> none
    '''
    print()
    print()
    print("**********")
    print("*        *")
    print("*        *")
    print("*        *")
    print("*        *")
    print("**********")
    print()
    print()
