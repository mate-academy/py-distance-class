class Distance:

    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> None:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> None:
        return f"Distance(km={self.km})"

    def __add__(self, other) -> None:
        if isinstance(other, Distance):
            return Distance(
                km=self.km + other.km
            )
        return Distance(
            km=self.km + other
        )

    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other):
        if not isinstance(other, Distance):
            return Distance(
                km=self.km * other
            )


    def __truediv__(self, other):
        if not isinstance(other, Distance):
            return Distance(
                km=round(self.km / other, 2)
            )


    def __lt__(self, other):
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other):
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other):
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other):
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other):
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other

    def __len__(self):
        return self.km
