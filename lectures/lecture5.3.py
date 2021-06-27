def area_circle(radius):
    '''
    (number) -> number
    '''
    area = 3.14 * radius ** 2
    return area

radius = 100

area = area_circle(radius)

print("The area of a circle of radius", radius, "is", area)



def increase(x):
    x = x + 1
    
x = 10
print(x)
increase(x)
print(x)
