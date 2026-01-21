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
            return Distance(new_km)
        if isinstance(other, int | float):
            new_km = self.km + other
            return Distance(new_km)
        return NotImplemented

    def __radd__(self, other: int | float) -> "Distance":
        if isinstance(other, int | float):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other: "int | float | Distance") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, int | float):
            self.km += other
            return self
        return NotImplemented

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return Distance(round(self.km / other, 2))

        return NotImplemented

    def __lt__(self, other: "int | float | Distance") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int | float):
            return self.km < other
        return NotImplemented

    def __gt__(self, other: "int | float | Distance") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int | float):
            return self.km > other
        return NotImplemented

    def __eq__(self, other: "int | float | Distance") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int | float):
            return self.km == other
        return NotImplemented

    def __le__(self, other: "int | float | Distance") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, int | float):
            return self.km <= other
        return NotImplemented

    def __ge__(self, other: "int | float | Distance") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, int | float):
            return self.km >= other
        return NotImplemented
