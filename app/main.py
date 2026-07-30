class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int) -> Distance:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        return Distance(self.km + other.km)

    def __mul__(self, other: int) -> Distance:
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> Distance:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            if self.km < other:
                return True
            return False

        if self.km < other.km:
            return True
        return False

    def __gt__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            if self.km > other:
                return True
            return False

        if self.km > other.km:
            return True
        return False

    def __le__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            if self.km <= other:
                return True
            return False

        if self.km <= other.km:
            return True
        return False

    def __ge__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            if self.km >= other:
                return True
            return False

        if self.km >= other.km:
            return True
        return False

    def __eq__(self, other: int) -> bool:
        if isinstance(other, (int, float)):
            if self.km == other:
                return True
            return False

        if self.km == other.km:
            return True
        return False

    def __iadd__(self, other: int) -> Distance:
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self
