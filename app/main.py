class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __add__(self, other: object | int | float) -> object:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        else:
            return Distance(self.km + other)

    def __iadd__(self, other: object | int | float) -> object:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        else:
            self.km += other
            return self

    def __mul__(self, other: int | float) -> object:
        if isinstance(other, Distance):
            raise TypeError(
                "This metod doesn't accept Distance class instances"
            )
        else:
            return Distance(self.km * other)

    def __truediv__(self, other: int | float) -> object:
        if isinstance(other, Distance):
            raise TypeError(
                "This metod doesn't accept Distance class instances"
            )
        else:
            return Distance(round(self.km / other, 2))

    def __lt__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other: object | int | float) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"
