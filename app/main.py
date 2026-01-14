class Distance:
    def __init__(self, km: float) -> None:
        """
        Initialize a Distance instance with a given distance in kilometers.
        """
        self.km = km

    def __str__(self) -> str:
        """
        Return a string representation of the Distance instance for printing.
        """
        return (
            f"Distance: {self.km} kilometers."
        )

    def __repr__(self) -> str:
        """
        Return a developer-friendly string representation of the Distance
        instance.
        """
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        """
        Add two Distance instances or a Distance instance and a number.
        """
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
            "Unsupported type for addition."
        )

    def __iadd__(self, other: object) -> "Distance":
        """
        Perform in-place addition of two Distance instances or a Distance and
        a number.
        """
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                "Unsupported type for in-place addition."
            )
        return self

    def __mul__(self, factor: float) -> "Distance":
        """
        Multiply a Distance instance by a number.
        """
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        raise TypeError(
            "Unsupported type for multiplication."
        )

    def __truediv__(self, divisor: float) -> "Distance":
        """
        Divide a Distance instance by a number, rounding the result to 2
        decimal places.
        """
        if divisor == 0:
            raise ZeroDivisionError(
                "Division by zero is not allowed."
            )
        if isinstance(divisor, (int, float)):
            return Distance(round(self.km / divisor, 2))
        raise TypeError(
            "Unsupported type for division."
        )

    def __lt__(self, other: object) -> bool:
        """
        Check if one Distance instance is less than another or a number.
        """
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        raise TypeError(
            "Unsupported type for comparison."
        )

    def __le__(self, other: object) -> bool:
        """
        Check if one Distance instance is less than or equal to another or a
        number.
        """
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError(
            "Unsupported type for comparison."
        )

    def __eq__(self, other: object) -> bool:
        """
        Check if two Distance instances or a Distance and a number are equal.
        """
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __gt__(self, other: object) -> bool:
        """
        Check if one Distance instance is greater than another or a number.
        """
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        raise TypeError(
            "Unsupported type for comparison."
        )

    def __ge__(self, other: object) -> bool:
        """
        Check if one Distance instance is greater than or equal to another or
        a number.
        """
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError(
            "Unsupported type for comparison."
        )
