class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        # Fix to match the expected output in the tests
        return f"Distance(km={self.km})"

    def __add__(self, other: str) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)  # Fix to use other.km
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Unsupported type for addition with Distance")

    def __iadd__(self, other: str) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported type for in-place "
                            "addition with Distance")
        return self  # Return self to support in-place addition

    def __mul__(self, other: str) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Unsupported type for multiplication with Distance")

    def __truediv__(self, other: str) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError("Unsupported type for division with Distance")

    def __lt__(self, other: str) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Unsupported type for comparison with Distance")

    def __gt__(self, other: str) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("Unsupported type for comparison with Distance")

    def __eq__(self, other: str) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        raise TypeError("Unsupported type for comparison with Distance")

    def __le__(self, other: str) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError("Unsupported type for comparison with Distance")

    def __ge__(self, other: str) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError("Unsupported type for comparison with Distance")
