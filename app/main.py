from __future__ import annotations


class Distance:
    # Write your code here
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def get_km(self, value: Distance | int | float) -> int | float:
        if isinstance(value, Distance):
            return value.km
        if isinstance(value, (int, float)):
            return value
        return NotImplemented

    def __add__(self, other_km: Distance | int | float) -> Distance:
        value = self.get_km(other_km)

        if value is NotImplemented:
            return NotImplemented

        return Distance(self.km + value)

    def __iadd__(self, other_km: Distance | int | float) -> Distance:
        value = self.get_km(other_km)
        if value is NotImplemented:
            return NotImplemented
        self.km += value
        return self

    def __mul__(self, other_km: int | float) -> Distance:
        if isinstance(other_km, (int, float)):
            return Distance(self.km * other_km)
        return NotImplemented

    def __rmul__(self, other_km: int | float) -> Distance:
        return self.__mul__(other_km)

    def __truediv__(self, other_km: int | float) -> Distance:
        if isinstance(other_km, (int, float)):
            result = round(self.km / other_km, 2)
            return Distance(result)
        return NotImplemented

    def __lt__(self, other_km: Distance | int | float) -> bool:
        value = self.get_km(other_km)
        if value is NotImplemented:
            return NotImplemented
        return self.km < value

    def __gt__(self, other_km: Distance | int | float) -> bool:
        value = self.get_km(other_km)
        if value is NotImplemented:
            return NotImplemented
        return self.km > value

    def __eq__(self, other_km: Distance | int | float) -> bool:
        value = self.get_km(other_km)
        if value is NotImplemented:
            return NotImplemented
        return self.km == value

    def __le__(self, other_km: Distance | int | float) -> bool:
        value = self.get_km(other_km)
        if value is NotImplemented:
            return NotImplemented
        return self.km <= value

    def __ge__(self, other_km: Distance | int | float) -> bool:
        value = self.get_km(other_km)
        if value is NotImplemented:
            return NotImplemented
        return self.km >= value
