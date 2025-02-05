class Distance:
    # Write your code here
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __add__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            entire_dist = self.km + other.km
        else:
            entire_dist = self.km + other
        return Distance(entire_dist)

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            self.km += other.km
        else:
            self.km += other
        return self

    def __mul__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            sol = self.km * other.km
            return None
        else:
            sol = self.km * other
            return Distance(sol)

    def __truediv__(self, other: object) -> "Distance":
        if isinstance(other, Distance):
            return None
        sol = round((self.km / other), 2)
        return Distance(sol)

    def __lt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __le__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __gt__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __ge__(self, other: object) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
