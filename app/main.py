from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Distance | int | float) -> Distance | TypeError:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            other = Distance(other)
            return Distance(self.km + other.km)
        raise TypeError(
            f"unsupported type for __add__ method. 'Distance', "
            f"<class 'float'> or <class 'int'> were expected. "
            f"But received {type(other)}"
        )

    def __iadd__(self, other: Distance | int | float) -> Distance | TypeError:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            other = Distance(other)
            self.km += other.km
            return self
        raise TypeError(
            f"unsupported type for __iadd__ method. 'Distance', "
            f"<class 'float'> or <class 'int'> were expected. "
            f"But received {type(other)}"
        )

    def __mul__(self, other: int | float) -> Distance | TypeError:
        if isinstance(other, (int, float)):
            other = Distance(other)
            return Distance(self.km * other.km)

        raise TypeError(
            f"unsupported type for __mul__ method. <class 'float'> "
            f"or <class 'int'> were expected. "
            f"But received {type(other)}"
        )

    def __truediv__(self, other: int | float) -> Distance | TypeError:
        if isinstance(other, (int, float)):
            other = Distance(other)
            return Distance(round(self.km / other.km, 2))
        raise TypeError(
            f"unsupported type for __truediv__ method. <class 'float'> "
            f"or <class 'int'> were expected. "
            f"But received {type(other)}"
        )

    def __lt__(self, other: int | float | Distance) -> bool | TypeError:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            other = Distance(other)
            return self.km < other.km
        raise TypeError(
            f"unsupported type. 'Distance', <class 'float'> "
            f"or <class 'int'> were expected. But received {type(other)}"
        )

    def __gt__(self, other: int | float | Distance) -> bool | TypeError:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            other = Distance(other)
            return self.km > other.km
        raise TypeError(
            f"unsupported type. 'Distance', <class 'float'> "
            f"or <class 'int'> were expected. But received {type(other)}"
        )

    def __eq__(self, other: int | float | Distance) -> bool | TypeError:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            other = Distance(other)
            return self.km == other.km
        raise TypeError(
            f"unsupported type. 'Distance', <class 'float'> "
            f"or <class 'int'> were expected. But received {type(other)}"
        )

    def __le__(self, other: int | float) -> bool | TypeError:
        return self.__eq__(other) or self.__lt__(other)

    def __ge__(self, other: int | float) -> bool | TypeError:
        return self.__eq__(other) or self.__gt__(other)
