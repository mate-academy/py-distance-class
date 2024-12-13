class Distance:
    def __init__(self, km: float) -> None:
        """
        Initialize the Distance object.
        :param km: The distance in kilometers.
        """
        self.km = km

    def __str__(self) -> str:
        """
        Return a user-friendly string representation of the Distance object.
        """
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(f"Unsupported operand type(s) "
                        f"for +: 'Distance' and '{type(other).__name__}'")

    def __iadd__(self, other: float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(f"Unsupported operand type(s) "
                            f"for +=: 'Distance' and '{type(other).__name__}'")
        return self

    def __mul__(self, factor: float) -> "Distance":
        if isinstance(factor, (int, float)):
            return Distance(self.km * factor)
        raise TypeError(f"Unsupported operand type(s) "
                        f"for *: 'Distance' and '{type(factor).__name__}'")

    def __truediv__(self, divisor: float) -> "Distance":
        if isinstance(divisor, (int, float)):
            if divisor == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Distance(round(self.km / divisor, 2))
        raise TypeError(f"Unsupported operand type(s) "
                        f"for /: 'Distance' and '{type(divisor).__name__}'")

    def __lt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError(f"Unsupported operand type(s) "
                        f"for <: 'Distance' and '{type(other).__name__}'")

    def __gt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        raise TypeError(f"Unsupported operand type(s) for >: "
                        f"'Distance' and '{type(other).__name__}'")

    def __eq__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        raise TypeError(f"Unsupported operand type(s) "
                        f"for ==: 'Distance' and '{type(other).__name__}'")

    def __le__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError(f"Unsupported operand type(s) "
                        f"for <=: 'Distance' and '{type(other).__name__}'")

    def __ge__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError(f"Unsupported operand type(s) "
                        f"for >=: 'Distance' and '{type(other).__name__}'")
