class Distance:
    def init(self, km: float) -> None:
        self.km: float = km

    def str(self) -> str:
        return f"Distance: {self.km} kilometers."

    def repr(self) -> str:
        return f"Distance(km={self.km})"

    def add(self, other: int | float) -> 'Distance':
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, int) or isinstance(other, float):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: "
                            "'Distance' and '{}'".format(type(other).name))

    def iadd(self, other: int | float) -> 'Distance':
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, int) or isinstance(other, float):
            self.km += other
        else:
            raise TypeError("Unsupported operand type(s) for +=:"
                            "'Distance' and '{}'".format(type(other).name))
        return self

    def mul(self, other: int | float) -> 'Distance':
        if isinstance(other, int) or isinstance(other, float):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: "
                            "'Distance' and '{}'".format(type(other).name))

    def truediv(self, other: int | float) -> 'Distance':
        if isinstance(other, int) or isinstance(other, float):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type(s) for /: "
                            "'Distance' and '{}'".format(type(other).name))

    def lt(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type(s) for <: "
                            "'Distance' and '{}'".format(type(other).name))

    def gt(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type(s) for >: "
                            "'Distance' and '{}'".format(type(other).name))

    def eq(self, other: int | float) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, int) or isinstance(other, float):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type(s) for ==: "
                            "'Distance' and '{}'".format(type(other).name))

    def le(self, other: int | float) -> bool:
        return self.__lt__(other) or self.__eq__(other)

    def ge(self, other: int | float) -> bool:
        return not self.__lt__(other)