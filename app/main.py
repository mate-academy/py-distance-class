class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> any:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int, float or object"
            )

    def __iadd__(self, other: int | float) -> any:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int, float or object"
            )
        return self

    def __mul__(self, other: int | float) -> any:
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int and float"
            )

    def __truediv__(self, other: int | float) -> any:
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero")
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int and float"
            )

    def __lt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int, float or object"
            )

    def __gt__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int, float or object"
            )

    def __eq__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int, float or object"
            )

    def __le__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int, float or object"
            )

    def __ge__(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError(
                "Unexpected operand type. Operand must be int, float or object"
            )
