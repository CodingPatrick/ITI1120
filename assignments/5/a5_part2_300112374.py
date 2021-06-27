class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'

### NEXT CLASS

class Rectangle:
    'class that represents a rectangle'

    def __init__(self, leftP, rightP, color):
        '''(Point, Point, str) -> None
        Initialises the rectangle with its bottom left Point, its top right Point and its color'''
        self.leftP = leftP
        self.rightP = rightP
        self.color = color

    def __repr__(self):
        '''() -> str
        Returns the formal way of seeing the Points and color of the rectangle in question'''
        return 'Rectangle(' + str(self.leftP) + ', ' + str(self.rightP) + ', \'' + str(self.color) + '\')'

    def __str__(self):
        '''() -> str
        Returns the informal way of seeing the Points and color of the rectangle in question'''
        return 'I am a ' + str(self.color) + ' rectangle with bottom left corner at ' + str(self.leftP.get()) + ' and top right corner at ' + str(self.rightP.get()) + '.'

    def __eq__(self, other):
        '''() -> bool
        Returns True if the Rectangles are equal, and False otherwise'''
        return self.leftP == other.leftP and self.rightP == other.rightP and self.color == other.color
    
    def get_bottom_left(self):
        '''() -> Point
        Returns the Point of the bottom left corner of the rectangle in question'''
        return self.leftP

    def get_top_right(self):
        '''() -> Point
        Returns the Point of the top right corner of the rectangle in question'''
        return self.rightP

    def get_color(self):
        '''() -> str
        Returns the string of the color of the rectangle in question'''
        return self.color

    def reset_color(self, newcolor):
        '''(str)  -> None
        Changes the set color of the Rectangle in question'''
        self.color = newcolor

    def get_perimeter(self):
        '''() -> float
        Returns the perimeter of the Rectangle in question'''
        return abs( ((self.rightP.get()[0] - self.leftP.get()[0]) + (self.rightP.get()[1] - self.leftP.get()[1])) * 2 )

    def get_area(self):
        '''() -> float
        Returns the area of the Rectangle in question'''
        return abs( (self.rightP.get()[0] - self.leftP.get()[0]) * (self.rightP.get()[1] - self.leftP.get()[1]) )

    def move(self, moveX, moveY):
        '''(float, float) -> None
        Moves the Rectangle by moveX digits towards the left/right and by moveY digits towards the top/bottom'''
        self.leftP.move(moveX, moveY)
        self.rightP.move(moveX, moveY)

    def intersects(self, other):
        '''(Rectangle) -> bool
        Returns True if the calling Rectangle intersects the given Rectangle, and False otherwise'''
        condition1 = other.leftP.get()[0] > self.rightP.get()[0] or self.leftP.get()[0] > other.rightP.get()[0]
        condition2 = other.leftP.get()[1] > self.rightP.get()[1] or self.leftP.get()[1] > other.rightP.get()[1]
        return not(condition1 or condition2)

    def contains(self, xCoord, yCoord):
        '''(float, float) -> bool
        Returns True if the Point(xCoord, yCoord) given is inside or on the border of the Rectangle in question, and False otherwise'''
        return xCoord <= self.rightP.get()[0] and xCoord >= self.leftP.get()[0] and yCoord <= self.rightP.get()[1] and yCoord >= self.leftP.get()[1]

### NEXT CLASS  

class Canvas:
    'class that represents a canvas'

    def __init__(self):
        ''' starts a list for all the rectangles in the Canvas'''
        self.canvas = []

    def __repr__(self):
        '''() -> str
        Returns canonical string representation Canvas([Rectangle(...), Rectangle(...), ...])'''
        return 'Canvas(' + str(self.canvas) + ')'

    def __len__(self):
        '''() -> int
        Returns the length of the Canvas, i.e. the amount of Rectangles in the Canvas'''
        return len(self.canvas)

    def add_one_rectangle(self, addRect):
        '''(Rectangle) -> None
        Adds the new Rectangle into the canvas.'''
        self.canvas.append(addRect)

    def count_same_color(self, color):
        '''(str) -> int
        Returns the amount of Rectangles with the same color as the color inserted into the function'''
        count = 0
        for i in self.canvas:
            if str(i.get_color()) == str(color):
                count = count + 1
        return count

    def total_perimeter(self):
        '''() -> float
        Returns the total perimeter of the Canvas, i.e. the added perimeter of every Rectangle in the Canvas'''
        total_p = 0
        for i in self.canvas:
            p = i.get_perimeter()
            total_p = total_p + p
        return total_p

    def min_enclosing_rectangle(self):
        '''() -> Rectangle
        Returns an object of type Rectangle representing the smallest possible Rectangle that can wrap around
        all the Rectangles in the Canvas'''
        bx = []
        sx = []
        by = []
        sy = []
        
        for i in self.canvas:
            bx.append(i.get_top_right().get()[0])
            sx.append(i.get_bottom_left().get()[0])
            by.append(i.get_top_right().get()[1])
            sy.append(i.get_bottom_left().get()[1])
        
        return Rectangle(Point(min(sx), min(sy)), Point(max(bx), max(by)), 'orange')

    def common_point(self):
        '''() -> bool
        Returns True if all the Rectangles in the Canvas have a common Point, and False otherwise'''
        for i in self.canvas:
            for j in self.canvas:
                if i.intersects(j) == False:
                    return False
        return True
