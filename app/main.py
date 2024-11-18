class Distance:
    def __init__(self, km: int) -> None:
        self.km = km
    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."
    def __repr__(self) -> str:
        return f"Distance(km={self.km})"
    def __add__(self, other: float | int) -> int | float:
        if isinstance(other, Distance):
            # Додавання значень двох лічильників
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            # Додавання цілого числа до лічильника
            return Distance(self.km + other)
        else:
            return NotImplemented
    def __iadd__(self, other: float | int) -> any:
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self
    def __mul__(self, other: float | int) -> any:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
    def __truediv__(self, other:  float | int) -> any:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
    def __lt__(self, other: float | int) -> any:
        return self.km < other
    def __gt__(self, other: float | int) -> any:
        return self.km > other
    def __eq__(self, other: float | int) -> any:
        return self.km == other
    def __le__(self, other: float | int) -> any:
        return self.km <= other
    def __ge__(self, other: float | int) -> any:
        return self.km >= other
