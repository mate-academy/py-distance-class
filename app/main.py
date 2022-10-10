class Distance:
    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return Distance(self.km + second)

    def __iadd__(self, other: (int, float)) -> object:
        other_distance = other if isinstance(other, (int, float)) else other.km
        self.km += other_distance

        return self

    def __mul__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return Distance(self.km * second)

    def __truediv__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return Distance(round(self.km / second, 2))

    def __lt__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km < second

    def __gt__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km > second

    def __eq__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km == second

    def __le__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km <= second

    def __ge__(self, other: (int, float)) -> object:
        second = other if isinstance(other, (int, float)) else other.km
        return self.km >= second

    def __len__(self) -> object:
        return len(self.km)
