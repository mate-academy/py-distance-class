class Distance:

    def __init__(self, km: any) -> None:
        self.km = km

    def __str__(self) -> str:
        return (f"Distance: {self.km} kilometers.")

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: any) -> None:
        if isinstance(other, (int, float)):
            return Distance(km=self.km + other)
        return Distance(km=self.km + other.km)

    def __iadd__(self, other: any) -> None:
        if isinstance(other, (int, float)):
            self.km += other
        else:
            self.km += other.km
        return self

    def __mul__(self, km: any) -> int:
        return Distance(self.km * km)

    def __truediv__(self, km: any) -> float:
        return Distance(round(self.km / km, 2))

    def __lt__(self, other: any) -> float:
        if isinstance(other, (int, float)):
            return self.km < other
        return self.km < other.km

    def __gt__(self, other: any) -> float:
        if isinstance(other, (int, float)):
            return self.km > other
        return self.km > other.km

    def __eq__(self, other: any) -> float:
        if isinstance(other, (int, float)):
            return self.km == other
        return self.km == other.km

    def __le__(self, other: any) -> float:
        if isinstance(other, (int, float)):
            return self.km <= other
        return self.km <= other.km

    def __ge__(self, other: any) -> float:
        if isinstance(other, (int, float)):
            return self.km >= other
        return self.km >= other.km
