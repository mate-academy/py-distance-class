class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + float(other))  # type: ignore

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += float(other)  # type: ignore
        return self

    def __mul__(self, other: object) -> "Distance":
        return Distance(self.km * float(other))  # type: ignore

    def __truediv__(self, other: object) -> "Distance":
        return Distance(round(self.km / float(other), 2))  # type: ignore

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < float(other)  # type: ignore

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > float(other)  # type: ignore

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == float(other)
        return NotImplemented

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= float(other)  # type: ignore

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= float(other)  # type: ignore
