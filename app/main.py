class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        km_display = int(self.km) if self.km.is_integer() else self.km
        return f"Distance: {km_display} kilometers."

    def __repr__(self) -> str:
        km_display = int(self.km) if self.km.is_integer() else self.km
        return f"Distance(km={km_display})"

    def __add__(
        self, other: "Distance | int | float"
    ) -> "Distance":
        if isinstance(other, Distance):
            value = other.km
        else:
            value = float(other)
        return Distance(self.km + value)

    def __radd__(self, other: "int | float") -> "Distance":
        return Distance(self.km + float(other))

    def __iadd__(
        self, other: "Distance | int | float"
    ) -> "Distance":
        if isinstance(other, Distance):
            value = other.km
        else:
            value = float(other)
        self.km += value
        return self

    def __mul__(self, other: "int | float") -> "Distance":
        return Distance(self.km * other)

    def __rmul__(self, other: "int | float") -> "Distance":
        return Distance(self.km * other)

    def __truediv__(self, other: "int | float") -> "Distance":
        return Distance(round(self.km / other, 2))

    def __lt__(
        self, other: "Distance | int | float"
    ) -> bool:
        value = other.km if isinstance(other, Distance) else float(other)
        return self.km < value

    def __le__(
        self, other: "Distance | int | float"
    ) -> bool:
        value = other.km if isinstance(other, Distance) else float(other)
        return self.km <= value

    def __eq__(
        self, other: "Distance | int | float"
    ) -> bool:
        value = other.km if isinstance(other, Distance) else float(other)
        return self.km == value

    def __ne__(
        self, other: "Distance | int | float"
    ) -> bool:
        return not self.__eq__(other)

    def __gt__(
        self, other: "Distance | int | float"
    ) -> bool:
        value = other.km if isinstance(other, Distance) else float(other)
        return self.km > value

    def __ge__(
        self, other: "Distance | int | float"
    ) -> bool:
        value = other.km if isinstance(other, Distance) else float(other)
        return self.km >= value
