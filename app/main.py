class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        raise TypeError("Unsupported type for addition with Distance")

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            self.km += other
        elif isinstance(other, Distance):
            self.km += other.km
        else:
            raise TypeError("Unsupported type for in-place addition with Distance")
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Unsupported type for multiplication with Distance")


    def __truediv__(self, other) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError("Unsupported type for division with Distance")


    def __lt__(self, other: "Distance"):
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: "Distance") -> bool:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __eq__(self, other: "Distance") -> bool:
        return self.km ==  (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: "Distance") -> bool:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: "Distance") -> bool:
        return self.km >= (other.km if isinstance(other, Distance) else other)