class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        if self.km.is_integer():
            return f"Distance: {int(self.km)} kilometers."
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        if self.km.is_integer():
            return f"Distance(km={int(self.km)})"
        return f"Distance(km={self.km})"

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + float(other))
        return NotImplemented

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):

            if isinstance(self.km, int):
                self.km += int(other)
            else:
                self.km += float(other)
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")
        return self

    def __mul__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * float(other))
        raise TypeError(f"Unsupported type for multiplication: {type(other)}")

    def __truediv__(self, other: object) -> "Distance":
        if isinstance(other, (int, float)):

            if other == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return Distance(round(self.km / float(other), 2))

        return NotImplemented

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < float(other)

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= float(other)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == float(other)
        return False

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > float(other)

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= float(other)
