class Distance:
    def __init__(self, km: float) -> float:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

    def __iadd__(self, other: float) -> float:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError
        return self

    def __truediv__(self, number: float) -> float:
        return Distance(round(self.km / number, 2))

    def __mul__(self, number: int) -> int:
        if isinstance(number, (int, float)):
            return Distance(self.km * number)

    def __lt__(self, number: float) -> bool:
        if isinstance(number, Distance):
            return self.km < number.km
        if isinstance(number, (int, float)):
            return self.km < number

    def __le__(self, number: float) -> bool:
        if isinstance(number, Distance):
            return self.km <= number.km
        if isinstance(number, (int, float)):
            return self.km <= number

    def __gt__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other

    def __eq__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km <= other

    def __ge__(self, other: float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
