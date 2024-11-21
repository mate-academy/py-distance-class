class Distance:
    def __init__(self, km: int):
        self.km = km

    def __str__(self) -> str:
        return f'Distance: {self.km} kilometers.'

    def __repr__(self) -> str:
        return f'Distance(km={self.km})'

    def __add__(self, other) -> object:
        return Distance(self.km + self.get_other_km(other))

    def __iadd__(self, other) -> object:
        self.km += self.get_other_km(other)
        return self

    def __mul__(self, other) -> object:
        return Distance(self.km * other)

    def __truediv__(self, other) -> object:
        return Distance(round(self.km / other, 2))

    def __lt__(self, other) -> bool:
        return self.km < self.get_other_km(other)

    def __gt__(self, other) -> bool:
        return self.km > self.get_other_km(other)

    def __eq__(self, other) -> bool:
        return self.km == self.get_other_km(other)

    def __le__(self, other) -> bool:
        return self.km <= self.get_other_km(other)

    def __ge__(self, other) -> bool:
        return self.km >= self.get_other_km(other)

    def __len__(self) -> int:
        return self.km

    @staticmethod
    def get_other_km(other) -> int | float:
        return other.km if isinstance(other, Distance) else other
