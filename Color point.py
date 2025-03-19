import random

from point import Point

class PointException(Exception):
    pass

class ColorPoint(Point):
    def __init__(self, x, y, color):
       # raise an expection if we try to have not a number
        if not isinstance(x,(int, float)):
            raise TypeError("x must be a number")
        if not isinstance(x,(int, float)):
            raise TypeError("y must be a number")
        super().__init__(x, y)
        self.color = color

        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"<{self.color}: {self.x}, {self.y}>"

p = ColorPoint(1, 2, "red")
print(p.distance_orig())
print(p)






# print(p)
# color = ["red","green", "blue", "yello", "black",]
# color_points = []
# for i in range(10):
#     color_points.append(
#         ColorPoint(random.randint(-10, 10),
#                    random.randint(-10, 10),
#                    random.choice(colors)))
#     print(color_points)
#

