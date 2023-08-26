class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:

        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Error_1")

    def __iadd__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Error_2")
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Error_3")

    def __truediv__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Error_4")

    def __lt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Error_5")

    def __gt__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Error_6")

    def __eq__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Error_7")

    def __le__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Error_8")

    def __ge__(self, other: "Distance") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Error_9")
