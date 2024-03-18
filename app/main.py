from __future__ import annotations


class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: int | float | Distance) -> Distance | TypeError:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        if isinstance(other, (int, float)):
            other = Distance(other)
            return Distance(self.km + other.km)
        raise self.add_iadd_error_handler(other)

    def __iadd__(self, other: int | float | Distance) -> Distance | TypeError:
        if isinstance(other, Distance):
            self.km += other.km
            return self
        if isinstance(other, (int, float)):
            other = Distance(other)
            self.km += other.km
            return self
        raise self.add_iadd_error_handler(other)

    def __mul__(self, other: int | float) -> Distance | TypeError:
        if isinstance(other, (int, float)):
            other = Distance(other)
            return Distance(self.km * other.km)
        raise self.mul_div_error_handler(other)

    def __truediv__(self, other: int | float) -> Distance | TypeError:
        if isinstance(other, (int, float)):
            other = Distance(other)
            return Distance(round(self.km / other.km, 2))
        raise self.mul_div_error_handler(other)

    def __lt__(self, other: int | float | Distance) -> bool | TypeError:
        if isinstance(other, Distance):
            return self.km < other.km
        if isinstance(other, (int, float)):
            other = Distance(other)
            return self.km < other.km
        raise self.comparison_error_handler(other)

    def __gt__(self, other: int | float | Distance) -> bool | TypeError:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            other = Distance(other)
            return self.km > other.km
        raise self.comparison_error_handler(other)

    def __eq__(self, other: int | float | Distance) -> bool | TypeError:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            other = Distance(other)
            return self.km == other.km
        raise self.comparison_error_handler(other)

    def __le__(
        self, other: int | float | Distance
    ) -> bool | callable(TypeError):
        return not self > other

    def __ge__(
        self, other: int | float | Distance
    ) -> bool | callable(TypeError):
        return not self < other

    @staticmethod
    def comparison_error_handler(other: int | float | Distance) -> TypeError:
        raise TypeError(
            f"Unsupported type for this method. 'Distance', <class 'float'> "
            f"or <class 'int'> were expected. But received {type(other)}"
        )

    @staticmethod
    def mul_div_error_handler(other: int | float) -> TypeError:
        raise TypeError(
            f"Unsupported type for this method. <class 'float'> "
            f"or <class 'int'> were expected. But received {type(other)}"
        )

    @staticmethod
    def add_iadd_error_handler(other: int | float | Distance) -> TypeError:
        raise TypeError(
            f"Unsupported type for this method. 'Distance', "
            f"<class 'float'> or <class 'int'> were expected. "
            f"But received {type(other)}"
        )
