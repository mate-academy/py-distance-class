class Distance:

    def __init__(self, km: int or float) -> callable:
        self.km = km

    def __str__(self) -> callable:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> callable:
        return f"Distance(km={self.km})"

    def __add__(self, other: int or float) -> callable:
        if type(other) == Distance:
            return Distance(
                self.km + other.km
            )
        return Distance(
            self.km + other
        )

    def __iadd__(self, other: int or float) -> callable:
        if type(other) == Distance:
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int or float) -> callable:
        return Distance(
            self.km * other
        )

    def __truediv__(self, other: int or float) -> callable:
        return Distance(
            round(self.km / other, 2)
        )

    def __lt__(self, other: int or float) -> callable:
        return self.km < other

    def __gt__(self, other: int or float) -> callable:
        return self.km > other

    def __eq__(self, other: int or float) -> callable:
        return self.km == other

    def __le__(self, other: int or float) -> callable:
        return self.km <= other

    def __ge__(self, other: int or float) -> callable:
        return self.km >= other

    def __len__(self) -> callable:
        return self.km
