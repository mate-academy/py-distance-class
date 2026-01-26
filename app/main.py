class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance") -> "Distance":
        if isinstance(other, Distance):
            return Distance(self.km + other.km)
        elif isinstance(other, (int, float)):
            return Distance(self.km + other)
        else:
            return NotImplemented

    def __iadd__(self, other: "Distance") -> int:
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: "Distance") -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(self.km * other)
        else:
            return NotImplemented

    def __truediv__(self, other: any) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(round(self.km / other, 2))
        else:
            return NotImplemented

    def __lt__(self, other: any) -> bool:
        compare_value = other.km if isinstance(other, Distance) else other
        return self.km < compare_value

    def __gt__(self, other: any) -> bool:
        compare_value = other.km if isinstance(other, Distance) else other
        return self.km > compare_value

    def __eq__(self, other: any) -> bool:
        compare_value = other.km if isinstance(other, Distance) else other
        return self.km == compare_value

    def __le__(self, other: any) -> bool:
        compare_value = other.km if isinstance(other, Distance) else other
        return self.km <= compare_value

    def __ge__(self, other: any) -> bool:
        compare_value = other.km if isinstance(other, Distance) else other
        return self.km >= compare_value
