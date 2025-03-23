class Distance:
    def __init__(self, km: int) -> None:
        self.km = km  # Save the value of distance in kilometers

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."  # User-friendly description

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"  # Developer-friendly representation

    def __add__(self, other: str) -> None:
        if isinstance(other, Distance):
            # Add two Distance objects together
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            # Add a number to the current distance
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: str) -> None:
        if isinstance(other, Distance):
            # In-place addition for Distance objects
            self.km += other.km
        elif isinstance(other, (int, float)):
            # In-place addition for numerical values
            self.km += other
        return self

    def __mul__(self, other: int) -> None:
        if isinstance(other, (int, float)):
            # Multiply distance by a number
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int) -> None:
        if isinstance(other, (int, float)) and other != 0:
            # Divide distance by a number
            return Distance(round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: int) -> None:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: int) -> None:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: int) -> None:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return NotImplemented

    def __le__(self, other: int) -> None:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: int) -> None:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return NotImplemented
