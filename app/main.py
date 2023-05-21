class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> "Distance":
        if isinstance(other, Distance):
            new_km = self.km + other.km
            return Distance(new_km)
        elif isinstance(other, (int, float)):
            new_km = self.km + other
            return Distance(new_km)

    def __iadd__(self, other: int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            multiplied = self.km * other
            return Distance(multiplied)

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            division = self.km / other
            return Distance(round(division, 2))

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < Distance(other).km

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > Distance(other).km

    def __eq__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == Distance(other).km

    def __le__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= Distance(other).km
        return False

    def __ge__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= Distance(other).km
        return False
