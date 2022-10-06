class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    @staticmethod
    def get_km_from_object(other: object) -> float:
        km = None
        if isinstance(other, Distance):
            km = other.km
        elif isinstance(other, (int, float)):
            km = other
        return km

    def __add__(self, other: object) -> object:
        return Distance(self.km + self.get_km_from_object(other))

    def __iadd__(self, other: object) -> object:
        self.km += self.get_km_from_object(other)
        return self

    def __mul__(self, other: object) -> object:
        return Distance(self.km * self.get_km_from_object(other))

    def __truediv__(self, other: object) -> object:
        return Distance(round(self.km / self.get_km_from_object(other), 2))

    def __len__(self) -> float:
        return self.km

    def __lt__(self, km: float) -> bool:
        return self.km < km

    def __le__(self, km: float) -> bool:
        return self.km <= km

    def __eq__(self, km: float) -> bool:
        return self.km == km

    def __gt__(self, km: float) -> bool:
        return self.km > km

    def __ge__(self, km: float) -> bool:
        return self.km >= km
