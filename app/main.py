class Distance:

    def __init__(self, km: int) -> int:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, other_distance: [int, float]) -> [int, float]:
        if isinstance(other_distance, Distance):
            return Distance(self.km + other_distance.km)
        return Distance(self.km + other_distance)

    def __iadd__(self, other_distance: [int, float]) -> [int, float]:
        if isinstance(other_distance, Distance):
            self.km += other_distance.km
        else:
            self.km += other_distance
        return self

    def __mul__(self, other_distance: [int, float]) -> [int, float]:
        return Distance(self.km * other_distance)

    def __truediv__(self, other_distance: [int, float]) -> [int, float]:
        return Distance(round(self.km / other_distance, 2))

    def __lt__(self, other_distance: [int, float]) -> bool:
        if isinstance(other_distance, Distance):
            return self.km < other_distance.km
        return self.km < other_distance

    def __gt__(self, other_distance: [int, float]) -> bool:
        if isinstance(other_distance, Distance):
            return self.km > other_distance.km
        return self.km > other_distance

    def __eq__(self, other: [int, float]) -> bool:
        return not self.__lt__(other) and not self.__gt__(other)

    def __le__(self, other: [int, float]) -> bool:
        return self.__lt__(other) is True or self.__eq__(other) is True

    def __ge__(self, other: [int, float]) -> bool:
        return self.__gt__(other) is True or self.__eq__(other) is True
