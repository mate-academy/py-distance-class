from typing import Type


class Distance:
    def __init__(self, km: any) -> None:
        self.km = km

    def __add__(self, other: Type["Distance"] | int | float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: "
                            f" 'Distance' and '{type(other).__name__}")

    def __iadd__(self, other: Type["Distance"] | int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(f"Unsupported operand type(s) for +: "
                            f" 'Distance' and '{type(other).__name__}")

        return self

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        else:
            raise TypeError(f"Unsupported operand type(s) for *: "
                            f" 'Distance' and '{type(other).__name__}")

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(km=round(self.km / other, 2))
        else:
            raise TypeError(f"Unsupported operand type(s) for /: "
                            f" 'Distance' and '{type(other).__name__}")

    def __lt__(self, other: int | float) -> bool:
        return self.km < other

    def __le__(self, other: int | float) -> bool:
        return self.km <= other

    def __gt__(self, other: int | float) -> bool:
        return self.km > other

    def __ge__(self, other: int | float) -> bool:
        return self.km >= other

    def __eq__(self, other: int | float) -> bool:
        return self.km == other

    def __ne__(self, other: int | float) -> bool:
        return self.km != other

    @classmethod
    def get_info_class(cls) -> Type["Distance"]:
        return cls

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(km={self.km})"
