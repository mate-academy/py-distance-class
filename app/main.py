class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance | int | float") -> None:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type for +")

    def __iadd__(self, other: "Distance | int | float") -> None:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type for +")
        return self

    def __mul__(self, other: "Distance | int | float") -> None:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other: "Distance | int | float") -> None:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type for /")

    def __lt__(self, other: "Distance | int | float") -> None:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type for <")

    def __gt__(self, other: "Distance | int | float") -> None:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type for >")

    def __eq__(self, other: "Distance | int | float") -> None:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            return False

    def __le__(self, other: "Distance | int | float") -> None:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: "Distance | int | float") -> None:
        return self.__gt__(other) or self.__eq__(other)
