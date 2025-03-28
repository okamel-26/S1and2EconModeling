from point import Point  # point is the file, Point is the class
import random

class ColorPoint(Point):
    """
    A subclass of Point that includes a color attribute for the 2D point.
    """

    def __init__(self, x, y, color):
        """
        Initializes a ColorPoint with x and y coordinates and a color.
        """
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        """
        Returns a string representation of the ColorPoint in the format <x,y>(color).
        """
        return f"<{self.x},{self.y}>({self.color})"

if __name__ == '__main__':  # to make sure that this code does not run when imported
    """
    Generates a list of random ColorPoint instances and prints them
    before and after sorting.
    """
    color_points = []
    colors = ["red", "blue", "green", "yellow", "black", "white", "purple"]
    for _ in range(5):
        p = ColorPoint(
            random.randint(-100, 100),
            random.randint(-100, 100),
            random.choice(colors))
        color_points.append(p)
    print("random color points:")
    print(color_points)
    color_points.sort()
    print("color points in order:")
    print(color_points)