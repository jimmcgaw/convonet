class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Vector: (%i, %i)" % (self.x, self.y)

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

v1 = Vector(2,1)
print v1
v2 = Vector(3,4)
print v2

v3 = v1 + v2
print v3
