class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def get_value(obj: Distance | int | float) -> int | float:
        if isinstance(obj, (int, float)):
            return obj
        if isinstance(obj, Distance):
            return obj.km
        raise TypeError(f"Unsupported type: {type(obj).__name__}")

    def __add__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.get_value(other))

    def __radd__(self, other: Distance | int | float) -> Distance:
        return Distance(self.km + self.get_value(other))

    def __iadd__(self, other: Distance | int | float) -> Distance:
        self.km += self.get_value(other)
        return self

    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    def __eq__(self, value: Distance | int | float) -> bool:
        return self.km == self.get_value(value)

    def __gt__(self, value: Distance | int | float) -> bool:
        return self.km > self.get_value(value)

    def __ge__(self, value: Distance | int | float) -> bool:
        return self.km >= self.get_value(value)

    def __lt__(self, value: Distance | int | float) -> bool:
        return self.km < self.get_value(value)

    def __le__(self, value: Distance | int | float) -> bool:
        return self.km <= self.get_value(value)
