from operator import truediv


class Distance:

    def __init__(self, kilometers: int) -> None:
        self.km = kilometers

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" or int) -> "Distance":
        if type(other) is Distance:
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: "Distance") -> "Distance":
        if type(other) is Distance:
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, number: int) -> "Distance":
        return Distance(round(truediv(self.km, number), 2))

    def __lt__(self, other: "Distance" or int) -> bool:
        if type(other) is Distance:
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: "Distance" or int) -> bool:
        if type(other) is Distance:
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: "Distance" or int) -> bool:
        if type(other) is Distance:
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: "Distance" or int) -> bool:
        if type(other) is Distance:
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: "Distance" or int) -> bool:
        if type(other) is Distance:
            return self.km >= other.km
        else:
            return self.km >= other
