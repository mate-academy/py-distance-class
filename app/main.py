class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    @staticmethod
    def _to_km(other: object) -> float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"'Distance' and '{type(other).__name__}'")

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            other_km = other.km
        elif isinstance(other, (int, float)):
            other_km = other
        else:
            raise TypeError(f"unsupported operand type(s) for +: "
                            f"'Distance' and '{type(other).__name__}'")

        return Distance(km=self.km + other_km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self._to_km(other)
        return self

    def __mul__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError("can only multiply Distance by int or float")
        return Distance(self.km * other)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, (int, float)):
            raise TypeError("can only divide Distance by int or float")
        return Distance(round(self.km / other, 2))

    def __eq__(self, other: Distance | int | float) -> bool:
        if not isinstance(other, (Distance, int, float)):
            return False
        return self.km == self._to_km(other)

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self._to_km(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self._to_km(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self._to_km(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self._to_km(other)
