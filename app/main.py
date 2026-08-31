class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            distance3 = self.km + other.km
        else:
            distance3 = self.km + other
        return self.__class__(distance3)

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            distance2 = self.km * other.km
        else:
            distance2 = self.km * other
        return self.__class__(distance2)

    def __truediv__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            distance2 = self.km / other.km
        else:
            distance2 = self.km / other
        return self.__class__(round(distance2, 2))
