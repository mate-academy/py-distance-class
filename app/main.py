class Distance:
    def __init__(self, km: int) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, distance: int | float | Distance) -> Distance:
        if isinstance(distance, Distance):
            return Distance(self.km + distance.km)
        return Distance(self.km + distance)

    def __iadd__(self, distance: int | float | Distance) -> Distance:
        if isinstance(distance, Distance):
            self.km += distance.km
        else:
            self.km += distance
        return self

    def __mul__(self, distance: int | float) -> Distance | None:
        if isinstance(distance, (int, float)):
            return Distance(self.km * distance)
        return None

    def __truediv__(self, distance: int | float) -> Distance | None:
        if isinstance(distance, (int, float)):
            return Distance(round(self.km / distance, 2))
        return None

    def __lt__(self, distance: int | float | Distance) -> bool:
        if isinstance(distance, Distance):
            return self.km < distance.km
        return self.km < distance

    def __gt__(self, distance: int | float | Distance) -> bool:
        if isinstance(distance, Distance):
            return self.km > distance.km
        return self.km > distance

    def __eq__(self, distance: int | float | Distance) -> bool:
        if isinstance(distance, Distance):
            return self.km == distance.km
        return self.km == distance

    def __le__(self, distance: int | float | Distance) -> bool:
        if isinstance(distance, Distance):
            return self.km <= distance.km
        return self.km <= distance

    def __ge__(self, distance: int | float | Distance) -> bool:
        if isinstance(distance, Distance):
            return self.km >= distance.km
        return self.km >= distance
