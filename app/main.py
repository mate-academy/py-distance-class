class Distance:

    def __init__(self, km: (int, float)) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: any) -> object:
        if isinstance(other, (int, float)):
            return Distance(self.km + other)
        if isinstance(other, Distance):
            return Distance(self.km + other.km)

    def __iadd__(self, other: any) -> callable:
        if isinstance(other, (int, float)):
            self.km = self.km + other
        if isinstance(other, Distance):
            self.km = self.km + other.km
        return self

    def __mul__(self, other: (int, float)) -> [object, None]:
        if isinstance(other, (int, float)):
            self.km = self.km * other
            return self

    def __truediv__(self, other: [int, float]) -> object:
        if isinstance(other, (int, float)) and other:
            divide = round(self.km / other, 2)
            return Distance(divide)

    def __lt__(self, other: [int, float, object]) -> bool:
        if isinstance(other, (int, float)):
            return self.km < other
        if isinstance(other, Distance):
            return self.km < other.km

    def __gt__(self, other: [int, float, object]) -> bool:
        if isinstance(other, (int, float)):
            return self.km > other
        if isinstance(other, Distance):
            return self.km > other.km

    def __eq__(self, other: [int, float, object]) -> bool:
        if isinstance(other, (int, float)):
            return self.km == other
        if isinstance(other, Distance):
            return self.km == other.km

    def __le__(self, other: [int, float, object]) -> bool:
        if isinstance(other, (int, float)):
            return self.km <= other
        if isinstance(other, Distance):
            return self.km <= other.km

    def __ge__(self, other: [int, float, object]) -> bool:
        if isinstance(other, (int, float)):
            return self.km >= other
        if isinstance(other, Distance):
            return self.km >= other.km
