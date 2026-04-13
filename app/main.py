class Distance:

    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            self.km += other
            return self
        raise TypeError(f"Cannot add {type(other)} to {type(self)}")

    def __mul__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km * other)
        return Distance(self.km * other.km)

    def __truediv__(self, other: Distance | int | float) -> Distance:
        if not isinstance(other, Distance):
            return Distance(self.km / other)
        return Distance(self.km / other.km)

# -----------------------------------------------------

    def adept_km(self, other: Distance | int | float) -> int | float:
        if isinstance(other, Distance):
            return other.km
        if isinstance(other, (int, float)):
            return other
        raise TypeError(
            f"Cannot be compared {type(other)} and {type(self)}"
        )

# ------------------------------------------------------

    def __lt__(self, other: Distance | int | float) -> bool:
        return self.km < self.adept_km(other)

    def __gt__(self, other: Distance | int | float) -> bool:
        return self.km > self.adept_km(other)

    def __eq__(self, other: Distance | int | float) -> bool:
        return self.km == self.adept_km(other)

    def __le__(self, other: Distance | int | float) -> bool:
        return self.km <= self.adept_km(other)

    def __ge__(self, other: Distance | int | float) -> bool:
        return self.km >= self.adept_km(other)
