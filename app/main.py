class Distance:

    def __init__(self, km: int | float) -> None:
        self.km: float = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new_km: "Distance | int | float") -> "Distance":
        if isinstance(new_km, Distance):
            return Distance(self.km + new_km.km)
        elif isinstance(new_km, (int, float)):
            return Distance(self.km + new_km)
        raise TypeError("Can only add Distance or int")

    def __eq__(self, new_km: "Distance | int | float") -> bool:
        if isinstance(new_km, Distance):
            return self.km == new_km.km
        elif isinstance(new_km, (int, float)):
            return self.km == new_km
        return False

    def __iadd__(self, new_value: "Distance | int | float") -> "Distance":
        if isinstance(new_value, Distance):
            self.km += new_value.km
        elif isinstance(new_value, (int, float)):
            self.km += new_value
        return self

    def __mul__(self, other: "Distance | int | float") -> "Distance | None":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        return None

    def __truediv__(self, other: "Distance | int | float") -> "Distance":
        if not isinstance(other, (int, float)):
            raise TypeError("Can only divide by an int or float")
        if other == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: "Distance | int") -> bool | None:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: "Distance | int") -> bool | None:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __le__(self, other: "Distance | int") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: "Distance | int") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
