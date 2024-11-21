class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return "Distance(km=" + str(self.km) + ")"

    def __add__(self, other: int | float | object) -> object:
        return Distance(self.km + getattr(other, "km", other))

    def __iadd__(self, other: int | float | object) -> object:
        self.km += getattr(other, "km", other)
        return self

    def __mul__(self, other: int | float | object) -> object:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float | object) -> object:
        result = self.km / other
        return Distance(round(result, 2))

    def __lt__(self, other: int | float | object) -> bool:
        return self.km < other

    def __gt__(self, other: int | float | object) -> bool:
        return self.km > other

    def __eq__(self, other: int | float | object) -> bool:
        return self.km == other

    def __le__(self, other: int | float | object) -> bool:
        return self.km <= other

    def __ge__(self, other: int | float | object) -> bool:
        return self.km >= other
