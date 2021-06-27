# data types
    # bool
    # string
    # turtle
    # etc.

# HOW TO CREATE YOUR OWN DATA TYPE:

class Point:
    def __init__(self, xcoord=0,ycoord=0):
        '''(Point, float, float) -> None'''
        self.x = xcoord
        self.y = ycoord

    def reflect_y(self):
        self.x = - self.x

    def reflect_x(self):
        self.y = - self.y

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def __eq__(ob1, ob2):
        return ob1.x == ob2.x and ob1.y == ob2.y

    def __repr__(self):
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def __str__(self):
        return 'I am a point with coordinates: (' +str(self.x)+','+str(self.y)+')'
        

# When you make a call Point(2,3), what happens?
#
# 1. object of type Point gets created
# 2. The address of that object gets assigned to variable self
# 3. __init__ function gets executed

