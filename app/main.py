from typing import Any


class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        else:
            raise TypeError(f"Unsupported operand type for + : {type(other)}!")

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            raise TypeError(f"Unsupported operand type for + : {type(other)}!")

    def __mul__(self, other: Any) -> Any:
        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        else:
            raise TypeError(f"Unsupported operand type for * : {type(other)}!")

    def __truediv__(self, other: Any) -> Any:
        if isinstance(other, (int, float)) and other != 0:
            return Distance(km=round((self.km / other), 2))
        elif other == 0:
            return print("Can't division by 0!")
        else:
            raise TypeError(f"Unsupported operand type for / : {type(other)}!")

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            print(f"the {other} is not a Distance and it doesn't a number!")
            return False

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        if isinstance(other, (int, float)):
            return self.km > other
        else:
            print(f"the {other} is not a Distance and it doesn't a number!")
            return False

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        if isinstance(other, (int, float)):
            return self.km == other
        else:
            print(f"the {other} is not a Distance and it doesn't a number!")
            return False

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            print(f"the {other} is not a Distance and it doesn't a number!")
            return False

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        if isinstance(other, (int, float)):
            return self.km >= other
        else:
            print(f"the {other} is not a Distance and it doesn't a number!")
            return False
