class Distance:
    def __init__(self, km: int | float):
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float) -> object:
        if not isinstance(other, Distance):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __iadd__(self, other: int | float) -> object:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int | float) -> object:
        return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> object:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int | float | object) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            if self.km < other:
                return True
            return False

        if self.km < other.km:
            return True
        return False

    def __gt__(self, other: int | float | object) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            if self.km > other:
                return True
            return False

        if self.km > other.km:
            return True
        return False

    def __eq__(self, other: int | float | object) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            if self.km == other:
                return True
            return False

        if self.km == other.km:
            return True
        return False

    def __le__(self, other: int | float | object) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            if self.km <= other:
                return True
            return False

        if self.km <= other.km:
            return True
        return False

    def __ge__(self, other: int | float | object) -> bool:
        if isinstance(other, int) or isinstance(other, float):
            if self.km >= other:
                return True
            return False

        if self.km >= other.km:
            return True
        return False
