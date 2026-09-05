class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            new_km = self.km + other.km
        else:
            new_km = self.km + other
        return Distance(new_km)

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: "int | float") -> "Distance":
        new_km = self.km * other
        return Distance(new_km)

    def __truediv__(self, other: "int | float") -> "Distance":
        new_km = round(self.km / other, 2)
        return Distance(new_km)

    def __eq__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __lt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __le__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
