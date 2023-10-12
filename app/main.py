class Distance:
    """
    Magic methods
    """
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return "Distance(km=" + str(self.km) + ")"

    def __add__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + other)

    def __iadd__(self, other: int) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
            return self
        self.km += other
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: int) -> "Distance":
        return Distance(round((self.km / other), 2))

    def __lt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            if self.km < other.km:
                return True
        else:
            if self.km < other:
                return True
        return False

    def __gt__(self, other: int) -> bool:
        if isinstance(other, Distance):
            if self.km > other.km:
                return True
        else:
            if self.km > other:
                return True
        return False

    def __eq__(self, other: int) -> bool:
        if isinstance(other, Distance):
            if self.km == other.km:
                return True
        else:
            if self.km == other:
                return True
        return False

    def __le__(self, other: int) -> bool:
        if isinstance(other, Distance):
            if self.km <= other.km:
                return True
        else:
            if self.km <= other:
                return True
        return False

    def __ge__(self, other: int) -> bool:
        if isinstance(other, Distance):
            if self.km >= other.km:
                return True
        else:
            if self.km >= other:
                return True
        return False
