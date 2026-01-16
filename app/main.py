# from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        """Initialize a Distance instance with kilometers."""
        self.km: float = km

    def __str__(self) -> str:
        """Return a string representation of the distance."""
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        """Return a detailed representation of the distance."""
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> "Distance":
        """Return a new Distance instance as the sum of two distances."""
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: float) -> "Distance":
        """Add a distance or a number to this instance."""
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, factor: float) -> "Distance":
        """Return a new Distance instance multiplied by a factor."""
        return Distance(self.km * factor)

    def __truediv__(self, divisor: float) -> "Distance":
        """Return a new Distance instance divided by a divisor."""
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, other: float) -> bool:
        """Check if this distance is less than another."""
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: float) -> bool:
        """Check if this distance is greater than another."""
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: float) -> bool:
        """Check if this distance is equal to another."""
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: float) -> bool:
        """Check if this distance is less than or equal to another."""
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: float) -> bool:
        """Check if this distance is greater than or equal to another."""
        return self.km >= (other.km if isinstance(other, Distance) else other)
