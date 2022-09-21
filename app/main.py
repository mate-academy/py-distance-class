class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> ["Distance", int]:
        if isinstance(other, (int, float)) is True:
            return Distance(other + self.km)
        return Distance(other.km + self.km)

    def __iadd__(self, other) -> "Distance":
        if isinstance(other, (int, float)) is True:
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, other) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other) -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(self, other) -> bool:
        if isinstance(other, (int, float)) is True:
            return self.km < other
        return self.km < other.km

    def __gt__(self, other) -> bool:
        if isinstance(other, (int, float)) is True:
            return self.km > other
        return self.km > other.km

    def __eq__(self, other) -> bool:
        if isinstance(other, (int, float)) is True:
            return self.km == other
        return self.km == other.km

    def __le__(self, other) -> bool:
        return True if self.__gt__(other) is False else False

    def __ge__(self, other) -> bool:
        return True if self.__lt__(other) is False else False

    def __len__(self) -> "Distance":
        return self
