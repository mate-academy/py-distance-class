class Distance:
    def __init__(self, km: float | int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other: "Distance" or int) -> "Distance":
        other = self.check_or_made_instance(other)
        return Distance(
            self.km + other.km
        )

    def __iadd__(self, other: "Distance" or int) -> "Distance":
        other = self.check_or_made_instance(other)
        self.km += other.km
        return self

    def __mul__(self, other: int) -> "Distance":
        return Distance(
            self.km * other
        )

    def __truediv__(self, other: int) -> "Distance":
        return Distance(
            round(self.km / other, 2)
        )

    def __lt__(self, other: "Distance" or int) -> bool:
        other = self.check_or_made_instance(other)
        return self.km < other.km

    def __gt__(self, other: "Distance" or int) -> bool:
        other = self.check_or_made_instance(other)
        return self.km > other.km

    def __eq__(self, other: "Distance" or int) -> bool:
        other = self.check_or_made_instance(other)
        return self.km == other.km

    def __le__(self, other: "Distance" or int) -> bool:
        other = self.check_or_made_instance(other)
        return self.km <= other.km

    def __ge__(self, other: "Distance" or int) -> bool:
        other = self.check_or_made_instance(other)
        return self.km >= other.km

    def __len__(self) -> int:
        return self.km

    @staticmethod
    def check_or_made_instance(other: "Distance" or int) -> "Distance":
        if not isinstance(other, Distance):
            other = Distance(other)
        return other
