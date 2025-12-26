from typing import Union


class Distance:
    """
    Represents a distance measurement in kilometers.

    This class provides various utilities for creating,
    comparing, and modifying  distance values. It supports
    arithmetic operations like addition, multiplication,
    and division, along with comparison operations such as
    less than, greater than, equal to, etc. The Distance object
    encapsulates distances as integers or floats, allowing users
    to manipulate and analyze distance data in an intuitive manner.

    :ivar km: Distance in kilometers.
    :type km: int
    """
    def __init__(self, km: int) -> None:
        """
        Represents an entity encapsulating information about
        kilometers.

        The purpose of this class is to initialize and store a
        value representing distance in kilometers.

        :parameter km: The distance in kilometers
        :type km: int
        """
        self.km = km

    def __str__(self) -> str:
        """
        Converts the distance information into a readable
        string format.

        :return: A string representation of the distance
        in the format.
        :rtype: str
        """
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """
        Provides a string representation of the
        Distance object.

        The __repr__ method is used to generate an official
        string representation of the Distance object. This
        string is ideally suited for debugging and will
        show the distance in kilometers.

        :return: A string representation of the Distance
        object.
        :rtype: str
        """
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[int, float]) -> "Distance":
        """
        Adds two Distance objects or a Distance object
        and a numeric value.

        This method allows you to add a numeric value or
        another Distance object to the current Distance instance.
        If the operand is a Distance object, the method computes
        the sum of kilometers from both instances.
        If the operand is a numeric value, it adds that value to
        the kilometers of the current Distance instance.

        :param other: The value to add, either a Distance object
        or a numeric value.
        :type other: Distance or numeric (float, int)
        :return: A new Distance object representing the sum of
        the current value and the operand.
        :rtype: Distance
        """
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: Union[int, float]) -> "Distance":
        """
        Modifies the current Distance object by incrementing
        its "km" value with the given "other" value. If "other"
        is an instance of Distance, its "km" value will be added.
        Otherwise, it is assumed that "other" is a numeric value,
        and it will be directly added.
        The method returns the modified Distance object.

        :param other: The value to be added to the "km" attribute
        of the current object. It can either be an instance of
        Distance or a numeric value.
        :return: The modified current Distance object with the
        updated "km" value.
        """
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        """
        Multiplies the current Distance instance by a given
        numeric factor.

        This method supports multiplying a distance object
        (in kilometers) by a numeric value, resulting in a
        new Distance object. It does not alter the original
        instance.

        :param other: The numeric factor by which the distance
        will be multiplied.
        :type other: float or int
        :return: A new Distance instance where the distance
        in kilometers is multiplied by the given factor.
        :rtype: Distance
        """
        return Distance(self.km * other)

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        """
        Divides the current `Distance` instance by a given
        value and returns a new `Distance` instance with the
        result rounded to two decimal places.

        :param other: The value to divide the current distance by.
                      Expected to be of a numeric type.
        :type other: float
        :return: A new `Distance` instance with the divided and
        rounded result.
        :rtype: Distance
        """
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: Union[int, float]) -> bool:
        """
        Compares the current Distance object with another
        Distance object or a numeric value to determine
        if it is less than the given value.

        :param other: The value to compare against. This can
        be either another Distance object or a numeric value
        representing a distance.
        :type other: Union[Distance, float, int]
        :return: True if the current Distance object is less
        than the provided value or Distance object, otherwise
        False.
        :rtype: bool
        """
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union[int, float]) -> bool:
        """
        Compares the current Distance object with another
        object to determine if the current Distance is
        greater than the other.

        :param other: The object to compare against. It can
            be either another Distance object or a numerical
            value representing a distance.
        :type other: Distance | float | int
        :return: True if the current Distance is greater
            than the other object; False otherwise.
        :rtype: bool
        """
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union[int, float]) -> bool:
        """
        Compares two distances for equality.

        This method overrides the equality operator
        for the Distance class, allowing comparisons
        to be made either with another Distance object
        or with a numerical value.

        :param other: The object or value to compare
            against. It can either be an instance of
            the Distance class or a numeric
            value (int or float).
        :type other: Distance | int | float
        :return: True if the comparison evaluates
        to equality, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union[int, float]) -> bool:
        """
        Determines if the current Distance object is less
        than or equal to another distance or a numeric value.

        :param other: Another Distance object or a numeric value
            to compare. Must be numeric or an instance of Distance.
        :type other: Distance or float
        :return: True if the current Distance is less than or
            equal to the `other` Distance or value, otherwise False.
        :rtype: bool
        """
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union[int, float]) -> bool:
        """
        Checks if this Distance object is greater than or equal
        to another Distance object or a numeric value.

        This method compares the current object's distance in
        kilometers to either another Distance object's kilometers
        or a numeric value. If the "other" value is an instance of
        "Distance", their kilometers are compared; otherwise,
        the current object's kilometers are checked against
        the numeric value.

        :param other: Another Distance object or a numeric
            value to compare against this Distance instance.
        :type other: Distance or float
        :return: True if this Distance instance's kilometers
            are greater than or equal to the compared kilometers
            or numeric value, False otherwise.
        :rtype: bool
        """
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
