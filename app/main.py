class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError(
                f"Unsupported operand type for + Distance and {type(other)}"
            )

    def __iadd__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        raise TypeError(
                f"Unsupported operand type for += Distance and {type(other)}"
            )
        return self

    def __mul__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError(
                f"Unsupported operand type for * Distance and {type(other)}"
            )

    def __truediv__(self, other: Distance | int | float) -> bool:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        raise TypeError(
                f"Unsupported operand type for / Distance and {type(other)}"
            )

    def __lt__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError(
                f"Unsupported operand type for < Distance and {type(other)}"

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError(
            f"Unsupported operand type for >= Distance and {type(other)}"
        )
        

    def __eq__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        raise TypeError(
                f"Unsupported operand type for == Distance and {type(other)}"
            )

    def __le__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError(
                f"Unsupported operand type for <= Distance and {type(other)}"
            )

    def __ge__(self, other: Distance | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError(
                f"Unsupported operand type for >= Distance and {type(other)}"
            )
            
