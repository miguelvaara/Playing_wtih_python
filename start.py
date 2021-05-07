
class Coordinates(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distance(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

test = Coordinates(5, 5)

print(Coordinates.distance(Coordinates(2, 2), Coordinates(4, 4)))
print(Coordinates)
print(type(test))
print(type(Coordinates))


