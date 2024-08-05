class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> "Distance":
        if isinstance(other, Distance):
            total = self.km + other.km
        elif isinstance(other, (int, float)):
            total = self.km + other
        else:
            return NotImplemented
        return Distance(total)

    def __iadd__(self, other: int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, multiply: int | float) -> "Distance":
        if isinstance(multiply, (int, float)):
            return Distance(self.km * multiply)
        return NotImplemented

    def __truediv__(self, division: int | float) -> "Distance":
        if isinstance(division, (int, float)):
            if division == 0:
                raise ValueError("Cannot divide by zero")
            return Distance(round(self.km / division, 2))
        return NotImplemented

    def __lt__(self, order: int | float) -> bool:
        if isinstance(order, Distance):
            return self.km < order.km
        elif isinstance(order, (int, float)):
            return self.km < order
        return NotImplemented

    def __le__(self, order: int | float) -> bool:
        if isinstance(order, Distance):
            return self.km <= order.km
        elif isinstance(order, (int, float)):
            return self.km <= order
        return NotImplemented

    def __gt__(self, order: int | float) -> bool:
        if isinstance(order, Distance):
            return self.km > order.km
        elif isinstance(order, (int, float)):
            return self.km > order
        return NotImplemented

    def __ge__(self, order: int | float) -> bool:
        if isinstance(order, Distance):
            return self.km >= order.km
        elif isinstance(order, (int, float)):
            return self.km >= order
        return NotImplemented

    def __eq__(self, order: int | float) -> bool:
        if isinstance(order, Distance):
            return self.km == order.km
        elif isinstance(order, (int, float)):
            return self.km == order
        return NotImplemented
