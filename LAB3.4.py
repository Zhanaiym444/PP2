import math
class Point:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    def show(self):
        print(self.x, self.y)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
