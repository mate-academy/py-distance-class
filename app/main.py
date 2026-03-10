class Distance:
    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" | int | float) -> "Distance":
        if isinstance(other, Distance):
            return Distance(km=self.km + other.km)
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        return NotImplemented

    def __iadd__(self, other: "Distance" | int | float) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        elif isinstance(other, (int, float)):
            self.km += other
        else:
            return NotImplemented
        return self

    def __mul__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            return Distance(km=self.km * other)
        return NotImplemented

    def __truediv__(self, other: int | float) -> "Distance":
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("You cannot divide by zero.")
            return Distance(km=round(self.km / other, 2))
        return NotImplemented

    def __lt__(self, other: "Distance" | int | float) -> bool:
        compare_val = other.km if isinstance(other, Distance) else other
        return self.km < compare_val

    def __gt__(self, other: "Distance" | int | float) -> bool:
        compare_val = other.km if isinstance(other, Distance) else other
        return self.km > compare_val

    def __eq__(self, other: "Distance" | int | float) -> bool:
        compare_val = other.km if isinstance(other, Distance) else other
        return self.km == compare_val

    def __le__(self, other: "Distance" | int | float) -> bool:
        return self < other or self == other

    def __ge__(self, other: "Distance" | int | float) -> bool:
        return self > other or self == other
