class Distance:
    def __init__(self, km) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance:
        if type(other) is Distance:
            return Distance(round((self.km + other.km), 2))
        return Distance(round((self.km + other), 2))

    def __iadd__(self, other: int | float | Distance) -> Distance:
        if type(other) is Distance:
            self.km = round((self.km + other.km), 2)
        else:
            self.km = round((self.km + other), 2)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(round((self.km * other), 3))

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    def __eq__(self, other: int | float) -> bool:
        return self.km == other

    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float) -> bool:
        return self.km >= other
