class Distance:

    def __init__(self, km: int | float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, another_distance: object | int) -> object:
        if isinstance(another_distance, Distance):
            return Distance(self.km + another_distance.km)
        return Distance(self.km + another_distance)

    def __iadd__(self, another_distance: object | int) -> object:
        if isinstance(another_distance, Distance):
            self.km += another_distance.km
        else:
            self.km += another_distance
        return self

    def __mul__(self, another_distance: int) -> object:
        return Distance(self.km * another_distance)

    def __truediv__(self, another_distance: int) -> object:
        return Distance(round(self.km / another_distance, 2))

    def __lt__(self, another_distance: object | int) -> bool:
        if isinstance(another_distance, Distance):
            return self.km < another_distance.km
        return self.km < another_distance

    def __gt__(self, another_distance: object | int) -> bool:
        if isinstance(another_distance, Distance):
            return self.km > another_distance.km
        return self.km > another_distance

    def __eq__(self, another_distance: object | int) -> bool:
        if isinstance(another_distance, Distance):
            return self.km == another_distance.km
        return self.km == another_distance

    def __le__(self, another_distance: object | int) -> bool:
        if isinstance(another_distance, Distance):
            return self.km <= another_distance.km
        return self.km <= another_distance

    def __ge__(self, another_distance: object | int) -> bool:
        if isinstance(another_distance, Distance):
            return self.km >= another_distance.km
        return self.km >= another_distance
