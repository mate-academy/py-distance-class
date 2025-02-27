class Distance:

    def __init__(self, km):
        self.km = km

    def __str__(self):
        return f"Distance: {self.km} kilometers."

    def __repr__(self):
        return f"Distance(km={self.km})"

    def __add__(self, new_km: "Distance | int | float") -> "Distance":
        if isinstance(new_km, Distance):
            return Distance(self.km + new_km.km)
        elif isinstance(new_km, (int, float)):
            return Distance(self.km + new_km)
        raise TypeError("Can only add Distance or int")

    def __eq__(self, new_km: "Distance | int | float") -> "Distance | bool":
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

    def __truediv__(self, other):
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
