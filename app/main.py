class Distance:
    def __init__(self, km: float) -> None:
        self.km = float(km)

    def __str__(self) -> str:
        return f"{self.km} km"

    def __repr__(self) -> str:
        return f"Distance({self.km})"

    # Operações aritméticas
    def __add__(self, other) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return NotImplemented

    def __iadd__(self, other) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, value) -> "Distance":
        if not isinstance(value, (int, float)):
            return NotImplemented
        return Distance(self.km * value)

    def __truediv__(self, value) -> "Distance":
        if not isinstance(value, (int, float)):
            return NotImplemented
        return Distance(round(self.km / value, 2))

    # Comparações
    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        return False

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            return self.km < other
        return NotImplemented

    def __le__(self, other) -> bool:
        return self == other or self < other

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        return NotImplemented

    def __ge__(self, other) -> bool:
        return self == other or self > other
