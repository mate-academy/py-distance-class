from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = km

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
            raise TypeError(f"Unsupported type for addition: {type(other)}")

    def __iadd__(self, other: Union["Distance", int, float]) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError(f"Unsupported type for addition: {type(other)}")
        return self

    def __mul__(self, other: Union[int, float]) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            raise TypeError(
                f"Unsupported type for multiplication: {type(other)}"
            )

    def __truediv__(self, other):
        if isinstance(other, Distance):
            raise TypeError(f"Division between two Distance instances is not supported.")
        elif isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))  # Round the result to 2 decimal places
        else:
            raise TypeError(f"Unsupported type for division: {type(other)}")

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __ne__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km != other.km
        elif isinstance(other, (int, float)):
            return self.km != other
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        else:
            raise TypeError(f"Unsupported type for comparison: {type(other)}")
