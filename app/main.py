from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        """
        Initializes a new instance of the Distance class.

        Args:
            km (int | float): Take an integer o floating-point number thar represents
            the distance in kilometer.

        Returns:
            None

        Raises:
            TypeError: when km is not an integer or float.
            ValueError: when km is a negative number.
        """
        if not isinstance(km, (int, float)):
            raise TypeError("The distance must be a number!")
        elif km < 0:
            raise ValueError("The distance must be positive!")
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_dist: Distance | int | float) -> Distance:
        """
        Add a distance object or number to the current instance.

        Args:
            other_dist (Distance | int | float): value to add. Can be a distanse object,
            integer o floating-point.

        Returns:
            Distance: a new instance with the result of the sum.

        Raises:
            ValueError: if the value of the sum is negative.
        """
        if isinstance(other_dist, Distance):
            new_dist = self.km + other_dist.km
        elif isinstance(other_dist, (int, float)):
            new_dist = self.km + other_dist
        else:
            return NotImplemented
        return type(self)(new_dist)

    def __radd__(self, other_dist: Distance | int | float) -> Distance:
        """
        It allows addition when the Distance object to the rigth of the "+" operator.

        Args:
            other_dist (Distance | int | float): a Distanse object, integer or floating-point.

       Returns:
            Call the add method that return a Distance object.
        """
        return self.__add__(other_dist)

    def __iadd__(self, other_dist: Distance | int | float) -> Distance:
        """
        Add a value to the current instance, modifying its state

         Args:
            other_dist (Distance | int | float): a Distanse object, integer or floating-point

        Returns:
            Distance: the self intance, with the km atribute actualized
            NotImplementedType: if other_dist is not supported,
                python will habdle the type error

        Raises:
            ValueError: if the product is negative.
        """
        if isinstance(other_dist, Distance):
            new_dist = self.km + other_dist.km
        elif isinstance(other_dist, (int, float)):
            new_dist = self.km + other_dist
        else:
            return NotImplemented
        if new_dist <= 0:
            raise ValueError("The distanse must be positive!")
        self.km = new_dist
        return self

    def __mul__(self, other_dist: int | float) -> Distance:
        """
        Multiply the distance by a scalar number.

        Args:
            other_dist (Distance | int | float): The multiplicatio factor.

        Returns:
            Distance: a new instance objetc with the distance multiplied.

        Raises:
            ValueError: when the number is not positive.
        """
        if other_dist < 0:
            raise ValueError("The number must be positive!")
        return type(self)(self.km * other_dist)

    def __truediv__(self, other_dist: int | float) -> Distance:
        """
        Divide the distance by a scalar number.

        Args:
            other_dist (Distance | int | float): The divisor.

        Return:
            A new instance with the result of the division with two decimal places.

        Raises:
            ZeroDivisionError: if the divisor is 0.
        ValueError: when the divisor is not positive.
        """
        if other_dist == 0:
            raise ZeroDivisionError("Cannot divide distanse by zero!")
        if other_dist < 0:
            raise ValueError("The number must be positive!")
        return type(self)(round(self.km / other_dist, 2))

    def __lt__(self, other_dist: Distance | int | float) -> bool:
        """
        Compares if the current instance is less than another value.

        Args:
            other_dist(Distance | int | float): The distance or numeric value to compare.

        Returns:
            bool: True if the current distance is strictly less.
            NotImplementedType: If other_dist is not an instance of Distance, int, or float.
        """
        if not isinstance(other_dist, (Distance, int, float)):
            return NotImplemented
        new_val = other_dist.km if isinstance(
            other_dist, Distance) else other_dist
        return self.km < new_val

    def __gt__(self, other_dist: Distance | int | float) -> bool:
        """
        Compares if the current instance is greater than another value.

        Args:
            other_dist(Distance | int | float): The distance or numeric value to compare.

        Returns:
            bool: True if the current distance is strictly greater.
            NotImplementedType: If other_dist is not an instance of Distance, int, or float.
        """
        if not isinstance(other_dist, (Distance, int, float)):
            return NotImplemented
        new_val = other_dist.km if isinstance(
            other_dist, Distance) else other_dist
        return self.km > new_val

    def __eq__(self, other_dist: Distance | int | float) -> bool:
        """
        Compares if the current instance is equal to another value.

        Args:
            other_dist (Distance | int | float): The distance or numeric value to compare.

        Returns:
            bool: True if the current distance and the ther value are equal.
            NotImplementedType: If other_dist is not an instance of Distance, int, or float.
        """
        if not isinstance(other_dist, (Distance, int, float)):
            return NotImplemented
        new_val = other_dist.km if isinstance(
            other_dist, Distance) else other_dist
        return self.km == new_val

    def __ge__(self, other_dist: Distance | int | float) -> bool:
        """
        Compares if the current instance is equal to or greater than another value.

        Args:
            other_dist (Distance | int | float): The distance or numeric value to compare.

        Returns:
            bool: True if the current distance is equal or greater.
            NotImplementedType: If other_dist is not an instance of Distance, int, or float.
        """
        if not isinstance(other_dist, (Distance, int, float)):
            return NotImplemented
        new_val = other_dist.km if isinstance(
            other_dist, Distance) else other_dist
        return self.km >= new_val

    def __le__(self, other_dist: Distance | int | float) -> bool:
        """
        Compares whether the current instance is equal to or less than another value.

        Args:
            other_dist (Distance | int | float): The distance or numeric value to compare.

        Returns:
            bool: True if the current distance is equal or less.
            NotImplementedType: If other_dist is not an instance of Distance, int, or float.
        """
        if not isinstance(other_dist, (Distance, int, float)):
            return NotImplemented
        new_val = other_dist.km if isinstance(
            other_dist, Distance) else other_dist
        return self.km <= new_val
