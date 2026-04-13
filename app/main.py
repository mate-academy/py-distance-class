class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            raise TypeError(f"Cannot add {type(other)} to {type(self)}")

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: float) -> Distance:
        return Distance(round(self.km / other, 2))

# -----------------------------------------------------

    def adept_km(self, other: Distance | int | float) -> int:
        if isinstance(other, Distance):
            return other.km
        elif isinstance(other, (int, float)):
            return other
        else:
            raise TypeError(
                f"Cannot be compared {type(other)} and {type(self)}"
            )

# ------------------------------------------------------

    def __lt__(self, other: Distance | int) -> bool:
        return self.km < self.adept_km(other)

    def __gt__(self, other: Distance | int) -> bool:
        return self.km > self.adept_km(other)

    def __eq__(self, other: Distance) -> bool:
        return self.km == self.adept_km(other)

    def __le__(self, other: Distance) -> bool:
        return self.km <= self.adept_km(other)

    def __ge__(self, other: Distance) -> bool:
        return self.km >= self.adept_km(other)
