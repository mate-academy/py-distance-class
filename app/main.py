class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> any:
        return Distance(
            km=self.km + (other.km if isinstance(other, Distance) else other)
        )

    def __iadd__(self, other: int) -> any:
        self.km = (self.km
                   + (other.km if isinstance(other, Distance) else other)
                   )
        return self

    def __mul__(self, other: int) -> any:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)

    def __truediv__(self, other: int) -> any:
        if isinstance(other, (int, float)):
            return Distance(round((self.km / other), 2))

    def __eq__(self, other: int) -> any:
        return self.km == (other.km if isinstance(other, Distance) else other)

    def __ne__(self, other: int) -> any:
        return self.km != (other.km if isinstance(other, Distance) else other)

    def __lt__(self, other: int) -> any:
        return self.km < (other.km if isinstance(other, Distance) else other)

    def __gt__(self, other: int) -> any:
        return self.km > (other.km if isinstance(other, Distance) else other)

    def __le__(self, other: int) -> any:
        return self.km <= (other.km if isinstance(other, Distance) else other)

    def __ge__(self, other: int) -> any:
        return self.km >= (other.km if isinstance(other, Distance) else other)
