class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            distance = self.km + other.km
        elif isinstance(other, (int, float)):
            distance = self.km + other
        else:
            raise TypeError("Unsupported operand type")
        return Distance(distance)

    def __radd__(self, other: object) -> "Distance":
        return self + other  # дозволяє 10 + Distance(5)

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type")
        return self

    def __mul__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            result = self.km * other
        else:
            raise TypeError("Unsupported operand type")
        return Distance(result)

    def __truediv__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            result = self.km / other
        else:
            raise TypeError("Unsupported operand type")
        return Distance(round(result, 2))

    def get_km(self, other: object) -> float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError("Unsupported operand type")

    def __lt__(self, other: object) -> bool:
        return self.km < self.get_km(other)

    def __gt__(self, other: object) -> bool:
        return self.km > self.get_km(other)

    def __eq__(self, other: object) -> bool:
        return self.km == self.get_km(other)

    def __le__(self, other: object) -> bool:
        return self.km <= self.get_km(other)

    def __ge__(self, other: object) -> bool:
        return self.km >= self.get_km(other)
