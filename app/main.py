from typing import Union, Any

class Distance:
    def __init__(self, km: float) -> None:
        self.km = km  # Основна одиниця зберігання - кілометри

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: Union['Distance', float]) -> 'Distance':
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        raise TypeError("Operand must be Distance or number")

    def __iadd__(self, other: Union['Distance', float]) -> 'Distance':
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            raise TypeError("Operand must be Distance or number")
        return self

    def __mul__(self, other: float) -> 'Distance':
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        raise TypeError("Can only multiply by number")

    def __truediv__(self, other: Union[float, 'Distance']) -> Union['Distance', float]:
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        elif isinstance(other, Distance):
            raise TypeError("Cannot divide Distance by Distance")
        raise TypeError("Can only divide by number")

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        elif isinstance(other, (int, float)):
            return self.km == other
        return False

    def __lt__(self, other: Union['Distance', float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        elif isinstance(other, (int, float)):
            return self.km < other
        raise TypeError("Can only compare with Distance or number")

    def __le__(self, other: Union['Distance', float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        elif isinstance(other, (int, float)):
            return self.km <= other
        raise TypeError("Can only compare with Distance or number")

    def __gt__(self, other: Union['Distance', float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        elif isinstance(other, (int, float)):
            return self.km > other
        raise TypeError("Can only compare with Distance or number")

    def __ge__(self, other: Union['Distance', float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        elif isinstance(other, (int, float)):
            return self.km >= other
        raise TypeError("Can only compare with Distance or number")
