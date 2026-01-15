from typing import Union


class Distance:
    pass


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union[Distance, float, int]) -> Distance:
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type for +:"
                            " Distance and {}".format(type(other)))

    def __iadd__(self, other: Union[Distance, float, int]) -> Distance:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type for +=:"
                            " Distance and {}".format(type(other)))
        return self

    def __mul__(self, scalar: Union[float, int]) -> Distance:
        if isinstance(scalar, (int, float)):
            return Distance(self.km * scalar)
        else:
            raise TypeError("Unsupported operand type for *:"
                            " Distance and {}".format(type(scalar)))

    def __truediv__(self, divisor: Union[float, int]) -> Distance:
        if isinstance(divisor, (int, float)):
            result = self.km / divisor
            return Distance(round(result, 2))
        else:
            raise TypeError("Unsupported operand type for /:"
                            " Distance and {}".format(type(divisor)))

    def __lt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type for <:"
                            " Distance and {}".format(type(other)))

    def __gt__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type for >:"
                            " Distance and {}".format(type(other)))

    def __eq__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type for ==:"
                            " Distance and {}".format(type(other)))

    def __le__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type for <=:"
                            " Distance and {}".format(type(other)))

    def __ge__(self, other: Union[Distance, float, int]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type for >=:"
                            " Distance and {}".format(type(other)))
