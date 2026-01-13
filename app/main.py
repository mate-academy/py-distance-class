from __future__ import annotations

from typing import Any


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        """
        Returns a human-readable string describing the distance. This
        is what gets shown when you print a Distance instance.
        :return: formatted string like "Distance: 20 kilometers."
        """
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """
        Returns an unambiguous string representation that can be used for
        debugging and ideally recreating the object.
         :return: string like "Distance(km=20)"
        """
        return f"Distance(km={self.km})"

    @staticmethod
    def is_distance_type(obj: Any) -> bool:
        """
        Checks whether the given object is an instance of Distance. This
        helper is used to normalize behavior in arithmetic/comparison
        methods that accept either Distance or numeric values.
         :param obj: object to check
         :return: True if obj is a Distance instance, otherwise False
        """
        return isinstance(obj, Distance)

    def get_km(self, other: Distance | int | float) -> int | float:
        """
        Extracts a numeric kilometer value from the given operand. If the
        operand is another Distance instance, its `km` attribute is returned.
        If the operand is int or float, it is treated directly as a
        kilometer value. This helper method is used to unify arithmetic and
        comparison operations that must support both Distance objects and
        numeric types.
         :param other: Distance or numeric value from which to obtain a
         kilometer value
         :return: numeric kilometer value taken from the operand
        """
        return other.km if self.is_distance_type(other) else other

    def __add__(self, other: Distance | int | float) -> Distance:
        """
        Creates a new Distance instance representing the sum of this
        distance and another operand. The operand can be another Distance
        (in which case its km value is used) or a plain number treated as
        kilometers.
         :param other: Distance or numeric kilometers to add
         :return: new Distance instance with summed kilometers
        """
        return Distance(
            self.km + self.get_km(other)
        )

    def __iadd__(self, other: Distance | int | float) -> Distance:
        """
        Performs in-place addition (+=). Mutates the current instance by
        increasing its km value. Accepts either another Distance or a
        numeric kilometers value. Returns self to preserve chaining and
        correct += semantics.
         :param other: Distance or numeric kilometers to add
         :return: the same Distance instance after modification
        """
        self.km += self.get_km(other)
        return self

    def __mul__(self, value: int | float) -> Distance:
        """
        Creates a new Distance instance scaled by a numeric multiplier.
        Only numeric values are supported, as multiplying two distances
        is not meaningful for this task.
         :param value: scalar multiplier (int or float)
         :return: new Distance instance with scaled kilometers
        """
        return Distance(self.km * value)

    def __truediv__(self, value: int | float) -> Distance:
        """
        Creates a new Distance instance divided by a numeric scalar.
        The result is rounded to 2 decimal places according to the task
        requirements.
         :param value: scalar divisor (int or float)
         :return: new Distance instance with divided kilometers
        """
        return Distance(round(self.km / value, 2))

    def __lt__(self, other: Distance | int | float) -> bool:
        """
        Implements the '<' comparison. Supports comparing with another
        Distance or a numeric value interpreted as kilometers.
         :param other: Distance or numeric kilometers to compare against
         :return: True if self is less than other, otherwise False
        """
        return (
            self.km < self.get_km(other)
        )

    def __gt__(self, other: Distance | int | float) -> bool:
        """
        Implements the '>' comparison. Supports comparing with another
        Distance or a numeric value interpreted as kilometers.
         :param other: Distance or numeric kilometers to compare against
         :return: True if self is greater than other, otherwise False
        """
        return (
            self.km > self.get_km(other)
        )

    def __eq__(self, other: Distance | int | float) -> bool:
        """
        Implements the '==' comparison. Supports comparing with another
        Distance or a numeric value interpreted as kilometers.
         :param other: Distance or numeric kilometers to compare against
         :return: True if distances are equal, otherwise False
        """
        return (
            self.km == self.get_km(other)
        )

    def __le__(self, other: Distance | int | float) -> bool:
        """
        Implements the '<=' comparison. Supports comparing with another
        Distance or a numeric value interpreted as kilometers.
         :param other: Distance or numeric kilometers to compare against
         :return: True if self is less than or equal to other, otherwise False
        """
        return (
            self.km <= self.get_km(other)
        )

    def __ge__(self, other: Distance | int | float) -> bool:
        """
        Implements the '>=' comparison. Supports comparing with another
        Distance or a numeric value interpreted as kilometers.
         :param other: Distance or numeric kilometers to compare against
         :return: True if self is greater than or equal to other,
          otherwise False
        """
        return (
            self.km >= self.get_km(other)
        )
