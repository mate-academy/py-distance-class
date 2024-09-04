from __future__ import annotations
from functools import total_ordering


@total_ordering
class Distance:
    """
    A class to represent a distance measurement in kilometers.

    The Distance class supports various operations such as addition,
    multiplication, division, and comparison with both other Distance
    instances and numeric values. The class also includes a string
    representation.

    Attributes:
        km (int | float): The distance in kilometers.
    """

    def __init__(self, km: int | float) -> None:
        """
        Initialize the Distance instance.

        Args:
            km (int | float): The distance in kilometers.
        """
        self.km = km

    def __str__(self) -> str:
        """
        Return the string representation of the Distance instance.

        Returns:
            str: A string in the format "Distance: {km} kilometers."
        """
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """
        Return the official string representation of the Distance instance.

        Returns:
            str: A string in the format "Distance(km={km})".
        """
        return f"Distance(km={self.km})"

    def __add__(self, distance: Distance | int | float) -> Distance:
        """
        Add another Distance instance or a numeric value to this Distance.

        Args:
            distance (Distance | int | float):
                The other Distance or numeric value.

        Returns:
            Distance: A new Distance instance representing the sum.
        """
        return Distance(self.km + self.get_km(distance))

    def __iadd__(self, distance: Distance | int | float) -> Distance:
        """
        In-place addition of another Distance instance or a numeric value.

        Args:
            distance (Distance | int | float):
                The other Distance or numeric value.

        Returns:
            Distance: The updated Distance instance.
        """
        self.km += self.get_km(distance)
        return self

    def __mul__(self, km: int | float) -> Distance:
        """
        Multiply the Distance by a numeric value.

        Args:
            km (int | float): The numeric value to multiply by.

        Returns:
            Distance: A new Distance instance representing the product.
        """
        return Distance(self.km * km)

    def __truediv__(self, km: int | float) -> Distance:
        """
        Divide the Distance by a numeric value.

        Args:
            km (int | float): The numeric value to divide by.

        Returns:
            Distance: A new Distance instance representing the quotient,
            rounded to 2 decimal places.
        """
        return Distance(round(self.km / km, 2))

    def __lt__(self, distance: Distance | int | float) -> bool:
        """
        Compare if this Distance is less
            than another Distance or numeric value.

        Args:
            distance (Distance | int | float):
                The other Distance or numeric value.

        Returns:
            bool: True if this Distance is less, False otherwise.
        """
        return self.km < self.get_km(distance)

    def __eq__(self, distance: Distance | int | float) -> bool:
        """
        Compare if this Distance is equal to another Distance or numeric value.

        Args:
            distance (Distance | int | float):
                The other Distance or numeric value.

        Returns:
            bool: True if both are equal, False otherwise.
        """
        return self.km == self.get_km(distance)

    @staticmethod
    def get_km(distance: Distance | int | float) -> float:
        """
        Retrieve the distance in kilometers
            from a Distance instance or numeric value.

        Args:
            distance (Distance | int | float):
                The Distance instance or numeric value.

        Returns:
            float: The distance in kilometers.
        """
        return distance.km if isinstance(distance, Distance) else distance
