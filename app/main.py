class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | int | float) -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    def __mul__(self, number: int | float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> "Distance":
        return Distance(round(self.km / number, 2))

    def __lt__(self, other: "Distance" | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: "Distance" | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: "Distance" | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __le__(self, other: "Distance" | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: "Distance" | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
