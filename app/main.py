class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int or float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int) or isinstance(other, float):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: "
                            "'Distance' and '{}'".format(type(other).__name__))

    def __iadd__(self, other: int or float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, int) or isinstance(other, float):
            self.km += other
        else:
            raise TypeError("Unsupported operand type(s) for +=:"
                            "'Distance' and '{}'".format(type(other).__name__))
        return self

    def __mul__(self, other: int or float) -> "Distance":
        if isinstance(other, int) or isinstance(other, float):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: "
                            "'Distance' and '{}'".format(type(other).__name__))

    def __truediv__(self, other: int or float) -> "Distance":
        if isinstance(other, int) or isinstance(other, float):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type(s) for /: "
                            "'Distance' and '{}'".format(type(other).__name__))

    def __lt__(self, other: int or float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type(s) for <: "
                            "'Distance' and '{}'".format(type(other).__name__))

    def __gt__(self, other: int or float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type(s) for >: "
                            "'Distance' and '{}'".format(type(other).__name__))

    def __eq__(self, other: int or float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type(s) for ==: "
                            "'Distance' and '{}'".format(type(other).__name__))

    def __le__(self, other: int or float) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other: int or float) -> bool:
        return not self.__lt__(other)
