class Coordinate(object):
    """
    Class to to represent the coordinates (x, y) in the Cartesian plane.
    """

    def __init__(self, x, y):
        assert isinstance(x, int) and isinstance(y, int), \
            "x and y should be integers."
        self.x = x
        self.y = y

    @property
    def x_point(self) -> int:
        """Get x point."""
        return self.x

    @x_point.setter
    def x_point(self, new_x):
        """Set x point."""
        assert isinstance(new_x, int), "x should be an integer."
        self.x = new_x

    @property
    def y_point(self) -> int:
        """Get y point."""
        return self.y

    @y_point.setter
    def y_point(self, y_new):
        assert isinstance(y_new, int), "y should be an integer."
        self.y = y_new

    def __str__(self) -> str:
        """ Returns a string representation of self """
        return f"<({self.x},{self.y})>"

    def distance(self, other) -> float:
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5


origin = Coordinate(0, 0)
print(origin)
c = Coordinate(1, 2)
print(c)
print(c.x_point)
c.x_point = 5
print(c)
print(c.x_point)
print(origin.distance(c))
print(Coordinate.distance(c, origin))