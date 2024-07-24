class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, other: "Distance") -> "Distance":
        if not isinstance(other, Distance):
            if isinstance(other, int | float):
                return Distance(self.km + other)
            raise TypeError(
                f"unsupported operand type(s) for +: 'Distance' and "
                f"{type(other)}"
            )

        return Distance(self.km + other.km)

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __iadd__(self, other: "Distance") -> "Distance":
        if not isinstance(other, Distance):
            if isinstance(other, int | float):
                self.km += other
                return self
            raise TypeError(
                f"unsupported operand type(s) for +=: 'Distance' and "
                f"{type(other)}"
            )

        self.km += other.km
        return self

    def __mul__(self, multiplier: int | float) -> "Distance":
        return Distance(self.km * multiplier)

    def __truediv__(self, divisor: int | float) -> "Distance":
        return Distance(round(self.km / divisor, 2))

    def __eq__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            if isinstance(other, int | float):
                return self.km == other
            raise TypeError(
                f"unsupported operand type(s) for ==: 'Distance' and "
                f"{type(other)}"
            )

        return self.km == other.km

    def __ne__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            if isinstance(other, int | float):
                return self.km != other
            raise TypeError(
                f"unsupported operand type(s) for !=: 'Distance' and "
                f"{type(other)}"
            )

        return self.km != other.km

    def __gt__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            if isinstance(other, int | float):
                return self.km > other
            raise TypeError(
                f"unsupported operand type(s) for >: 'Distance' and "
                f"{type(other)}"
            )

        return self.km > other.km

    def __ge__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            if isinstance(other, int | float):
                return self.km >= other
            raise TypeError(
                f"unsupported operand type(s) for >=: 'Distance' and "
                f"{type(other)}"
            )

        return self.km >= other.km

    def __lt__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            if isinstance(other, int | float):
                return self.km < other
            raise TypeError(
                f"unsupported operand type(s) for <: 'Distance' and "
                f"{type(other)}"
            )

        return self.km < other.km

    def __le__(self, other: "Distance") -> bool:
        if not isinstance(other, Distance):
            if isinstance(other, int | float):
                return self.km <= other
            raise TypeError(
                f"unsupported operand type(s) for <=: 'Distance' and "
                f"{type(other)}"
            )

        return self.km <= other.km
