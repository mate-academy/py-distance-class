from typing import Union


class Distance:
    def __init__(self, km: Union[int, float]) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            raise TypeError("Unsupported operand type(s) for +: 'Distance' and '{}'".format(type(other)))  # noqa: E501

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Unsupported operand type(s) for +=: 'Distance' and '{}'".format(type(other)))  # noqa: E501
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Distance' and '{}'".format(type(other)))  # noqa: E501

    def __truediv__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            raise TypeError("Unsupported operand type(s) for /: 'Distance' and '{}'".format(type(other)))  # noqa: E501

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError("Unsupported operand type(s) for <: 'Distance' and '{}'".format(type(other)))  # noqa: E501

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError("Unsupported operand type(s) for >: 'Distance' and '{}'".format(type(other)))  # noqa: E501

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError("Unsupported operand type(s) for ==: 'Distance' and '{}'".format(type(other)))  # noqa: E501

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError("Unsupported operand type(s) for <=: 'Distance' and '{}'".format(type(other)))  # noqa: E501

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError("Unsupported operand type(s) for >=: 'Distance' and '{}'".format(type(other)))  # noqa: E501
