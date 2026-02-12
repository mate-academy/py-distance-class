class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def _value(other: "Distance | int | float") -> float:
        if isinstance(other, Distance):
            return other.km
        return other

    # + and += support Distance | int | float
    def __add__(self, other: "Distance | int | float") -> "Distance":
        return Distance(self.km + self._value(other))

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        self.km += self._value(other)
        return self

    # * and / only support int | float
    def __mul__(self, other: "int | float") -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: "int | float") -> "Distance":
        return Distance(round(self.km / other, 2))

    # Comparisons support Distance | int | float
    def __lt__(self, other: "Distance | int | float") -> bool:
        return self.km < self._value(other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        return self.km > self._value(other)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return False
        return self.km == self._value(other)

    def __le__(self, other: "Distance | int | float") -> bool:
        return self.km <= self._value(other)

    def __ge__(self, other: "Distance | int | float") -> bool:
        return self.km >= self._value(other)
