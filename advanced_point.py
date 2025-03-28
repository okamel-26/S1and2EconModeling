from color_point import ColorPoint

class AdvancedPoint(ColorPoint):  # this means we are inheriting from ColorPoint
    """
    Represents a 2D point with a color. Inherits from ColorPoint.
    Supports coordinate and color validation, color management, and utility methods.
    """

    COLORS = ["red", "green", "blue", "black", "white"]

    def __init__(self, x, y, color):
        """
        Initializes an AdvancedPoint instance with x, y coordinates and a color.
        Raises:
            TypeError: if x or y is not a number.
            ValueError: if color is not in the allowed COLORS list.
        """
        if not isinstance(x, (int, float)):
            raise TypeError("x must be a number")
        if not isinstance(y, (int, float)):
            raise TypeError("y must be a number")
        if not color in self.COLORS:
            raise ValueError(f"color must be one of: {self.COLORS}")
        # super().__init__(x, y, color) # call the init method of the parent
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        """
        Returns the x-coordinate of the point.
        """
        return self._x

    @property
    def y(self):
        """
        Returns the y-coordinate of the point.
        """
        return self._y

    @property
    def color(self):
        """
        Returns the current color of the point.
        """
        return self._color

    @color.setter
    def color(self, new_color):
        """
        Sets a new color for the point after validating it.

        Raises:
            ValueError: if the new color is not in the COLORS list.
        """
        if new_color not in AdvancedPoint.COLORS:
            raise ValueError(f"color must be one of: {AdvancedPoint.COLORS}")
        self._color = new_color

    @classmethod
    def add_color(cls, new_color):
        """
        Adds a new color to the list of allowed COLORS.
        """
        cls.COLORS.append(new_color)

    @staticmethod
    def distance_2_points(p1, p2):
        """
        Calculates the Euclidean distance between two AdvancedPoint objects.

        Returns:
            float: distance between p1 and p2
        """
        return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5

    @staticmethod
    def from_dictionary(dict):
        """
        Creates an AdvancedPoint instance from a dictionary.
        Uses default values if keys are missing.

        Returns:
            AdvancedPoint: new instance based on dictionary values
        """
        x = dict.get("x", 10)
        y = dict.get("y", 20)
        color = dict.get("color", "black")
        return AdvancedPoint(x, y, color)


# Example usage
AdvancedPoint.add_color("amber")
p2 = AdvancedPoint(1, 2, "amber")
p2.color = "blue"
p3 = AdvancedPoint(-1, -2, "blue")
print(AdvancedPoint.distance_2_points(p2, p3))
p4 = AdvancedPoint.from_dictionary({"x": 44})
print(p4)