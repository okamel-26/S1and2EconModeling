import random
from ftplib import parse227


class Point:
    """
    Class modeling a real life 2D point
    """

    def __init__(self, x, y):
        """
        Initialize the point instance
        :param x: the x axis coordinate value
        :param y: the y axis coordinate value
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a user-friendly string representation of the point in the format <x, y>.
        """
        return f"<{self.x}, {self.y}>"

    def __repr__(self):
        """
        Returns the official string representation of the point.
        Uses the same format as __str__.
        """
        return self.__str__()

    def distance_orig(self):
        """
        Calculates and returns the Euclidean distance from the origin (0, 0) to the point.
        """
        return (self.x**2 + self.y**2)**0.5

    def __gt__(self, other):
        """
        Magic method that is called when you do self > other
        :param other: the other point comparing against
        :return: True/False
        """
        return self.distance_orig() > other.distance_orig()

    def __eq__(self, other):
        """
        Compares two points for equality based on their distance from the origin.
        Returns True if distances are equal, otherwise False.
        """
        return self.distance_orig() == other.distance_orig()


"""
Test block to demonstrate creation, sorting, and equality probability of Point instances.
Generates random points, prints sorted lists, and estimates the probability of two
points being equal in distance from the origin.
"""
if __name__ == "__main__":
    points = []
    for i in range(5):
        # create a random point
        p = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        # append it to the list
        points.append(p)

    print("unsorted points")
    print(points)
    print("sorted points")
    points.sort()
    print(points)

    found_equal = 0
    count = 0
    while True:
        if found_equal == 10000:
            break
        p1 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        p2 = Point(
            random.randint(-100, 100),
            random.randint(-100, 100)
        )
        count += 1
        if p1 == p2:
            # print(p1, p2)
            found_equal += 1

    print(f"probability is 1 in {count/found_equal} ")