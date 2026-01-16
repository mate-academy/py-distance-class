class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Operand must be Distance, int or float")

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Operand must be Distance, int or float")
        return self

    def __mul__(self, other: "int | float") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Operand must be int or float")

    def __truediv__(self, other: "int | float") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError("Operand must be int or float")

    def __lt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Operand must be Distance, int or float")

    def __gt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("Operand must be Distance, int or float")

    def __eq__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        raise TypeError("Operand must be Distance, int or float")

    def __le__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError("Operand must be Distance, int or float")

    def __ge__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError("Operand must be Distance, int or float")
