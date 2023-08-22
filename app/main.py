class Distance:
    """
    p.s  Не совсем уверен по поводу аннотации типов ,
    пытался добавить -> Distance к add, iadd, mul, truediv ,
    но выдает ошибку. или добавить просто int|float ?
    не ругается только на object.
    """
    def __init__(self, km) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other):
        if isinstance(other, Distance):
            result = self.km + other.km
        else:
            result = self.km + other

        return Distance(result)


    def __iadd__(self, other):
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other):
        result = self.km * other
        return Distance(result)

    def __truediv__(self, other):
            result = self.km / other
            return Distance(round(result, 2))

    def __lt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        else:
            return self.km < other

    def __gt__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        else:
            return self.km > other

    def __eq__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        else:
            return self.km == other

    def __le__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        else:
            return self.km <= other

    def __ge__(self, other) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        else:
            return self.km >= other
