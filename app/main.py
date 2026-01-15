from __future__ import annotations


class Distance:
    """A class to represent distance in kilometers.

    :param km: The distance in kilometers.
    :type km: RealNum
    """

    def __init__(self, km: RealNum) -> None:
        """Initializes a Distance object.

        :param km: The distance in kilometers.
        :type km: RealNum
        """
        self.km = max(km, 0)

    def __str__(self) -> str:
        """Returns a string representation of the Distance object.

        :return: A string representation of the distance.
        :rtype: str
        """
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """Returns a string representation of
        the Distance object for developers.

        :return: A string representation of the Distance object.
        :rtype: str
        """
        return f"Distance(km={self.km})"

    @staticmethod
    def get_other_km(other: DistanceOrRealNum) -> RealNum:
        """A static method to get the kilometers from
        another Distance object or a real number.

        :param other: The other object to get the kilometers from.
        :type other: DistanceOrRealNum
        :return: The distance in kilometers.
        :rtype: RealNum
        """
        return other.km if isinstance(other, Distance) else other

    def __add__(self, other: DistanceOrRealNum) -> Distance:
        """Adds two Distance objects.

        :param other: The other Distance object or real number to add.
        :type other: DistanceOrRealNum
        :return: A new Distance object representing the sum.
        :rtype: Distance
        """
        return Distance(self.km + Distance.get_other_km(other))

    def __iadd__(self, other: DistanceOrRealNum) -> Distance:
        """Adds another Distance object to the current one.

        :param other: The other Distance object or real number to add.
        :type other: DistanceOrRealNum
        :return: The modified Distance object.
        :rtype: Distance
        """
        self.km = max(self.km + Distance.get_other_km(other), 0)

        return self

    def __mul__(self, multiplier: RealNum) -> Distance:
        """Multiplies a Distance object by a real number.

        :param multiplier: The number to multiply the distance by.
        :type multiplier: RealNum
        :return: A new Distance object representing the product.
        :rtype: Distance
        """
        return Distance(self.km * multiplier)

    def __truediv__(self, divider: RealNum) -> Distance:
        """Divides a Distance object by a real number.

        :param divider: The number to divide the distance by.
        :type divider: RealNum
        :return: A new Distance object representing the division.
        :rtype: Distance
        """
        return Distance(round(self.km / divider, 2))

    def __eq__(self, other: DistanceOrRealNum) -> bool:
        """Checks if two Distance objects are equal.

        :param other: The other Distance object or real number to compare.
        :type other: DistanceOrRealNum
        :return: True if the distances are equal, False otherwise.
        :rtype: bool
        """
        return self.km == Distance.get_other_km(other)

    def __lt__(self, other: DistanceOrRealNum) -> bool:
        """Checks if one Distance object is less than another.

        :param other: The other Distance object or real number to compare.
        :type other: DistanceOrRealNum
        :return: True if the distance is less than the other, False otherwise.
        :rtype: bool
        """
        return self.km < Distance.get_other_km(other)

    def __gt__(self, other: DistanceOrRealNum) -> bool:
        """Checks if one Distance object is greater than another.

        :param other: The other Distance object or real number to compare.
        :type other: DistanceOrRealNum
        :return: True if the distance is greater than the other,
            False otherwise.
        :rtype: bool
        """
        return self.km > Distance.get_other_km(other)

    def __le__(self, other: DistanceOrRealNum) -> bool:
        """Checks if one Distance object is less than or equal to another.

        :param other: The other Distance object or real number to compare.
        :type other: DistanceOrRealNum
        :return: True if the distance is less than or equal to the other,
            False otherwise.
        :rtype: bool
        """
        return self.km <= Distance.get_other_km(other)

    def __ge__(self, other: DistanceOrRealNum) -> bool:
        """Checks if one Distance object is greater than or equal to another.

        :param other: The other Distance object or real number to compare.
        :type other: DistanceOrRealNum
        :return: True if the distance is greater than or equal to the other,
            False otherwise.
        :rtype: bool
        """
        return self.km >= Distance.get_other_km(other)


RealNum = int | float
DistanceOrRealNum = Distance | RealNum
