import random

class Point:
    def __init__(self, x, y):
        """
        Initialize a Point object.
        :parm x: the x position on the axis
        :parm y: the y position on the exis
        """
        self.x = x #define x attribute cia self.x
        self.y = y #and assign the value x to it

    def __str__(self):
        """"magic method that is called when we try to print an instance """

        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        return self.__str__() #use the same way of printiong as str

    def distance_orig(self):
        return(self.x**2 + self.y**2)**0.5 #square root of the sum of x and y

    def __gt__(self, other):
        my_distance = self.distance_orig()
        other_distance = other.distance_orig()
        return my_distance == other_distance
if __name__ == "__main__":

     #now we need to instentiate it
    p = Point(1, 2)  # p is an intance of 1 and 2
    p2 = Point(2, 3)
    p4 = Point(4.4, -55)
    print(f"p.x={p.x} and p.y={p.y}")
    print(f"p4.x={p4.x} and p4.y={p4.y}")
    p.x = 20
    print(f"p.x={p.x} and p.y={p.y}")
    print(p)
    #create a list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10), # x value
                            random.randint(-10, 10))) # y value
    print("I got these 5 random points:")
    print(points)
    p= Point(3, 4)
    print(p.distance_orig()) #expect 5 answers
    p2 = Point(1,1)
    print(f"I am comparing p > p2{p>p2}")
    print("the sorted list of points is:")
    points.sort()
    print(points)
