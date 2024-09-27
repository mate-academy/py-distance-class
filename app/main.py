class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float, object)) -> object:
        if type(other) is float or type(other) is int:
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: (int, float, object)) -> object:
        if type(other) is float or type(other) is int:
            self.km = self.km + other
        else:
            self.km = self.km + other.km
        return self

    def __mul__(self, other: (int, float, object)) -> object:
        return Distance(km=self.km * other)

    def __truediv__(self, other: (int, float, object)) -> object:
        return Distance(km=round(self.km / other, 2))

    def __lt__(self, other: (int, float, object)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: (int, float, object)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: (int, float, object)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km == other
        return self.km == other.km

    def __le__(self, other: (int, float, object)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: (int, float, object)) -> bool:
        if type(other) is float or type(other) is int:
            return self.km >= other
        return self.km >= other.km
