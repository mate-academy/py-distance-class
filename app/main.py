class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: Distance | int | float) -> Distance | str:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        return "Invalid number!"

    def __iadd__(self, other: Distance | int | float) -> Distance | str:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        return "Invalid number!"

    def __mul__(self, other: int | float) -> Distance | str:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
            f"unsupported operand type(s) for *: 'Distance' and '"
            f"{type(other).__name__}'"
        )

    def __truediv__(self, other: int | float) -> Distance | str:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError(
            f"unsupported operand type(s) for /: 'Distance' and '"
            f"{type(other).__name__}'"
        )

    def __lt__(self, other: Distance | int | float) -> bool | str:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        return "Invalid number!"

    def __le__(self, other: Distance | int | float) -> bool | str:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        return "Invalid number!"

    def __eq__(self, other: Distance | int | float) -> bool | str:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return "Invalid number!"

    def __gt__(self, other: Distance | int | float) -> bool | str:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        return "Invalid number!"

    def __ge__(self, other: Distance | int | float) -> bool | str:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        return "Invalid number!"
