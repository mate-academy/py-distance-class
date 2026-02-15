class Distance:
    def __init__(self, km: float) -> None:
        self.km: float = float(km)

    def __str__(self) -> str:
        km_str = str(int(self.km)) if self.km.is_integer() else str(self.km)
        return f"Distance: {km_str} kilometers."

    def __repr__(self) -> str:
        km_str = str(int(self.km)) if self.km.is_integer() else str(self.km)
        return f"Distance(km={km_str})"

    def __add__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        return Distance(self.km + float(other))

    def __iadd__(self, other: "Distance | int | float") -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += float(other)
        return self

    def __mul__(self, other: int | float) -> "Distance":
        return Distance(self.km * float(other))

    def __truediv__(self, other: int | float) -> "Distance":
        return Distance(round(self.km / float(other), 2))

    def __lt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < float(other)

    def __gt__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > float(other)

    def __eq__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == float(other)

    def __le__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= float(other)

    def __ge__(self, other: "Distance | int | float") -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= float(other)
