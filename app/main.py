class Distance:
    def __init__(self, km: (float, int)) -> None:
        self.km = km

    def __add__(self, other: (int, float, "Distance")) -> "Distance":
        km = other if isinstance(other, (int, float)) else other.km
        return Distance(
            km=self.km + km
        )

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __iadd__(self, other: (int, float, "Distance")) -> "Distance":
        km = other if isinstance(other, (int, float)) else other.km
        self.km += km
        return self

    def __mul__(self, factor: (int, float)) -> "Distance":
        return Distance(
            km=self.km * factor
        )

    def __truediv__(self, divisor: (int, float)) -> "Distance":
        return Distance(
            km=round(self.km / divisor, 2)
        )

    def __lt__(self, other: (int, float, "Distance")) -> bool:
        km = other if isinstance(other, (int, float)) else other.km
        return self.km < km

    def __gt__(self, other: (int, float, "Distance")) -> bool:
        km = other if isinstance(other, (int, float)) else other.km
        return self.km > km

    def __eq__(self, other: (int, float, "Distance")) -> bool:
        km = other if isinstance(other, (int, float)) else other.km
        return self.km == km

    def __le__(self, other: (int, float, "Distance")) -> bool:
        km = other if isinstance(other, (int, float)) else other.km
        return self.km <= km

    def __ge__(self, other: (int, float, "Distance")) -> bool:
        km = other if isinstance(other, (int, float)) else other.km
        return self.km >= km
