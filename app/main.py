class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        return Distance(self.km + other_distance)

    def __iadd__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        self.km += other_distance

        return self

    def __mul__(self, other: (int, float)) -> object:
        if isinstance(other, Distance):
            return None
        other = self.km * other
        return Distance(other)

    def __truediv__(self, other: (int, float)) -> object:
        if isinstance(other, Distance):
            return None
        return Distance(round(self.km / other, 2))

    def __lt__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        return self.km < other_distance

    def __gt__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        return self.km > other_distance

    def __eq__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        return self.km == other_distance

    def __le__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        return self.km <= other_distance

    def __ge__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        return self.km >= other_distance

    def __len__(self) -> object:
        return len(self.km)
