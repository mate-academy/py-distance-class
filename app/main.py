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
            return f"the {other} is not a Distance and it doesn't a number!"

    def __iadd__(self, other: Any) -> Any:
        if isinstance(other, Distance):
            self.km = self.km + other.km
            return self
        elif isinstance(other, (int, float)):
            self.km += other
            return self
        else:
            return f"the {other} is not a Distance and it doesn't a number!"

    def __mul__(self, other: Any) -> Any:
        return Distance(km=self.km * other)

    def __truediv__(self, other: Any) -> Any:
        return Distance(km=round((self.km / other), 2))

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
