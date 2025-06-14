class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | object) -> object:

        return Distance(self.km + self.get_int(other))

    def __iadd__(self, other: int | float | object) -> object:
        self.km += self.get_int(other)

        return self

    def __mul__(self, other: int | float) -> object:

        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> object:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | object) -> bool:
        return (self.km < self.get_int(other))

    def __gt__(self, other: int | float | object) -> bool:
        return (self.km > self.get_int(other))

    def __eq__(self, other: int | float | object) -> bool:
        return (self.km == self.get_int(other))

    def __le__(self, other: int | float | object) -> bool:
        return (self.km <= self.get_int(other))

    def __ge__(self, other: int | float | object) -> bool:
        return (self.km >= self.get_int(other))

    def get_int(self, other: int | float | object) -> int | float:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError(f"Falscher Typ: '{type(other).__name__}'. "
                            f"Erwartet 'Distance', 'int' oder 'float'.")
