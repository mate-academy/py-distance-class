from __future__ import annotations

class Distance:
    def __init__(self, km: int | float) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        # Якщо km ціле число, показати без .0
        km_display = int(self.km) if self.km.is_integer() else self.km
        return f"Distance: {km_display} kilometers."

    def __repr__(self) -> str:
        km_display = int(self.km) if self.km.is_integer() else self.km
        return f"Distance(km={km_display})"

    # Додавання
    def __add__(self, other: Distance | int | float) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        return Distance(self.km + value)

    def __iadd__(self, other: Distance | int | float) -> Distance:
        value = other.km if isinstance(other, Distance) else other
        self.km += value
        return self

    # Множення
    def __mul__(self, other: int | float) -> Distance:
        return Distance(self.km * other)

    # Ділення
    def __truediv__(self, other: int | float) -> Distance:
        return Distance(round(self.km / other, 2))

    # Порівняння
    def __lt__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km < value

    def __gt__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km > value

    def __eq__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km == value

    def __le__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km <= value

    def __ge__(self, other: Distance | int | float) -> bool:
        value = other.km if isinstance(other, Distance) else other
        return self.km >= value
