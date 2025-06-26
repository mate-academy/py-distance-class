class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: "int | float") -> "Distance":
        self.km *= other
        return Distance(self.km)

    def __truediv__(self, other: "int | float") -> "Distance":
        self.km /= other
        return Distance(round(self.km, 2))

    def __lt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return True if self.km < other.km else False
        else:
            return True if self.km < other else False

    def __gt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return True if self.km > other.km else False
        else:
            return True if self.km > other else False

    def __eq__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return True if self.km == other.km else False
        else:
            return True if self.km == other else False

    def __le__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return True if self.km <= other.km else False
        else:
            return True if self.km <= other else False

    def __ge__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return True if self.km >= other.km else False
        else:
            return True if self.km >= other else False
