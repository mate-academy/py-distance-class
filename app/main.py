from numbers import Number


error_msg = "Type mismatch: requires Distance or Number and received"


class Distance:
    def __init__(self, km: Number) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: any) -> any:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, Number):
            return Distance(self.km + other)

        raise TypeError(error_msg + type(other))

    def __iadd__(self, other: any) -> any:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        elif isinstance(other, Number):
            self.km += other
            return self

        raise TypeError(error_msg + type(other))

    def __mul__(self, number: Number) -> any:
        if not isinstance(number, Number):

            raise TypeError(error_msg + type(number))

        return Distance(self.km * number)

    def __truediv__(self, number: Number) -> any:
        if not isinstance(number, Number):

            raise TypeError(error_msg + type(number))

        return Distance(round(self.km / number, 2))

    def __lt__(self, other: any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, Number):
            return self.km < other

        raise TypeError(error_msg + type(other))

    def __gt__(self, other: any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, Number):
            return self.km > other

        raise TypeError(error_msg + type(other))

    def __eq__(self, other: any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, Number):
            return self.km == other

        raise TypeError(error_msg + type(other))

    def __le__(self, other: any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, Number):
            return self.km <= other

        raise TypeError(error_msg + type(other))

    def __ge__(self, other: any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, Number):
            return self.km >= other

        raise TypeError(error_msg + type(other))
