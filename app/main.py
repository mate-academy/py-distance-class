class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | int | float) -> "Distance":
        value_to_add = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value_to_add)

    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        self.km += other.km if isinstance(other, Distance) else other
        return self

    def __mul__(self, number: int | float) -> "Distance":
        return Distance(self.km * number)

    def __truediv__(self, number: int | float) -> "Distance":
        return Distance(round((self.km / number), 2))

    def __lt__(self, other: "Distance" | int | float) -> bool:
        value_lt = other.km if isinstance(other, Distance) else other
        return self.km < value_lt

    def __gt__(self, other: "Distance" | int | float) -> bool:
        value_lt = other.km if isinstance(other, Distance) else other
        return self.km > value_lt

    def __eq__(self, other: "Distance" | int | float) -> bool:
        value_lt = other.km if isinstance(other, Distance) else other
        return self.km == value_lt

    def __ge__(self, other: "Distance" | int | float) -> bool:
        value_lt = other.km if isinstance(other, Distance) else other
        return self.km >= value_lt

    def __le__(self, other: "Distance" | int | float) -> bool:
        value_lt = other.km if isinstance(other, Distance) else other
        return self.km <= value_lt
