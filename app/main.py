class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
        return self

    def __iadd__(self, other: int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        if isinstance(other, int) or isinstance(other, float):
            self.km += other
        return self

    def __mul__(self, other: int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        if isinstance(other, int) or isinstance(other, float):
            result_km = round(self.km / other, 2)
            return Distance(result_km)

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km < other

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km > other

    def __eq__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km == other

    def __le__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, int) or isinstance(other, float):
            return self.km >= other
