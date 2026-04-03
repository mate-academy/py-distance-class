class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | int | float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int | float) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> "Distance":
        return Distance(round(self.km / other, 2))

    def _get_value(self, other: "Distance" | int | float) -> float:
        if isinstance(other, Distance):
            return other.km
        return float(other)

    def __lt__(self, other: "Distance" | int | float) -> bool:
        return self.km < self._get_value(other)

    def __gt__(self, other: "Distance" | int | float) -> bool:
        return self.km > self._get_value(other)

    def __eq__(self, other: "Distance" | int | float) -> bool:
        return self.km == self._get_value(other)

    def __le__(self, other: "Distance" | int | float) -> bool:
        return self.km <= self._get_value(other)

    def __ge__(self, other: "Distance" | int | float) -> bool:
        return self.km >= self._get_value(other)
