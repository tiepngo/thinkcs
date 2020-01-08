
class Point:
    """Point in 2D"""
    def __init__(self,x=0, y=0):
        """Create new x and y value"""
        self.x = x
        self.y = y
    
    def reflect_x(self):
        return Point(self.x, -self.y)
    
    def slope_from_origin(self):
        return self.y/self.x

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y


def distance(p1,p2):
    """Caculate distance between 2 point p1 & p2"""
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5

p1 = Point(0,0)
p2 = Point(3,4)

print("New value after reflect y = {} ".format(Point(3,5).reflect_x().get_y()))
def test_distance():
    assert distance(p1,p2) == 5
    assert distance(p1,p2.reflect_x()) == 5
    assert Point(3, 5).reflect_x().get_y() is  Point(3, -5).get_y()
    assert Point(4, 10).slope_from_origin() == 2.5
