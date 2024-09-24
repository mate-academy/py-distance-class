class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            new_distance = self.km + other.km
        elif isinstance(other, (int, float)):
            new_distance = self.km + other
        else:
            raise TypeError
        return Distance(new_distance)

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError
        return self

    def __mul__(self, other: int) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError

    def __truediv__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            raise TypeError
        elif isinstance(other, (int, float)) and other != 0:
            return Distance(round(self.km / other, 2))
        raise ValueError("Invalid type for division.")

    def __eq__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return False

    def __lt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError

    def __gt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError

    def __le__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError

    def __ge__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError
