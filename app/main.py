class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: None) -> None:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int) or isinstance(other, float):
            return Distance(self.km + other)

    def __iadd__(self, other: None) -> None:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, int) or isinstance(other, float):
            self.km += other
        return self

    def __mul__(self, num: int) -> None:
        return Distance(self.km * num)

    def __truediv__(self, num: int) -> None:
        return Distance(round(self.km / num, 2))

    def __lt__(self, other: None) -> None:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km < other

    def __gt__(self, other: None) -> None:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km > other

    def __eq__(self, other: None) -> None:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km == other

    def __le__(self, other: None) -> None:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km <= other

    def __ge__(self, other: None) -> None:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km >= other
